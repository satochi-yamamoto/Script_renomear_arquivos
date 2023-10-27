import os
import shutil

def mover_e_renomear_arquivo(caminho_origem, caminho_destino):
    contador = 1
    nome_arquivo = os.path.basename(caminho_origem)
    nome_base, extensao = os.path.splitext(nome_arquivo)
    while os.path.exists(caminho_destino):
        novo_nome = f"{nome_base}_Copia_{contador}{extensao}"
        caminho_destino = os.path.join(os.path.dirname(caminho_destino), novo_nome)
        contador += 1
    shutil.move(caminho_origem, caminho_destino)
    print(f"Arquivo movido e renomeado: {nome_arquivo} -> {os.path.basename(caminho_destino)}")

def mover_arquivos_jpg(pasta_origem, pasta_destino):
    for pasta_atual, _, arquivos in os.walk(pasta_origem):
        for nome_arquivo in arquivos:
            if nome_arquivo.lower().endswith(".jpg"):
                caminho_origem = os.path.join(pasta_atual, nome_arquivo)
                caminho_destino = os.path.join(pasta_destino, nome_arquivo)
                if os.path.exists(caminho_destino):
                    mover_e_renomear_arquivo(caminho_origem, caminho_destino)
                else:
                    shutil.move(caminho_origem, caminho_destino)
                    print(f"Arquivo movido: {nome_arquivo}")

pasta_origem = r"Z:\Minhas_imagens\Pasta_Fotos_Unificadas"
pasta_destino = r"Z:\Minhas_imagens\Geral"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

mover_arquivos_jpg(pasta_origem, pasta_destino)
