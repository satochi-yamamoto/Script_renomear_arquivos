# SCRIPT PARA RENOMEAR ARQUIVOS POR DATA
Este script utiliza Python para renomear os arquivos de uma pasta substituindo o nome pelo valor da data de criação. Para fazer isso, você pode usar a biblioteca os para manipular os arquivos e a biblioteca datetime para obter a data de criação. Certifique-se de que o Python esteja instalado em seu sistema.
Certifique-se de substituir "z:/fotos" pelo caminho da pasta em que você deseja renomear os arquivos. Este script irá renomear os arquivos na pasta especificada com base na data de criação no formato "AAAA-MM-DD_HH-MM-SS.extensao". Certifique-se de fazer um backup dos arquivos antes de executar o script, pois ele irá renomeá-los permanentemente.

renomear_v2.py 
Este script verifica se o novo nome já existe na pasta e, se existir, adiciona "_copiaX" ao nome, onde X é um número crescente para evitar colisões de nomes. Isso garantirá que os arquivos duplicados tenham nomes únicos na pasta.

O renomear_03.py 
Este script irá renomear os arquivos na pasta especificada, bem como em todas as subpastas recursivamente. Ele usa uma função recursiva chamada renomear_arquivos_em_pasta para lidar com as subpastas. Certifique-se de fazer um backup dos arquivos antes de executar o script, pois ele irá renomeá-los permanentemente.
