# Pertemuan 06 Nested Loop Python

Nama: Mutiara Sari  
NIM: 2225250071  
Kelas: 3A  

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam Python.

## Cara Menjalankan

Program utama dapat dijalankan dengan perintah:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

Program akan meminta input bilangan `n`. Nilai `n` harus berupa bilangan positif. Jika `n` kurang dari atau sama dengan 0, program akan meminta input kembali.

## Algoritma Tugas 3

Program menggunakan nested loop untuk membuat tabel perkalian berukuran `n × n`.

- **Loop luar (`i`)** berperan mengatur baris tabel, dengan nilai dari 1 sampai `n`.
- **Loop dalam (`j`)** berperan mengatur kolom tabel, dengan nilai dari 1 sampai `n`.
- **Akumulator `total_baris`** digunakan untuk menjumlahkan seluruh hasil perkalian pada setiap baris. Nilainya diatur kembali menjadi 0 pada awal setiap baris.
- **Akumulator `total_semua`** digunakan untuk menjumlahkan seluruh hasil perkalian dari semua baris.
- **Counter `count_pasangan`** digunakan untuk menghitung banyaknya pasangan `(i, j)` yang dihasilkan oleh nested loop.
- **Counter `count_genap`** digunakan untuk menghitung banyaknya hasil perkalian yang bernilai genap. Counter bertambah satu hanya ketika `hasil % 2 == 0`.

Pada setiap iterasi loop dalam, program menghitung:

```text
hasil = i × j
```

Kemudian hasil tersebut digunakan untuk memperbarui jumlah baris, total keseluruhan, jumlah pasangan, dan counter hasil genap.

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| `n = 1` | 1 pasangan, total 1, hasil genap 0 | 1 pasangan, total 1, hasil genap 0 | Berhasil |
| `n = 2` | 4 pasangan, total 9, hasil genap 3 | 4 pasangan, total 9, hasil genap 3 | Berhasil |
| `n = 3` | 9 pasangan, total 36, hasil genap 5 | 9 pasangan, total 36, hasil genap 5 | Berhasil |

Jumlah setiap baris juga sesuai dengan hasil pengujian:

- `n = 1` → jumlah baris: `1`
- `n = 2` → jumlah baris: `3, 6`
- `n = 3` → jumlah baris: `6, 12, 18`

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali dan untuk setiap iterasi loop luar, loop dalam juga berjalan sebanyak `n` kali.

Dengan demikian, badan loop dalam berjalan:

```text
n × n = n² kali
```

Contohnya:

- `n = 1` → `1² = 1` kali
- `n = 2` → `2² = 4` kali
- `n = 3` → `3² = 9` kali

Jadi, jumlah iterasi badan loop dalam bertambah secara kuadrat terhadap nilai `n`.

## Refleksi

Salah satu kesalahan yang perlu diperhatikan pada nested loop adalah menempatkan akumulator `total_baris = 0` di luar loop luar. Jika hal tersebut dilakukan, nilai jumlah baris sebelumnya akan ikut terbawa ke baris berikutnya sehingga jumlah setiap baris menjadi tidak benar.

Perbaikannya adalah menempatkan `total_baris = 0` di dalam loop luar, sebelum loop dalam dimulai. Dengan demikian, setiap baris memiliki akumulator baru yang dimulai dari 0.