#Kelas utama
class Laptop:
  SSD_sekarang = 256

#fungsi construktor
  def __init__ (self, nama_merk, kapasitas_RAM, CPU_processor):
    self.nama_merk = nama_merk
    self.kapasitas_RAM = kapasitas_RAM
    self.CPU_processor = CPU_processor
    print(f'Laptop {self.nama_merk},{self.kapasitas_RAM}, {self.CPU_processor} dioperasikan')

    def menambahSSD(self, menambahSSD):
      self.SSD_sekarang = self.SSD_sekarang + menambahSSD
      print('SSD_sekarang ', self.SSD_sekarang)
   
#destructor
  def __del__ (self):
    print(f'Laptop {self.nama_merk},{self.kapasitas_RAM}, {self.CPU_processor} dimatikan')
  

#membuat objek
laptop_kuliah = Laptop('Dell','8 GB','Intel core I7')
laptop_kerja = Laptop('Macbook','16 GB','Mac OS' )

print(' ')
print('=================================================')
print(' ')

del laptop_kuliah
del laptop_kerja

print(' ')
print('=================================================')
print(' ')

print('SSD Laptop Sekarang :', Laptop.SSD_sekarang)
print('SSD Laptop setelah ditambah :', Laptop.SSD_sekarang + 256)

