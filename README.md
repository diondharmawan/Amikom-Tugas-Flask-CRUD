# 🚀 Tugas Praktikum CRUD: Flask + MySQL + AdminLTE

Halo! 👋 Selamat datang di repositori saya. Ini adalah tempat saya nyimpen *source code* buat tugas praktikum mata kuliah pemrograman web. Di proyek ini, saya lagi belajar gimana caranya bikin fitur CRUD (Create, Read, Update, Delete) yang paling *basic* tapi super penting, pakai framework **Flask** di Python dan databasenya pakai **MySQL**. 

Biar tampilannya nggak kaku-kaku amat dan kelihatan lebih pro, saya pakai template **AdminLTE** sama **Bootstrap**. Lumayan seru sih ngulik-ngulik cara nempelin template HTML ke Flask pakai Jinja2!

---

## 🧑‍💻 Jurnal Belajar (Student's Log)

Jujur aja, pas awal ngerjain tugas ini rasanya lumayan pusing, apalagi pas nyambungin rute (routing) di Flask sama *query* SQL-nya. Tapi setelah diulik-ulik, konsepnya mulai masuk akal:
1. **GET & POST:** Belajar kapan harus pakai GET (buat nampilin form/data) dan kapan pakai POST (buat ngirim data yang disubmit ke database).
2. **Template Engine (Jinja2):** Ini ngebantu banget biar nggak nulis ulang kode HTML dari awal terus. Fitur `{% extends 'base.html' %}` bener-bener *lifesaver* buat bikin layout *dashboard* yang konsisten.
3. **Database Connector:** Pakai `mysql-connector-python` ternyata lumayan gampang buat eksekusi *query* kayak `INSERT`, `UPDATE`, atau `DELETE` langsung dari Python.

Intinya, proyek ini bikin saya lumayan paham gimana alur data dari *browser* dikirim ke *server*, diproses, disimpen ke *database*, terus ditampilin lagi ke *user*.

---

## ⚙️ Gimana Sih Alur Programnya?

Biar lebih gampang ngebayangin alur kerjanya, saya iseng bikin *flowchart* sederhana pakai Mermaid.js di bawah ini:

```mermaid
graph TD
    A([Browser Mahasiswa]) -->|Buka Web (GET /)| B{Flask: app.py}
    B -->|Ambil Data| C[(Database MySQL)]
    C -->|Kirim Data| B
    B -->|Render tabel| D[index.html]
    D --> A

    A -->|Submit Form (POST)| E[Proses Tambah/Ubah]
    E -->|INSERT / UPDATE SQL| C
    E -->|Redirect ke Awal| B
```

---

## 🛠️ Cara Jalanin di Komputer Sendiri

Kalau kebetulan mampir dan pengen coba jalanin kode ini, ini langkah-langkahnya:

1. **Clone dulu reponya:**
   ```bash
   git clone https://github.com/diondharmawan/Amikom-Tugas-Flask-CRUD.git
   cd Amikom-Tugas-Flask-CRUD
   ```

2. **Siapin Database:**
   Buka MySQL, bikin database namanya `db_kuliah`, terus bikin tabel `mahasiswa`. (Kalau mau gampang, *import* aja dari modul/instruksi yang ada).

3. **Bikin Virtual Environment (Biar Rapi):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install Flask mysql-connector-python
   ```

4. **Jalanin Server Flask:**
   ```bash
   flask run
   ```
   Tinggal buka `http://127.0.0.1:5000` di *browser*. Sip, jalan deh! 🎉

---

## 👨‍🎓 Identitas Mahasiswa

| Detail | Info |
| :--- | :--- |
| **Nama** | Fransiscus Asisi Kananda Herdion Dharmawan |
| **NIM** | 24.83.1107 |
| **Prodi** | Teknik Komputer |
| **Kampus** | Universitas Amikom Yogyakarta |

*Dibuat dengan ☕ dan banyak error log di terminal.*
