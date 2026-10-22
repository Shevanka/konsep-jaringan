# Catatan dan Tugas Konsep Jaringan

Repositori ini berisi kumpulan tugas, materi, skrip simulasi, dan catatan praktikum mata kuliah **Konsep Jaringan (TI043102)** - Program Studi D4 Teknik Informatika, Politeknik Elektronika Negeri Surabaya (PENS).

---

## Peta dan Pelacak Tugas (Task Roadmap)

| No | Nama Tugas | Ruang Lingkup Materi | Status | Berkas Terkait |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Tugas Bab 1 & Protokol Wi-Fi** | • 26 Soal Bab 1 (Pengantar Jaringan & Internet)<br>• Tabel UTP Cat 1–9<br>• Standar Wi-Fi IEEE 802.11 a/b/g/n/ac/ax/be<br>• Timeline Sejarah Internet<br>• Analisis Metrik Fast.com | ✅ **Selesai** | • [`Tugas 1 - Pengantar Konsep Jaringan.md`](Tugas%201%20-%20Pengantar%20Konsep%20Jaringan.md) |
| **2** | **Tugas Bab 2 (A, B, C)** | • Soal Level A: Pemahaman Model OSI & TCP/IP (10 Soal)<br>• Soal Level B: Analisis & Enkapsulasi Paket (10 Soal)<br>• Soal Level C: Evaluasi & Sintesis Desain Jaringan (10 Soal) | ✅ **Selesai** | • [`Tugas 2 - Model OSI dan TCPIP.md`](Tugas%202%20-%20Model%20OSI%20dan%20TCPIP.md) |
| **3** | **Visualisasi Harmonisa Fourier & Analisis IP** | • Simulasi interaktif penjumlahan sinyal harmonisa ganjil ($n = 1, 3, 5, \dots$)<br>• Pembentukan gelombang kotak (*square wave*) via deret Fourier<br>• Plot ganda: Domain Waktu & Domain Frekuensi dengan GUI Slider<br>• Analisis IP Classful (5 Alamat IP) | ✅ **Selesai** | • [`Tugas 3 - Visualisasi Harmonisa dan Analisis IP.md`](Tugas%203%20-%20Visualisasi%20Harmonisa%20dan%20Analisis%20IP.md)<br>• [`Visualisasi.py`](Visualisasi.py) |
| **4** | **Perhitungan Subnetting** | • Analisis Classful IP (Kelas A, B, C, Network, Host, Broadcast)<br>• Subnetting Classless (Prefix /27, /20, /18)<br>• Desain topologi segmentasi jaringan | ✅ **Selesai** | • Folder `[ 5 ] 24 September 2026` (`Tugas - Classless IP.docx`) |
| **5** | **Analisis Traceroute & TTL** | • Cara kerja utilitas `traceroute` / `tracert`<br>• Mekanisme *Time to Live* (TTL) & Hop Limit<br>• Respon ICMP *Time Exceeded* (Type 11) & ICMP *Echo Reply* / UDP Unreachable<br>• Perbedaan implementasi OS & analisis *hop latency* / timeout | 📝 *Siap Dikerjakan* | — |
| **6** | **Perancangan VLSM 10.252.108.0 /24** | • Alokasi blok subnet variabel berbasis efisiensi kebutuhan host:<br>&nbsp;&nbsp;1. **Lab A**: 90 host $\rightarrow$ `/25`<br>&nbsp;&nbsp;2. **Lab B**: 60 host $\rightarrow$ `/26`<br>&nbsp;&nbsp;3. **Administrasi**: 14 host $\rightarrow$ `/28`<br>&nbsp;&nbsp;4. **End-point (Link P2P)**: 2 host $\rightarrow$ `/30` | 📝 *Siap Dikerjakan* | — |
| **7** | **Essay & Slide Presentasi Routing (APNIC)** | • Rujukan: [APNIC Academy Routing Fundamentals](https://academy.apnic.net/en/course/routing-fundamentals-course)<br>• Modul 1: Routing Basics<br>• Modul 2: Use Cases of Static Routes<br>• Modul 3: OSPF Basics (Link-State IGP)<br>• Modul 4: IS-IS Basics (OSI L2/CLNS IGP)<br>• Modul 5: BGP Basics (Path-Vector EGP)<br>• *Output:* Dokumen cetak (Print) & Slide PPT | 📝 *Siap Dikerjakan* | — |

---

## Struktur Direktori Repositori

```text
konsep-jaringan/
├── .gitignore
├── README.md                                          # Indeks dan pelacak tugas
├── Tugas 1 - Pengantar Konsep Jaringan.md             # Bab 1 & Protokol Wi-Fi
├── Tugas 2 - Model OSI dan TCPIP.md                   # Bab 2 (Level A, B, C)
├── Tugas 3 - Visualisasi Harmonisa dan Analisis IP.md # Fourier Series & Analisis IP
├── Visualisasi.py                                     # Skrip GUI interaktif Fourier
└── asset/
    ├── fourier_n1.png                                 # Hasil simulasi n=1
    ├── fourier_n9.png                                 # Hasil simulasi n=9
    ├── image1.png
    ├── image2.png
    └── image3.png
```
