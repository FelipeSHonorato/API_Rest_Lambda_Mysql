from chalicelib.db.db_connection import DbConnection
from chalicelib.utils.date_utils import format_date
from datetime import datetime, date

class ViewTasks:

    # Função responsável em visualizar as tarefas no sistema
    def view_tasks(self):

        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Efetuando a pesistencia no banco de dados - visualizando tarefas
        try:
            sql = "SELECT * FROM todolist"
            cursor.execute(sql)
            rows = cursor.fetchall()

            if not rows:
                return {"message": "Não existem tarefas registradas"}
            tasks = []
            for row in rows:
                task = {
                    "ID": row[0],
                    "Descricao": row[1],
                    "Status": row[2],
                    "DataCriação": format_date(row[3])
                }
                tasks.append(task)
            return {"tarefas": tasks}

        except Exception as e:
            return {"error": str(e)}
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)

            
