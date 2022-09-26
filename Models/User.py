from Database.Connection import Conexao


class User():

        def __init__(self,conn):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = """"""
            cursor.execute(sql)
            conn.commit()
 
         
            
        def getUser(self, login, senha):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = """SELECT * FROM usuario WHERE login = %s AND senha = %s"""
            cursor.execute(sql, (login,senha))
            result = cursor.fetchone()
            return result
    
        def inserir_usuario(self,login,senha):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = """insert into usuario(login,senha,fk_permissao_id_permissao) values (%s, %s, '5')"""
            cursor.execute(sql, (login,senha))
            conn.commit()
            
        def inserir_usuario_master(self,login,senha,permissao):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = """insert into usuario(login,senha,fk_permissao_id_permissao) values (%s, %s, %s)"""
            cursor.execute(sql, (login,senha,permissao))
            conn.commit()
            
        def inserir_adm_usuario(self,login,senha):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = """INSERT INTO usuario (login,senha) VALUES (%s,%s)"""
            cursor.execute(sql, (login,senha))
            conn.commit()    
            
        def consultar_usuario(self, login):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = f"""SELECT * FROM usuario WHERE login= '{login}'"""
            cursor.execute(sql)
            result = cursor.fetchone()
            return result     
             
    
        @staticmethod
        def listar_usuarios():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,fk_permissao_id_permissao FROM usuario where fk_permissao_id_permissao = '5' ")
                result = cursor.fetchall()
                return result
            except:
                pass
                      
        @staticmethod
        def listar_todos():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,senha,fk_permissao_id_permissao FROM usuario")
                result = cursor.fetchall()
                return result
            except:
                pass  
            
        @staticmethod
        def listar_usuario_permissao():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,fk_permissao_id_permissao FROM usuario where fk_permissao_id_permissao")
                result = cursor.fetchall()
                return result
            except:
                pass      
            
              
        
        @staticmethod
        def listar_usuario():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,fk_permissao_id_permissao FROM usuario where fk_permissao_id_permissao = '5'  ")
                result = cursor.fetchall()
                return result
            except:
                pass  
          
        @staticmethod
        def listar_adm():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,senha,fk_permissao_id_permissao FROM usuario where fk_permissao_id_permissao = '5'")
                result = cursor.fetchall()
                return result
            except:
                pass      
            
            
        @staticmethod
        def listar_tela_adm():
            try:
                conn = Conexao.connection()
                cursor = conn.cursor()
                cursor.execute("SELECT id_usuario,login,fk_permissao_id_permissao FROM usuario where fk_permissao_id_permissao = '5' or ")
                result = cursor.fetchall()
                return result
            except:
                pass        
            
        def atualizar_tela_adm(self,id,login,senha):
            conn = Conexao.connection()
            cursor = conn.cursor()
            #sql = f"UPDATE product SET name = '{name}', price = '{price}', category = '{category}' WHERE cod = '{cod}'  "
            sql = f"UPDATE usuario SET login = '{login}', senha = '{senha}' where id_usuario = '{id}'   "
            cursor.execute(sql)
            conn.commit()    
            
        def atualizar_usuario_master(self,id,login,senha,permissao):
            conn = Conexao.connection()
            cursor = conn.cursor()
            #sql = f"UPDATE product SET name = '{name}', price = '{price}', category = '{category}' WHERE cod = '{cod}'  "
            sql = f"UPDATE usuario SET login = '{login}', senha = '{senha}', fk_permissao_id_permissao = '{permissao}' where id_usuario = '{id}'   "
            cursor.execute(sql)
            conn.commit() 
                 
        def deletar_usuario(self,id):
            conn = Conexao.connection()
            cursor = conn.cursor()
            sql = f"""DELETE FROM usuario WHERE id_usuario ='{id}'"""
            cursor.execute(sql)
            conn.commit()
            
              
            