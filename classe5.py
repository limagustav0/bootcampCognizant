def escreveArquivo(texto):
    arquivo = open('arquivo.txt',"w")
    arquivo.write(texto)
    arquivo.close()

def atualizaArquivo(texto):
    arquivo = open('arquivo.txt',"a")
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(arquivo):
    arquivo = open(arquivo,'r')
    conteudo = arquivo.read()
    print(conteudo)

def mediaNotas(arquivo):
    listaMedia=[]
    arquivo = open(arquivo,"r")
    alunoNota = arquivo.read()
    alunoNota = alunoNota.split('\n')
    for x in alunoNota:
        listaNotas = x.split(',')
        aluno = listaNotas[0]
        listaNotas.pop(0)
        media = lambda notas : sum([int(i) for i in listaNotas]) / len(listaNotas)
        listaMedia.append({aluno:media(listaNotas)})
    return listaMedia

listaMedia = mediaNotas('arquivo.txt')

print(listaMedia)




if __name__ ==  "__main__":
    escreveArquivo("bia, 9,9,9,9\n")
    atualizaArquivo("evandro, 9,9,9,9\n")
    atualizaArquivo("carla, 9,8,2,1\n")
    atualizaArquivo("dias, 9,4,9,1")
    mediaNotas('arquivo.txt')


