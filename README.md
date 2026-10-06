# Mini Project 2: Program Manajemen Latihan Fisik (FitLog)

Nama: Gresius Krisna Samuel
NIM: 058
Kelas:B


# 1. Deskripsi Singkat Program
FitLog adalah program berbasis Command Line Interface (CLI) yang dibangun menggunakan bahasa Python. Program ini dirancang untuk mencatat dan mengelola rencana latihan fisik. di versi ini, program telah dikembangkan sesuai instruksi di GCR.

Program ini memiliki sistem autentikasi (login) sederhana yang membagi pengguna menjadi dua batasan hak akses (role), yaitu:
**Admin**: Memiliki hak akses penuh untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data latihan.
 **User**: Memiliki hak akses terbatas, yaitu hanya untuk melihat daftar latihan dan mencari latihan berdasarkan kategori otot.

# 2. Gambar Flowchart dan Penjelasan Alur

Program ini dibagi menjadi tiga alur utama untuk memudahkan pembacaan logika berjalannya aplikasi.

# A. Alur Utama (Sistem Login)

```mermaid
flowchart TD
    classDef default fill:#fff,stroke:#000,stroke-width:2px,color:#000;
    
    A([Mulai]) --> B[/Inisialisasi Dictionary users & data_latihan/]
    B --> C[Tampilkan Menu Utama]
    C --> D[/Input Pilihan 1/2/]
    
    D --> E{Input == Angka?}
    E -- Tidak --> C
    E -- Ya --> F{Pilihan Menu?}
    
    F -- 2 (Keluar) --> G([Selesai])
    F -- 1 (Login) --> H[/Input Username & Password/]
    
    H --> I{Cocok di Dictionary?}
    I -- Tidak --> C
    I -- Ya --> J{Cek Role Akun?}
    
    J -- Admin --> K[[Masuk Alur Admin]]
    J -- User --> L[[Masuk Alur User]]
    
    K --> C
    L --> C
```

# Penjelasan Alur Utama:
Program dimulai dengan menginisialisasi nested dictionary untuk menyimpan data akun dan data latihan. Pengguna akan melihat menu utama untuk memilih Login atau Keluar. Program memvalidasi input tersebut. Jika memilih Login, sistem akan meminta input username dan password. Jika data cocok dengan isi dictionary, sistem akan memeriksa hak akses (role) pengguna dan mengarahkan mereka ke menu Admin atau menu User.



```mermaid
flowchart TD
    classDef default fill:#fff,stroke:#000,stroke-width:2px,color:#000;
    
    A([Mulai Menu Admin]) --> B[Tampilkan Menu Admin 1-5]
    B --> C[/Input Pilihan/]
    
    C --> D{Input == Angka?}
    D -- Tidak --> B
    D -- Ya --> E{Pilihan Menu?}
    
    E -- 1 (Lihat) --> F[/Tampilkan Tabel Latihan/] --> B
    
    E -- 2 (Tambah) --> G[/Input ID Baru/]
    G --> H{ID Sudah Ada?}
    H -- Ya --> B
    H -- Tidak --> I[/Input Nama, Kategori, Target/]
    I --> J[/Input Beban/]
    J --> K{Beban == Angka?}
    K -- Tidak --> J
    K -- Ya --> L[Simpan ke data_latihan] --> B
    
    E -- 3 (Ubah) --> M[/Input ID Ubah/]
    M --> N{ID Ditemukan?}
    N -- Tidak --> B
    N -- Ya --> O[/Input Nama, Kategori, Target Baru/]
    O --> P[/Input Beban Baru/]
    P --> Q{Beban == Angka?}
    Q -- Tidak --> P
    Q -- Ya --> R[Update data_latihan] --> B
    
    E -- 4 (Hapus) --> S[/Input ID Hapus/]
    S --> T{ID Ditemukan?}
    T -- Tidak --> B
    T -- Ya --> U[/Konfirmasi Hapus y/n/]
    U --> V{Yakin 'y'?}
    V -- Ya --> W[Hapus dari data_latihan] --> B
    V -- Tidak --> B
    
    E -- 5 (Logout) --> X([Kembali ke Menu Utama])
```
  
# Penjelasan Alur Admin:
Setelah berhasil login sebagai Admin, pengguna akan masuk ke dalam perulangan menu operasi CRUD.

1. Opsi Lihat akan membaca dan memprint seluruh isi tabel
2. Opsi Tambah akan meminta masukan ID baru (divalidasi supaya engga duplikat), beserta kelengkapan data lainnya.
3. Opsi Ubah akan mencari data berdasarkan ID. Jika ditemukan, pengguna dapat memasukkan data baru (atau menekan Enter untuk mempertahankan data lama).
4. Opsi Hapus akan mencari ID, meminta konfirmasi, lalu menghapus elemen dictionary tersebut.
5. Opsi Logout akan mengembalikan pengguna ke menu utama aplikasi.



