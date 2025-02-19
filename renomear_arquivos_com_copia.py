import os
import datetime

pasta_origem = "c:\Minhas_imagens\Geral"  # Substitua pelo caminho da pasta de origem

def renomear_arquivo_com_verificacao(nome_arquivo, pasta_origem):
    caminho_completo = os.path.join(pasta_origem, nome_arquivo)

    if os.path.isfile(caminho_completo):
        data_criacao = datetime.datetime.fromtimestamp(os.path.getctime(caminho_completo))
        novo_nome = data_criacao.strftime("%Y-%m-%d_%H-%M-%S") + os.path.splitext(nome_arquivo)[1]

        # Verifique se o novo nome já existe na pasta
        contador = 1
        while os.path.exists(os.path.join(pasta_origem, novo_nome)):
            novo_nome = data_criacao.strftime("%Y-%m-%d_%H-%M-%S") + f"_copia{contador}" + os.path.splitext(nome_arquivo)[1]
            contador += 1

        novo_caminho = os.path.join(pasta_origem, novo_nome)
        os.rename(caminho_completo, novo_caminho)
        print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")

if not os.path.exists(pasta_origem):
    print(f"A pasta {pasta_origem} não existe.")
else:
    for nome_arquivo in os.listdir(pasta_origem):
        renomear_arquivo_com_verificacao(nome_arquivo, pasta_origem)
