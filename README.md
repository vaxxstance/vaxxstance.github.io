## VaxxStance@IberLEF 2021

The VaxxStance shared task is part of IberLEF 2021, the [3rd Workshop on Iberian Languages Evaluation Forum](https://sites.google.com/view/iberlef2021), co-located with the SEPLN Conference, which will be held in September 2021 in XXXXX, Spain.

### Task Description

The aim of VaxxStance@IberLEF 2021 is to detect stance in social media on a very controversial and trendy topic, namely, the Antivaxxers movement, in two languages: **Basque** and **Spanish**. Following previous tasks (Mohammad et al. 2016, Taule et al. 2018, Cignarella et al. 2020), the aim is determining whether a given tweet expresses an AGAINST, FAVOR or NEUTRAL (NONE) stance towards a previously defined topic.

In the two examples given below, the tweet on the left expresses a FAVOR stance towards vaccines whereas the one on the right conveys an AGAINST stance.

![]({{ vaxxstance.github.io }}/images/eu-example.png) ![]({{ vaxxstance.github.io }}/images/es-example.png)

As the task contains tweets in two different languages, we would like to propose the following participation tracks for each language (Basque and Spanish):

1. **Close Track**: Language-specific evaluation. Only the provided data for each of the languages is allowed. There are two evaluation settings:
1.1 *Textual*: Only provided tweets in the target language can be used for development.
1.2 *Contextual*: Text plus given Twitter-related information will be used by the participants. Contextual information refers to features related with user-based Twitter information: friends, retweets, followers, replies, etc. (Cignarella et al. 2020).
2. **Open Track**: Participants can use any kind of data. The main objective consists of exploring data augmentation and knowledge transfer techniques for cross-lingual stance detection.
3. **Zero-shot Track**: Texts (tweets) of the target language cannot be used for training. The main objective is to explore how to develop systems that do not have access to text in the target language, especially using Twitter-related information.

Additionally, and inspired by the recently held SardiStance 2020 shared task (Cignarella et al. 2020), the Close Track will include **two evaluation settings per language**: *Textual* and *Contextual*. Furthermore, the **Open and Zero-shot tracks** will include only **one evaluation setting per language**, one for Spanish and one for Basque.

### Participation rule

Participants *can submit their systems to any of the tracks*, but **it will be compulsory to participate in both languages for the chosen track**.

+ Example 1: If a team only takes part in the **Close Track** then that team would have to submit runs for **both Basque and Spanish in each evaluation setting, Textual and Contextual**. 

+ Example 2.: If a team articipates in the **Zero-shot** or **Open tracks** then runs must be submitted for **both Basque and Spanish** languages.

### References

Alessandra Teresa Cignarella, Mirko Lai, Cristina Bosco, Viviana Patti, and Paolo Rosso. 2020. Overview of the EVALITA 2020 Task on Stance Detection in Italian Tweets (SardiStance). In Valerio Basile, Danilo Croce, Maria Di Maro, and Lucia C. Passaro, editors, EVALITA 2020. CEUR-WS.org.

María S. Espinosa, Rodrigo Agerri, Alvaro Rodrigo and Roberto Centeno. DeepReading @ SardiStance: Combining Textual, Social and Emotional Features. In Valerio Basile, Danilo Croce, Maria Di Maro, and Lucia C. Passaro, editors, EVALITA 2020. CEUR-WS.org.

Joulin, A., Grave, E., Bojanowski, P., Mikolov, T., 2017. Bag of tricks for efficient text classification. In EACL 2017.

Lai, M., Cignarella, A., Hernandez Farias, D., Bosco, C., Patti, V., Rosso, P., 2020. Multilingual Stance Detection in Social Media Political Debates. In Computer Speech & Language.

Mohammad, S., Kiritchenko, S., Sobhani, P., Zhu, X., & Cherry, C. (2016, June). Semeval-2016 task 6: Detecting stance in tweets. In Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016) (pp. 31-41). 

Taulé, M., Rangel, F., Martí, M.A., Rosso, P., 2018. Overview of the task on multimodal stance detection in tweets on catalan 1oct referendum. In IberEval 2018. 

Zotova, E., Agerri, R., Nuñez, M., Rigau, G., 2020. [Multilingual Stance Detection in Tweets: The Catalonia Independence Corpus](https://www.aclweb.org/anthology/2020.lrec-1.171.pdf). In LREC 2020.

Zotova, E. Agerri, R., Rigau, G, 2021. [Semi-automatic generation of multilingual datasets for stance detection in Twitter](https://authors.elsevier.com/a/1cOaa_LnESXY5N). Expert Systems with Applications, 170 (2021).[Preprint] ()[https://doi.org/10.1016/j.eswa.2020.114547](https://doi.org/10.1016/j.eswa.2020.114547)

