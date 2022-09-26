import mysql.connector
class Conexao():
    
    def connection():
        conn = mysql.connector.connect(
            host="localhost", port=3306, user="root",
            password="", db="projeto"
        )
        
        print('Database is Connected!')
        
        return conn