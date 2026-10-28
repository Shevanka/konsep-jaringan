# TUGAS KONSEP JARINGAN
## TUGAS KE – 4: Classless Inter-Domain Routing (CIDR) & Perancangan Subnetting IP

<p align="center">
  <img src="asset/pens_logo.png" alt="Logo PENS" width="220">
</p>

| Informasi | Keterangan |
| :--- | :--- |
| **Nama** | Shevanka Bagus Dwiyudi Kurniawan |
| **NRP** | 3125600044 |
| **Dosen Pengajar** | Dr. Ferry Astika Saputra, ST, M.Sc |
| **Mata Kuliah** | Konsep Jaringan (TI043102) |
| **Program Studi** | D4 Teknik Informatika |
| **Institusi** | Politeknik Elektronika Negeri Surabaya (PENS) |
| **Tahun Akademik** | 2026 |
| **Berkas Sumber** | [`Tugas - Classless IP.docx`](Tugas%20-%20Classless%20IP.docx) &bull; [`Tugas - Classless IP.pdf`](Tugas%20-%20Classless%20IP.pdf) |

---

## Daftar Isi

1. [Deskripsi Penugasan](#1-deskripsi-penugasan)
2. [Landasan Teori: Pengalamatan Classless dan Subnetting](#2-landasan-teori-pengalamatan-classless-dan-subnetting)
   - 2.1 [Prinsip CIDR dan Variasi Panjang Prefix](#21-prinsip-cidr-dan-variasi-panjang-prefix)
   - 2.2 [Formulasi Peminjaman Bit (*Bit Borrowing*) dan Aturan Subnet-Zero](#22-formulasi-peminjaman-bit-bit-borrowing-dan-aturan-subnet-zero)
   - 2.3 [Penentuan Interval Blok Subnet (*Magic Number / Step*)](#23-penentuan-interval-blok-subnet-magic-number--step)
3. [Pembahasan Soal 1: `192.168.1.0/24` (4 Segmentasi)](#3-pembahasan-soal-1-1921681024-4-segmentasi)
   - 3.1 [Perhitungan Matematis Subnetting](#31-perhitungan-matematis-subnetting)
   - 3.2 [Tabel Alokasi Subnet](#32-tabel-alokasi-subnet)
   - 3.3 [Skema Diagram Topologi dan Berkas Simulasi Packet Tracer](#33-skema-diagram-topologi-dan-berkas-simulasi-packet-tracer)
   - 3.4 [Analisis Arsitektur Topologi Jaringan](#34-analisis-arsitektur-topologi-jaringan)
4. [Pembahasan Soal 2: `132.10.0.0/16` (10 Segmentasi)](#4-pembahasan-soal-2-132100016-10-segmentasi)
   - 4.1 [Perhitungan Matematis Subnetting](#41-perhitungan-matematis-subnetting)
   - 4.2 [Tabel Alokasi Subnet](#42-tabel-alokasi-subnet)
   - 4.3 [Skema Diagram Topologi dan Berkas Simulasi Packet Tracer](#43-skema-diagram-topologi-dan-berkas-simulasi-packet-tracer)
   - 4.4 [Analisis Arsitektur Topologi Jaringan](#44-analisis-arsitektur-topologi-jaringan)
5. [Pembahasan Soal 3: `17.8.0.0/16` (4 Segmentasi)](#5-pembahasan-soal-3-1780016-4-segmentasi)
   - 5.1 [Perhitungan Matematis Subnetting](#51-perhitungan-matematis-subnetting)
   - 5.2 [Tabel Alokasi Subnet](#52-tabel-alokasi-subnet)
   - 5.3 [Skema Diagram Topologi dan Berkas Simulasi Packet Tracer](#53-skema-diagram-topologi-dan-berkas-simulasi-packet-tracer)
   - 5.4 [Analisis Arsitektur Topologi Jaringan](#54-analisis-arsitektur-topologi-jaringan)
6. [Pembahasan Soal 4: `8.32.0.0/12` (6 Segmentasi)](#6-pembahasan-soal-4-8320012-6-segmentasi)
   - 6.1 [Perhitungan Matematis Subnetting](#61-perhitungan-matematis-subnetting)
   - 6.2 [Tabel Alokasi Subnet](#62-tabel-alokasi-subnet)
   - 6.3 [Skema Diagram Topologi dan Berkas Simulasi Packet Tracer](#63-skema-diagram-topologi-dan-berkas-simulasi-packet-tracer)
   - 6.4 [Analisis Arsitektur Topologi Jaringan](#64-analisis-arsitektur-topologi-jaringan)
7. [Tabel Komparasi dan Rekapitulasi Seluruh Soal](#7-tabel-komparasi-dan-rekapitulasi-seluruh-soal)
8. [Kesimpulan](#8-kesimpulan)

---

## 1. Deskripsi Penugasan

Dalam praktikum dan penugasan mata kuliah **Konsep Jaringan**, mahasiswa diminta untuk melakukan analisis perhitungan pembagian segmen (*subnetting*) berbasis pengalamatan tanpa kelas (*Classless Inter-Domain Routing* - CIDR), menyusun tabel alokasi alamat IP secara mendalam, serta merancang arsitektur topologi jaringan interkoneksi perangkat menggunakan simulator **Cisco Packet Tracer**.

Terdapat 4 (empat) butir penugasan yang harus diselesaikan:
1. **Soal 1:** Merancang topologi dan alokasi alamat dari blok dasar **`192.168.1.0/24`** untuk kebutuhan **4 segmentasi jaringan**.
2. **Soal 2:** Merancang topologi dan alokasi alamat dari blok dasar **`132.10.0.0/16`** untuk kebutuhan **10 segmentasi jaringan**.
3. **Soal 3:** Merancang topologi dan alokasi alamat dari blok dasar **`17.8.0.0/16`** untuk kebutuhan **4 segmentasi jaringan**.
4. **Soal 4:** Merancang topologi dan alokasi alamat dari blok dasar **`8.32.0.0/12`** untuk kebutuhan **6 segmentasi jaringan**.

---

## 2. Landasan Teori: Pengalamatan Classless dan Subnetting

### 2.1 Prinsip CIDR dan Variasi Panjang Prefix
Pada era awal arsitektur Internet (RFC 791), pengalamatan IPv4 dibagi secara kaku ke dalam format *Classful* (Kelas A, B, C, D, dan E). Keterbatasan pembagian kelas tersebut menimbulkan inefisiensi alokasi ruang alamat (*address exhaustion*) karena lompatan kapasitas yang sangat besar:
* **Kelas A:** Mengalokasikan $2^{24} - 2 = 16.777.214$ host per network.
* **Kelas B:** Mengalokasikan $2^{16} - 2 = 65.534$ host per network.
* **Kelas C:** Mengalokasikan $2^8 - 2 = 254$ host per network.

Standar **CIDR (*Classless Inter-Domain Routing*)** yang distandarisasi melalui **RFC 1519** dan diperbarui dalam **RFC 4632** menghapus batas-batas kelas alami tersebut. CIDR memperkenalkan notasi *slash* (misalnya `/27`, `/20`, `/19`, `/15`) yang merepresentasikan jumlah bit biner bernilai `1` pada *Subnet Mask*, memungkinkan pemisahan antara Network ID dan Host ID dilakukan pada posisi bit mana pun.

```text
IPv4 32-bit:
[               Network Prefix               |             Host Bits             ]
|<------------------ /P bits --------------->|<--------- (32 - P) bits --------->|
```

### 2.2 Formulasi Peminjaman Bit (*Bit Borrowing*) dan Aturan Subnet-Zero
Untuk memecah suatu network asal menjadi sejumlah $N$ subnet baru, sejumlah $n$ bit dipinjam dari porsi Host ID menjadi Subnet ID. 

Terdapat dua pendekatan dalam penentuan jumlah subnet valid:
1. **Pendekatan Tradisional / Subnet-Zero RFC 950:**
   Pada standar lama, subnet pertama bernilai biner all-zeros (*subnet zero*) dan subnet terakhir bernilai biner all-ones (*all-ones subnet*) dihindari untuk mencegah ambiguitas dengan Network Address induk dan Broadcast Address induk. Formulasinya:
   $$\sum \text{Subnet Valid} = 2^n - 2 \ge N$$
2. **Pendekatan Modern (RFC 1878 / CIDR):**
   Pada sistem operasi dan router modern (`ip subnet-zero` diaktifkan secara default pada Cisco IOS), semua kombinasi biner dapat digunakan penuh:
   $$\sum \text{Subnet} = 2^n \ge N$$

> [!NOTE]
> Pada penugasan ini, perhitungan subnetting menerapkan formula konservatif/klasik $2^n - 2$ untuk memastikan alokasi segmen aman dan redundan, di mana subnet-zero (`000...`) dan all-ones (`111...`) dialokasikan sebagai ruang cadangan (*reserved/spares*).

### 2.3 Penentuan Interval Blok Subnet (*Magic Number / Step*)
Interval antar subnet dihitung dengan rumus:
$$\text{Interval Step} = 256 - \text{Nilai Desimal Oktet Kritis Mask}$$
atau setara dengan bobot bit terkecil (*Least Significant Bit* / LSB) dari bit subnet yang dipinjam:
$$\text{Interval Step} = 2^{8 - m}$$
di mana $m$ adalah jumlah bit subnet yang dipinjam pada oktet kritis bersangkutan.

Kapasitas host yang dapat digunakan (*usable host*) pada setiap subnet dirumuskan sebagai:
$$\text{Jumlah Usable Host} = 2^h - 2$$
di mana $h = 32 - \text{Prefix Baru}$ adalah jumlah sisa bit host, dikurangi 2 untuk **Network Address** (semua bit host bernilai 0) dan **Broadcast Address** (semua bit host bernilai 1).

---

## 3. Pembahasan Soal 1: `192.168.1.0/24` (4 Segmentasi)

### 3.1 Perhitungan Matematis Subnetting

* **Alamat Jaringan Dasar:** `192.168.1.0/24`
  * Kelas Alamiah: Kelas C
  * Default Subnet Mask: `255.255.255.0` (`/24`)
  * Representasi Biner Mask: `11111111.11111111.11111111.00000000`
* **Target Kebutuhan:** 4 segmentasi jaringan valid.
* **Penentuan Jumlah Bit yang Dipinjam ($n$):**
  Menggunakan rumus subnet valid:
  $$2^n - 2 \ge 4 \implies 2^3 - 2 = 8 - 2 = 6 \ge 4$$
  Maka dipinjam $n = 3$ bit pada oktet ke-4.
* **Prefix Baru:**
  $$\text{Prefix Baru} = /24 + 3 = /27$$
* **Subnet Mask Baru:**
  Bit oktet ke-4: `11100000` biner $= 128 + 64 + 32 = 224$ desimal.
  $$\text{Subnet Mask} = 255.255.255.224$$
* **Interval Blok Subnet (*Step*):**
  $$\text{Step} = 256 - 224 = 32$$
* **Kapasitas Usable Host per Subnet:**
  Sisa bit host $h = 32 - 27 = 5$ bit.
  $$\text{Host Usable} = 2^5 - 2 = 32 - 2 = 30 \text{ host/subnet}$$

### 3.2 Tabel Alokasi Subnet

| No | Nilai Biner (3-bit) | Network Address | Host Pertama (Gateway) | Host Terakhir | Broadcast Address | Peruntukan dalam Topologi |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| - | `000` | `192.168.1.0/27` | `192.168.1.1` | `192.168.1.30` | `192.168.1.31` | *Subnet-Zero (Cadangan)* |
| **1** | **`001`** | **`192.168.1.32/27`** | **`192.168.1.33`** | **`192.168.1.62`** | **`192.168.1.63`** | **Transit Backbone (Router Core $\leftrightarrow$ Router1, 2, 3)** |
| **2** | **`010`** | **`192.168.1.64/27`** | **`192.168.1.65`** | **`192.168.1.94`** | **`192.168.1.95`** | **LAN 1 (Router1 $\leftrightarrow$ Switch1 $\leftrightarrow$ PC0)** |
| **3** | **`011`** | **`192.168.1.96/27`** | **`192.168.1.97`** | **`192.168.1.126`** | **`192.168.1.127`** | **LAN 2 (Router2 $\leftrightarrow$ Switch2 $\leftrightarrow$ PC1)** |
| **4** | **`100`** | **`192.168.1.128/27`** | **`192.168.1.129`** | **`192.168.1.158`** | **`192.168.1.159`** | **LAN 3 (Router3 $\leftrightarrow$ Switch3 $\leftrightarrow$ PC2)** |
| - | `101` | `192.168.1.160/27` | `192.168.1.161` | `192.168.1.190` | `192.168.1.191` | *Subnet Cadangan 5* |
| - | `110` | `192.168.1.192/27` | `192.168.1.193` | `192.168.1.222` | `192.168.1.223` | *Subnet Cadangan 6* |
| - | `111` | `192.168.1.224/27` | `192.168.1.225` | `192.168.1.254` | `192.168.1.255` | *All-Ones Subnet (Cadangan)* |

### 3.3 Skema Diagram Topologi dan Berkas Simulasi Packet Tracer

> [!TIP]
> Berkas rancangan topologi dan simulasi aktif dapat diunduh langsung:
> 📦 **Berkas Simulasi Cisco Packet Tracer:** [`Soal 1.pkt`](Soal%201.pkt)

<p align="center">
  <img src="asset/Soal 1.png" alt="Skema Diagram Topologi Soal 1 (192.168.1.0/24)" width="100%">
  <br>
  <em>Gambar 1: Arsitektur Topologi Jaringan 4 Segmentasi Subnet 192.168.1.0/24</em>
</p>

### 3.4 Analisis Arsitektur Topologi Jaringan

1. **Struktur Hirarki Dua Tingkat (Core & Leaf):**
   * **Router Core (Cisco 2911):** Bertindak sebagai gateway utama yang menghubungkan keseluruhan sistem inter-jaringan kampus/kantor ke WAN (*Internet Cloud*).
   * **Transit Subnet (`192.168.1.32/27`):** Menghubungkan antarmuka *downlink* Router Core (`.33`) dengan 3 buah Leaf Router melalui **Switch0** (Cisco Catalyst 2960-24TT):
     * Router1 antarmuka transit: `192.168.1.34`
     * Router2 antarmuka transit: `192.168.1.35`
     * Router3 antarmuka transit: `192.168.1.36`
2. **Segmentasi Akses Lokal (Access LAN):**
   * **LAN 1 (`192.168.1.64/27`):** Disediakan oleh antarmuka LAN Router1 (`192.168.1.65/27`) melalui Switch1 untuk melayani PC0 (`192.168.1.66/27`).
   * **LAN 2 (`192.168.1.96/27`):** Disediakan oleh antarmuka LAN Router2 (`192.168.1.97/27`) melalui Switch2 untuk melayani PC1 (`192.168.1.98/27`).
   * **LAN 3 (`192.168.1.128/27`):** Disediakan oleh antarmuka LAN Router3 (`192.168.1.129/27`) melalui Switch3 untuk melayani PC2 (`192.168.1.130/27`).
3. **Penyekatan Broadcast Domain:** Setiap LAN berada pada broadcast domain terisolasi di bawah router masing-masing, sehingga badai broadcast (*broadcast storm*) pada PC0 tidak merambat ke segmen PC1 maupun PC2.

---

## 4. Pembahasan Soal 2: `132.10.0.0/16` (10 Segmentasi)

### 4.1 Perhitungan Matematis Subnetting

* **Alamat Jaringan Dasar:** `132.10.0.0/16`
  * Kelas Alamiah: Kelas B
  * Default Subnet Mask: `255.255.0.0` (`/16`)
  * Representasi Biner Mask: `11111111.11111111.00000000.00000000`
* **Target Kebutuhan:** 10 segmentasi jaringan.
* **Penentuan Jumlah Bit yang Dipinjam ($n$):**
  Untuk mencakup minimal 10 subnet:
  $$2^n \ge 10 \implies n = 4 \quad (2^4 = 16 \text{ subnet})$$
  Dipinjam $n = 4$ bit pada oktet ke-3.
* **Prefix Baru:**
  $$\text{Prefix Baru} = /16 + 4 = /20$$
* **Subnet Mask Baru:**
  Bit oktet ke-3: `11110000` biner $= 128 + 64 + 32 + 16 = 240$ desimal.
  $$\text{Subnet Mask} = 255.255.240.0$$
* **Interval Blok Subnet (*Step*):**
  $$\text{Step} = 256 - 240 = 16 \text{ (pada oktet ke-3)}$$
* **Kapasitas Usable Host per Subnet:**
  Sisa bit host $h = 32 - 20 = 12$ bit (4 bit di oktet ke-3 dan 8 bit di oktet ke-4).
  $$\text{Host Usable} = 2^{12} - 2 = 4.096 - 2 = 4.094 \text{ host/subnet}$$

### 4.2 Tabel Alokasi Subnet

| No | Nilai Biner (4-bit) | Network Address | Host Pertama (Gateway) | Host Terakhir | Broadcast Address | Status / Keterangan |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| - | `0000` | `132.10.0.0/20` | `132.10.0.1` | `132.10.15.254` | `132.10.15.255` | *Subnet-Zero (Cadangan)* |
| **1** | **`0001`** | **`132.10.16.0/20`** | **`132.10.16.1`** | **`132.10.31.254`** | **`132.10.31.255`** | **Segmen 1: Transit Backbone Router0 $\leftrightarrow$ Router1–4** |
| **2** | **`0010`** | **`132.10.32.0/20`** | **`132.10.32.1`** | **`132.10.47.254`** | **`132.10.47.255`** | **Segmen 2: LAN 1 (Router1 $\leftrightarrow$ Switch1 $\leftrightarrow$ PC0)** |
| **3** | **`0011`** | **`132.10.48.0/20`** | **`132.10.48.1`** | **`132.10.63.254`** | **`132.10.63.255`** | **Segmen 3: LAN 2 (Router2 $\leftrightarrow$ Switch2 $\leftrightarrow$ PC1)** |
| **4** | **`0100`** | **`132.10.64.0/20`** | **`132.10.64.1`** | **`132.10.79.254`** | **`132.10.79.255`** | **Segmen 4: LAN 3 (Router3 $\leftrightarrow$ Switch3 $\leftrightarrow$ PC2)** |
| **5** | **`0101`** | **`132.10.80.0/20`** | **`132.10.80.1`** | **`132.10.95.254`** | **`132.10.95.255`** | **Segmen 5: LAN 4 (Router4 $\leftrightarrow$ Switch4 $\leftrightarrow$ PC3)** |
| **6** | **`0110`** | **`132.10.96.0/20`** | **`132.10.96.1`** | **`132.10.111.254`** | **`132.10.111.255`** | Segmen 6 (Alokasi Subnet Lanjutan) |
| **7** | **`0111`** | **`132.10.112.0/20`** | **`132.10.112.1`** | **`132.10.127.254`** | **`132.10.127.255`** | Segmen 7 (Alokasi Subnet Lanjutan) |
| **8** | **`1000`** | **`132.10.128.0/20`** | **`132.10.128.1`** | **`132.10.143.254`** | **`132.10.143.255`** | Segmen 8 (Alokasi Subnet Lanjutan) |
| **9** | **`1001`** | **`132.10.144.0/20`** | **`132.10.144.1`** | **`132.10.159.254`** | **`132.10.159.255`** | Segmen 9 (Alokasi Subnet Lanjutan) |
| **10** | **`1010`** | **`132.10.160.0/20`** | **`132.10.160.1`** | **`132.10.175.254`** | **`132.10.175.255`** | Segmen 10 (Alokasi Subnet Lanjutan) |
| - | `1011`–`1110` | *Blok Cadangan* | *...* | *...* | *...* | *Cadangan Ekspansi Skala Besar* |
| - | `1111` | `132.10.240.0/20` | `132.10.240.1` | `132.10.255.254` | `132.10.255.255` | *All-Ones Subnet (Cadangan)* |

### 4.3 Skema Diagram Topologi dan Berkas Simulasi Packet Tracer

> [!TIP]
> Berkas rancangan topologi dan simulasi aktif dapat diunduh langsung:
> 📦 **Berkas Simulasi Cisco Packet Tracer:** [`Soal 2.pkt`](Soal%202.pkt)

<p align="center">
  <img src="asset/Soal 2.png" alt="Skema Diagram Topologi Soal 2 (132.10.0.0/16)" width="480">
  <br>
  <em>Gambar 2: Topologi Jaringan Interkoneksi Router dan 4 Cabang LAN (132.10.0.0/20)</em>
</p>

### 4.4 Analisis Arsitektur Topologi Jaringan

* **Peran Port & Sambungan Antarmuka:**
  * **Router0 (Core Router 2911):** Menghubungkan interface `Gig0/0` ke Internet dan interface `Fa0/1` menuju **Switch0** (`Fa0/1`).
  * **Switch0 (Distribution Switch):** Mendistribusikan jalur transit ke 4 router cabang:
    * Port `Fa0/2` $\rightarrow$ `Gig0/0` pada Router1
    * Port `Fa0/3` $\rightarrow$ `Gig0/0` pada Router2
    * Port `Fa0/4` $\rightarrow$ `Gig0/0` pada Router3
    * Port `Fa0/5` $\rightarrow$ `Gig0/0` pada Router4
* **Distribusi Subnet LAN:** Masing-masing router cabang (Router1 hingga Router4) menyediakan jalur LAN berkecepatan tinggi via port `Gig0/1` ke port `Fa0/1` pada Switch akses (Switch1–Switch4), yang kemudian mengalirkan paket data ke port `Fa0` pada PC klien (PC0–PC3).
* **Kapasitas Skalabilitas:** Alokasi prefix `/20` menyediakan kapasitas luar biasa besar (4.094 host per subnet), sangat ideal untuk jaringan kampus terdistribusi atau gedung perkantoran multi-lantai.

---

## 5. Pembahasan Soal 3: `17.8.0.0/16` (4 Segmentasi)

### 5.1 Perhitungan Matematis Subnetting

* **Alamat Jaringan Dasar:** `17.8.0.0/16`
  * Format Pengalamatan: Blok CIDR `/16` dari alokasi kelas publik.
  * Subnet Mask Default: `255.255.0.0`
* **Target Kebutuhan:** 4 segmentasi valid.
* **Penentuan Jumlah Bit yang Dipinjam ($n$):**
  Menggunakan rumus subnet valid tradisonal:
  $$2^n - 2 \ge 4 \implies 2^3 - 2 = 6 \ge 4$$
  Dipinjam $n = 3$ bit pada oktet ke-3.
* **Prefix Baru:**
  $$\text{Prefix Baru} = /16 + 3 = /19$$
* **Subnet Mask Baru:**
  Bit oktet ke-3: `11100000` biner $= 128 + 64 + 32 = 224$ desimal.
  $$\text{Subnet Mask} = 255.255.224.0$$
* **Interval Blok Subnet (*Step*):**
  $$\text{Step} = 256 - 224 = 32 \text{ (pada oktet ke-3)}$$
* **Kapasitas Usable Host per Subnet:**
  Sisa bit host $h = 32 - 19 = 13$ bit (5 bit di oktet ke-3 dan 8 bit di oktet ke-4).
  $$\text{Host Usable} = 2^{13} - 2 = 8.192 - 2 = 8.190 \text{ host/subnet}$$

### 5.2 Tabel Alokasi Subnet

| No | Nilai Biner (3-bit) | Network Address | Host Pertama (Gateway) | Host Terakhir | Broadcast Address | Peruntukan dalam Topologi |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| - | `000` | `17.8.0.0/19` | `17.8.0.1` | `17.8.31.254` | `17.8.31.255` | *Subnet-Zero (Cadangan)* |
| **1** | **`001`** | **`17.8.32.0/19`** | **`17.8.32.1`** | **`17.8.63.254`** | **`17.8.63.255`** | **Transit Backbone (Router Core $\leftrightarrow$ Router1, 2, 3)** |
| **2** | **`010`** | **`17.8.64.0/19`** | **`17.8.64.1`** | **`17.8.95.254`** | **`17.8.95.255`** | **LAN 1 (Router1 $\leftrightarrow$ Switch1 $\leftrightarrow$ PC0)** |
| **3** | **`011`** | **`17.8.96.0/19`** | **`17.8.96.1`** | **`17.8.127.254`** | **`17.8.127.255`** | **LAN 2 (Router2 $\leftrightarrow$ Switch2 $\leftrightarrow$ PC2)** |
| **4** | **`100`** | **`17.8.128.0/19`** | **`17.8.128.1`** | **`17.8.159.254`** | **`17.8.159.255`** | **LAN 3 (Router3 $\leftrightarrow$ Switch3 $\leftrightarrow$ PC3)** |
| - | `101`–`110` | *Blok Cadangan* | *...* | *...* | *...* | *Cadangan Segmen Masa Depan* |
| - | `111` | `17.8.224.0/19` | `17.8.224.1` | `17.8.255.254` | `17.8.255.255` | *All-Ones Subnet (Cadangan)* |

### 5.3 Skema Diagram Topologi dan Berkas Simulasi Packet Tracer

> [!TIP]
> Berkas rancangan topologi dan simulasi aktif dapat diunduh langsung:
> 📦 **Berkas Simulasi Cisco Packet Tracer:** [`Soal 3.pkt`](Soal%203.pkt)

<p align="center">
  <img src="asset/Soal 3.png" alt="Skema Diagram Topologi Soal 3 (17.8.0.0/16)" width="420">
  <br>
  <em>Gambar 3: Desain Topologi Jaringan 4 Segmen Berbasis Alamat IP 17.8.0.0/19</em>
</p>

### 5.4 Analisis Arsitektur Topologi Jaringan

1. **Topologi Fisik:** Terdiri dari 1 Router Utama (`Router0`) yang terhubung langsung ke Cloud Internet lewat interface `Gig0/0`.
2. **Konektivitas Backbone:** Port `Fa0/1` Router0 terhubung ke Switch0 (`Fa0/1`). Dari Switch0, jalur didistribusikan ke 3 Router downstream:
   * Switch0 `Fa0/2` $\rightarrow$ Router1 `Gig0/0`
   * Switch0 `Fa0/3` $\rightarrow$ Router2 `Gig0/0`
   * Switch0 `Fa0/4` $\rightarrow$ Router3 `Gig0/0`
3. **Konektivitas LAN End-User:** Masing-masing router downstream menghubungkan interface `Gig0/1` ke switch masing-masing (Switch1, Switch2, Switch3), melayani workstation akhir (PC0, PC2, PC3). Seluruh segmen menggunakan subnet mask `255.255.224.0`.

---

## 6. Pembahasan Soal 4: `8.32.0.0/12` (6 Segmentasi)

### 6.1 Perhitungan Matematis Subnetting

* **Alamat Jaringan Dasar:** `8.32.0.0/12`
  * Format Alokasi: Alamat kelas besar (blok `/12`).
  * Subnet Mask Awal: `255.240.0.0`
  * Representasi Biner Mask Awal: `11111111.11110000.00000000.00000000`
* **Target Kebutuhan:** 6 segmentasi jaringan valid.
* **Penentuan Jumlah Bit yang Dipinjam ($n$):**
  Menggunakan rumus subnet valid:
  $$2^n - 2 \ge 6 \implies 2^n \ge 8 \implies n = 3 \text{ bit}$$
  Bit ini dipinjam dari Host ID pada **oktet ke-2** (melanjutkan 4 bit Network ID yang sudah ada).
* **Prefix Baru:**
  $$\text{Prefix Baru} = /12 + 3 = /15$$
* **Penyusunan Subnet Mask Baru:**
  * Oktet 1: `11111111` $= 255$
  * Oktet 2: 4 bit awal (`1111`) + 3 bit subnet baru (`111`) + 1 bit host (`0`) $= 11111110 \text{ biner} = 254$ desimal.
  * Oktet 3 & 4: `00000000.00000000` $= 0.0$
  $$\text{Subnet Mask Baru} = 255.254.0.0$$
* **Interval Blok Subnet (*Step*):**
  $$\text{Step} = 256 - 254 = 2 \text{ (pada oktet ke-2)}$$
* **Kapasitas Usable Host per Subnet:**
  Sisa bit host $h = 32 - 15 = 17$ bit (1 bit pada oktet ke-2, 8 bit pada oktet ke-3, dan 8 bit pada oktet ke-4).
  $$\text{Host Usable} = 2^{17} - 2 = 131.072 - 2 = 131.070 \text{ host/subnet}$$

### 6.2 Tabel Alokasi Subnet

| No | Nilai Biner (3-bit) | Network Address | Host Pertama (Gateway) | Host Terakhir | Broadcast Address | Peruntukan dalam Topologi |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| - | `000` | `8.32.0.0/15` | `8.32.0.1` | `8.33.255.254` | `8.33.255.255` | *Subnet-Zero (Cadangan)* |
| **1** | **`001`** | **`8.34.0.0/15`** | **`8.34.0.1`** | **`8.35.255.254`** | **`8.35.255.255`** | **Transit Backbone (Router0 $\leftrightarrow$ Router1 s/d Router5)** |
| **2** | **`010`** | **`8.36.0.0/15`** | **`8.36.0.1`** | **`8.37.255.254`** | **`8.37.255.255`** | **LAN 1 (Router1 $\leftrightarrow$ Switch1 $\leftrightarrow$ PC0)** |
| **3** | **`011`** | **`8.38.0.0/15`** | **`8.38.0.1`** | **`8.39.255.254`** | **`8.39.255.255`** | **LAN 2 (Router2 $\leftrightarrow$ Switch2 $\leftrightarrow$ PC1)** |
| **4** | **`100`** | **`8.40.0.0/15`** | **`8.40.0.1`** | **`8.41.255.254`** | **`8.41.255.255`** | **LAN 3 (Router3 $\leftrightarrow$ Switch3 $\leftrightarrow$ PC2)** |
| **5** | **`101`** | **`8.42.0.0/15`** | **`8.42.0.1`** | **`8.43.255.254`** | **`8.43.255.255`** | **LAN 4 (Router4 $\leftrightarrow$ Switch4 $\leftrightarrow$ PC3)** |
| **6** | **`110`** | **`8.44.0.0/15`** | **`8.44.0.1`** | **`8.45.255.254`** | **`8.45.255.255`** | **LAN 5 (Router5 $\leftrightarrow$ Switch5 $\leftrightarrow$ PC4)** |
| - | `111` | `8.46.0.0/15` | `8.46.0.1` | `8.47.255.254` | `8.47.255.255` | *All-Ones Subnet (Cadangan)* |

### 6.3 Skema Diagram Topologi dan Berkas Simulasi Packet Tracer

> [!TIP]
> Berkas rancangan topologi dan simulasi aktif dapat diunduh langsung:
> 📦 **Berkas Simulasi Cisco Packet Tracer:** [`Soal 4.pkt`](Soal%204.pkt)

<p align="center">
  <img src="asset/Soal 4.png" alt="Skema Diagram Topologi Soal 4 (8.32.0.0/12)" width="520">
  <br>
  <em>Gambar 4: Desain Topologi Jaringan 6 Segmen Berbasis Blok Alamat Supernetting 8.32.0.0/15</em>
</p>

### 6.4 Analisis Arsitektur Topologi Jaringan

* **Struktur Bus / Star Distribusi:**
  * Router Core (`Router0`) terhubung ke Cloud Internet via `Gig0/0`, dan terhubung ke Switch Backbone (`Switch0`) melalui port `Fa0/1`.
  * **Switch0** mendistribusikan jalur backbone transit (`8.34.0.0/15`) menuju 5 (lima) router cabang:
    * Port `Fa0/2` menuju Router1 (`Gig0/0`)
    * Port `Fa0/3` menuju Router2 (`Gig0/0`)
    * Port `Fa0/4` menuju Router3 (`Gig0/0`)
    * Port `Fa0/5` menuju Router4 (`Gig0/0`)
    * Port `Fa0/6` menuju Router5 (`Gig0/0`)
* **Penyediaan Segmen LAN Pelanggan / Institusi:**
  Setiap router cabang menyediakan jaringan LAN otonom berkapasitas sangat masif (hingga 131.070 host):
  * **LAN 1:** `8.36.0.0/15` $\rightarrow$ Switch1 $\rightarrow$ PC0
  * **LAN 2:** `8.38.0.0/15` $\rightarrow$ Switch2 $\rightarrow$ PC1
  * **LAN 3:** `8.40.0.0/15` $\rightarrow$ Switch3 $\rightarrow$ PC2
  * **LAN 4:** `8.42.0.0/15` $\rightarrow$ Switch4 $\rightarrow$ PC3
  * **LAN 5:** `8.44.0.0/15` $\rightarrow$ Switch5 $\rightarrow$ PC4

---

## 7. Tabel Komparasi dan Rekapitulasi Seluruh Soal

Berikut adalah tabel rekapitulasi perbandingan metrik teknis perhitungan subnetting dari keempat butir soal:

| Parameter Evaluasi | Soal 1 | Soal 2 | Soal 3 | Soal 4 |
| :--- | :---: | :---: | :---: | :---: |
| **Alamat Jaringan Dasar** | `192.168.1.0/24` | `132.10.0.0/16` | `17.8.0.0/16` | `8.32.0.0/12` |
| **Kelas Alami IP** | Kelas C | Kelas B | Kelas B (Classless) | Kelas A (Supernet) |
| **Default Prefix Mask** | `/24` | `/16` | `/16` | `/12` |
| **Kebutuhan Subnet** | 4 segmen | 10 segmen | 4 segmen | 6 segmen |
| **Bit Dipinjam ($n$)** | 3 bit | 4 bit | 3 bit | 3 bit |
| **Oktet Tempat Peminjaman** | Oktet ke-4 | Oktet ke-3 | Oktet ke-3 | Oktet ke-2 |
| **Prefix Baru (CIDR)** | **`/27`** | **`/20`** | **`/19`** | **`/15`** |
| **Subnet Mask Baru** | `255.255.255.224` | `255.255.240.0` | `255.255.224.0` | `255.254.0.0` |
| **Interval Blok (*Step*)** | 32 (oktet 4) | 16 (oktet 3) | 32 (oktet 3) | 2 (oktet 2) |
| **Total Subnet Dihasilkan** | 8 ($2^3$) | 16 ($2^4$) | 8 ($2^3$) | 8 ($2^3$) |
| **Jumlah Subnet Terpakai** | 4 subnet aktif | 10 subnet aktif | 4 subnet aktif | 6 subnet aktif |
| **Usable Host per Subnet** | **30 host** | **4.094 host** | **8.190 host** | **131.070 host** |
| **Total Kapasitas Host Aktif** | $4 \times 30 = 120$ | $10 \times 4.094 = 40.940$ | $4 \times 8.190 = 32.760$ | $6 \times 131.070 = 786.420$ |
| **Tautan Berkas Simulasi** | [`Soal 1.pkt`](Soal%201.pkt) | [`Soal 2.pkt`](Soal%202.pkt) | [`Soal 3.pkt`](Soal%203.pkt) | [`Soal 4.pkt`](Soal%204.pkt) |
| **Diagram Gambar Topologi** | [`Soal 1.png`](asset/Soal%201.png) | [`Soal 2.png`](asset/Soal%202.png) | [`Soal 3.png`](asset/Soal%203.png) | [`Soal 4.png`](asset/Soal%204.png) |

---

## 8. Kesimpulan

1. **Efektivitas Segmentasi Classless:** Implementasi CIDR dan teknik peminjaman bit terbukti mampu memecah berbagai tingkatan alamat IP (mulai dari kelas C `/24` hingga supernet `/12`) menjadi jumlah subnet yang presisi sesuai kebutuhan organisasi tanpa terikat batasan kelas konvensional.
2. **Keteraturan Alokasi Alamat:** Melalui penentuan *Interval Step* yang tepat pada oktet kritis (oktet 4 pada Soal 1, oktet 3 pada Soal 2 & 3, serta oktet 2 pada Soal 4), batas-batas Network Address dan Broadcast Address dapat ditentukan secara matematis tanpa adanya tumpang tindih (*address overlapping*).
3. **Penerapan Hirarki Jaringan:** Seluruh desain topologi mengadopsi model *Core-Distribution-Access* yang memisahkan segmen transit antar-router (*backbone*) dengan segmen akses lokal (*access LAN*). Hal ini mengisolasi lalu lintas lokal, mengeliminasi dampak badai broadcast antar-departemen, serta memfasilitasi penerapan kebijakan keamanan lalu lintas (*firewall/ACL*) di tingkat router.
4. **Validasi Simulasi Perangkat:** Rancangan topologi telah diuji dan didokumentasikan ke dalam berkas **Cisco Packet Tracer** (`.pkt`), membuktikan bahwa seluruh gateway antarmuka dan alamat IP klien berada dalam kondisi operasional dan valid.
