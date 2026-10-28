# TUGAS KONSEP JARINGAN
## TUGAS KE – 7: Essay & Slide Presentasi Routing Fundamentals (APNIC)

| Informasi | Keterangan |
| :--- | :--- |
| **Nama** | Shevanka Bagus Dwiyudi Kurniawan |
| **NRP** | 3125600044 |
| **Dosen Pengajar** | Dr. Ferry Astika Saputra, ST, M.Sc |
| **Mata Kuliah** | Konsep Jaringan (TI043102) |
| **Program Studi** | D4 Teknik Informatika |
| **Institusi** | Politeknik Elektronika Negeri Surabaya (PENS) |
| **Tahun Akademik** | 2026 |
| **Berkas Presentasi** | [Tugas7_PPT_Routing_Fundamentals.pptx](Tugas7_PPT_Routing_Fundamentals.pptx) |
| **Referensi Utama** | [APNIC Academy – Routing Fundamentals Course](https://academy.apnic.net/en/course/routing-fundamentals-course) |

---

## Module 1: Routing Basics

### 1.1 Pengertian Router dan Routing

Router adalah perangkat jaringan yang beroperasi pada Layer 3 (Network Layer) model OSI, berfungsi sebagai penghubung antar jaringan (internetwork) yang berbeda. Berbeda dengan switch yang bekerja pada Layer 2 menggunakan MAC address untuk meneruskan frame dalam satu jaringan lokal (LAN), router menggunakan alamat IP untuk menentukan jalur terbaik dalam meneruskan paket data dari satu jaringan ke jaringan lainnya.

Proses routing secara fundamental melibatkan dua fungsi utama yang berbeda namun saling terkait:

- **Control Plane (Routing):** Bertanggung jawab dalam membangun dan memelihara tabel routing. Control plane menjalankan protokol routing, bertukar informasi topologi dengan router tetangga, dan menghitung jalur terbaik menuju setiap destinasi jaringan.
- **Data Plane (Forwarding):** Bertanggung jawab dalam meneruskan paket data secara aktual. Ketika sebuah paket tiba di router, data plane membaca header IP, melakukan lookup pada tabel forwarding, dan mengirimkan paket melalui interface yang sesuai.

### 1.2 Proses Forwarding Paket

Ketika router menerima sebuah paket, proses forwarding berlangsung sebagai berikut:

1. **Dekapsulasi:** Router membuka (strip) frame Layer 2 yang membungkus paket.
2. **Inspeksi Header:** Router membaca alamat IP tujuan (destination IP address) pada header Layer 3.
3. **Table Lookup:** Router mencari kecocokan di tabel routing/forwarding menggunakan algoritma **Longest Prefix Match (LPM)**.
4. **Modifikasi Paket:** Router mengurangi nilai TTL (Time to Live) sebesar 1.
5. **Enkapsulasi Ulang:** Router membungkus paket dalam frame Layer 2 baru dengan MAC address tujuan berikutnya (diperoleh melalui ARP).
6. **Pengiriman:** Paket dikirim melalui interface keluar (egress interface) yang sesuai.

### 1.3 RIB dan FIB

- **RIB (Routing Information Base):** Merupakan tabel routing utama yang dikelola oleh control plane. RIB berisi semua rute yang dipelajari dari berbagai sumber (connected, static, dynamic protocols). Ketika beberapa sumber memberikan rute ke destinasi yang sama, RIB menggunakan **Administrative Distance (AD)** untuk memilih rute terbaik.
- **FIB (Forwarding Information Base):** Merupakan tabel forwarding yang dioptimalkan dan disimpan di hardware (misalnya TCAM pada router modern). FIB merupakan subset dari RIB yang berisi hanya rute-rute terbaik dan digunakan oleh data plane untuk forwarding berkecepatan tinggi.

### 1.4 Longest Prefix Match (LPM)

Algoritma LPM adalah mekanisme fundamental yang digunakan router untuk memilih rute ketika terdapat multiple entry yang cocok dengan alamat IP tujuan. Router selalu memilih rute dengan prefix length terpanjang (subnet mask terbesar) karena rute tersebut paling spesifik.

**Contoh:**
Jika tabel routing memiliki tiga entry:
- `0.0.0.0/0` → Default route
- `10.0.0.0/8` → Rute ke jaringan 10.x.x.x
- `10.10.10.0/24` → Rute spesifik

Untuk paket dengan tujuan `10.10.10.55`, router akan memilih `10.10.10.0/24` karena memiliki prefix terpanjang (/24 > /8 > /0).

### 1.5 Klasifikasi Protokol Routing

Protokol routing diklasifikasikan berdasarkan cakupan operasinya:

- **Interior Gateway Protocol (IGP):** Protokol yang beroperasi dalam satu Autonomous System (AS). Contoh: OSPF, IS-IS, EIGRP, RIP.
- **Exterior Gateway Protocol (EGP):** Protokol yang beroperasi antar Autonomous System. Contoh utama: BGP.

Berdasarkan mekanisme kerjanya, IGP dibagi menjadi:
- **Distance-Vector:** Setiap router hanya mengetahui jarak (metric) dan arah (next-hop) menuju destinasi. Contoh: RIP, EIGRP.
- **Link-State:** Setiap router memiliki peta topologi lengkap jaringan dan menghitung jalur terbaik secara mandiri. Contoh: OSPF, IS-IS.

### 1.6 Autonomous System (AS)

Autonomous System adalah kumpulan jaringan IP yang dikelola oleh satu entitas administratif (ISP, perusahaan besar, universitas) dengan kebijakan routing yang unified. Setiap AS diidentifikasi dengan **Autonomous System Number (ASN)** yang unik secara global, dialokasikan oleh Regional Internet Registry (RIR) seperti APNIC untuk kawasan Asia-Pasifik.

---

## Module 2: Use Cases of Static Routes

### 2.1 Pengertian Static Route

Static route adalah rute yang dikonfigurasi secara manual oleh administrator jaringan ke dalam tabel routing router. Tidak seperti rute dinamis yang dipelajari secara otomatis melalui protokol routing, static route bersifat tetap dan tidak berubah kecuali administrator mengubahnya secara manual.

Sintaks umum konfigurasi static route:
```
ip route [network-destination] [subnet-mask] [next-hop-address | exit-interface]
```

### 2.2 Jenis-Jenis Static Route

#### a. Connected Routes (Directly Connected)
Rute yang secara otomatis muncul di tabel routing ketika sebuah interface dikonfigurasi dengan alamat IP dan dalam keadaan aktif (up/up). Ini adalah bentuk routing paling dasar.

#### b. Default Route
Default route (`0.0.0.0/0` untuk IPv4 atau `::/0` untuk IPv6) berfungsi sebagai "gateway of last resort" — jalur yang digunakan ketika tidak ada rute spesifik lain yang cocok dengan alamat tujuan paket. Default route sangat penting pada router edge yang terhubung ke ISP.

#### c. Floating Static Route
Floating static route adalah static route yang dikonfigurasi dengan Administrative Distance (AD) yang lebih tinggi dari rute dinamis yang dipelajari melalui protokol routing. Rute ini berfungsi sebagai jalur backup: dalam kondisi normal, rute dinamis digunakan karena memiliki AD lebih rendah; ketika rute dinamis gagal, floating static route secara otomatis aktif.

#### d. Null/Blackhole Route
Null route mengarahkan trafik ke interface "null" (Null0), yang secara efektif membuang (discard) paket tersebut. Digunakan untuk:
- Memblokir trafik yang tidak diinginkan
- Mencegah routing loop
- Mengimplementasikan Remotely Triggered Black Hole (RTBH) filtering untuk mitigasi DDoS

#### e. Equal-Cost Multi-Path (ECMP) Static Routes
Beberapa static route dengan metric yang sama menuju destinasi yang sama, memungkinkan load balancing trafik melalui beberapa jalur secara bersamaan.

### 2.3 Kapan Menggunakan Static Route

| Skenario | Penjelasan |
|----------|-----------|
| **Stub Network** | Jaringan kecil (kantor cabang) dengan satu jalur keluar. Tidak perlu overhead protokol dinamis. |
| **Default Route ke ISP** | Router edge cukup menggunakan satu default route menuju ISP upstream. |
| **Backup Link** | Floating static route sebagai failover ketika jalur utama (dinamis) gagal. |
| **Keamanan** | Memaksa trafik sensitif melewati jalur tertentu yang telah diaudit. |
| **Perangkat Terbatas** | Router dengan CPU/memori terbatas yang tidak mampu menjalankan protokol dinamis. |
| **Blackhole Filtering** | Null route untuk memblokir trafik serangan (DDoS mitigation). |

### 2.4 Kelebihan dan Kekurangan Static Routing

**Kelebihan:**
- **Tidak ada overhead:** Tidak mengonsumsi CPU, memori, atau bandwidth untuk pertukaran routing update.
- **Keamanan tinggi:** Topologi jaringan tidak diadvertise ke router lain.
- **Deterministik:** Jalur yang dilalui paket sepenuhnya dapat diprediksi.
- **Sederhana:** Konfigurasi mudah untuk jaringan kecil.

**Kekurangan:**
- **Tidak skalabel:** Menambah satu subnet baru memerlukan konfigurasi manual di banyak router.
- **Tidak adaptif:** Tidak dapat otomatis beralih ke jalur alternatif ketika terjadi kegagalan link (kecuali floating static).
- **Rawan human error:** Kesalahan ketik pada IP atau subnet mask dapat menyebabkan black hole atau routing loop.
- **Memerlukan pengetahuan topologi lengkap:** Administrator harus memahami seluruh topologi jaringan.

---

## Module 3: OSPF Basics

### 3.1 Pengenalan OSPF

**Open Shortest Path First (OSPF)** adalah protokol routing link-state yang terstandarisasi oleh IETF dan didefinisikan dalam RFC 2328 (OSPFv2 untuk IPv4) dan RFC 5340 (OSPFv3 untuk IPv6). OSPF merupakan Interior Gateway Protocol (IGP) yang paling banyak digunakan di jaringan enterprise dan service provider.

Karakteristik utama OSPF:
- **Tipe:** Link-state protocol
- **Algoritma:** Dijkstra's Shortest Path First (SPF)
- **Metric:** Cost, dihitung berdasarkan bandwidth interface: `Cost = Reference Bandwidth / Interface Bandwidth` (default reference = 100 Mbps)
- **Administrative Distance:** 110
- **Transport:** Berjalan langsung di atas IP menggunakan Protocol Number 89 (bukan TCP/UDP)
- **Update:** Triggered update — hanya mengirim update ketika terjadi perubahan topologi
- **Multicast Address:** 224.0.0.5 (All OSPF Routers) dan 224.0.0.6 (DR/BDR)

### 3.2 Cara Kerja Link-State Routing

Proses link-state pada OSPF mengikuti langkah-langkah berikut:

1. **Neighbor Discovery:** Router mengirim paket **Hello** melalui interface yang menjalankan OSPF untuk menemukan router tetangga dan membentuk adjacency.
2. **LSA Generation:** Setelah adjacency terbentuk, setiap router menghasilkan **Link-State Advertisement (LSA)** yang berisi informasi tentang interface, status, dan cost link-nya.
3. **LSA Flooding:** LSA di-flood ke seluruh router dalam area yang sama hingga semua router memiliki informasi yang identik.
4. **LSDB Construction:** Semua LSA dikumpulkan dalam **Link-State Database (LSDB)**, membentuk peta topologi lengkap jaringan.
5. **SPF Calculation:** Router menjalankan algoritma Dijkstra pada LSDB untuk menghitung jalur terpendek (least-cost) ke setiap destinasi.
6. **Routing Table Population:** Hasil perhitungan SPF dimasukkan ke tabel routing.

### 3.3 Desain Hierarkis: Area OSPF

Untuk skalabilitas, OSPF menggunakan struktur area hierarkis:

- **Area 0 (Backbone Area):** Area inti yang wajib ada dalam setiap deployment OSPF multi-area. Semua area lain harus terhubung ke Area 0 (baik langsung maupun melalui virtual link).
- **Standard Area:** Area reguler yang terhubung ke Area 0.
- **Stub Area:** Memblokir LSA Type 5 (external routes) untuk mengecilkan tabel routing.
- **Totally Stubby Area:** Memblokir LSA Type 3 dan 5, hanya menerima default route dari ABR.
- **Not-So-Stubby Area (NSSA):** Memperbolehkan redistribusi rute external secara terbatas menggunakan LSA Type 7.

### 3.4 Tipe Router dalam OSPF

- **Internal Router:** Semua interface berada dalam satu area yang sama.
- **Area Border Router (ABR):** Menghubungkan dua atau lebih area OSPF; meringkas informasi routing antar area.
- **Autonomous System Boundary Router (ASBR):** Menghubungkan domain OSPF dengan jaringan eksternal yang menjalankan protokol routing berbeda.
- **Designated Router (DR) / Backup DR (BDR):** Dipilih pada jaringan multi-access (Ethernet) untuk mengurangi jumlah adjacency dan LSA flooding.

### 3.5 Tipe-Tipe LSA

| Tipe | Nama | Sumber | Fungsi |
|------|------|--------|--------|
| Type 1 | Router LSA | Setiap router | Mendeskripsikan interface dan cost dalam satu area |
| Type 2 | Network LSA | Designated Router (DR) | Mendaftar semua router pada segmen multi-access |
| Type 3 | Summary LSA | ABR | Mengadvertise jaringan antar area |
| Type 4 | ASBR Summary LSA | ABR | Mengadvertise reachability ke ASBR |
| Type 5 | AS External LSA | ASBR | Meng-inject rute dari luar domain OSPF |

### 3.6 Algoritma SPF (Dijkstra)

Algoritma Dijkstra memodelkan jaringan sebagai graph berbobot:
- **Node (Vertices)** = Router dan jaringan
- **Edge** = Link penghubung
- **Weight** = OSPF cost

Proses perhitungan:
1. Router menempatkan dirinya sebagai root (cost = 0).
2. Mengevaluasi semua neighbor, menghitung cumulative cost.
3. Memilih node dengan cost terendah dan menambahkannya ke **Shortest Path Tree (SPT)**.
4. Proses diulang secara iteratif hingga semua destinasi terevaluasi.
5. Hasil SPT dikompilasi menjadi tabel routing.

---

## Module 4: IS-IS Basics

### 4.1 Pengenalan IS-IS

**Intermediate System to Intermediate System (IS-IS)** adalah protokol routing link-state yang awalnya dikembangkan oleh ISO (International Organization for Standardization) untuk jaringan OSI. IS-IS banyak digunakan oleh Internet Service Provider (ISP) besar dan operator backbone karena skalabilitas dan stabilitasnya yang sangat baik.

Meskipun berasal dari arsitektur OSI, IS-IS modern (dikenal sebagai **Integrated IS-IS**, RFC 1195) telah diperluas untuk mendukung IPv4 dan IPv6 melalui mekanisme **Type-Length-Value (TLV)**.

### 4.2 Perbedaan Fundamental IS-IS vs OSPF

| Aspek | IS-IS | OSPF |
|-------|-------|------|
| **Asal** | ISO/OSI (CLNS) | IETF (IP-native) |
| **Enkapsulasi** | Berjalan langsung di Layer 2 | Berjalan di atas IP (Protocol 89) |
| **Addressing** | NSAP/NET (OSI) | IP Address |
| **Hierarki** | Level 1 / Level 2 | Area (Area 0 = backbone) |
| **Batas Area** | Pada link antar router | Pada router (ABR) |
| **Extensibility** | Mudah diperluas via TLV | Memerlukan standar baru (RFC) |
| **Penggunaan Dominan** | ISP/backbone besar | Enterprise/medium network |

### 4.3 CLNS dan NSAP Addressing

#### CLNS (Connectionless-mode Network Service)
CLNS adalah layanan jaringan connectionless pada arsitektur OSI, setara dengan IP pada TCP/IP. IS-IS beroperasi secara native di atas CLNS, bahkan ketika membawa informasi routing IPv4/IPv6.

#### NSAP (Network Service Access Point)
Setiap router IS-IS harus memiliki alamat NSAP yang berfungsi sebagai identitas dalam domain IS-IS. Alamat NSAP yang digunakan router disebut **NET (Network Entity Title)**, dengan NSEL (N-Selector) byte terakhir selalu bernilai `00`.

**Struktur NET:**
```
49.0001.0192.1680.0001.00
│     │     │              │
│     │     │              └─ NSEL (00 = router itu sendiri)
│     │     └──────────────── System ID (6 bytes, unik per router)
│     └────────────────────── Area ID
└──────────────────────────── AFI (Authority & Format Indicator)
```

- **AFI 49:** Menunjukkan private/local addressing
- **Area ID:** Mengidentifikasi area routing (contoh: 0001)
- **System ID:** 6 byte, unik per router dalam area (sering diderivasi dari IP loopback)
- **NSEL:** Selalu 00 untuk NET

### 4.4 Hierarki Level IS-IS

IS-IS menggunakan hierarki dua level:

#### Level 1 (L1) — Intra-Area Routing
- Setara dengan non-backbone area di OSPF.
- Router L1 hanya membentuk adjacency dengan router L1 lain **dalam area yang sama**.
- Memelihara LSDB yang hanya berisi informasi area lokal.
- Untuk mencapai destinasi di luar area, L1 router bergantung pada default route dari router L1/L2.

#### Level 2 (L2) — Inter-Area / Backbone Routing
- Setara dengan OSPF backbone (Area 0).
- Router L2 membentuk backbone yang menghubungkan area-area berbeda.
- Memelihara L2 LSDB yang berisi informasi topologi inter-area.

#### Level 1/2 (L1/L2) — Border Router
- Berfungsi sebagai jembatan antara routing L1 dan L2 (mirip ABR di OSPF).
- Memelihara **dua LSDB terpisah** secara bersamaan (L1 dan L2).
- Mengatur **ATT (Attached) bit** pada L1 LSP untuk menginformasikan router L1 bahwa ada jalur keluar area.

### 4.5 Perbedaan Kunci: Batas Area

Pada OSPF, batas area terletak **di dalam router** — satu ABR memiliki interface di beberapa area. Pada IS-IS, batas area terletak **pada link antar router** — setiap router berada hanya dalam satu area, dan link yang menghubungkannya ke router di area berbeda merupakan batas area.

### 4.6 Keunggulan IS-IS

- **Skalabilitas superior:** Arsitektur TLV memungkinkan penambahan fitur baru tanpa mengubah protokol dasar.
- **Stabilitas:** Karena berjalan di Layer 2, IS-IS tidak terpengaruh oleh masalah pada layer IP.
- **Efisiensi:** Lebih efisien dalam jaringan backbone besar dengan ribuan router.
- **Multi-protocol support:** Dapat membawa informasi routing untuk multiple network layer protocol.

---

## Module 5: BGP Basics

### 5.1 Pengenalan BGP

**Border Gateway Protocol (BGP)** adalah satu-satunya Exterior Gateway Protocol (EGP) yang digunakan di internet modern. BGP bertanggung jawab untuk mempertukarkan informasi routing antar Autonomous System (AS) yang berbeda, menjadikannya "protokol yang menjalankan internet."

Karakteristik utama BGP:
- **Tipe:** Path-vector protocol
- **Transport:** TCP port 179
- **Administrative Distance:** 20 (EBGP), 200 (IBGP)
- **Update:** Incremental — setelah pertukaran tabel routing awal, hanya mengirim perubahan
- **Versi:** BGP-4 (RFC 4271) adalah versi yang digunakan saat ini

### 5.2 Autonomous System dan ASN

Setiap AS di internet memiliki **Autonomous System Number (ASN)** yang unik:
- **2-byte ASN:** Rentang 0–65535 (format lama)
- **4-byte ASN:** Rentang 0–4.294.967.295 (format baru, mengantisipasi kehabisan ASN 2-byte)
- **Private ASN:** 64512–65534 (2-byte) dan 4200000000–4294967294 (4-byte), digunakan untuk internal dan harus di-strip sebelum diadvertise ke internet publik

ASN dialokasikan oleh Regional Internet Registry (RIR):
- APNIC (Asia-Pasifik)
- RIPE NCC (Eropa)
- ARIN (Amerika Utara)
- LACNIC (Amerika Latin)
- AFRINIC (Afrika)

### 5.3 EBGP vs IBGP

#### External BGP (EBGP)
- Peering antara router di **AS yang berbeda**
- Secara default, peer harus directly connected
- Administrative Distance: 20
- Setiap kali rute melewati EBGP peer, ASN ditambahkan ke AS_PATH
- Digunakan untuk interkoneksi antar ISP, peering di IXP, koneksi customer-provider

#### Internal BGP (IBGP)
- Peering antara router **dalam AS yang sama**
- Peer tidak perlu directly connected (menggunakan IGP untuk reachability)
- Administrative Distance: 200
- Memerlukan **full-mesh** topology antar semua IBGP speaker (atau menggunakan Route Reflector / Confederation)
- Rute yang dipelajari dari IBGP peer **tidak diadvertise ulang** ke IBGP peer lain (loop prevention)

### 5.4 BGP Path Attributes

Path attributes adalah metadata yang dilampirkan pada setiap prefix (NLRI) yang diadvertise BGP. Atribut-atribut ini digunakan dalam proses seleksi jalur terbaik.

**Kategori Path Attributes:**
1. **Well-known Mandatory:** Wajib dikenali dan ada di setiap update (AS_PATH, NEXT_HOP, ORIGIN)
2. **Well-known Discretionary:** Wajib dikenali tapi opsional dalam update (LOCAL_PREF, ATOMIC_AGGREGATE)
3. **Optional Transitive:** Opsional dikenali; jika tidak dikenali, tetap diteruskan
4. **Optional Non-transitive:** Jika tidak dikenali, diabaikan dan tidak diteruskan (MED)

**Atribut Utama:**

| Atribut | Kategori | Fungsi | Preferensi |
|---------|----------|--------|------------|
| **Weight** | Cisco proprietary, lokal | Memilih jalur keluar pada satu router | Higher = better |
| **LOCAL_PREF** | Well-known Discretionary | Memilih exit path dalam satu AS (IBGP) | Higher = better (default 100) |
| **AS_PATH** | Well-known Mandatory | Daftar AS yang dilalui; loop prevention | Shorter = better |
| **ORIGIN** | Well-known Mandatory | Asal rute (IGP=0, EGP=1, Incomplete=2) | Lower = better |
| **MED** | Optional Non-transitive | Menyarankan entry point ke AS tetangga | Lower = better |
| **NEXT_HOP** | Well-known Mandatory | IP address next-hop untuk mencapai prefix | Must be reachable |

### 5.5 BGP Session States (Finite State Machine)

Proses pembentukan BGP session melewati 6 state:

1. **Idle:** State awal; router belum memulai koneksi TCP.
2. **Connect:** Router mencoba membuat koneksi TCP ke port 179 peer.
3. **Active:** Koneksi TCP gagal; router mencoba ulang secara aktif.
4. **OpenSent:** Koneksi TCP berhasil; router mengirim pesan OPEN.
5. **OpenConfirm:** Pesan OPEN diterima dan parameter disepakati; menunggu KEEPALIVE.
6. **Established:** Session BGP aktif; pertukaran routing update dimulai.

### 5.6 Proses Seleksi Jalur Terbaik BGP

Ketika BGP menerima multiple path menuju prefix yang sama, ia menjalankan **Best Path Selection Algorithm** dengan urutan prioritas:

1. **Highest Weight** (Cisco proprietary)
2. **Highest LOCAL_PREF**
3. **Locally originated route** (route yang di-originate oleh router itu sendiri)
4. **Shortest AS_PATH**
5. **Lowest Origin type** (IGP < EGP < Incomplete)
6. **Lowest MED**
7. **EBGP over IBGP**
8. **Nearest IGP neighbor** (lowest IGP metric to next-hop)
9. **Oldest route** (untuk stabilitas)
10. **Lowest Router ID**

### 5.7 Peran BGP di Internet

BGP memainkan peran krusial dalam:
- **Internet routing:** Menghubungkan lebih dari 70.000 AS di internet global
- **Traffic engineering:** Mengontrol jalur masuk/keluar trafik melalui manipulasi path attributes
- **Multihoming:** Memungkinkan organisasi terhubung ke multiple ISP untuk redundansi
- **Internet Exchange Point (IXP):** Memfasilitasi peering langsung antar ISP
- **Content Delivery:** CDN menggunakan BGP untuk mengoptimalkan distribusi konten

---

## Kesimpulan

Routing merupakan fondasi dari komunikasi data modern. Pemahaman yang komprehensif tentang routing dimulai dari konsep dasar (routing vs forwarding, RIB/FIB, longest prefix match), berlanjut ke penggunaan static route untuk skenario sederhana, kemudian mendalami protokol routing dinamis IGP (OSPF dan IS-IS) untuk routing internal, dan akhirnya memahami BGP sebagai protokol yang menjalankan internet global.

Setiap teknologi memiliki kasus penggunaan spesifik:
- **Static route** ideal untuk stub network dan backup path
- **OSPF** cocok untuk jaringan enterprise menengah hingga besar
- **IS-IS** menjadi pilihan utama ISP dan backbone operator
- **BGP** merupakan satu-satunya pilihan untuk routing antar-AS di internet

Pemahaman mendalam tentang kelima modul ini memberikan fondasi yang kuat bagi siapa pun yang ingin berkarir di bidang jaringan komputer dan internet, sejalan dengan kurikulum yang disampaikan dalam APNIC Academy Routing Fundamentals Course.

---

## Daftar Referensi

1. APNIC Academy. *Routing Fundamentals Course*. https://academy.apnic.net/en/course/routing-fundamentals-course
2. Cisco Systems. *IP Routing: Longest Prefix Match*. Cisco Documentation.
3. IETF. RFC 2328 – *OSPF Version 2*. April 1998.
4. IETF. RFC 5340 – *OSPF for IPv6*. July 2008.
5. IETF. RFC 1195 – *Use of OSI IS-IS for Routing in TCP/IP and Dual Environments*. December 1990.
6. IETF. RFC 4271 – *A Border Gateway Protocol 4 (BGP-4)*. January 2006.
7. Cloudflare. *What is BGP?* Cloudflare Learning Center.
8. APNIC. *BGP Basics*. APNIC Blog.
