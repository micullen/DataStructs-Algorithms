"""

## A Notebook investigating the correlations between some of the provided features within the json.

You may be required to run

`pip install -r requirements-pip.txt`

to install all the pip requirements. and just the one conda requirements below

`conda install -c plotly plotly-orca`


in your terminal.
"""

import pandas as pd
import plotly.express as px
import pycountry_convert as pc

from pandas import DataFrame


def read_data() -> DataFrame:
    # May need to adjust file path
    jsonlist = open('weather.json')
    df = pd.read_json(jsonlist, lines=True)
    jsonlist.close()

    # A very non-elegant way of separating each dictionary out into df columns
    df['weather'] = df['weather'].apply(lambda x: x[0])

    df['id'] = df['city'].apply(lambda x: x['id'])
    df['name'] = df['city'].apply(lambda x: x['name'])
    df['country'] = df['city'].apply(lambda x: x['country'])
    df['lon'] = df['city'].apply(lambda x: x['coord']['lon'])
    df['lat'] = df['city'].apply(lambda x: x['coord']['lat'])
    df['zoom'] = df['city'].apply(lambda x: x['zoom'])

    df['temp'] = df['main'].apply(lambda x: x['temp'])
    df['pressure'] = df['main'].apply(lambda x: x['pressure'])
    df['humidity'] = df['main'].apply(lambda x: x['humidity'])
    df['temp_min'] = df['main'].apply(lambda x: x['temp_min'])
    df['temp_max'] = df['main'].apply(lambda x: x['temp_max'])

    df['wind_speed'] = df['wind'].apply(lambda x: x['speed'])
    df['wind_deg'] = df['wind'].apply(lambda x: x['deg'])

    df['clouds'] = df['clouds'].apply(lambda x: x['all'])

    df['weather_id'] = df['weather'].apply(lambda x: x['id'])
    df['weather_main'] = df['weather'].apply(lambda x: x['main'])
    df['weather_description'] = df['weather'].apply(lambda x: x['description'])
    df['weather_icon'] = df['weather'].apply(lambda x: x['icon'])

    df = df.drop(['city', 'main', 'wind', 'weather'], axis='columns')

    return df


def add_continent(df: DataFrame) -> DataFrame:
    country_list = df['country'].to_list()
    invalid_countries = []
    valid_countries = []
    for country in set(country_list):
        try:
            valid_countries.append(pc.country_alpha2_to_continent_code(country))
        except:
            invalid_countries.append(country)

    # Get rid of invalid country codes, only losing 35 rows out of ~210000
    for country in invalid_countries:
        df = df.loc[df['country'] != country]

    df['continent'] = df['country'].apply(lambda x: pc.country_alpha2_to_continent_code(x))

    return df


df = read_data()
df = add_continent(df)

df['Latitude°'] = df['lat']
df['Temp°'] = df['temp']
df['Continent'] = df['continent']

x = "Latitude°"
y = "Temp°"

fig = px.scatter(df, x=x, y=y,
                 color="humidity", hover_name="country", facet_col="Continent",
                 range_x=[df[x].min(),df[x].max()],
                 range_y=[df[y].min(), df[y].max()], title="A Plot Displaying How Temperature Varies With Latitude and Humidity")
fig.show()
fig.write_image("whiteswandatacontinents.png")

"""
The images below plot temperature vs latitude, where each individual data point is a country,
each plot is a continent and the colour indicates the humidity at the time recorded.

As you would expect for each continent, as latitude nears 0, from negative or positive values, 
the temperature begins to increase. This is shown as the data points either lean towards 0 or plot 
an 'n' shape around 0. 

What's interesting is how the uppermost temperatures on latitude lines are accompanied by low humidity for Asia
Africa, Europe and Oceania. Whilst North America and South America, showed little correlation between humidity 
and temperature.

A negative to this plot is that the time of the recordings aren't all identical, however they were all recorded 
within ~5 minutes of each other so it would be relatively safe to assume that the time difference wouldn't have
skewed the results.
"""

