from subprocess import *
import platform
import sys
import io
import os

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

#Logo
print("    __  __               ___                ")
print("   / / / / ___  __  __  / _ \     __  __  _____  ____")
print(GREEN+"  / /_/ / / _ \/ / / / / /_\ \   / /_/ / /_  _/ /   /"+RESET)
print(" /_____/ /_/ \__/ /_/ /_/   \_\ /_____/   /_/  /___/")
print("------------------------------------------------------")
#logo

print("Bem vindo a o UnixAutomate v0.1!")
print("O shell para iniciantes em terminal linux.")
print("------------------------------------------------------")

print("Digite")
print("")
print("*"+GREEN+"updatemenu "+RESET+"para ir a o menu de atualizações")
print("*"+GREEN+"exit "+RESET+"para sair do sistema")

def updatemenu(): # menu de update

    print("")
    print("Digite" + GREEN + " update " + RESET + "para Atualizar e instalar atualizações")
    print("Digite" + GREEN + " sysupdate " + RESET + "para atualizar versão do sistema")
    print("Digite" + GREEN + " exit " + RESET + "para sair do sistema")
    print("")

    def update():
        call(["sudo", "apt-get", "update"])
        call(["sudo", "apt-get", "upgrade"])

    def sysupdate():
        call(["sudo", "apt-get", "update"])
        call(["sudo", "apt-get", "upgrade"])
        call(["sudo","do-release-upgrade"])

    def readsysversion():
        os.chdir("/etc") #Funciona apenas em distros linux, não consegui fazer de outra forma.
        f = io.open("os-release", "r") #io.chdir não funciona então importamos as duas frameworks (os e io).
        lines = f.readlines() #Lê as linhas do arquivo de texto.
        linha = lines[4] #Seleciona qual é a linha do texto.
        char = linha[13:29] #Seleciona do caracter na posição [13] até a [29].
        return char #Retorna o resultado da função que é o nome e versão do os.

    def updateinput():
        a = input('>: ')
        if a == "update":
            update()

        elif a == "return":
            mainmenu()

        elif a == "sysupdate":
            print("Tem certeza que quer atualizar para a versão mais recente?")
            print("Versão atual, "+ GREEN +readsysversion()+ RESET)
            b = input('s/n: ')
            if (b == "s"):
                sysupdate()
                mainmenu()
                
            elif (b == "n"):
                print("Operação abortada")
                mainmenu()

        else:
            cmdnfound()

    updateinput()

def mainmenu():
    mn = input('>: ')
    if (mn == "updatemenu"):
        updatemenu()

    elif (mn == "exit"):
        sys.exit()

    else:
        cmdnfound()
        mainmenu()

def cmdnfound():
        print(RED + "Comando não encontrado!" + RESET)
        mainmenu()




mainmenu()
    
