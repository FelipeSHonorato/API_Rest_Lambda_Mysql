from chalice import Response
from chalicelib.db.db_connection import DbConnection

class EditTask:

    # Função responsável em editar tarefas no sistema
    def edit_task(self, id_task, data):

        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Efetuando a pesistencia no banco de dados - editando tarefa
        try:
            check_sql = "SELECT ID FROM todolist WHERE ID = %s"
            cursor.execute(check_sql, (id_task,))
            
            if cursor.rowcount == 0:
                return Response(body={"message": f"Nenhuma tarefa encontrada com o ID {id_task}."}, 
                                status_code= 404,
                                headers={'Content-Type': 'application/json'})
            else:
                description = data.json_body.get("descricao")
                status = data.json_body.get("status")

                if status not in ['Concluída', 'Não concluída']:
                    return Response(body={"message": "O status só pode ser modificado para status 'Concluída' ou 'Não concluída'."}, 
                                    status_code= 400,
                                    headers={'Content-Type': 'application/json'})
                
                else:
                    sql = "UPDATE todolist SET Descricao = %s, Status = %s WHERE ID = %s"
                    cursor.execute(sql, (description, status, id_task))
                    db_connection.commit()
                
                    return Response(body={"message": f"Tarefa com ID {id_task} atualizada com sucesso."}, 
                                    status_code= 200,
                                    headers={'Content-Type': 'application/json'})
 
        except Exception as e:
            return Response(body={"error": str(e)}, 
                            status_code= 500,
                            headers={'Content-Type': 'application/json'})
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)

