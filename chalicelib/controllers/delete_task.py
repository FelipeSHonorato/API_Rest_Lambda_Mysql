from chalice import Response
from chalicelib.db.db_connection import DbConnection

class DeleteTask:

    # Função responsável em deletar tarefas no sistema
    def delete_task(self, id_task):
        
        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Efetuando a pesistencia no banco de dados - excluindo tarefa
        try:
            sql = "DELETE FROM todolist WHERE ID = %s"
            cursor.execute(sql, (id_task,))
            db_connection.commit()

            if cursor.rowcount == 0:
                return Response(body={"message": "Tarefa não encontrada ou já foi excluída."}, 
                                status_code= 404,
                                headers={'Content-Type': 'application/json'})
            else:
                return Response(body={"message": f"Tarefa com ID {id_task} foi excluída com sucesso."}, 
                                status_code= 200,
                                headers={'Content-Type': 'application/json'})

        except Exception as e:
            return Response(body={"error": str(e)}, 
                    status_code=500,
                    headers={'Content-Type': 'application/json'})
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
