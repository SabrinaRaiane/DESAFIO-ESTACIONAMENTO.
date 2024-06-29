def estacionamento(N, clientes):
    intervalo = []
    
    for i in clientes:
        if i not in intervalo:
            intervalo.append(i)
    
    return len(intervalo)