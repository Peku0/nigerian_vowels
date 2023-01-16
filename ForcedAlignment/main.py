import pandas as np
import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.stats import median_test
from matplotlib import colors
from sklearn.cluster import KMeans

# Read the .csv file with stress parameter, speaker data, and normalised vowel measurements
formantsdf = join('..', 'ForcedAlignment', 'cache', 'stress_and_normalised_vowels.csv')
formantsdf = pd.read_csv(formantsdf)

# Create separate data frames for stressed and unstressed tokens
stressed_formantsdf = formantsdf.loc[formantsdf['stress'] == 1]

unstressed_formantsdf = formantsdf.loc[formantsdf['stress'] == 0]

# Create vowel spaces as dataframes for each phoneme for each stressing parameter
si_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['i'])
]

ui_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['i'])
]

se_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['e'])
]

ue_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['e'])
]

sface_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['ɛ'])
]

uface_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['ɛ'])
]

sa_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['a'])
]

ua_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['a'])
]

su_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['u'])
]

uu_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['u'])
]

sul_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['uː'])
]

uul_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['uː'])
]

sfoot_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['ʊ'])
]

ufoot_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['ʊ'])
]

so_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['o'])
]

uo_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['o'])
]

sthought_vowel_space = stressed_formantsdf[
    stressed_formantsdf.phoneme.isin(['ɔ'])
]

uthought_vowel_space = unstressed_formantsdf[
    unstressed_formantsdf.phoneme.isin(['ɔ'])
]


# Define a function to create plot for vowel spaces
def plot(s_vowel_space, u_vowel_space, vowel):
    """x = vowel_space['duration']
    y = vowel_space['F0']
    z = vowel_space['intensity']"""
    f1s = s_vowel_space['F1/S(F1)']
    f2s = s_vowel_space['F2/S(F2)']
    f1u = u_vowel_space['F1/S(F1)']
    f2u = u_vowel_space['F2/S(F2)']

    plt.scatter(f2s, f1s, s=4, label='stressed')
    plt.scatter(f2u, f1u, s=4, label='unstressed')
    plt.xlabel('F2 (normalised)')
    plt.ylabel('F1 (normalised)')
    plt.title(vowel)
    plt.legend()
    plt.grid(True)
    plt.show()


# Plot all vowel spaces
plot(si_vowel_space, ui_vowel_space, 'i')
plot(se_vowel_space, ue_vowel_space, 'e')
plot(sface_vowel_space, uface_vowel_space, 'ɛ')
plot(sa_vowel_space, ua_vowel_space, 'a')
plot(su_vowel_space, uu_vowel_space, 'u')
plot(sul_vowel_space, uul_vowel_space, 'uː')
plot(sfoot_vowel_space, ufoot_vowel_space, 'ʊ')
plot(so_vowel_space, uo_vowel_space, 'o')
plot(sthought_vowel_space, uthought_vowel_space, 'ɔ')

# Create empty lists to collect metadata

i_metadata = []
e_metadata = []
face_metadata = []
a_metadata = []
u_metadata = []
ul_metadata = []
foot_metadata = []
o_metadata = []
thought_metadata = []


# Define a function to test for a difference in medians between stressed and unstressed vowel tokens

def acoustic_test(s_vowel_space, u_vowel_space):
    f1s = s_vowel_space['F1/S(F1)']
    f2s = s_vowel_space['F2/S(F2)']
    f1u = u_vowel_space['F1/S(F1)']
    f2u = u_vowel_space['F2/S(F2)']
    durs = s_vowel_space['duration']
    duru = u_vowel_space['duration']

    res_f1 = median_test(f1s, f1u)
    res_f2 = median_test(f2s, f2u)
    res_dur = median_test(durs, duru)

    res_f1 = res_f1[0:3]
    res_f2 = res_f2[0:3]
    res_dur = res_dur[0:3]

    result = pd.DataFrame([res_f1, res_f2, res_dur], columns = ['statistic', 'pvalue', 'median'])
    result.index = ['F1', 'F2', 'duration']

    return result

# Assemble metadata for each vowel

i_metadata = acoustic_test(si_vowel_space, ui_vowel_space)
i_metadata = pd.DataFrame(i_metadata)

e_metadata = acoustic_test(se_vowel_space, ue_vowel_space)
e_metadata = pd.DataFrame(e_metadata)

face_metadata = acoustic_test(sface_vowel_space, uface_vowel_space)
face_metadata = pd.DataFrame(face_metadata)

a_metadata = acoustic_test(sa_vowel_space, ua_vowel_space)
a_metadata = pd.DataFrame(a_metadata)

u_metadata = acoustic_test(su_vowel_space, uu_vowel_space)
u_metadata = pd.DataFrame(u_metadata)

ul_metadata = acoustic_test(sul_vowel_space, uul_vowel_space)
ul_metadata = pd.DataFrame(ul_metadata)

foot_metadata = acoustic_test(sfoot_vowel_space, ufoot_vowel_space)
foot_metadata = pd.DataFrame(foot_metadata)

o_metadata = acoustic_test(so_vowel_space, uo_vowel_space)
o_metadata = pd.DataFrame(o_metadata)

thought_metadata = acoustic_test(sthought_vowel_space, uthought_vowel_space)
thought_metadata = pd.DataFrame(thought_metadata)

# Export metadata to .csv files

i_metadata.to_csv('i_metadata.csv')
e_metadata.to_csv('e_metadata.csv')
face_metadata.to_csv('face_metadata.csv')
a_metadata.to_csv('a_metadata.csv')
u_metadata.to_csv('u_metadata.csv')
ul_metadata.to_csv('ul_metadata.csv')
foot_metadata.to_csv('foot_metadata.csv')
o_metadata.to_csv('o_metadata.csv')
thought_metadata.to_csv('thought_metadata.csv')