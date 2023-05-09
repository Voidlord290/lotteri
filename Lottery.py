import random
class Lotteri:

    def __init__(self):
        self.list_vinster = ["Cola", "fanta", "sprite", "trocadero", "redbull"]

    def get_vinst(self):
        slumptal = random.randint(0, 4)
        return self.list_vinster[slumptal]