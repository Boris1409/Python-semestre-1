class Gato:
    def __init__(self, name, sex, age, weight, color, texture):
        self.name = name 
        self.sex = sex
        self.age= age
        self.weight = weight
        self.color = color
        self.texture = texture  
        # print(f'''Name: {self.name}
        #       ''')
    def meow(self):
        print(f'{self.name}: MEOW')
    
    def getWeight(self):
        return self.weight
    
    def set_age(self):
        self.age = input('ingrese su edad')
        return self.age
    
        