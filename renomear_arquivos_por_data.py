import os
import datetime

pasta_origem = "c:\Minhas_imagens\Geral"  # Substitua pelo caminho da pasta de origem

# Verifique se a pasta de origem existe
if not os.path.exists(pasta_origem):
    print(f"A pasta {pasta_origem} não existe.")
else:
    # Percorre todos os arquivos na pasta
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_completo = os.path.join(pasta_origem, nome_arquivo)
        
        # Verifique se o caminho é um arquivo
        if os.path.isfile(caminho_completo):
            data_criacao = datetime.datetime.fromtimestamp(os.path.getctime(caminho_completo))
            novo_nome = data_criacao.strftime("%Y-%m-%d_%H-%M-%S") + os.path.splitext(nome_arquivo)[1]
            novo_caminho = os.path.join(pasta_origem, novo_nome)
            
            # Renomeia o arquivo
            os.rename(caminho_completo, novo_caminho)
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")
