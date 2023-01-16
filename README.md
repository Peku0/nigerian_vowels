# nigerian_vowels
A repository containing materials used for an acoustic analysis of F1, F2, and duration of stressed and unstressed vowels in Nigerian English. 

The code, phonetic data, and metadata shared in this repository have been used to perform statistical analysis of the differences between stressed and unstressed vowels in Nigerian English in their F1, F2, and duration to test for statistically significant differences to investigate whether vowel weakening occurs in Nigerian English. 

The phonetic data was extracted using Praat [1] scripting and Montreal Forced Aligner [2] based on a Nigerian English dictionary [3] and an acoustic model [4].

The two subfolders found in the main folder are:

* 'ForcedAlignment' - stores the 'main.py' file for statistical analysis and extracing metadata on phonetic features in the corpus, also stored in the same folder, the 'meas.py' file for data preprocessing, and the 'cache' folder containing .csv files with exported Phonetic features of speech, with the 'n1673719069_out-vowel-data-0.txt' file containing NORM-normalised [5] formant measurements (Watt and Fabricius modified method). 
* 'scripts' - stores the 'formant_meas' file with a Praat script used for automatic extraction of phonetic data from a corpus of speech.

One folder named 'data' containing recordings and orthographic transcription of Nigerian English speech has not been shared here.

## References
<a id="1">[1]</a> 
Boersma, Paul and Weenink, David. 2022. 
Praat: doing phonetics by computer [Computer program]. Version 6.3.03, retrieved 17 December 2022 from http://www.praat.org/

<a id="2">[2]</a> 
McAuliffe, Michael and Socolof, Michaela and Mihuc, Sarah and Wagner, Michael and Sonderegger, Morgan. 2017. 
”Montreal Forced Aligner: Trainable Text-Speech Alignment Using Kaldi.” 
Proc. Interspeech: 498-502, doi: 10.21437/Interspeech.2017-1386.

<a id="3">[3]</a> 
McAuliffe, Michael and Sonderegger, Morgan. 2022. 
English (Nigeria) MFA dictionary [Computer program]. Version 2.0.0, retrieved 25 November 2022 from https://mfa-models.readthedocs.io/en/latest/index.html.

<a id="4">[4]</a> 
McAuliffe, Michael and Sonderegger, Morgan. 2022a. 
English (Nigeria) MFA G2P model [Computer program]. Version 2.0.0, retrieved 25 November 2022 from https://mfa-models.readthedocs.io/en/latest/index.html.

<a id="5">[5]</a> 
Thomas, Erik R. and Tyler Kendall. 2007. 
NORM: The vowel normalization and plotting suite. [Online Resource: http://ncslaap.lib.ncsu.edu/tools/norm/]


