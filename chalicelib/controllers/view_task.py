from chalicelib.db.db_connection import DbConnection
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
                return {"message": "Tarefa não encontrada"}

            else:
                task = {
                    "ID": row[0],
                    "Descricao": row[1],
                    "Status": row[2],
                    "DataCriacao": format_date(row[3])
                }

            return {"tarefa": task}

        except Exception as e:
            return {"error": str(e)}

        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
