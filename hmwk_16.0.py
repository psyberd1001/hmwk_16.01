from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')


class Shop:

    def __init__(self, __file_name='products.txt'):
        self.file_name = __file_name

    def get_products(self):
        file = open(self.file_name, 'r+', encoding='utf-8')
        read_file = file.readline()
        file.close()
        return read_file

    def add(self, *products):
        get_current_products = self.get_products()
        file1 = open(self.file_name, 'a+', encoding='utf-8')
        print(type(get_current_products))
        print(type(products))
        for i in range(len(products)):
            if str(products[i]) not in get_current_products:
                file1.write(f'{products[i]}')
            else:
                file1.write(f'\n{products[i]} уже есть в магазине')
        file1.close()
        return file1


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
