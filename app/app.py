#Load libraries for data management
import pandas as pd
import numpy as np
import os

#Load libraries for connecting with database
from sqlalchemy import create_engine

#Load libraries for managing json data
import requests
import json

#Obtain the secrets to connect to SQL server
secret_path = os.environ.get('SECRET_PATH', '/app/secret/secret.json')

with open(secret_path, 'r') as f:
    secrets = json.load(f)

#Define connection to Postgres Database
sql_engine = create_engine(f"postgresql+psycopg2://{secrets['db_user']}:{secrets['db_password']}@host.docker.internal/test_etl_db")

#Request list of pokemon games
str_url_pokemon_games = 'https://pokeapi.co/api/v2/generation/5/'
response_pokemon_games = requests.get(str_url_pokemon_games)

#Get the different pokemon versions games
dict_version_games = json.loads(response_pokemon_games.content)['version_groups']

#Convert into pandas DataFrame
df_version_games = pd.DataFrame(dict_version_games)

#Input execution date
df_version_games['date_exec'] = pd.Timestamp.now()

#Load into database
df_version_games.to_sql('games_history', con = sql_engine, if_exists = 'append', schema = 'poke_games')