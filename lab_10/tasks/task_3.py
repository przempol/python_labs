import filecmp
import pathlib
from typing import Union

import pandas as pd
from os import listdir
from os.path import isfile, join


API_URL = 'https://www.metaweather.com/api/'


def concat_data(path: Union[str, pathlib.Path],):
    df: pd.DataFrame = pd.DataFrame()

    for file in listdir(path):
        if isfile(join(path, file)):
            current_day = int(file.split('_')[2].split('.')[0])

            data: pd.DataFrame = pd.read_csv(pathlib.Path(path) / file)
            data = data[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility',
                         'wind_direction_compass', 'wind_direction', 'wind_speed']]
            data = data.rename(columns={'the_temp': 'temp'})
            data_created = pd.to_datetime(data.created)
            data = data[data_created.dt.day == current_day]
            df = df.append(data)

    df = df.sort_values(by=['created'])
    df['created'] = pd.to_datetime(df['created']).dt.strftime('%Y-%m-%dT%H:%M')

    df.to_csv("{}.csv".format(path), index=False)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
