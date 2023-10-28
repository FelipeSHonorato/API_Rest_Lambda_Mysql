from chalicelib.db.db_connection import DbConnection
from datetime import datetime
from chalicelib.errors.http_errors import HttpCustomErrors

class InsertTask:

    # Função responsável em inserir tarefas no sistema
    def insert_task(self, data):
        
        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

         # Instanciando classe de erros customizados
        customError = HttpCustomErrors()

        # Efetuando a pesistencia no banco de dados - excluindo tarefa
        try:
            description = data.json_body.get("descricao")
            
            if description:
                date_now = datetime.now().strftime("%Y/%m/%d")
                status = "Não concluída"
            
                sql = "INSERT INTO todolist (Descricao, Status, dataCriacao) VALUES (%s, %s, %s)"
                cursor.execute(sql, (description, status, date_now))
                db_connection.commit()

                return customError.action_successfully({"message":"Tarefa inserida com sucesso."})
            
            else:
                return customError.json_error("Informar uma descricao é obrigatório.")
            
        except Exception as e:
            return customError.server_error(e)
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)