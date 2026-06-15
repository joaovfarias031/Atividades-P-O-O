class onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False]*num_assentos

    def __len__(self):
        return self.len(self.assentos)

    def __getitem__(self, indice):
        if indice >= 0 or indice < len(self.assentos):
            if self.assentos[indice] == False:
                return self.assentos[indice] 
            elif self.assentos[indice] == True:
                return self.assentos[indice] 
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")


    def __setitem__(self, indice, valor):
        if indice >= 0 or indice < len(self.assentos):
            if isinstance(valor, bool):
                if self.assentos[indice] == False:
                    return valor
                elif self.assentos[indice] == True:
                    return valor
            else:
                raise TypeError(f"Valor deve ser booleano (True/False)")
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
         


    def __str__(self):
        txt = f"Ônibus (Placa: {self.placa}) Motorista: {self.nome_motorista}"
        txt += f"Assentos totais: {len(self.assentos)}"
        txt += f"Assentos ocupados: {len(self.assentos == True)}"
        txt += f"Assentos Livres: {len(self.assentos == False)}"
        return txt

onibus = onibus("ABC-1234", "João Silva", 10) # Ônibus com 10 assentos
print(len(onibus)) # Verificando total de assentos 
onibus[0] = True # Ocupando o primeiro assento (índice 0) 
print(onibus) # Exibindo informações do ônibus 

