"""
A Notebook investigating the correlations between some of the provided features within the json.
You may be required to run pip install seaborn in your terminal for usage of seaborn here.
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from pandas import DataFrame


def read_data() -> DataFrame:
    # May need to adjust file path
    jsonlist = open('whiteswandatatest.json')
    df = pd.read_json(jsonlist)

    return df


def clean_data(df: DataFrame) -> DataFrame:
    # Create a column for the number of friends
    df['#friends'] = df['friends'].str.len()

    # Create a column for a persons number of unread messages
    df['#msgs'] = df['greeting'].str.extract('(\d+)')

    # Create column for number of tags
    df['#tags'] = df['tags'].str.len()

    # Create dictionaries to replace words with numbers for easier analysis
    gender = {'male': 1, 'female': 2}
    fruit = {'banana': 1, 'strawberry': 2, 'apple': 3}
    eye = {1: 1, 'blue': 2, 'brown': 3, 'green': 4}

    # Replace words we want with the numbers specified above
    df['eyeColor'] = df['eyeColor'].fillna(1)
    df['eyeColor'] = [eye[item] for item in df['eyeColor']]

    df['fruit'] = [fruit[item] for item in df['favoriteFruit']]
    df['gender'] = [gender[item] for item in df['gender']]

    # Drop columns we don't want
    df = df.drop(['guid', 'picture', 'registered', 'phone', 'email', 'name', 'tags', 'address',
                  'greeting', 'friends', 'company', 'longitude', 'latitude', 'isActive', '#tags'], axis='columns')

    return df

raw_df = read_data()
clean_df = clean_data(raw_df)

# Define popular people as having friends of 2 or 3, and unpopular people as having friends of 1 or 2.
pop_people = clean_df.loc[clean_df['#friends'] > 1]
unpop_people = clean_df.loc[clean_df['#friends'] <= 1]

# Mean age is 29.8 so split
pop_young_people = pop_people.loc[pop_people['age'] <= 29.8]
unpop_young_people = unpop_people.loc[unpop_people['age'] <= 29.8]


# Compute the correlations of the remaining features
young_pop = pop_young_people.corr(method='spearman')
young_unpop = unpop_young_people.corr(method='spearman')

# Plot!
fig, (ax1, ax2) = plt.subplots(1,2)
sns.heatmap(young_unpop, xticklabels=young_unpop.columns, yticklabels=young_unpop.columns, annot=True, ax=ax1, fmt='.2f')
sns.heatmap(young_pop, xticklabels=young_pop.columns, yticklabels=young_pop.columns, annot=True, ax=ax2, fmt='.2f')
ax1.set_title('Young People With Below Average #Friends')
ax2.set_title('Young People With Above Average #Friends')
fig.suptitle('Comparisons of Correlations of Features Between Young People', fontsize=16)
plt.savefig("WhiteSwanData")

"""
Correlations can give you an edge in a market, whether that be targeted ads of young unpopular people with 
fruit, or when assetts with a long history of a correlation have diverged and you believe they will pair again.

The Seaborn plot itself is also very easy to digest, you don't have to trawl through the table to find the 
interesting correlations.

The cons of correlations would be that some could be take them as causation. They're also not eternal
and should not be treated as such. Bitcoin is often correlated to the S&P500, but blindly following
every move pulled by the S&P500 would most likely end badly.

Whilst the correlations found between features in young people with below average friends is noticeably more than
those with above average friends, I'd be wary to trust the results given the sample size of roughly 100 for each table.
"""





