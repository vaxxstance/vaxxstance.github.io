# -*- coding: utf-8 -*-

import argparse
import io
import os
import sys
import pandas as pd
from pathlib import Path

import sklearn.utils
from sklearn import preprocessing
from sklearn import svm
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline


def main():
    parser = argparse.ArgumentParser(description="SVM with TF-IDF and grid search for stance detection")
    parser.add_argument('--train_data', default=sys.stdin.fileno(), help="The input file for training")
    parser.add_argument('--output_dir', default=sys.stdout.fileno(), help="The output directory for training results")
    parser.add_argument('--encoding', default='utf-8', help='The character encoding for input/output (it defaults to utf-8)')
    parser.add_argument('--processor_nodes', type=int, default=4, help="The number of processing nodes")
    args = parser.parse_args()
    print(vars(args))

    output_path = Path(args.output_dir, encoding=args.encoding)
    output_path.mkdir(parents=True, exist_ok=True)

    tweets_train = pd.read_csv(args.train_data, encoding=args.encoding, dtype={'user_id': 'object'}, sep=',')
    tweets_train = sklearn.utils.shuffle(tweets_train)  # shuffle dataset
    tweets_train = tweets_train.fillna('')
    tweets_train_text = list(tweets_train.text.values)  # list of tweets
    labels_train = list(tweets_train.label.values)  # list of labels

    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(tweets_train_text)
    print('X TRAIN ', X_train.shape)

    le = preprocessing.LabelEncoder()
    le.fit(['AGAINST', 'FAVOR', 'NONE'])
    y_train = le.transform(labels_train)
    print('Y TRAIN ', y_train.shape)


    print('=====================================================')
    print('grid search')

    NUM_FEATURES = 'all'  # 12000
    pipeline1 = Pipeline(
    [("filter", SelectKBest(mutual_info_classif, k=NUM_FEATURES)),
     ("classification", svm.SVC(kernel="rbf"))])

    grid_parameters_tune = [{"classification__C": [1, 10, 100, 300, 500, 700, 1000],
                             'classification__gamma': [0, 0.1, 0.01, 0.001, 0.25, 0.5, 0.75, 1]}]
    model = GridSearchCV(pipeline1, grid_parameters_tune, cv=5, n_jobs=args.processor_nodes, verbose=True)
    model.fit(X_train, y_train)

    # print(model.cv_results_)

    grid_result = pd.DataFrame(model.cv_results_)
    grid_best = pd.DataFrame(model.best_params_, index=[0])
    grid_result.to_csv(f"{output_path}/grid_results.csv", encoding='utf-8', index=False)

    # select the best parameters
    df_grid_first = grid_result.loc[grid_result['rank_test_score'] == 1]
    C = list(df_grid_first.param_classification__C.values)
    gamma = list(df_grid_first.param_classification__gamma.values)
    print('Parameters:\n', 'C: ', C, 'gamma: ', gamma)

    df_grid_first.to_csv(f"{output_path}/best_params.csv", encoding='utf-8', index=False)
    features = dict(zip(vectorizer.get_feature_names(), mutual_info_classif(X_train, y_train, discrete_features=True)))

    # print(features)

    print("===============================================")
    print("Cross Validation")

    clf = Pipeline(
            [("filter", SelectKBest(mutual_info_classif, k=NUM_FEATURES)),
                ("classification", svm.SVC(kernel="rbf", gamma=gamma[0], C=C[0]))])
    cv_results = cross_validate(clf, X_train, y_train, cv=5, n_jobs=args.processor_nodes, scoring='f1_macro')

    print('CV RESULTS ', cv_results['test_score'])


    y_pred = cross_val_predict(clf, X_train, y_train, cv=5, n_jobs=args.processor_nodes)

    target_names = ["AGAINST", "FAVOR", "NONE"]
    cl_report = classification_report(y_train, y_pred, target_names=target_names, digits=4)
    cm = confusion_matrix(y_train, y_pred)
    print(cm)
    print("CROSS VALIDATION")
    print(cl_report)

    # saving classification reports
    report_df = pd.read_fwf(io.StringIO(cl_report), sep="\s+")
    report_df.to_csv(f"{output_path}/CV_evaluation_results.csv", encoding='utf-8', sep='\t', index=False)
    # saving predicted and wrong predicted examples
    tweets_train['predicted'] = y_pred
    tweets_train['true'] = y_train
    tweets_train.to_csv(f"{output_path}/predicted_cross_validation.csv", encoding='utf-8', index=False)
    df1 = tweets_train.loc[tweets_train['predicted'] != tweets_train['true']]
    wrong_prediction = df1[['tweet_id', 'user_id', 'text', 'label', 'predicted', 'true']]
    wrong_prediction.to_csv(f"{output_path}/wrong_prediction_cross_validation.csv", encoding='utf-8', index=False)

if __name__ == '__main__':
    main()

