def estacionamento(N, clientes):
    intervalo = []
    
    for i in clientes:
        if i not in intervalo:
            intervalo.append(i)
    
    return len(intervalo)

N = int(input("Número de vagas: "))
M = int(input("Número de clientes: "))

if 1 > N or N > 100000:
    print("O número de vagas deve estar entre 1 e 100000.")
elif 1 > M or M > 100000:
    print("O número de clientes deve estar entre 1 e 100000.")
else:
    clientes = []
    cont = 0

    while cont < M:
        num_cliente = int(input('Cliente: '))
        
        if 1 > num_cliente or num_cliente > N:
            print(f"O número do cliente deve estar entre 1 e {N}.")
            break
        clientes.append(num_cliente)
        cont += 1
    else:  
        resposta = estacionamento(N, clientes)
        print(f"O número de carros que poderão estacionar são: {resposta}")

