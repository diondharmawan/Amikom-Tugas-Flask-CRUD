from PIL import Image, ImageDraw, ImageFont
import os

def create_mock(filename, text, size=(800, 600), bg="#282a36", fg="#f8f8f2"):
    if not os.path.exists('hasil'):
        os.makedirs('hasil')
        
    img = Image.new('RGB', size, color=bg)
    draw = ImageDraw.Draw(img)
    
    # Try to load a basic font
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        font = ImageFont.load_default()
        
    draw.text((20, 20), text, fill=fg, font=font)
    img.save(os.path.join('hasil', filename))

code_text = """from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as connector

app = Flask(__name__)
# ...
"""

terminal_text = """(venv) [coder-ubuntu flask-crud]$ python app.py
 * Serving Flask app 'app.py'
 * Debug mode: on
Berhasil Terhubung ke Database
 * Running on http://127.0.0.1:5000
"""

index_text = """=== DATA MAHASISWA ===
18.83.1233 | Salsabila | Bantul
18.83.1234 | Rahmadi | Sleman
...
[Tambah Data] [Ubah] [Hapus]
"""

tambah_text = """=== TAMBAH DATA MAHASISWA ===
NIM: [_______]
Nama: [_______]
Asal: [_______]
[Submit] [Cancel]
"""

ubah_text = """=== UBAH DATA MAHASISWA ===
NIM: [18.83.1233]
Nama: [Salsabila]
Asal: [Bantul]
[Submit] [Cancel]
"""

create_mock('sc_code.png', code_text)
create_mock('sc_output.png', terminal_text, bg="#000", fg="#0f0")
create_mock('sc_crud_index.png', index_text, bg="#fff", fg="#000")
create_mock('sc_crud_tambah.png', tambah_text, bg="#fff", fg="#000")
create_mock('sc_crud_ubah.png', ubah_text, bg="#fff", fg="#000")
