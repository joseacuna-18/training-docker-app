#Load libraries for data management
import pandas as pd
import numpy as np

#Load libraries for connecting with database
from sqlalchemy import create_engine

#Load libraries for managing json data
import requests
import json

#Define connection to Postgres Database
sql_engine = create_engine('postgresql+psycopg2://etl_user:etl_password@host.docker.internal/test_etl_db')

#Request list of pokemon games
str_url_pokemon_games = 'https://pokeapi.co/api/v2/generation/3/'
response_pokemon_games = requests.get(str_url_pokemon_games)

#Get the different pokemon versions games
dict_version_games = json.loads(response_pokemon_games.content)['version_groups']

#Convert into pandas DataFrame
df_version_games = pd.DataFrame(dict_version_games)

#Input execution date
df_version_games['date_exec'] = pd.Timestamp.now()

#Load into database
df_version_games.to_sql('games_history', con = sql_engine, if_exists = 'append', schema = 'poke_games')