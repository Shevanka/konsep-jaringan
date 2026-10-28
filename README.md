# Repositori Konsep Jaringan (TI043102)

<p align="center">
  <img src="Tugas 4/asset/pens_logo.png" alt="Logo PENS" width="200">
</p>

Repositori ini memuat dokumentasi resmi, laporan teknis, berkas simulasi (*Cisco Packet Tracer*), berkas presentasi, dan skrip komputasi/visualisasi Python untuk seluruh rangkaian tugas mata kuliah **Konsep Jaringan (TI043102)** pada Program Studi **D4 Teknik Informatika**, **Politeknik Elektronika Negeri Surabaya (PENS)**.

---

## Informasi Akademik

| Bidang | Informasi |
| :--- | :--- |
| **Nama Mahasiswa** | Shevanka Bagus Dwiyudi Kurniawan |
| **NRP** | 3125600044 |
| **Dosen Pengampu** | Dr. Ferry Astika Saputra, ST, M.Sc |
| **Mata Kuliah** | Konsep Jaringan (TI043102) |
| **Program Studi** | D4 Teknik Informatika |
| **Institusi** | Politeknik Elektronika Negeri Surabaya (PENS) |
| **Tahun Akademik** | 2026 |

---

## Peta dan Pelacak Tugas (Roadmap Tugas 1 – 7)

Setiap tugas telah dirapikan ke dalam satu direktori mandiri (*self-contained folder*) yang dilengkapi dengan dokumen laporan format Markdown (`README.md`), aset visual (`asset/`), serta berkas pelengkap lainnya (skrip program, file simulasi `.pkt`, dokumen `.docx`/`.pdf`, dan slide `.pptx`).

