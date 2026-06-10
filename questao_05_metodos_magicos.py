class onibus:
    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False]*num_assentos

    def __len__(self):
        return self.len(self.assentos)

    def __getitem__(self, indice):
        pass

    def __setitem__(self, indice, valor):
        pass

    def __str__(self):
        return f"Ônibus (Placa: {self.placa}) Motorista: {self.nome_motorista}
                 