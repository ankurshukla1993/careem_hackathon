import sqlalchemy
from sqlalchemy import Table, Column, String, Float, Integer, ForeignKeyConstraint

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'aman'
DB_HOST = 'localhost'
DB_PORT = 5432


def create_db_tables(connection, meta):
    if not connection.dialect.has_table(connection, 'user_info'):
        user = Table('user_info', meta,
            Column('id', Integer, autoincrement=True, primary_key=True),
            Column('name', String, nullable=False),
            Column('country', String),
            Column('phone_number', String, nullable=False),
            Column('email_address', String),
            Column('password', String),
            Column('rating', Float),
            Column('type', String),
        )

    if not connection.dialect.has_table(connection, 'comments'):
        comments = Table('comments', meta,
            Column('id', Integer, autoincrement=True, primary_key=True),
            Column('comment', String),
            Column('user_id', Integer),
            Column('ride_id', Integer),
            ForeignKeyConstraint(['user_id'], ['user_info.id'])
        )

    # Create the above tables
    meta.create_all(connection)


def create_db_connection():
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    connection = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=connection, reflect=True)
    create_db_tables(connection, meta)
    return connection, meta

