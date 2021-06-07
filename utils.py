import numpy as np 
import pandas as pd 

def region_pop() -> pd.DataFrame:
    """
    Clean the data. It returns region_population
    """
    # Load data
    xl_data_1 = pd.read_excel("./data/world population.xlsx", sheet_name=0, header=16)
    # Tidy the data i.e Convert from wide format to long format
    population = (
            pd.melt(xl_data_1, 
                    id_vars=['Index', 'Variant', 'Region, subregion, country or area *', 'Notes', 'Country code', 'Type', 'Parent code'],
                    var_name='Years',
                    value_name='Population(Thousands)')  
        )

    # clean the data
    population = population.copy()
    # replace 'NaNs' with 'null'
    population['Notes'] = population['Notes'].replace(np.nan, '')
    # convert to string
    population['Notes'] = population['Notes'].astype('string')
    # filter out Groups, Continents and Regions
    regions = ['Africa', 'Asia', 'Europe', 'Latin America and the Caribbean', 'Northern America', 'Oceania']
    region_population = population.loc[population['Region, subregion, country or area *'].isin(regions)]
    region_population = region_population.copy()
    # rename column
    region_population.rename(columns={'Region, subregion, country or area *': 'Region'}, inplace=True)
    # convert to datetime
    region_population['Years'] = pd.to_datetime(region_population['Years'])
    # replace '...' with '0'
    region_population['Population(Thousands)'] = region_population['Population(Thousands)'].replace('...', 0)
    # convert to int
    region_population['Population(Thousands)'] = region_population['Population(Thousands)'].apply(lambda x: int(x))

    return region_population


def ctry_pop() -> pd.DataFrame:
    """
    Clean the data. It returns country_population
    """
    # Load data
    xl_data_1 = pd.read_excel("./data/world population.xlsx", sheet_name=0, header=16)
    # Tidy the data i.e Convert from wide format to long format
    population = (
            pd.melt(xl_data_1, 
                    id_vars=['Index', 'Variant', 'Region, subregion, country or area *', 'Notes', 'Country code', 'Type', 'Parent code'],
                    var_name='Years',
                    value_name='Population(Thousands)')  
        )

    # clean the data
    population = population.copy()
    # replace 'NaNs' with 'null'
    population['Notes'] = population['Notes'].replace(np.nan, '')
    # convert to string
    population['Notes'] = population['Notes'].astype('string')
    # filter out Countries
    countries_population = population.loc[population['Type'] == 'Country/Area']
    countries_population = countries_population.copy()
    # rename column
    countries_population.rename(columns={'Region, subregion, country or area *': 'Country'}, inplace=True)
    # convert to datetime
    countries_population['Years'] = pd.to_datetime(countries_population['Years'])
    # convert to int
    countries_population['Population(Thousands)'] = countries_population['Population(Thousands)'].apply(lambda x: int(x))
    # drop column
    countries_population = countries_population.drop(columns=['Notes'])
    return countries_population


# if __name__ == '__main__':
#     countries = ctry_pop()
#     print(countries.head())
