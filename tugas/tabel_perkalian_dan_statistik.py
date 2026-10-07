# Tugas 3 - Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

total_semua = 0
count_genap = 0
count_pasangan = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil
        count_pasangan += 1

        if hasil % 2 == 0:
            count_genap += 1

    print(f" | jumlah baris = {total_baris}")

print(f"Banyak pasangan = {count_pasangan}")
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")