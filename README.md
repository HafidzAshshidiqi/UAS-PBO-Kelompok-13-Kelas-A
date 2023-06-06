# UAS-PBO-Kelompok-13-Kelas-A
UAS PBO Kelompok 13 
Dalam implementasi Notepad menggunakan Tkinter dalam Python dengan konsep OOP, beberapa konsep OOP yang diterapkan adalah sebagai berikut:

1. *Kelas Notepad*: Kelas `Notepad` merupakan kelas utama yang mewakili aplikasi Notepad. Ini adalah contoh dari konsep pewarisan, di mana `Notepad` dapat mewarisi atau memperluas fungsionalitas dari kelas lain jika diperlukan.

2. *Enkapsulasi*: Atribut dan metode dalam kelas `Notepad` didefinisikan dengan visibilitas yang tepat. Misalnya, atribut `root`, `_textArea`, `_menu`, `file_menu`, dan `edit_menu` hanya dapat diakses di dalam kelas `Notepad`. Ini membantu dalam menjaga integritas data dan memisahkan logika aplikasi.

3. *Metode _init**: Metode `*: Metode `_init_` di dalam kelas `Notepad` digunakan sebagai konstruktor yang dipanggil saat objek `Notepad` dibuat. Ini memungkinkan Anda untuk melakukan inisialisasi awal dan menyediakan pengaturan antarmuka grafis Notepad.

4. *Metode-metode lain*: Metode `open_file`, `save_file`, `cut`, `copy`, dan `paste` adalah metode yang mewakili aksi atau operasi tertentu pada Notepad. Ini memisahkan logika pengolahan dari tampilan antarmuka, sehingga memudahkan pemeliharaan dan perubahan di masa mendatang.

5. *Pemisahan tanggung jawab*: Dalam contoh ini, tanggung jawab menangani antarmuka grafis ditangani oleh Tkinter, sedangkan tanggung jawab logika Notepad ditangani oleh kelas `Notepad`. Ini memungkinkan pemisahan jelas antara antarmuka pengguna dan logika aplikasi, sehingga mempermudah pemeliharaan dan pengembangan lebih lanjut.

6. *Penggunaan library eksternal*: Dalam contoh ini, Tkinter digunakan sebagai library eksternal untuk membangun antarmuka grafis Notepad. Ini adalah contoh penggunaan komponen dan fitur yang disediakan oleh library eksternal untuk memperluas fungsionalitas aplikasi.
