# MiniProject2_GresiusKrisnaSamuel_058

flowchart TD
    Start([Mulai]) --> Init[Inisialisasi Dictionary users & data_latihan]
    Init --> MenuAwal[/Menu Awal: 1.Login, 2.Register, 3.Keluar/]
    
    MenuAwal --> CekMenuAwal{Input Angka Valid?}
    CekMenuAwal -- "Bukan Angka (Error)" --> MenuAwal
    
    CekMenuAwal -- "Pilih 3 (Keluar)" --> End([Selesai])
    
    CekMenuAwal -- "Pilih 2 (Register)" --> RegInput[/Input Username & Pwd Baru/]
    RegInput --> RegSave[Simpan ke Dictionary users] --> MenuAwal
    
    CekMenuAwal -- "Pilih 1 (Login)" --> LogInput[/Input Username & Password/]
    LogInput --> CekLogin{Cocok di Dictionary?}
    
    CekLogin -- "Gagal" --> CekKesempatan{Kesempatan Habis?}
    CekKesempatan -- "Belum" --> LogInput
    CekKesempatan -- "Ya" --> End
    
    CekLogin -- "Berhasil" --> CekRole{Cek Role Akun}
    
    %% Alur Admin
    CekRole -- "Admin" --> MenuAdmin[/Menu Admin 1-5/]
    MenuAdmin --> PilihAdmin{Pilih Menu?}
    PilihAdmin -- "Bukan Angka (Error)" --> MenuAdmin
    
    PilihAdmin -- "1 (Lihat)" --> AdminRead[/Tampil Tabel Latihan/] --> MenuAdmin
    PilihAdmin -- "2 (Tambah)" --> AdminInput[/Input Data Latihan Baru/] --> AdminSave[Simpan ke data_latihan] --> MenuAdmin
    PilihAdmin -- "3 (Ubah)" --> AdminUbah[/Input ID & Update Data/] --> AdminUpdate[Update data_latihan] --> MenuAdmin
    PilihAdmin -- "4 (Hapus)" --> AdminHapus[/Konfirmasi Hapus Data/] --> AdminDel[Hapus dari data_latihan] --> MenuAdmin
    PilihAdmin -- "5 (Logout)" --> MenuAwal
    
    %% Alur User
    CekRole -- "User" --> MenuUser[/Menu User 1-4/]
    MenuUser --> PilihUser{Pilih Menu?}
    PilihUser -- "Bukan Angka (Error)" --> MenuUser
    
    PilihUser -- "1 (Lihat)" --> UserRead[/Tampil Tabel Latihan/] --> MenuUser
    PilihUser -- "2 (Cari)" --> UserCari[/Input Kategori & Tampil Hasil/] --> MenuUser
    PilihUser -- "3 (Gacha)" --> UserGacha[Acak Latihan dgn Library random] --> UserTampilGacha[/Tampilkan Latihan Acak/] --> MenuUser
    PilihUser -- "4 (Logout)" --> MenuAwal
    
