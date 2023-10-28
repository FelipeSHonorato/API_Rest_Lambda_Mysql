from chalice import Response
from chalicelib.db.db_connection import DbConnection
from datetime import datetime

class InsertTask:

    # Função responsável em inserir tarefas no sistema
    def insert_task(self, data):
        
        # Instanciando classe de conexão e recebendo conexão e cursor
        connection = DbConnection()
        db_connection, cursor = connection.db_connection()

        # Efetuando a pesistencia no banco de dados - excluindo tarefa
        try:
            description = data.json_body.get("descricao")
            
            if description:
                date_now = datetime.now().strftime("%Y/%m/%d")
                status = "Não concluída"
            
                sql = "INSERT INTO todolist (Descricao, Status, dataCriacao) VALUES (%s, %s, %s)"
                cursor.execute(sql, (description, status, date_now))
                db_connection.commit()

                return Response(body={"message": "Tarefa inserida com sucesso."}, 
                                status_code= 200,
                                headers={'Content-Type': 'application/json'})
 
            else:
                return Response(body={"message": "Campo 'descricao' é obrigatório."}, 
                                status_code= 400,
                                headers={'Content-Type': 'application/json'})

        except Exception as e:
             return Response(body={"error": str(e)}, 
                            status_code= 500,
                            headers={'Content-Type': 'application/json'})
        
        # Chamando função para fechamento do cursor e conexão com o banco
        finally:
            connection.db_close(cursor, db_connection)
            