def calculate_total(price, quantity):
    total_price = price * quantity
    return total_price

# Menampilkan daftar laptop dan harganya
print("Daftar Laptop:")
print("1. Laptop Asus - Rp 10.000.000")
print("2. Laptop ROG - Rp 8.000.000")
print("3. Laptop Lenovo - Rp 12.000.000")

# Meminta input dari pengguna
choice = int(input("Pilih nomor laptop yang ingin dibeli (1-3): "))
quantity = int(input("Masukkan jumlah yang ingin dibeli: "))

# Inisialisasi harga dan nama laptop berdasarkan pilihan pengguna
if choice == 1:
    laptop_name = "Laptop Asus"
    laptop_price = 10000000
elif choice == 2:
    laptop_name = "Laptop ROG"
    laptop_price = 8000000
elif choice == 3:
    laptop_name = "Laptop Lenovo"
    laptop_price = 12000000
else:
    print("Pilihan tidak valid. Silakan pilih nomor laptop dari daftar.")

# Menghitung total harga
if choice in [1, 2, 3] and quantity > 0:
    total_price = calculate_total(laptop_price, quantity)
    print(f"Anda telah memilih {laptop_name} sebanyak {quantity} unit.")
    print(f"Total harga: Rp {total_price}")
elif quantity <= 0:
    print("Jumlah harus lebih dari 0.")
