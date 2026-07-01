class carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = float(saldo)

    def __add__(self, valor_yuan):
        if self.moeda == "USD":
            return (self.saldo * 0.14) + valor_yuan
        elif self.moeda == "BRL":     
            return (self.saldo * 0.85) + valor_yuan
        else:
            return self.saldo + valor_yuan

    def __sub__(self, valor_yuan):
        if self.moeda == "USD":
            return (self.saldo * 0.14) - valor_yuan
        elif self.moeda == "BRL":     
            return (self.saldo * 0.85) - valor_yuan
        else:
            return self.saldo - valor_yuan

carteira_usd = carteira("USD", 100.0)
carteira_BRL = carteira("BRL", 200.0)
carteira_CNY = carteira("CNY", 300.0)
print("soma de carteira USD + 50 yuan =", carteira_usd + 50.0)
print("soma de carteira BRL + 50 yuan =", carteira_BRL + 50.0)
print("soma de carteira CNY + 50 yuan =", carteira_CNY + 50.0)
print("subtração de carteira USD + 50 yuan =", carteira_usd - 50.00)
print("subtração  de carteira BRL + 50 yuan =", carteira_BRL - 50.0)
print("subtração  de carteira CNY + 50 yuan =", carteira_CNY - 50.0)

