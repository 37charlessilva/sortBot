import os
from pathlib import Path

pasta = "/home/charles/Documents/Projetos/sortBot/"
arquivos = os.listdir(pasta)  # lista tudo (arquivos + pastas)

for nome in arquivos:
    #caminho = os.path.join(pasta, nome)
    #if os.path.isfile(caminho):
    #    print("Arquivo:", caminho)
    # Vamos fazer u prefixo de 4 caracteres pra mover pra pasta certa
    # Fazer um divisão pra criar pastas(conteudo, listas, exercicios e programas caso tenha algum)
    # Verificar com uma api pra fazer backup pro drive e receber backup tambem
    # Colocar as pastas que vão ser criadas a flags e prefisos em um arquivo txt(talvez dois né pra subdividir)
    # Fazer uma hud pro app, Talvez as flags possam ser apenas numeros ai fica mais facil de verificar(tipo12 1 pra calulo e 2 pra exercicios)
    # caln pra calculonumerico
    if(nome[:4] == "Text"):

        print(f"arquivo {nome} movido pra pasta correta")
        new = Path(nome)

        new.rename("Pastatexte/"+nome[4:])
    
    # Computação gráfica

    # Sistemas Operacionais 

    # Ética e sociedade

    # Big data

    # Otimização em grafos