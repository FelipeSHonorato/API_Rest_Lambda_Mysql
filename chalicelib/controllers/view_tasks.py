from chalice import Response
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
                return Response(body={"message": "Não existem tarefas registradas."}, 
                                status_code= 404,
                                headers={'Content-Type': 'application/json'})
            tasks = []
            for row in rows:
                task = {
                    "ID": row[0],
                    "Descricao": row[1],
                    "Status": row[2],
                    "DataCriação": format_date(row[3])
                }
                tasks.append(task)
            return Response(body={"tarefas": tasks}, 
                            status_code= 200,
                            headers={'Content-Type': 'application/json'})

        except Exception as e:
            return Response(body={"error": str(e)}, 
                            status_code= 500,
                            headers={'Content-Type': 'application/json'})
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
            
