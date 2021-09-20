'''Sistema que calcula quantas pessoas são necessárias para se obter 80% de chance de duas pessoas fazerem aniversário no mesmo dia'''

class Birthday: # Define a classe "Birthaay"
    def __init__(self):
        self.__numero_pessoas = self.__calcula_pessoas() # Atributo do número de pessoas
    

    @staticmethod
    def  __calcula_pessoas(): # Método calcula o número de pessoas
        pessoas = (0.8 * 23) / 0.5

        return round(pessoas)


    @property
    def numero_pessoas(self): # Getter do número de pessoas
        return self.__numero_pessoas


if __name__ == '__main__':
    birthday = Birthday()

    print(birthday.numero_pessoas)
