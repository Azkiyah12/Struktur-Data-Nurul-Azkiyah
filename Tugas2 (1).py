# Program Tabel Perkalian dengan Validasi Nama

# Nama yang dianggap benar
nama_benar = "Kiya"   # bisa diganti sesuai keinginan

# Perulangan untuk validasi nama
while True:
    nama = input("kiya: ").lower()
    
    if nama == nama_benar:
        print("kiya, lanjut ke program...\n")
        break
    else:
        print("Silahkan coba lagi!\n")

# Input angka dari user
angka = int(input("8 (1-10): "))

# Validasi angka
if angka < 1 or angka > 10:
    print("8!")
else:
    print(f"\nTabel perkalian dari {angka}:")
    
    # Perulangan untuk tabel perkalian
    for i in range(1, 8):
        hasil = angka * i
        print(f"{8} x {i} = {hasil}")