```mermaid
flowchart TD
    classDef default fill:#fff,stroke:#000,stroke-width:2px,color:#000;
    
    A([Mulai Menu User]) --> B[Tampilkan Menu User 1-3]
    B --> C[/Input Pilihan/]
    
    C --> D{Input == Angka?}
    D -- Tidak --> B
    D -- Ya --> E{Pilihan Menu?}
    
    E -- 1 (Lihat) --> F[/Tampilkan Tabel Latihan/] --> B
    
    E -- 2 (Cari) --> G[/Input Kategori Otot/]
    G --> H[Cari kecocokan di data_latihan]
    H --> I{Ditemukan?}
    I -- Ya --> J[/Tampilkan Hasil Pencarian/] --> B
    I -- Tidak --> K[/Tampilkan Pesan Kosong/] --> B
    
    E -- 3 (Logout) --> L([Kembali ke Menu Utama])
```

# Penjelasan Alur User:
Alur user dirancang lebih terbatas. Selain opsi Logout dan Lihat Data, fitur utamanya adalah Cari Data. Pengguna akan menginputkan kata kunci kategori otot. Program akan melakukan perulangan ke dalam dictionary untuk menyaring data yang relevan dan mencetaknya dalam bentuk tabel baru.





# 3. Dokumentasi Program dan Output

A. Tampilan Login dan Penyembunyian Karakter Kata Sandi

<img width="1128" height="634" alt="28968" src="https://github.com/user-attachments/assets/a23a360f-bf2f-4ac0-8767-1d1147751a21" />

<img width="1128" height="634" alt="28969" src="https://github.com/user-attachments/assets/929960e5-9a93-456f-8d16-78dd800bcd81" />

Tampilan ini menunjukkan proses login aplikasi. Kata sandi yang dimasukkan oleh pengguna tidak ditampilkan di layar (berubah menjadi asteris) demi keamanan informasi kredensial.



B. Pengujian Akses Admin (Fungsi CRUD)

<img width="1128" height="634" alt="28974" src="https://github.com/user-attachments/assets/a3fa307f-d980-40b8-a3a5-17c35feea0a7" />

<img width="1128" height="634" alt="28973" src="https://github.com/user-attachments/assets/51d48769-ddf6-4b7a-9153-008c69d8462f" />

<img width="1128" height="634" alt="28972" src="https://github.com/user-attachments/assets/137f3d3a-d5e9-4098-8edb-c9140ba85d8e" />

<img width="1128" height="634" alt="28971" src="https://github.com/user-attachments/assets/62a463b6-460d-4704-8e41-c5702c88f27b" />

Tampilan ini menunjukkan menu utama admin serta hasil uji coba penambahan data (Create) dan pembaruan data (Update). Input ID divalidasi agar selalu menggunakan format kapital.


C. Pengujian Akses User (Fungsi Pencarian)

<img width="1128" height="634" alt="28970" src="https://github.com/user-attachments/assets/36f139f1-154d-4243-bda4-f1f56f59d29a" />

<img width="1128" height="634" alt="28975" src="https://github.com/user-attachments/assets/7741539c-0680-4867-81b4-5ef60f47749d" />

Tampilan ini menunjukkan hak akses pengguna yang masuk sebagai "user". Terdapat proses pencarian data menggunakan kata kunci tertentu (misalnya kategori "Dada"), dan program merespons dengan tabel berisi data yang relevan.




D. Pengujian Kesalahan Input (Error Handling)

<img width="1128" height="634" alt="28976" src="https://github.com/user-attachments/assets/cf2f0714-8cfc-4f29-9a6c-139577fd7c73" />

Tampilan ini membuat situasi di mana program meminta masukan berupa angka (seperti saat memilih menu atau memasukkan beban), namun diisi dengan huruf. Program menolak masukan tersebut, memberikan pesan peringatan, dan meminta ulang masukan tanpa mengalami crash.




# A. Validasi Error Handling
Program ini dikembangkan supaya tahan terhadap kesalahan input tipe data dengan memanfaatkan fungsi bawaan tipe data string, yaitu .isdigit(). Validasi ini diletakkan pada setiap bagian kode yang membutuhkan input numerik (seperti penentuan angka menu dan penentuan jumlah beban). Jika pengguna memasukkan huruf atau karakter khusus, .isdigit() akan mengembalikan nilai False. Program akan mencetak peringatan error dan mengulang permintaan input tanpa menyebabkan eror yang dapat menghentikan paksa (crash) jalannya program.

# B. Penggunaan 4 Library Python
Program ini memanfaatkan empat pustaka:

os: Digunakan bersama fungsi os.system() untuk membersihkan antarmuka layar terminal secara otomatis pada setiap perpindahan menu.

time: Digunakan bersama fungsi time.sleep() untuk menahan atau memberikan jeda waktu sekian detik sebelum program memuat ulang menu, sehingga pesan notifikasi dapat terbaca oleh pengguna.

pwinput: Digunakan untuk memodifikasi input kata sandi pada menu login. Karakter yang diketik akan disamarkan menjadi tanda bintang (*).

prettytable: Digunakan untuk membangun dan merender data dari dalam dictionary ke dalam format representasi visual tabel ASCII agar struktur data mudah dibaca.


