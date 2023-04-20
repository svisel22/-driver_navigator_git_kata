import pandas as pd 

def male():
    # Read in Titanic dataset
    titanic_df = pd.read_csv('./data/titanic.csv') # always be in the -driver_navigator... folder

    # Filter to only include female passengers
    df = titanic_df[titanic_df['Sex'] == 'male']

    # Return filtered dataframe
    return df

print(male())