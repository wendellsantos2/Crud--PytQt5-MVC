import os

def converter(tipo_conversao: int):
    os.system("cls")
    if tipo_conversao == 0:
        caminho_arquivos = input('Insira o caminho dos arquivos:')
        if os.path.exists(fr"{os.getcwd()}\{caminho_arquivos}"):
            caminho_arquivos = fr"{os.getcwd()}\{caminho_arquivos}".replace("\\\\", "\\")
        os.system('cls')
        caminho_novo = input(f'Em qual pasta os arquivos devem ser colocados ?\nPasta Atual: {caminho_arquivos}\nPara voltar uma pasta digite -> ".."\n\nR:') 
        arquivos = [arquivo for arquivo in os.listdir(caminho_arquivos) if '.ui' in arquivo]
        if len(arquivos) > 0:
            os.system('cls')
            print(f'Os arquivos que podem ser convertidos são:')
            for indice in range(len(arquivos)):
                print(f'{indice} - {arquivos[indice]}')
            arquivos_converter = input("\n\nEx de resposta: 1, 3, 5, 9\n\nQuais arquivos deseja converter:")
            if arquivos_converter == "all":
                for arquivo in arquivos:
                    os.chdir(caminho_arquivos)
                    os.system(f'pyuic5 {arquivo} -o {arquivo.split(".")[0]}.p1y')
            else:
                for arquivo in arquivos_converter.split(','):
                    os.chdir(caminho_arquivos)
                    os.system(f'pyuic5 {arquivos[arquivo]} -o {arquivos[arquivo].split(".")[0]}.py')
            while True != False:
                try:
                    arquivos_convertidos = [arquivo for arquivo in os.listdir() if ".py" in arquivo != "Conversor.py"]
                    for arquivo in arquivos_convertidos:
                        os.system(f'move /Y {arquivo} {caminho_novo}')
                        os.system('cls')
                    break
                except Exception:
                    print('Pasta não encontrada\nTente novamente')
        print("Procedimento concluído com sucesso")
    elif tipo_conversao == 1:
        try:
            # Usado no diretório atual da Workspace
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.split(".")[-1] == "py"]
            print("Qual arquivo gostaria de converter para executavel?")
            for indice_lista in range(len(arquivos)):
                print(f"{(indice_lista + 1)} - {arquivos[indice_lista]}")
                if indice_lista == (len(arquivos) - 1):
                    print(f"0 - Cancelar")
            arquivo_escolhido = int(input("R: -> ")) - 1
            if arquivo_escolhido == -1:
                raise Exception("Operação Cancelada!")
            novo_nome_arquivo = arquivos[arquivo_escolhido].split(".")[0]+".pyw"
            os.system(f"rename {arquivos[arquivo_escolhido]} {novo_nome_arquivo}")
            os.system(f"python -m PyInstaller --onefile {novo_nome_arquivo}")
            os.system(f"rename {novo_nome_arquivo} {arquivos[arquivo_escolhido]}")
            os.system(f"move /Y .\\dist\\{arquivos[arquivo_escolhido].split('.')[0]}.exe .\\")
            os.rmdir(".\\dist")
            os.system("cls")
            print('Procedimento concluído com sucesso')
        except Exception as e:
            print(str(e))

    else:
        raise Exception("Comando não encontrado")

if __name__ == '__main__':
    converter((int(input('Deseja converter que tipo de arquivo ?:\n1)UI\n2)PyInstaller\nR:')) - 1))
