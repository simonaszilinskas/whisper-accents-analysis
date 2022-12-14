
# Is feeding speech recognition models more data an efficient way to reduce bias?

A project by Antonin, Gabriel, Lance, Simonas, Wiktor

![](https://www.xrtoday.com/wp-content/uploads/2022/01/What_Speech_Recognition_Technology_VR.jpg)

## Introduction

In our daily lives, we are progressively being surrounded by smart devices that use artificial intelligence, most notably automatic speech recognition, ranging from mobile phones, automatic captioning in video conferencing tools to digital assistants that aim to simplify our lives. Moreover, this technology is continually improving, its uses will undoubtedly expand into different fields like  healthcare and security. Given its omnipresence in the future, a bias arising from it would most likely lead to prejudices towards marginalized groups due to the algorithms used by machines. Hence, it is important to assure that these technologies are free from biases and ones that might emerge should be detected as soon as possible in order to fix them as its inclusivity is primordial in preserving social equality in our societies. 

In the short term, due to the dominance of the most spoken languages (English, Mandarin, Spanish, etc.), the speech recognition models are also focused on these languages. Less popular language native speakers thus have to leverage the same interface in their non-native languages and hence the question of accent understanding is crucial.

In 2022 Open AI, the artificial intelligence research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc, have released [Whisper](https://openai.com/blog/whisper/) - an open source neural net, that according to its creators “approaches human level robustness and accuracy on English speech recognition”. Trained on 680,000 hours of voice recordings from the web, Whisper claims to be game-changing in terms of dealing with accents. 

## Literature Review

Automatic Speech Recognition (ARS) has been a subject of research by many researchers where biases on accents has been a key research topic. Tatman (2017) has indicated that ARS has biases against some accents due to the lack of diversity the dataset used to train them. She also found out that it was more accurate for men than for women while it was the opposite in the study of Goldwater et al. (2010) and Sawalha et al. (2013). On the other hand, Gamerin et al. (2021) has found that the accuracy based on gender is minimized as the training corpus becomes equally distributed. Feng et al. (2021) made a study for Dutch and found a bias towards native speakers and differences in regional accents. In a similar study, Cambra, Guillermo et al. (2021) also showed that native English speakers, American accents notably, were a lot more accurate than Asian accents where differences could reach up to 10%, most likely due to unequal representation of accents in the training dataset. 


## Methodology

![Method](data-vizualizations/Method.png)

For the purpose of our research in the field of biases in AI, we wanted to put Whisper’s performance with different accents to the test. This allowed us to analyze whether Whisper’s chosen method of model training is a step in the right direction for creating a robust bias-free automatic speech recognition algorithm. 

Leveraging the fact that Whisper has different levels of models: tiny, base, small, medium and large, which are different in their size and speed, we wanted to see how each of them performs with different accents. 

As our accent library, we used audio recordings for [The Speech Accent Archive](https://accent.gmu.edu), a database of audio recordings of individuals having different native languages reading the same identical text which contains almost every English consonant and vowel sounds: 

```http
“Please call Stella. Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station.”
```
Each entry in the database provides information about the age, the age of English onset, native language, gender and birthplace of the individual. The database had some imperfections that necessitated the removal of a few entries with no audio recordings. Our final database consisted of 2138 audio files. We then used Python on Google Colab to run Whisper using the audio files we had collected. To do so, we decided to use three model sizes of Whisper and compare their performance. We ran the Tiny, Small and Medium models, wherein the relative speed becomes slower once the model becomes larger. 

In order to facilitate the running of a dataset that comprises more than two thousand files, we used a for loop to run each audio and then transcribe its corresponding text into another column of our dataframe. The process was repeated for every model, hence we have three transcriptions for each audio file. To check the similarity of the transcribed texts to the original one, we used two measures. The Levenshtein distance measures the minimum number of single-character modifications needed in order to change a word to another which means that the higher the distance, the more different it is. The Jaro-Winkler distance, on the other hand, measures the similarity of two strings, whose values are within the range of 0 to 1, wherein 1 means that both strings are identical.

In order to properly analyze these similarity scores, we have done some regression analysis and visualization on R, taking into account other control variables such as age, age of English onset and native language. 

## Results

### Median scores

The first observation that comes to mind regarding the median similarity scores is that for both Jaro-Winker and Levenshtein distances, the tiny model has poorer performance than the small and medium ones. It is also interesting to note that the difference is more pronounced for the former metric. This result was expected as the tiny model can transcribe a file 16 times faster than the medium model at the expense of the accuracy of said transcription.

![Median similarity (Jaro-Winkler distance)](https://github.com/simonaszilinskas/whisper-accents-analysis/blob/main/data-vizualizations/median-similarities/Median%20similarity%20score%20by%20model%20size%20(Lev)%20(1).png?raw=true)

### Gender

We have also looked into possible biases that could arise from the gender of the speaker. Our results have shown that Whisper does not comport any bias based on the gender of the speaker as we can see that for all three models, the two similarity metrics are almost identical and the differences are not significant. 

![genderjarlev](data-vizualizations/genderjarlev.png)

### Age, Onset Age in English & Number Years of Learning English

We have also looked at the biases that may occur in relation to the speaker’s age and the length of time he or she has been learning English. There seems to be no correlation between the age of the speaker and to both similarity metrics. On the other hand, there is a positive correlation between age onset and the Jaro-Winker distance while it has a negative correlation with the Levenshtein distance, while it is the opposite in relation to the number of years a person has been learning English. The interpretation remains the same, that the earlier a person starts to speak or learn English or the longer it speaks it, the more accurate Whisper is able to transcribe their speech into text.

![age_jar](data-vizualizations/age_jar.png)

![age_lev](data-vizualizations/age_lev.png)

![onset_jar](data-vizualizations/onset_jar.png)

![onset_lev](data-vizualizations/onset_lev.png)

![years_jar](data-vizualizations/year_jar.png)

![years_lev](data-vizualizations/year_lev.png)

### Native language

We have also tested the performance of Whisper based on the native language of the speaker. For both similarity metrics, its performance improves for both groups of speakers, which was expected. It is also interesting to see that native English speakers have equal performance and even outperformed by around 10 language groups in the tiny and small model while it reached up to 17 in the medium model. It is also worthwhile to note that native English speakers still have a very high performance compared to the vast majority of language groups.


![LanguageGroupLev](data-vizualizations/LanguageGroupLev.png)

![LanguageGroupJaro](data-vizualizations/LanguageGroupJaro.png)



## Limitations 

We have analyzed our results through regression analysis albeit with several limitations. The dataset that we have only provides limited variables explaining the characteristics of each speaker resulting in a poor fit of our regression models. The presence of more explanatory variables would probably increase the fit of the model since several variables such as the level of education, socio-professional status, exposure to the English language and other variables would improve the model and eliminate the problem of omitted variable bias.

Moreover, the Speech Accent Archive database has a significant number of audio recordings from people with various ages, English proficiency and country of origin; it can therefore be considered as rather comprehensive. However, it is lacking in one specific area: the number of native languages. The database is composed of audio files from individuals with 214 different native languages and, according to most linguists, more than 7,000 languages are spoken daily. This discrepancy is mainly due to the fact that most of these languages are only spoken by a few hundred individuals and are threatened with extinction while others such as English, Mandarin or Spanish have several hundred million daily speakers. Although the Speech Accent Archive also includes native speakers of “rare” languages like the Yupik language which is spoken by a little bit more than a thousand people in the Alaska peninsula, it is mainly comprised of the most spoken languages, and understandably so as it would be incredibly difficult to find native speakers of every language, especially when the groups speaking these “rare” languages are leaving in very secluded areas. Nevertheless, regarding our search for possible biases in Whisper’s speech recognition, the fact that we could not include such data in our study necessarily leads to skewed results since it is clear that the minorities which still rely on these “rare” languages daily are likely to face prejudice in many areas of the society. It would have been interesting to see if Whisper is perpetuating those biases.

## Conclusion and Recommendation

Whisper like several ARS algorithms tend to perform some biases with regards to certain groups of population. Our analysis has demonstrated that the algorithm works equally well regardless of the age of the speaker; however, the number of years that a speaker has been exposed to the English language does have an impact. There is also no evidence of gender bias and it is interesting to note that some language groups perform equally well or even better than English native speakers. As expected, larger models of Whisper generally perform better for all language groups.

For future research, it would also be insightful to test the large model, provided the availability of a hardware capable running it, as well as to have a more balanced and equal dataset wherein all languages are equally represented. In addition, it would also be interesting to be able to test its performance on people encountering speech difficulties, on infants and other social minorities relevant to our constantly evolving society.

## Goggle Colab Notebook

https://drive.google.com/file/d/1woJsBZ_C8raJPLkjy3_cTEDEOb9Z2ETe/view?usp=sharing

## References

Cámbara, G., Peiró-Lilja, A., Farrús, M., & Luque, J. (2021). English Accent Accuracy Analysis in a State-of-the-Art Automatic Speech Recognition System. arXiv preprint arXiv:2105.05041.

Feng, S., Kudina, O., Halpern, B. M., & Scharenborg, O. (2021). Quantifying bias in automatic speech recognition. arXiv preprint arXiv:2103.15122.

Garnerin, M., Rossato, S., & Besacier, L. (2021, August). Investigating the impact of gender representation in asr training data: a case study on librispeech. In 3rd Workshop on Gender Bias in Natural Language Processing (pp. 86-92). Association for Computational Linguistics.

Goldwater, S., Jurafsky, D., & Manning, C. D. (2010). Which words are hard to recognize? Prosodic, lexical, and disfluency factors that increase speech recognition error rates. Speech Communication, 52(3), 181-200.

Sawalha, M., & Abu Shariah, M. (2013). The effects of speakers' gender, age, and region on overall performance of Arabic automatic speech recognition systems using the phonetically rich and balanced Modern Standard Arabic speech corpus. In Proceedings of the 2nd Workshop of Arabic Corpus Linguistics WACL-2. Leeds.

Tatman, R. (2017, April). Gender and dialect bias in YouTube’s automatic captions. In Proceedings of the first ACL workshop on ethics in natural language processing (pp. 53-59).
