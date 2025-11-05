import os
from pathlib import Path

file = "config.txt" # Arquivo de configuração
flag = ["root", "source"] # flags com as paradas
data = {} # Os dados que vão vir dos arquivos

    
def read():
    """Le o arquivo de configuração, para receber os nomes de pastas e subpastas além do diretorio raiz, onde sera criado as pastas e movido os arquivos"""
    with open(file, "r", encoding="utf-8") as f:
        for lines in f:
            line = lines.strip()
            if(line):

                if(line.startswith("@")):
                    currentFlag = line[1:]
                    if(currentFlag in flag):
                        data[currentFlag] = ""
                    else:
                        data[currentFlag] = []
                        
                else:
                    if(currentFlag in flag):
                        data[currentFlag] = line
                    else:
                        data[currentFlag].append(line)


read()

arquivos = os.listdir(data["source"])  # lista tudo (arquivos + pastas)

for nome in arquivos:
    if(nome[:4] == "Text"):

        print(f"arquivo {nome} movido pra pasta correta")
        new = Path(nome)

        new.rename("Pastatexte/"+nome[4:])
    print(nome)
    
    # Computação gráfica

    # Sistemas Operacionais 

    # Ética e sociedade

    # Big data

    # Otimização em grafos