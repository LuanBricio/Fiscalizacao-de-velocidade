print("=" * 30)
print("  Programa da FiscalizaCity")
print("=" * 30)


#Variaveis
velocidade = 1
vel_total = 0
multa = 14
multa_total = 0
velocidade_permit = 0
velocidade_acima = 0

#Condição para enquato a velocidade for maior que 0 e menor que 220 ele repetir a pergunta e registrar
while velocidade > 0 and velocidade < 220:

    #Recebe o valor da variavel velocidade
    velocidade = float(input("Informe a velocidade atual, em km:"))

    #Evita que os numero 0 ou menos e 220 ou mais façam parte do calculo
    if velocidade > 0 and velocidade < 220:

        #Contabiliza o total de multas arrecadadas e a velocidade dos veiculos acima do limite
        if velocidade > 60:
            multa_total += multa
            vel_total += velocidade
            velocidade_acima += 1
        else:
            #Registra o total de veiculos na velocidade permitida
            velocidade_permit += 1


#Calcula a media da velocidade dos veiculos acima da velocidade
vel_media = vel_total / velocidade_acima


#Resultados
print("A quantidade de veículos que foram registrados com velocidade no limite permitido foi:", velocidade_permit)

print("O valor total arrecadado com as multas aplicadas foi de: R$",multa_total)

print("A média de velocidade dos veículos com velocidade acima do limite permitido:",vel_media)
