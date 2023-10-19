from chalicelib.db.db_connection import DbConnection

    # Função para criar uma cursor e conexão com o banco de dados.
def db_creation():
      
    connection = DbConnection()
    db_connection, cursor = connection.db_connection()
    
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todolist (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao VARCHAR(255) NOT NULL,
                status ENUM('Não concluída', 'Concluída') NOT NULL,
                dataCriacao DATE NOT NULL
            )
        """)
        
        db_connection.commit()

        print ("Tabela e entidades criadas com sucesso")
        
    except Exception as e:
        print(f"Erro ao criar a tabela: {str(e)}")
    
    # Chamando função para fechamento do cursor e conexão com o banco
    finally:
        connection.db_close(cursor, db_connection)

if __name__ == "__main__":
    db_creation()