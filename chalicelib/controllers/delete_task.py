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
                return ({"message": "Tarefa não encontrada ou já foi excluída."})
            else:
                return {"message": f"Tarefa com ID {id_task} foi excluída com sucesso."}

        except Exception as e:
            return {"error": str(e)}
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
