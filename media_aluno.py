
#metodo de calcular a media do aluno sem o uso de si 

materia1 = int(input('qual foi a sua nota primeiro simestre: '))
materia2 = int(input('qual foi a sua nota segundo simestre: '))
materia3 = int(input('qual foi a sua nota terceiro simestre: '))

soma_nota = materia1 + materia2 + materia3 
result_media = soma_nota / 3

aprovado_ou_nao = result_media > 7 

print(f'voce foi aprovado {aprovado_ou_nao}')