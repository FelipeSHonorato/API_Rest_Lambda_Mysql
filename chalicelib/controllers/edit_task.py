from chalicelib.db.db_connection import DbConnection
from chalicelib.errors.http_errors import HttpCustomErrors

class EditTask:

    # Função responsável em editar tarefas no sistema
    def edit_task(self, id_task, data):

        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Instanciando classe de erros customizados
        customError = HttpCustomErrors()

        # Efetuando a pesistencia no banco de dados - editando tarefa
        try:
            check_sql = "SELECT ID FROM todolist WHERE ID = %s"
            cursor.execute(check_sql, (id_task,))
            
            if cursor.rowcount == 0:
                return customError.not_found_error(f"Nenhuma tarefa encontrada com o ID {id_task}.")
            
            else:
                description = data.json_body.get("descricao")
                status = data.json_body.get("status")

                if status not in ['Concluída', 'Não concluída']:
                    return customError.json_error("O status só pode ser modificado para status 'Concluída' ou 'Não concluída'.")
                
                else:
                    sql = "UPDATE todolist SET Descricao = %s, Status = %s WHERE ID = %s"
                    cursor.execute(sql, (description, status, id_task))
                    db_connection.commit()
                
                    return customError.action_successfully({"message":f"Tarefa com ID {id_task} atualizada com sucesso."})
                
        except Exception as e:
            return customError.server_error(e)
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)

