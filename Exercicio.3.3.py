# escreva uma expresão para determinar se uma pessoa deve ou nao pagar imposto. considere que pagam impostos pessoas(...)
# (...) cujo o salario é maior que R$ 1,200

salario = float(input('quantos voce ganha por mês: '))
impost = float(input('quanto porcento vc vai pagar de imposto: '))
imposto = salario > 1200

perImpost = salario * impost

print(f'voce paga imposto pelo fato de seu salario ser maio que 1.200. seu imposto é: {perImpost}')
