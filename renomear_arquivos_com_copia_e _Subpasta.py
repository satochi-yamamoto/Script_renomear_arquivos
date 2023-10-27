import os
import datetime

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

def renomear_arquivos_em_pasta(pasta):
    for nome_arquivo in os.listdir(pasta):
        renomear_arquivo_com_verificacao(nome_arquivo, pasta)

    for nome_subpasta in os.listdir(pasta):
        caminho_subpasta = os.path.join(pasta, nome_subpasta)
        if os.path.isdir(caminho_subpasta):
            renomear_arquivos_em_pasta(caminho_subpasta)

pasta_origem = "Z:\Minhas_imagens\Pasta_Fotos_Unificadas"  # Substitua pelo caminho da pasta de origem

if not os.path.exists(pasta_origem):
    print(f"A pasta {pasta_origem} não existe.")
else:
    renomear_arquivos_em_pasta(pasta_origem)
