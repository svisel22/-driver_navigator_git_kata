import pandas as pd 

def female():
    # Read in Titanic dataset
    titanic_df = pd.read_csv('./data/titanic.csv') # always be in the -driver_navigator... folder

    # Filter to only include female passengers
    female_df = titanic_df[titanic_df['Sex'] == 'female']

    # Return filtered dataframe
    return female_df

print(female())