| No | Folder Tugas | Ruang Lingkup Materi | Status | Berkas Utama & Berkas Pendukung |
| :---: | :--- | :--- | :---: | :--- |
| **1** | [**`Tugas 1/`**](Tugas%201/) | • 26 Soal Bab 1 (Pengantar Jaringan & Internet)<br>• Standarisasi Kabel UTP (Cat 1 s.d. Cat 9)<br>• Evolusi Protokol Wi-Fi IEEE 802.11 a/b/g/n/ac/ax/be<br>• Garis Waktu Sejarah Internet & Protokol Dasar<br>• Analisis Metrik Jaringan Fast.com | ✅ **Selesai** | • [Dokumentasi Tugas 1](Tugas%201/README.md)<br>• [`Tugas - Pengantar Konsep Jaringan.docx`](Tugas%201/Tugas%20-%20Pengantar%20Konsep%20Jaringan.docx)<br>• [`Tugas - Pengantar Konsep Jaringan.pdf`](Tugas%201/Tugas%20-%20Pengantar%20Konsep%20Jaringan.pdf) |
| **2** | [**`Tugas 2/`**](Tugas%202/) | • Soal Level A: Pemahaman Model OSI & TCP/IP (10 Soal)<br>• Soal Level B: Analisis & Enkapsulasi Protokol Data Unit (10 Soal)<br>• Soal Level C: Evaluasi & Sintesis Desain Arsitektur Jaringan (10 Soal) | ✅ **Selesai** | • [Dokumentasi Tugas 2](Tugas%202/README.md) |
| **3** | [**`Tugas 3/`**](Tugas%203/) | • Simulasi interaktif penjumlahan sinyal harmonisa ganjil ($n = 1, 3, 5, \dots$)<br>• Pembentukan gelombang kotak (*square wave*) via deret Fourier<br>• Plot ganda interaktif: Domain Waktu & Frekuensi dengan GUI Slider<br>• Analisis Pengalamatan IP Classful (5 Alamat Uji) | ✅ **Selesai** | • [Dokumentasi Tugas 3](Tugas%203/README.md)<br>• Skrip GUI: [`Visualisasi.py`](Tugas%203/Visualisasi.py)<br>• [`Tugas - Network Layer.docx`](Tugas%203/Tugas%20-%20Network%20Layer.docx)<br>• [`Tugas - Network Layer.pdf`](Tugas%203/Tugas%20-%20Network%20Layer.pdf) |
| **4** | [**`Tugas 4/`**](Tugas%204/) | • Teori CIDR, *Bit Borrowing*, dan Aturan Subnet-Zero<br>• Pembahasan Soal 1: `192.168.1.0/24` (4 Segmentasi Subnet)<br>• Pembahasan Soal 2: `132.10.0.0/16` (10 Segmentasi Subnet)<br>• Pembahasan Soal 3: `17.8.0.0/16` (4 Segmentasi Subnet)<br>• Pembahasan Soal 4: `8.32.0.0/12` (6 Segmentasi Subnet)<br>• Validasi Desain Topologi Cisco Packet Tracer | ✅ **Selesai** | • [Dokumentasi Tugas 4](Tugas%204/README.md)<br>• Simulasi: [`Soal 1.pkt`](Tugas%204/Soal%201.pkt), [`Soal 2.pkt`](Tugas%204/Soal%202.pkt), [`Soal 3.pkt`](Tugas%204/Soal%203.pkt), [`Soal 4.pkt`](Tugas%204/Soal%204.pkt)<br>• [`Tugas - Classless IP.docx`](Tugas%204/Tugas%20-%20Classless%20IP.docx)<br>• [`Tugas - Classless IP.pdf`](Tugas%204/Tugas%20-%20Classless%20IP.pdf) |
| **5** | [**`Tugas 5/`**](Tugas%205/) | • Mekanisme utilitas `traceroute` (UDP) & `tracert` (ICMP Echo)<br>• Siklus hidup nilai *Time to Live* (TTL) & Hop Limit IPv6<br>• Respon ICMP *Time Exceeded* (Type 11, Code 0) & Unreachable<br>• Arsitektur Router: *Fast Path* (Hardware ASIC/TCAM) vs *Slow Path* (Control CPU)<br>• Verifikasi algoritma RFC 1071 IP Header Checksum & visualisasi latensi | ✅ **Selesai** | • [Dokumentasi Tugas 5](Tugas%205/README.md)<br>• Skrip Analisis & Visualisasi: [`Traceroute_TTL_Analyzer.py`](Tugas%205/Traceroute_TTL_Analyzer.py) |
| **6** | [**`Tugas 6/`**](Tugas%206/) | • Alokasi Variable Length Subnet Mask (VLSM) blok `10.252.108.0/24`<br>&nbsp;&nbsp;1. **Lab A**: 90 Host $\rightarrow$ `/25`<br>&nbsp;&nbsp;2. **Lab B**: 60 Host $\rightarrow$ `/26`<br>&nbsp;&nbsp;3. **Administrasi**: 14 Host $\rightarrow$ `/28`<br>&nbsp;&nbsp;4. **Link P2P**: 2 Host $\rightarrow$ `/30`<br>• Efisiensi alokasi 88,28% dan pencegahan *overlapping* alamat<br>• Engine kalkulator VLSM & generator diagram topologi otomatis | ✅ **Selesai** | • [Dokumentasi Tugas 6](Tugas%206/README.md)<br>• Mesin Kalkulator & Plot: [`VLSM_Calculator.py`](Tugas%206/VLSM_Calculator.py) |
| **7** | [**`Tugas 7/`**](Tugas%207/) | • Rujukan Kursus Resmi [APNIC Academy Routing Fundamentals](https://academy.apnic.net/en/course/routing-fundamentals-course)<br>• Modul 1: Routing Basics (RIB, FIB, Longest Prefix Match)<br>• Modul 2: Use Cases of Static Routes (Default, Blackhole, Floating, ECMP)<br>• Modul 3: OSPF Basics (Link-State IGP, SPF Dijkstra, OSPFv2 & OSPFv3)<br>• Modul 4: IS-IS Basics (OSI Layer 2/CLNS IGP, NET Address, Two-Level Hierarchy)<br>• Modul 5: BGP Basics (Path-Vector EGP, IBGP vs EBGP, Path Attributes, Best Path) | ✅ **Selesai** | • [Dokumentasi Essay Tugas 7](Tugas%207/README.md)<br>• Slide Presentasi: [`Tugas7_PPT_Routing_Fundamentals.pptx`](Tugas%207/Tugas7_PPT_Routing_Fundamentals.pptx) |

---

## Struktur Direktori Repositori

```text
konsep-jaringan/
├── .gitignore                                         # Konfigurasi pengecualian file git
├── README.md                                          # Indeks utama repositori dan peta penugasan
├── Tugas 1/                                           # Direktori Tugas 1: Pengantar Konsep Jaringan
│   ├── README.md                                      # Laporan lengkap pembahasan Bab 1 & Wi-Fi
│   ├── Tugas - Pengantar Konsep Jaringan.docx         # Salinan dokumen Word
│   ├── Tugas - Pengantar Konsep Jaringan.pdf          # Salinan dokumen PDF
│   └── asset/                                         # Aset grafis penugasan
│       └── pens_logo.png                              # Logo resmi PENS
├── Tugas 2/                                           # Direktori Tugas 2: Model OSI dan TCP/IP
│   ├── README.md                                      # Laporan komprehensif Level A, B, dan C
│   └── asset/                                         # Aset grafis penugasan
│       └── pens_logo.png
├── Tugas 3/                                           # Direktori Tugas 3: Visualisasi Harmonisa & IP
│   ├── README.md                                      # Laporan deret Fourier & analisis IP classful
│   ├── Visualisasi.py                                 # Skrip GUI simulasi interaktif deret Fourier
│   ├── Tugas - Network Layer.docx                     # Salinan dokumen Word
│   ├── Tugas - Network Layer.pdf                      # Salinan dokumen PDF
│   └── asset/                                         # Aset hasil simulasi sinyal
│       ├── fourier_n1.png                             # Plot spektrum sinyal harmonisa n=1
│       ├── fourier_n9.png                             # Plot spektrum sinyal harmonisa n=9
│       └── pens_logo.png
├── Tugas 4/                                           # Direktori Tugas 4: Perancangan Subnetting CIDR
│   ├── README.md                                      # Laporan perancangan subnetting Soal 1 s.d. 4
│   ├── Soal 1.pkt                                     # File Cisco Packet Tracer Soal 1 (192.168.1.0/24)
│   ├── Soal 2.pkt                                     # File Cisco Packet Tracer Soal 2 (132.10.0.0/16)
│   ├── Soal 3.pkt                                     # File Cisco Packet Tracer Soal 3 (17.8.0.0/16)
│   ├── Soal 4.pkt                                     # File Cisco Packet Tracer Soal 4 (8.32.0.0/12)
│   ├── Tugas - Classless IP.docx                      # Salinan dokumen Word penugasan
│   ├── Tugas - Classless IP.pdf                       # Salinan dokumen cetak PDF
│   └── asset/                                         # Diagram skema topologi jaringan
│       ├── pens_logo.png                              # Logo resmi PENS
│       ├── Soal 1.png                                 # Skema diagram topologi Soal 1
│       ├── Soal 2.png                                 # Skema diagram topologi Soal 2
│       ├── Soal 3.png                                 # Skema diagram topologi Soal 3
│       └── Soal 4.png                                 # Skema diagram topologi Soal 4
├── Tugas 5/                                           # Direktori Tugas 5: Analisis Traceroute & TTL
│   ├── README.md                                      # Laporan teoritis dan eksperimen traceroute
│   ├── Traceroute_TTL_Analyzer.py                     # Program verifikasi checksum & generator visualisasi
│   └── asset/                                         # Aset telemetri dan arsitektur router
│       ├── fast_vs_slow_path_architecture.png         # Diagram Fast Path vs Slow Path router
│       ├── traceroute_latency_analysis.png            # Grafik analisis latensi per hop traceroute
│       └── pens_logo.png
├── Tugas 6/                                           # Direktori Tugas 6: Perancangan VLSM IPv4
│   ├── README.md                                      # Laporan perancangan subnetting VLSM hierarkis
│   ├── VLSM_Calculator.py                             # Skrip mesin kalkulator & generator visualisasi VLSM
│   └── asset/                                         # Diagram arsitektur dan partisi subnet
│       ├── vlsm_address_block_tree.png                # Diagram pohon partisi ruang alamat IPv4
│       ├── vlsm_host_efficiency_chart.png             # Grafik komparasi efisiensi alokasi host
│       ├── vlsm_network_topology.png                  # Diagram arsitektur topologi jaringan kampus
│       └── pens_logo.png
└── Tugas 7/                                           # Direktori Tugas 7: Routing Fundamentals (APNIC)
    ├── README.md                                      # Laporan essay komprehensif Modul 1 s.d. 5 APNIC
    ├── Tugas7_PPT_Routing_Fundamentals.pptx           # Berkas slide presentasi PowerPoint interaktif
    └── asset/                                         # Aset grafis penugasan
        └── pens_logo.png
```

---

## Petunjuk Penggunaan & Eksekusi Skrip

### 1. Menjalankan Simulasi Harmonisa Fourier (Tugas 3)
Skrip `Visualisasi.py` menyediakan GUI interaktif berbasis Matplotlib dengan kendali slider untuk mengeksplorasi pembentukan gelombang kotak secara *real-time*:
```bash
# Masuk ke direktori Tugas 3
cd "Tugas 3"

# Jalankan skrip Python
python Visualisasi.py
```

### 2. Membuka Berkas Simulasi Cisco Packet Tracer (Tugas 4)
Berkas konfigurasi topologi jaringan pada Tugas 4 dapat dibuka menggunakan **Cisco Packet Tracer** (versi 8.0 atau yang lebih baru):
- Buka Cisco Packet Tracer.
- Pilih menu **File** $\rightarrow$ **Open**, kemudian navigasikan ke direktori `Tugas 4/` dan pilih berkas simulasi yang diinginkan:
  - `Soal 1.pkt` (Subnetting prefix `/26` pada jaringan Kelas C)
  - `Soal 2.pkt` (Subnetting prefix `/20` pada jaringan Kelas B)
  - `Soal 3.pkt` (Subnetting prefix `/18` pada jaringan Kelas A/B)
  - `Soal 4.pkt` (Subnetting prefix `/15` pada jaringan Kelas A)

### 3. Menjalankan Simulasi TTL & Telemetri Traceroute (Tugas 5)
Skrip `Traceroute_TTL_Analyzer.py` melakukan perhitungan matematis terhadap dekrementasi TTL, rekalkulasi IP Header Checksum sesuai RFC 1071, serta menghasilkan grafik telemetri latensi:
```bash
# Masuk ke direktori Tugas 5
cd "Tugas 5"

# Jalankan skrip analisis dan generator plot
python Traceroute_TTL_Analyzer.py
```
Hasil plot akan tersimpan secara otomatis pada direktori `Tugas 5/asset/`.

### 4. Menjalankan Mesin Perhitungan & Visualisasi VLSM (Tugas 6)
Skrip `VLSM_Calculator.py` memvalidasi alokasi subnet, menghitung pemborosan host (*wastage*), serta menghasilkan diagram partisi blok alamat dan topologi jaringan:
```bash
# Masuk ke direktori Tugas 6
cd "Tugas 6"

# Jalankan kalkulator VLSM
python VLSM_Calculator.py
```
Diagram visualisasi akan tersimpan secara otomatis pada direktori `Tugas 6/asset/`.

### 5. Membuka Slide Presentasi Routing Fundamentals (Tugas 7)
Berkas slide presentasi PowerPoint `Tugas7_PPT_Routing_Fundamentals.pptx` mencakup ringkasan eksekutif seluruh modul kursus APNIC Academy:
- Navigasikan ke direktori `Tugas 7/`.
- Buka berkas `Tugas7_PPT_Routing_Fundamentals.pptx` menggunakan Microsoft PowerPoint, LibreOffice Impress, atau Google Slides.

---

## Lisensi dan Hak Cipta

Seluruh materi, laporan praktikum, berkas simulasi, dan kode program dalam repositori ini disusun untuk keperluan akademik perkuliahan pada Politeknik Elektronika Negeri Surabaya (PENS). Dilarang keras melakukan plagiarisme langsung tanpa mencantumkan atribusi akademik yang sesuai.
