import os
import tarfile

pasta = 2017
diretorio= os.getcwd()
					
file = tarfile.open(diretorio + "/" + str(pasta) + ".tar.gz") #Descompacta o primeiro arquivo

file.extractall(diretorio) #Vai pro diretorio que esta o sript (descompacta)

file.close()

os.chdir(str(pasta))# Vai pra primeira pasta (2017)


pasta-=1

while pasta >=0:
	try:
		file = tarfile.open(os.getcwd() + "/" + str(pasta) + ".tar.gz") 

		file.extractall(diretorio) #Extrai tudo pro diretorio inicial

		file.close()

		os.chdir(diretorio) #Volta pro diretorio inicial
		os.chdir(str(pasta)) #Vai pra pasta q foi extraida

		pasta-=1 

	except:
		print("Acabou!")
