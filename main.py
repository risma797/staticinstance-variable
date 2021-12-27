class Laptop:

  #static variable
  SSD = 256

  #instance variable
  def __init__(self):
    self.RAM = 8 
    self.Type = 7470


Laptop_Dell = Laptop()
Laptop_Lenovo = Laptop()

Laptop_Dell.RAM = 16
Laptop_Dell.Type = 5470


Laptop.SSD = 512

print("\n")
print("RAM :", Laptop_Dell.RAM)
print("Type :", Laptop_Dell.Type )
print("SSD : ", Laptop_Dell.SSD)

print(" ")
print("======================================")
print(" ")

print("RAM :", Laptop_Lenovo.RAM)
print("Type :", Laptop_Lenovo.Type )
print("SSD : ", Laptop_Lenovo.SSD)

