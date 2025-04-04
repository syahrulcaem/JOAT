
```markdown
# 🧱 JOAT v3 - Just One Awesome Blockchain

**JOAT** adalah proyek edukatif blockchain berbasis Python, dirancang sederhana agar mudah dipelajari dan dikembangkan.  
Versi ke-1 ini merupakan pondasi awal yang fokus pada pencatatan transaksi dan penambangan blok.

---

## ✨ Fitur

- Tambah transaksi secara manual via API
- Tambang blok baru (tanpa Proof of Work)
- Lihat seluruh rantai blok
- Validasi integritas blockchain secara lokal

---

## 📁 Struktur Proyek

```
JOAT_v3/
├── blockchain/
│   └── __init__.py      # Modul utama blockchain (blok, transaksi)
├── node.py              # Web server Flask (API endpoint)
└── README.md            # Dokumentasi proyek
```

---

## ⚙️ Instalasi

### 1. Clone repositori

```bash
git clone https://github.com/username/JOAT_v3.git
cd JOAT_v3
```

### 2. Install dependensi

```bash
pip install flask
```

---

## 🚀 Menjalankan Server

```bash
python node.py
```

Server akan berjalan di `http://localhost:5000`

---

## 📡 API Endpoint

### ➕ Tambah Transaksi
```
POST /transactions/new
```
**Contoh Body:**
```json
{
  "sender": "Alice",
  "recipient": "Bob",
  "amount": 10
}
```

---

### ⛏ Tambang Blok Baru
```
GET /mine
```

---

### 🔗 Lihat Blockchain
```
GET /chain
```

---

### ✅ Validasi Blockchain
```
GET /validate
```

---

## 📌 Catatan Teknis

- Belum menggunakan kriptografi (tidak ada wallet / signature)
- Tidak ada sistem Proof of Work (blok langsung ditambang)
- Ideal untuk pembelajaran dan prototyping

---

## 🧭 Roadmap

- [x] Tambah transaksi dan tambang blok
- [ ] Integrasi Wallet & Signature (v4)
- [ ] Validasi transaksi dengan ECDSA (v5)
- [ ] P2P Node Communication (v6)
- [ ] Smart Contract Sederhana (v7)

---

## 🧑‍💻 Kontribusi

Pull request sangat terbuka!  
Laporkan bug atau ide fitur lewat Issues atau langsung buat PR.

---

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License.

---

## 🙋‍♂️ Author

Made with Syahrulcaem
