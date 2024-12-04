from sqlalchemy import create_engine

class PySqlConnector():
    
    def py_sql_connector():
        
        username = 'root'
        password = 'FzEqefKdVQLQ'
        host = '127.0.0.1'
        port = '3306'
        database = 'autodoc_dev_test'
        
        connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)
        
        return engine