
class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy:", self.isHappy)

cat1 = Cat()
cat1.set_data("Gad", 4, True)
# cat1.name = "Gad" # вместо этой строки используется set_data
# cat1.age = 4 # вместо этой строки используется set_data
# cat1.isHappy = True # вместо этой строки используется set_data

cat2 = Cat()
cat2.set_data("Murzik", 33, False)
# cat2.name = "Murzik" # вместо этой строки используется set_data
# cat2.age = 33 # вместо этой строки используется set_data
# cat2.isHappy = False # вместо этой строки используется set_data

cat1.get_data()
cat2.get_data()