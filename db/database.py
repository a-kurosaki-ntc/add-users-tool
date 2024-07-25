from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import certifi
from azure.identity import DefaultAzureCredential

import os
import dotenv
dotenv.load_dotenv()

SSL_CA = certifi.where()

def create_engine_with_token(token, username, hostname, database):
    url = f"mysql+pymysql://{username}:{token}@{hostname}/{database}"
    engine = create_engine(url, connect_args={'ssl_ca':  SSL_CA})
    return engine

cred = DefaultAzureCredential()
token = cred.get_token('https://ossrdbms-aad.database.windows.net').token
username = os.getenv('DB_USER')
hostname = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')

engine = create_engine_with_token(token, username, hostname, database)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()