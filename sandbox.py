from pwinput import pwinput
from sqlalchemy import create_engine
import pandas as pd


def connect_to_database():
    print('Connecting to Azure SQL database.')
    print('When prompted please enter username and password provided by email...')
    
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'demo-sql-azure.database.windows.net'
    database = 'az-demo-mssql-db'
    user = input('Enter Username: ')
    password = pwinput('Enter Password: ', mask="*")

    connection_string = f'mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}'
    engine = create_engine(connection_string)
    print('Checking connection...')
    try:
        engine.connect()
        engine.dispose()
        print('Connection established.')
        print('Engine can be used for further db connections.')
    except Exception as e:
        error_message = str(e)
        if 'Login failed for user' in error_message:
            print('Invalid username or password. Please try again.')
        elif 'Cannot open database' in error_message:
            print('The specified database does not exist or is unavailable.')
        elif 'pyodbc.InterfaceError' in error_message:
            print('Error with the ODBC driver. Ensure it is installed and correctly specified.')
        elif 'network-related' in error_message or 'server was not found' in error_message:
            print('Network issue: Unable to connect to the server. Check your connection and server name.')
        else:
            print(f'An unknown error occurred: {error_message}')
    
    return engine





