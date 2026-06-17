import random
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = int(vida)

    def tomar_dano(self, valor):
        self.vida -= valor

class Mago(Personagem):
    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.mana = 10

    def __str__(self):
        return f"nome: {self.nome}, vida: {self.vida}, mana: {self.mana}"

    def __add__(self, valor: float):
        self.mana += valor
        return self.mana

    def __sub__(self, valor: float):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana

    def __mul__(self, fator: float):
        self.mana *= fator 
        return self.mana

    def __truediv__(self, valor: float):
        self.mana /= valor
        return self.mana

    
class Barbaro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.stamina = 10
        self.fúria = False

    def __str__(self):
        return f"nome: {self.nome}, vida: {self.vida}, stamina: {self.stamina}, fúria: {self.furia}"

    def __add__(self, valor: float):
        self.stamina += valor
        if self.furia == True:
            self.stamina *= 1.5
            return self.stamina
        else:
            return self.stamina

        
    def __sub__(self, valor: float):
        self.stamina -= valor
        if self.stamina == 0 and not self.furia == True:
            self.furia = True
            self.stamina = 5
            return self.furia
            return self.stamina

        else:
            return self.stamina

    def __mul__(self, fator: float):
        self.stamina *= fator
        return self.stamina
        if self.furia == True:
            self.vida += 5
            return self.vida

    def __truediv__(self, valor: float):
        self.stamina /= valor
        return self.stamina


nome = input("Digite o nome do personagem: ")
vida = input("Digite a vida do personagem: ")
tipo  = input("Digite o tipo do personagem (Mago ou Bárbaro): ")
if tipo == 'Mago':
    Pm = Mago(nome, vida)
    while True:
        print("Escolha uma ação:")
        print("(1)Tomar poção simples")
        print("(2) Tomar poção especial")
        print("(3) ataque básico")
        print("(4) ataque especial")
        print(Pm)
        escolha = input("Digite o número da ação: ")
        if escolha == "1":
            Pm + 5
        elif escolha == "2":
            Pm * 1.5
        elif escolha == "3":
            Pm - 2 
        elif escolha == "4":
            Pm / 2
        valor_dano = random.randint(1, 10)
        Pm.tomar_dano(valor_dano)
        if Pm.vida == 0:
            break
        

elif tipo == 'Barbaro':
    Pb = Barbaro(nome, vida)
    while True:
        print("Escolha uma ação:")
        print("(1)Tomar poção simples")
        print("(2) Tomar poção especial")
        print("(3) ataque básico")
        print("(4) ataque especial")
        print(Pb)
        
        escolha = input("Digite o número da ação: ")
        if escolha == "1":
            Pb + 5
        elif escolha == "2":
            Pb * 1.5
        elif escolha == "3":
            Pb - 2 
        elif escolha == "4":
            Pb / 2
        valor_dano = random.randint(1, 10)
        Pb.tomar_dano(valor_dano)
        if Pb.vida == 0:
            break



    

        
