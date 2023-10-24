# Minta pengguna untuk memasukkan jenis minuman favorit
minuman_favorit = input("klik ENTER jika ingin menampilkan list minuman: ")

# List minuman
minuman = ["Air Mineral", "Teh Manis", "Kopi Hitam", "Es Jeruk", "Soda"]

# Tambahkan minuman favorit pengguna ke list
minuman.append(minuman_favorit)

# Cetak semua minuman
print("Berikut adalah beberapa jenis minuman:")
for minum in minuman:
    print(f"Saya suka minum {minum}.")
