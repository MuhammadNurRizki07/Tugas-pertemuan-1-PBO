def calculate_total(nasi_goreng_qty, mie_ayam_qty, nasi_kuning_qty):
    harga_nasi_goreng = 12000
    harga_mie_ayam = 10000
    harga_nasi_kuning = 15000

    total_nasi_goreng = nasi_goreng_qty * harga_nasi_goreng
    total_mie_ayam = mie_ayam_qty * harga_mie_ayam
    total_nasi_kuning = nasi_kuning_qty * harga_nasi_kuning

    total_harga = total_nasi_goreng + total_mie_ayam + total_nasi_kuning

    return total_harga

# Meminta input dari pengguna
nasi_goreng_qty = int(input("Masukkan jumlah porsi nasi goreng yang terjual: "))
mie_ayam_qty = int(input("Masukkan jumlah porsi mie ayam yang terjual: "))
nasi_kuning_qty = int(input("Masukkan jumlah porsi nasi kuning yang terjual: "))

# Menghitung total penjualan
total_harga = calculate_total(nasi_goreng_qty, mie_ayam_qty, nasi_kuning_qty)

# Menampilkan hasil
print(f"Total penjualan: Rp {total_harga}")
