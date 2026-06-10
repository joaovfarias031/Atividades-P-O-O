class carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = float(saldo)

    def __add__(self, valor_yuan):
        if self.moeda == "USD":
            return (self.saldo * 0.14) + valor_yuan
        elif self.moeda == "BRL":     
            return (self.saldo * 0.85) + valor_yuan

    def __sub__(self, valor_yuan):
        if self.moeda == "USD":
            return (self.saldo * 0.14) - valor_yuan
        elif self.moeda == "BRL":     
            return (self.saldo * 0.85) - valor_yuan

carteira_usd = carteira("USD", 10.0)
print("soma de carteira USD + 50 yuan =", carteira_usd + 50.0)
