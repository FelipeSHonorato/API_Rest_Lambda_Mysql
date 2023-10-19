from chalicelib.db import DB_HOST
from chalicelib.db import DB_USER
from chalicelib.db import DB_PASS
from chalicelib.db import DB_NAME
import pymysql

class DbConnection:

    # Função para criar uma cursor e conexão com o banco de dados.
    def db_connection(self):
      
      
        try:
            connection = pymysql.connect(
                host=DB_HOST, 
                user=DB_USER, 
                passwd=DB_PASS, 
                db=DB_NAME
            )
            
            cursor = connection.cursor()
            return connection, cursor

        except Exception as e:
            return {"error": str(e)}
        
    # Função de fechamento de cursor e conexão com o banco.     
    def db_close(self, cursor, connection):
        cursor.close()
        connection.close()