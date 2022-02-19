import pandas as pd
import json
import ast

#
# file = open('weather.json')
# array = file.readlines()
# for value in array:
#     load_val = json.loads(value)
#     load_val['weather'] = load_val['weather'][0]
#
# df = pd.DataFrame(array)
# x = df

df = pd.read_json('weather.json', lines=True)

#dict_df = pd.DataFrame([ast.literal_eval(i) for i in df.city.values])

df['id'] = df['city'].apply(lambda x: x['id'])
df['name'] = df['city'].apply(lambda x: x['name'])
df['country'] = df['city'].apply(lambda x: x['country'])
df['lon'] = df['city'].apply(lambda x: x['coord']['lon'])
df['lat'] = df['city'].apply(lambda x: x['coord']['lat'])
df['zoom'] = df['city'].apply(lambda x: x['zoom'])

df['time'] = df['time']

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

