from random import random

class Product():
    def __init__(self, name, space, value):
        self.name = name 
        self.space = space
        self.value = value 


class Individual():
    def __init__(self, spaces, values, limit_spaces, generation=0 ):
        self.spaces = spaces
        self.values = values    
        self.limit_spaces = limit_spaces
        self.note_assessment = 0
        self.spaces_used = 0
        self.generation = generation
        self.chromosome =[]

        for i in range(len(spaces)):
            if random()  < 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")    



    def assessment(self):
        note = 0
        sun_spaces = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == "1":
                note += self.values[i]
                sun_spaces += self.spaces[i]
        if sun_spaces > self.limit_spaces:
            note = 1
        self.note_assessment = note 
        self.spaces_used = sun_spaces            


if __name__== "__main__":      
    list_product = []
    list_product.append(Product("Refrigerator Dako", 0.751, 999.90))
    list_product.append(Product("Iphone 6", 0.0000899, 2911.12))
    list_product.append(Product("TV 55", 0.400, 4346))
    list_product.append(Product("TV 50' ", 0.290, 3999.90))
    list_product.append(Product("TV 42' ", 0.200, 2999.00))
    list_product.append(Product("Notebook Dell", 0.00350, 2499.90))
    list_product.append(Product("Ventilador Panasonic", 0.496, 199.90))
    list_product.append(Product("Microondas Electrolux", 0.0424, 308.66))
    list_product.append(Product("Microondas LG", 0.0544, 429.90))
    list_product.append(Product("Microondas Panasonic", 0.0319, 299.29))
    list_product.append(Product("Geladeira Brastemp", 0.635, 849.00))
    list_product.append(Product("Geladeira Consul", 0.870, 1199.89))
    list_product.append(Product("Notebook Lenovo", 0.498, 1999.90))
    list_product.append(Product("Notebook Asus", 0.527, 3999.00))


    spaces = []
    values = []
    names = []
    
    for product in list_product:
        spaces.append(product.space)
        values.append(product.value)
        names.append(product.name)
    limit = 3

    individual1 = Individual(spaces, values, limit)
    print(f"Espaços = {str(individual1.spaces)}")
    print(f"Valores = {str(individual1.values)}")  
    print(f"Cromossomo = {str(individual1.chromosome)}")

    print(f"\nCromossomo da carga")
    for i in range(len(list_product)):
        if individual1.chromosome[i] == "1":
            print(f"Nome: {list_product[i].name} R$: {list_product[i].value}")


    individual1.assessment()
    print(f"Nota = R$: {individual1.note_assessment:.2f}")
    print(f"Espaco usdo = {individual1.spaces_used}")        