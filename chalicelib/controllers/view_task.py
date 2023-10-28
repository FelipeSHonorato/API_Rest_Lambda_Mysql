from chalicelib.db.db_connection import DbConnection
from chalice import Response
from chalicelib.utils.date_utils import format_date

class ViewTask:

    # Função responsável em visualizar uma determinada tarefa no sistema
    def view_task(self, id_task):

        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Efetuando a pesistencia no banco de dados - visualizando tarefa
        try:
            sql = "SELECT * FROM todolist WHERE ID = %s"
            cursor.execute(sql,(id_task))
            row = cursor.fetchone()

            if cursor.rowcount == 0:
                return Response(body={"message": "Tarefa não encontrada."}, 
                                status_code= 404,
                                headers={'Content-Type': 'application/json'})

            else:
                task = {
                    "ID": row[0],
                    "Descricao": row[1],
                    "Status": row[2],
                    "DataCriacao": format_date(row[3])
                }

            return Response(body={"tarefa": task},
                            status_code= 200,
                            headers={'Content-Type': 'application/json'})

        except Exception as e:
            return Response(body={"error": str(e)}, 
                            status_code= 500,
                            headers={'Content-Type': 'application/json'})

        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
