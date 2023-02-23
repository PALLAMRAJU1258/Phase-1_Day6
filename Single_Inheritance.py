class Pet:
    def __init__(self,pet_type,name,DOB):
        self.pet_type=pet_type
        self.name=name
        self.DOB=DOB
    def details(self):
        print("I am pet")
class Cat(Pet):
    def __init__(self,pet_type,name,DOB):
        self.name="Black "+name
        self.pet_type= pet_type
    def sounds(self,sound):
        return sound
pet1=Pet("cat","Tiffany","08-08-2019")
pet2=Cat("cat","Gatsby","08-10-2018")
pet1.details()
pet2.details()
print(pet2.name,"is a",pet2.pet_type,"and it always runs around with",
      pet2.sounds("attention-seeking meows"))
