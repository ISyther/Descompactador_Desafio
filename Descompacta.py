import os
import tarfile

ano = 2017
diretorio= os.getcwd()

file = tarfile.open(diretorio + "/" + str(ano) + ".tar.gz") #Descompacta o primeiro arquivo

file.extractall(diretorio) #Vai pro diretorio que esta o sript (descompacta)

file.close()

os.chdir(str(ano))# Vai pra primeira pasta (2017)


ano-=1#Tira um ano para ir para pasta 2016

while ano >=0:
	file = tarfile.open(os.getcwd() + "/" + str(ano) + ".tar.gz") 

	file.extractall(diretorio) #Extrai tudo pro diretorio inicial

	file.close()

	os.chdir(diretorio) #Volta pro diretorio inicial
	os.chdir(str(ano)) #Vai pra pasta q foi extraida

	ano-=1 #Tira um ano

