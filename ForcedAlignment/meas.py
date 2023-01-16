from os.path import join
import pandas as pd

# THIS SCRIPT IS USED TO CREATE A MASTER .CSV FILE WITH ALL PRAAT-BASED VOWEL MEASUREMENTS FROM ALL SPEAKERS

formantsdf = pd.DataFrame()

# Iterate through results dataframes
for dataframe in ('results_00610.csv', 'results_01208.csv', 'results_01523.csv', 'results_02121.csv', 'results_02436.csv', 'results_02484.csv', 'results_03349.csv', 'results_03397.csv', 'results_04310.csv', 'results_08784.csv'):

    resdf = join('..', 'ForcedAlignment', 'cache', dataframe)
    resdf = pd.read_csv(resdf)
    data = [formantsdf, resdf]
    formantsdf = pd.concat(data)

# Define the list of vowels present in Nigerian English
vowel_list = ['i', 'iː', 'u', 'uː', 'e', 'ʊ', 'o', 'ɛ', 'ɛː', 'ɜ', 'ɔ', 'a', 'aː']

# Remove data about consonantal sounds from the dataframe
formantsdf = formantsdf[
    formantsdf.phoneme.isin(vowel_list)
]

# Export data to a .csv file

formantsdf.to_csv('vowel_meas.csv', sep='\t')