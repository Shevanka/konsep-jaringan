# TUGAS KONSEP JARINGAN
## TUGAS KE – 1: Pengantar Konsep Jaringan

| Informasi | Keterangan |
| :--- | :--- |
| **Nama** | Shevanka Bagus Dwiyudi Kurniawan |
| **NRP** | 3125600044 |
| **Dosen Pengajar** | Dr. Ferry Astika Saputra, ST, M.Sc |
| **Program Studi** | D4 Teknik Informatika |
| **Institusi** | Politeknik Elektronika Negeri Surabaya (PENS) |
| **Tahun** | 2026 |

---

## A. Tugas Bab 1

### Level A — Ingatan dan Pemahaman
1. Jelaskan pengertian jaringan komputer dengan menyebutkan empat unsur pokoknya.
2. Apa yang dimaksud dengan perangkat otonom dalam definisi jaringan?
3. Bedakan data, sinyal, dan paket.
4. Jelaskan perbedaan PAN, LAN, MAN, dan WAN tanpa hanya menggunakan ukuran jarak.
5. Apa perbedaan intranet, ekstranet, dan Internet publik?
6. Mengapa Wi-Fi tidak dapat disamakan dengan Internet?
7. Jelaskan perbedaan client, server, dan peer.
8. Apa perbedaan bandwidth, throughput, dan goodput?
9. Sebutkan empat komponen nodal delay.
10. Mengapa Web tidak sama dengan Internet?

### Level B — Penerapan dan Analisis
11. Sebuah paket berukuran 1.000 byte dikirim melalui tautan 10 Mbps. Hitung transmission delay ideal paket tersebut. Jelaskan komponen delay yang belum tercakup.
12. Sebuah kampus memiliki koneksi Internet 2 Gbps, tetapi pengguna di satu lantai hanya memperoleh throughput rendah. Susun sedikitnya lima hipotesis yang tidak langsung menyalahkan koneksi ISP.
13. Bandingkan kebutuhan jaringan untuk transfer berkas cadangan dan panggilan video. Metrik apa yang paling penting bagi masing-masing aplikasi?
14. Sebuah organisasi mempunyai dua koneksi Internet dari dua operator. Keduanya melewati tiang dan jalur ducting yang sama. Evaluasi kualitas redundansinya.
15. Jelaskan mengapa penambahan bandwidth tidak selalu mengurangi waktu akses ke server yang sangat jauh.
16. Sebuah layanan tersedia 99,9% selama satu tahun. Hitung perkiraan maksimum durasi ketidaktersediaannya. Bandingkan dengan target 99,99%.
17. Analisis kelebihan dan kelemahan client–server serta P2P untuk distribusi berkas berukuran besar kepada ribuan pengguna.
18. Berikan contoh ketika topologi fisik dan topologi logis pada jaringan kampus berbeda.

### Level C — Evaluasi dan Sintesis
19. Rancang klasifikasi kebutuhan jaringan kampus untuk mahasiswa, staf administrasi, tamu, kamera pengawas, dan laboratorium riset. Jelaskan alasan segmentasi dan aturan komunikasi utamanya.
20. Evaluasi pernyataan: “Jaringan internal tidak memerlukan enkripsi karena sudah dilindungi firewall.” Gunakan prinsip kerahasiaan, integritas, dan ketersediaan.
21. Diskusikan mengapa Internet dapat berkembang tanpa otoritas teknis pusat tunggal. Jelaskan manfaat serta risikonya.
22. Bandingkan circuit switching dan packet switching untuk layanan suara. Jelaskan mengapa suara modern tetap dapat berjalan pada jaringan paket.
23. Ambil satu keluhan nyata atau hipotetis berupa “Internet lambat”. Susun prosedur pengumpulan bukti, pengujian hipotesis, dan kriteria keberhasilan perbaikannya.
24. Kunjungi statistik IPv6 Google atau sumber pengukuran APNIC. Catat tanggal, definisi metrik, populasi yang diukur, dan nilai untuk Indonesia. Jelaskan mengapa angka dari dua sumber dapat berbeda.
25. Buat argumen mengenai penggunaan satelit orbit rendah sebagai koneksi utama atau cadangan bagi kampus di wilayah terpencil. Nilai kinerja, biaya, ketergantungan cuaca, pengelolaan, dan keamanan.
26. Jelaskan bagaimana otomatisasi jaringan dapat meningkatkan konsistensi sekaligus memperbesar dampak kesalahan. Usulkan kontrol teknis dan proses untuk mengurangi risiko tersebut.

---

## B. Jawaban Bab 1

### 1. Pengertian Jaringan Komputer dan Empat Unsur Pokoknya
Jaringan komputer adalah sekumpulan perangkat otonom yang saling terhubung melalui satu atau lebih media komunikasi untuk bertukar data dan berbagi sumber daya berdasarkan aturan komunikasi yang disepakati.

**Empat unsur pokoknya:**
- **Perangkat akhir (*end system/host*):** Sumber atau tujuan akhir data, seperti laptop, server, dan sensor.
- **Media komunikasi:** Saluran fisik atau nirkabel yang membawa sinyal, seperti kabel tembaga, serat optik, dan gelombang radio.
- **Perangkat perantara:** Komponen pengarah, penerus, dan pengaman aliran data, seperti switch, router, dan firewall.
- **Protokol:** Aturan formal mengenai format, urutan sintaks, semantik, serta perlakuan kesalahan dalam komunikasi.

---

### 2. Pengertian Perangkat Otonom dalam Definisi Jaringan
Perangkat otonom berarti setiap entitas yang terhubung tetap memiliki kendali komputasi, sistem operasi, status memori, dan fungsi pemrosesannya sendiri. Perangkat tidak kehilangan identitas independennya saat bergabung ke jaringan, berbeda dengan multiprosesor paralel ketat dalam satu mesin tunggal.

---

### 3. Perbedaan Data, Sinyal, dan Paket
- **Data:** Representasi digital dari informasi, seperti teks, audio, dan gambar, dalam deretan bit abstrak.
- **Sinyal:** Bentuk representasi fisik berupa gelombang elektromagnetik atau energi, seperti tegangan listrik, pulsa optik, dan modulasi frekuensi radio, yang merambat melalui media transmisi.
- **Paket:** Potongan data terstruktur yang dilengkapi metadata kendali, seperti header berisi alamat sumber/tujuan, nomor urut, dan checksum, untuk diangkut melalui jaringan.

---

### 4. Perbedaan PAN, LAN, MAN, dan WAN
- **PAN (*Personal Area Network*):** Berfokus pada ruang personal individu dengan teknologi jarak pendek dan berdaya rendah, seperti Bluetooth dan NFC.
- **LAN (*Local Area Network*):** Berada dalam satu domain kendali administrasi, seperti satu gedung, kampus, atau kantor, dengan latency yang relatif rendah.
- **MAN (*Metropolitan Area Network*):** Menghubungkan beberapa titik dalam kawasan perkotaan, umumnya menggunakan infrastruktur seperti Metro Ethernet atau jaringan fiber perkotaan.
- **WAN (*Wide Area Network*):** Menghubungkan jaringan dalam wilayah yang luas, seperti antarkota atau antarnegara, dan biasanya bergantung pada operator telekomunikasi seperti leased line, MPLS, satelit, atau Internet transit.

---

### 5. Perbedaan Intranet, Ekstranet, dan Internet Publik
- **Intranet:** Layanan berbasis teknologi IP/Web internal yang aksesnya terbatas untuk anggota internal suatu organisasi.
- **Ekstranet:** Ekstensi sebagian layanan intranet yang diberikan secara khusus dan terbatas kepada pihak luar yang telah terverifikasi, seperti vendor atau pemasok.
- **Internet Publik:** Interkoneksi global antarsistem jaringan mandiri yang dapat diakses oleh masyarakat umum di seluruh dunia.

---

### 6. Wi-Fi Tidak Dapat Disamakan dengan Internet
Wi-Fi (IEEE 802.11) hanyalah teknologi komunikasi nirkabel untuk jaringan lokal (LAN). Sebuah laptop dapat terhubung ke Wi-Fi dan berkomunikasi dengan printer atau perangkat lain secara lokal meskipun jaringan tersebut tidak memiliki akses ke Internet.

---

### 7. Perbedaan Client, Server, dan Peer
- **Client:** Node yang bertugas memulai koneksi dan mengirimkan permintaan layanan.
- **Server:** Node yang menyediakan dan merespons layanan kepada client, biasanya secara terpusat.
- **Peer:** Node dengan kedudukan setara yang dapat bertindak sebagai peminta sekaligus penyedia layanan kepada node lain.

---

### 8. Perbedaan Bandwidth, Throughput, dan Goodput
- **Bandwidth:** Kapasitas maksimum teoretis dari sebuah tautan jaringan, misalnya 100 Mbps.
- **Throughput:** Laju transmisi data aktual yang berhasil melewati jaringan dalam waktu tertentu, termasuk overhead protokol.
- **Goodput:** Laju transfer data aplikasi yang benar-benar berguna dan diterima, tanpa menghitung header protokol dan data yang ditransmisikan ulang.

---

### 9. Empat Komponen Nodal Delay
**Formula Nodal Delay:**
$$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

**Keterangan:**
- **Processing delay ($d_{proc}$):** Waktu yang diperlukan untuk memeriksa header paket, mendeteksi kesalahan, dan menentukan antarmuka keluaran.
- **Queuing delay ($d_{queue}$):** Waktu tunggu paket di dalam antrean buffer router sebelum diproses atau ditransmisikan.
- **Transmission delay ($d_{trans}$):** Waktu yang dibutuhkan untuk memasukkan seluruh bit paket ke media fisik. Rumusnya:
  $$d_{trans} = \frac{L}{R}$$
- **Propagation delay ($d_{prop}$):** Waktu yang dibutuhkan sinyal untuk merambat dari pengirim ke penerima melalui media. Rumusnya:
  $$d_{prop} = \frac{d}{s}$$

---

### 10. Mengapa Web Tidak Sama dengan Internet
Internet adalah infrastruktur dan jaringan global yang menghubungkan berbagai jaringan menggunakan protokol komunikasi seperti TCP/IP. Sedangkan Web (*World Wide Web*) adalah salah satu layanan aplikasi yang berjalan di atas Internet menggunakan HTTP/HTTPS, HTML, dan URI. Layanan seperti email, DNS, SSH, dan VoIP dapat bekerja tanpa menggunakan Web.

---

### 11. Perhitungan Transmission Delay dan Komponen yang Belum Tercakup
**Diketahui:**
- Ukuran paket ($L$) = $1.000\text{ byte} = 8.000\text{ bit}$
- Bandwidth tautan ($R$) = $10\text{ Mbps} = 10.000.000\text{ bps}$

**Perhitungan:**
$$d_{trans} = \frac{L}{R} = \frac{8.000\text{ bit}}{10.000.000\text{ bps}} = 0,0008\text{ detik} = 0,8\text{ ms}$$

Komponen yang belum tercakup adalah **processing delay**, **queuing delay**, dan **propagation delay**.

---

### 12. Lima Hipotesis Throughput Rendah di Satu Lantai
1. Terjadi kongesti atau interferensi kanal Wi-Fi karena banyak Access Point menggunakan channel yang bertumpuk, terutama pada pita 2,4 GHz.
2. Kapasitas switch akses lokal atau port uplink lantai tersebut terbatas.
3. Kepadatan pengguna pada satu Access Point terlalu tinggi sehingga terjadi persaingan penggunaan airtime.
4. Terjadi *broadcast storm* atau kesalahan konfigurasi VLAN/looping pada switch lantai tersebut.
5. Terdapat pembatasan kuota, QoS, atau *traffic shaping* pada firewall lokal yang terlalu ketat.

---

### 13. Perbandingan Kebutuhan Jaringan: Backup Berkas vs Panggilan Video
- **Transfer Berkas Cadangan:** Membutuhkan goodput/throughput tinggi dan toleransi kehilangan paket yang sangat rendah, tetapi relatif tidak sensitif terhadap delay dan jitter karena dapat dilakukan secara asinkron.
- **Panggilan Video:** Sangat sensitif terhadap latency rendah dan jitter minimal agar komunikasi berlangsung lancar. Kehilangan paket dalam jumlah kecil masih dapat ditoleransi oleh sistem kompresi video.

---

### 14. Evaluasi Kualitas Redundansi Dua Operator Jalur Fisik Sama
Kualitas redundansinya **sangat rendah** atau dapat disebut sebagai **redundansi semu**. Meskipun menggunakan dua ISP yang berbeda secara bisnis, keduanya tetap memiliki *Single Point of Failure* (SPoF) pada jalur fisik yang sama. Jika terjadi kerusakan pada tiang, kabel, ducting, atau jalur fisik tersebut, kedua koneksi dapat terputus secara bersamaan.

---

### 15. Penambahan Bandwidth Tidak Selalu Mengurangi Waktu Akses ke Server yang Jauh
Bandwidth hanya meningkatkan kapasitas data per detik dan dapat mengurangi *transmission delay*. Sementara itu, akses ke server yang sangat jauh banyak dipengaruhi oleh *propagation delay* (kecepatan rambat cahaya di media transmisi) dan jumlah hop perantara. Oleh karena itu, menambah bandwidth tidak secara langsung mempercepat waktu tempuh sinyal melalui jarak yang jauh.

---

### 16. Perhitungan Ketidaksediaan Layanan (Downtime 99,9% vs 99,99%)
$$1\text{ tahun} = 365 \times 24 \times 60 = 525.600\text{ menit}$$

**Ketersediaan 99,9%:**
- $\text{Downtime} = 100\% - 99,9\% = 0,1\%$
- $525.600 \times 0,001 = 525,6\text{ menit}$
- $525,6\text{ menit} \approx \mathbf{8\text{ jam } 45\text{ menit } 36\text{ detik per tahun}}$.

**Ketersediaan 99,99%:**
- $\text{Downtime} = 100\% - 99,99\% = 0,01\%$
- $525.600 \times 0,0001 = 52,56\text{ menit}$
- $52,56\text{ menit} \approx \mathbf{52\text{ menit } 34\text{ detik per tahun}}$.

> **Kesimpulan:** Target ketersediaan 99,99% memberikan toleransi batas downtime sekitar sepersepuluh dari target 99,9%.

---

### 17. Analisis Kelebihan dan Kelemahan Client–Server vs P2P untuk Distribusi Berkas Besar
**Client–Server:**
- **Kelebihan:** Mudah dikontrol, validitas berkas lebih mudah dijaga, dan manajemen akses dapat dilakukan secara terpusat.
- **Kelemahan:** Server utama menanggung beban bandwidth yang besar, dapat menjadi bottleneck, dan berpotensi menjadi *Single Point of Failure*.

**Peer-to-Peer (P2P):**
- **Kelebihan:** Lebih scalable karena setiap peer yang mengunduh dapat ikut menyediakan data kepada peer lain sehingga mengurangi beban server utama.
- **Kelemahan:** Lebih sulit mengontrol integritas berkas dan ketersediaan peer. Selain itu, komunikasi dapat terhambat oleh firewall atau NAT.

---

### 18. Perbedaan Topologi Fisik dan Topologi Logis pada Jaringan Kampus
Di laboratorium komputer kampus, seluruh PC terhubung menggunakan kabel UTP masing-masing ke sebuah switch sentral sehingga secara fisik membentuk **topologi Star**. Namun, switch tersebut dapat dikonfigurasi menjadi beberapa VLAN, misalnya VLAN Mahasiswa dan VLAN Dosen, sehingga secara logis jaringan tersebut terbagi menjadi beberapa broadcast domain yang berbeda.

---

### 19. Segmentasi Jaringan Kampus dan Aturan Komunikasi
**Segmentasi VLAN:**
- **VLAN Mahasiswa:** Digunakan untuk akses Internet dan LMS, dengan pembatasan bandwidth per perangkat serta *client isolation*.
- **VLAN Staf/Administrasi:** Digunakan untuk mengakses sistem informasi akademik dan server finansial dengan autentikasi ketat seperti 802.1X.
- **VLAN Tamu (Guest):** Menggunakan *captive portal* dan hanya menyediakan akses Internet publik dengan pembatasan bandwidth.
- **VLAN Kamera Pengawas (CCTV):** Digunakan khusus untuk komunikasi kamera dan NVR serta diisolasi dari Internet.
- **VLAN Lab Riset:** Memiliki bandwidth lebih besar dan fleksibilitas konfigurasi, tetapi tetap dipisahkan dari jaringan operasional kampus.

**Aturan Komunikasi:**
ACL (*Access Control List*) diterapkan pada router atau firewall inti untuk mengontrol lalu lintas antar-VLAN. Secara default, akses dari jaringan Mahasiswa dan Tamu menuju jaringan Finansial, Administrasi, dan CCTV harus ditolak.

---

### 20. Evaluasi Pernyataan: “Jaringan internal tidak memerlukan enkripsi karena sudah dilindungi firewall”
Pernyataan tersebut **keliru dan berbahaya**. Firewall hanya melindungi dan mengontrol lalu lintas pada batas perimeter jaringan, sehingga tidak menjamin keamanan seluruh komunikasi internal.

Ditinjau berdasarkan prinsip **CIA Triad**:
- **Kerahasiaan (*Confidentiality*):** Tanpa enkripsi, data internal dapat dibaca oleh penyerang di dalam jaringan, perangkat yang terinfeksi malware, atau pihak yang melakukan penyadapan (*sniffing*).
- **Integritas (*Integrity*):** Tanpa mekanisme enkripsi dan autentikasi seperti TLS, data dapat dimodifikasi di tengah jalan oleh pihak yang melakukan *Man-in-the-Middle* (MitM).
- **Ketersediaan (*Availability*):** Komunikasi tanpa perlindungan yang memadai dapat lebih mudah dimanipulasi atau diinjeksi paket berbahaya untuk mengganggu ketersediaan layanan.

---

### 21. Perkembangan Internet Tanpa Otoritas Tunggal: Manfaat dan Risiko
**Alasan:**
Internet dirancang sebagai arsitektur terbuka yang menghubungkan berbagai *Autonomous System* (AS) melalui protokol dan standar terbuka seperti BGP dan standar yang ditetapkan oleh IETF.

**Manfaat:**
- Mendorong inovasi terbuka dan perkembangan teknologi yang sangat pesat.
- Tidak dikendalikan sepenuhnya secara monopoli oleh satu perusahaan atau negara tertentu.
- Desentralisasi membuat Internet lebih tangguh (*fault-tolerant*) terhadap kegagalan satu titik pusat.

**Risiko:**
- Rentan terjadi masalah keamanan routing global, seperti *BGP hijacking* dan *route leak*.
- Koordinasi dan adopsi standar baru (contohnya IPv6 dan DNSSEC) dapat berlangsung lambat.
- Ketergantungan yang tinggi pada model kepercayaan (*trust*) dan kerja sama antaroperator jaringan global.

---

### 22. Perbandingan Circuit Switching vs Packet Switching untuk Layanan Suara
- **Circuit Switching:**
  Mengalokasikan kanal komunikasi fisik/logis khusus (*dedicated*) untuk suatu koneksi sehingga latency dan jitter relatif stabil. Namun, metode ini kurang efisien karena kapasitas kanal tetap dialokasikan meskipun pihak-pihak sedang diam (*silent periods*).
- **Packet Switching:**
  Membagi suara menjadi potongan paket-paket kecil yang dikirim melalui jaringan bersama dengan mekanisme *statistical multiplexing*, sehingga utilisasi bandwidth jauh lebih efisien.
- **Mengapa Suara Modern Tetap Berjalan pada Jaringan Paket:**
  Teknologi jaringan modern memungkinkan penerapan *Quality of Service* (QoS), pemberian prioritas pada paket suara, penggunaan *jitter buffer*, serta ketersediaan bandwidth transmisi yang sangat besar. Hal tersebut memungkinkan Voice over IP (VoIP) menghasilkan komunikasi suara dengan delay dan jitter yang cukup rendah untuk persepsi telinga manusia.

---

### 23. Prosedur Penanganan Keluhan “Internet Lambat”
#### A. Pengumpulan Bukti
1. Catat waktu kejadian, aplikasi spesifik yang bermasalah, jenis perangkat yang digunakan, dan lokasi pengguna.
2. Lakukan pengujian `ping` dan `traceroute` ke default gateway lokal serta ke beberapa server tujuan di Internet.
3. Catat metrik throughput, latency RTT, jitter, dan persentase packet loss untuk memetakan kondisi degradasi jaringan.

#### B. Pengujian Hipotesis
- **Hipotesis 1:** Masalah terdapat pada Wi-Fi lokal.  
  *Uji:* Hubungkan perangkat menggunakan kabel LAN (Ethernet) langsung. Jika performa kembali normal, periksa interferensi sinyal, kepadatan kanal, dan posisi Access Point.
- **Hipotesis 2:** Masalah terdapat pada resolusi nama (DNS).  
  *Uji:* Bandingkan kecepatan akses menggunakan alamat IP langsung vs nama domain (FQDN).
- **Hipotesis 3:** Uplink gateway mengalami utilisasi penuh (*saturation*).  
  *Uji:* Periksa grafik utilitas bandwidth pada router/firewall gateway dan identifikasi host yang mengonsumsi bandwidth berlebih.

#### C. Kriteria Keberhasilan
- Latency jaringan lokal berada di bawah 5 ms secara konsisten.
- Latency WAN kembali mendekati baseline normal.
- Packet loss berada pada nilai mendekati 0%.
- Seluruh aplikasi bisnis/akademik penting dapat diakses kembali dengan responsif tanpa gangguan.

---

### 24. Analisis Statistik IPv6 (Google vs APNIC untuk Indonesia)
**Catatan Karakteristik Pengukuran:**
- **Google IPv6:** Mengukur persentase akses pengguna ke layanan-layanan milik ekosistem Google (seperti Google Search, YouTube) yang menggunakan konektivitas IPv6 asli.
- **APNIC Labs:** Mengukur kapabilitas IPv6 pengguna global melalui skrip eksperimen berbasis web yang diinjeksi via penayangan iklan (*online ads*).

**Alasan Perbedaan Angka Antara Kedua Sumber:**
- **Perbedaan Populasi Target:** Google hanya mengukur pengguna yang secara aktif mengakses layanan Google, sedangkan APNIC menyasar sampel acak peselancar web umum yang memuat materi iklan.
- **Metodologi Pengukuran:** Google memantau sesi koneksi TCP/IP nyata ke server produksinya, sedangkan APNIC menjalankan pengujian kapabilitas fetch DNS dan fallback HTTP/IPv6 secara sintetis.
- **Kondisi Distribusi Provider:** Adopsi IPv6 di Indonesia sangat heterogen; beberapa operator seluler telah mengaktifkan IPv6 secara penuh (IPv6-only/NAT64), sedangkan mayoritas penyedia ISP fixed-broadband perumahan masih mengandalkan IPv4 + CGNAT.

---

### 25. Analisis Satelit Orbit Rendah (LEO) untuk Kampus di Wilayah Terpencil
- **Kinerja:** Satelit LEO (*Low Earth Orbit*, seperti Starlink) beroperasi pada ketinggian 500–1.200 km sehingga memiliki latency jauh lebih rendah (sekitar 25–50 ms) dibandingkan satelit geostasioner (GEO, latency >500 ms), dengan throughput unduh hingga ratusan Mbps yang memadai untuk operasional kampus.
- **Biaya:** Biaya pengadaan perangkat terminal dan langganan bulanan jauh lebih terjangkau dibandingkan biaya investasi pergelaran kabel serat optik (*fiber optic*) ke wilayah pedalaman yang sangat mahal.
- **Ketergantungan Cuaca:** Rentan mengalami degradasi sinyal (*rain fade*) saat terjadi hujan lebat atau cuaca ekstrem.
- **Pengelolaan dan Keamanan:** Terminal mudah dipasang (*plug-and-play*), namun pihak IT kampus memiliki kontrol yang terbatas terhadap infrastruktur perutean dan penanganan CGNAT milik operator satelit.
- **Rekomendasi:** LEO sangat cocok diimplementasikan sebagai **koneksi utama** bagi kampus di daerah terpencil yang belum terjangkau serat optik, atau sebagai **tautan cadangan (*failover*)** berkecepatan tinggi jika jalur terestrial sudah tersedia.

---

### 26. Dampak Otomatisasi Jaringan dan Mekanisme Mitigasi Risiko
**Dampak:**
Penggunaan perangkat otomasi seperti Ansible, Python (Netmiko/Nornir), dan *Software-Defined Networking* (SDN) meningkatkan efisiensi, akurasi, dan konsistensi konfigurasi perangkat jaringan dalam skala besar. Namun, jika terjadi kekeliruan sintaks atau logika dalam playbook/skrip, kesalahan tersebut dapat terdistribusi ke puluhan hingga ratusan perangkat sekaligus dalam hitungan detik (*blast radius* sangat besar).

**Kontrol Teknis:**
- Melakukan *dry-run* (mode simulasi/`--check`) dan pengujian validasi sintaks secara otomatis di lingkungan lab/staging virtual sebelum disebarkan ke perangkat produksi.
- Mengaktifkan fitur *automatic rollback* atau *commit-confirmed* (perangkat akan kembali ke konfigurasi sebelumnya jika koneksi manajemen putus dalam durasi tertentu).

**Kontrol Proses:**
- Menerapkan paradigma **GitOps** dengan *peer review* dan persetujuan formal (*Pull Request approval*) sebelum perubahan konfigurasi digabungkan ke branch produksi.
- Melakukan metode peluncuran bertahap (*canary deployment*), yaitu mengaplikasikan otomasi pada sebagian kecil perangkat terlebih dahulu, melakukan observasi kestabilan, baru kemudian memperluasnya ke seluruh infrastruktur.

---

## C. Tugas 4 Soal

1. Mencatat tentang kabel UTP cat 1 sampai cat 9
2. Standard Wi-Fi yang ada, cari tahu berapa abgn-nya
3. Mencari detail sejarah dan timeline Internet
4. Menginterpretasikan detail Internet yang muncul pada Fast.com

---

## D. Jawaban 4 Soal

### 1. Kategori Kabel UTP (Cat 1 sampai Cat 9)
Kabel *twisted-pair* dirancang berdasarkan batas frekuensi dan laju data yang dapat dilewatkan. Berikut adalah rincian spesifikasi dan karakteristik tiap generasinya:

| Kategori | Frekuensi Maksimum | Bandwidth Maksimum | Panjang Maksimum Kanal | Penggunaan Umum / Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **Cat 1** | < 1 MHz | Hingga 1 Mbps | - | Transmisi suara analog (telepon POTS klasik) dan ISDN; tidak layak untuk data modern. |
| **Cat 2** | 4 MHz | 4 Mbps | 100 m | Jaringan suara lama dan sistem IBM Token Ring awal (4 Mbps). |
| **Cat 3** | 16 MHz | 10 Mbps | 100 m | Standar 10BASE-T Ethernet kabel; masih sering ditemui pada instalasi telepon internal lama. |
| **Cat 4** | 20 MHz | 16 Mbps | 100 m | Digunakan terutama pada jaringan 16 Mbps Token Ring; sudah ditinggalkan. |
| **Cat 5** | 100 MHz | 100 Mbps | 100 m | Standar 100BASE-TX (Fast Ethernet); rentan terhadap interferensi crosstalk pada implementasi data tinggi. |
| **Cat 5e** *(Enhanced)* | 100 MHz | 1 Gbps (1000 Mbps) | 100 m | Memperketat spesifikasi crosstalk (NEXT/FEXT); standar minimum untuk 1000BASE-T (Gigabit Ethernet). |
| **Cat 6** | 250 MHz | 1 Gbps / 10 Gbps | 100 m (1 Gbps) / ~37–55 m (10 Gbps) | Memakai separator silang (*spline*) internal; mampu 10GBASE-T pada jarak pendek. |
| **Cat 6a** *(Augmented)* | 500 MHz | 10 Gbps | 100 m | Mengatasi alien crosstalk secara penuh; mendukung 10GBASE-T hingga jarak penuh 100 m. |
| **Cat 7** | 600 MHz | 10 Gbps | 100 m | Standar ISO/IEC 11801 (bukan TIA/EIA); kabel terpelindung penuh (S/FTP), konektor GG45/TERA atau RJ-45 kompatibel. |
| **Cat 7a** | 1.000 MHz (1 GHz) | 10 Gbps (hingga 40G jarak pendek) | 100 m (10G) / ~15–50 m (40G) | Versi peningkatan Cat 7 untuk aplikasi industri dan multimedia berfrekuensi tinggi. |
| **Cat 8** *(Cat 8.1 / 8.2)* | 2.000 MHz (2 GHz) | 25 Gbps hingga 40 Gbps | 30–36 m (Kanal) | Standar resmi tertinggi saat ini (ANSI/TIA-568-C.2-1 & ISO/IEC); ditujukan untuk koneksi antar-rak *switch-to-server* di data center. |
| **"Cat 9"** | *Non-standar* | *Tidak resmi* | *Tidak resmi* | Belum ada standar resmi dari badan standarisasi kabel (seperti TIA/EIA atau ISO/IEC) untuk "Cat 9". Penamaan Cat 9 di pasar umumnya merupakan strategi pemasaran (*marketing gimmick*) vendor tidak resmi atau riset internal yang belum disahkan menjadi standar IEEE/TIA. |

---

### 2. Standar Wi-Fi dan Keluarga IEEE 802.11 (a/b/g/n/ac/ax/be)
Standar Wi-Fi didefinisikan oleh IEEE 802.11 yang mengatur fungsi *Physical Layer* dan *Media Access Control* (MAC):

| Standar Wi-Fi | Generasi | Frekuensi | Kecepatan Puncak Teoretis | Modulasi / Teknologi Kunci | Karakteristik & Penggunaan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **802.11b** | Wi-Fi 1 | 2.4 GHz | 11 Mbps | DSSS, CCK | Standar nirkabel awal yang populer secara luas; jangkauan luas tetapi kapasitas rendah. |
| **802.11a** | Wi-Fi 2 | 5 GHz | 54 Mbps | OFDM | Minim interferensi karena memakai pita 5 GHz, namun redaman dinding lebih tinggi. |
| **802.11g** | Wi-Fi 3 | 2.4 GHz | 54 Mbps | OFDM, DSSS | Kompatibel mundur dengan 802.11b; membawa kecepatan 54 Mbps ke pita 2.4 GHz. |
| **802.11n** | Wi-Fi 4 | 2.4 GHz & 5 GHz | Hingga 600 Mbps | MIMO, Channel Bonding (40 MHz) | Memperkenalkan beberapa aliran spasial (*spatial streams*) untuk menaikkan throughput. |
| **802.11ac** | Wi-Fi 5 | Khusus 5 GHz | Hingga 6.9 Gbps | 256-QAM, MU-MIMO (downlink), kanal 80/160 MHz | Standar dominan untuk multimedia berkecepatan tinggi pada jaringan modern. |
| **802.11ax** | Wi-Fi 6 / 6E | 2.4 GHz, 5 GHz, 6 GHz (6E) | Hingga 9.6 Gbps | 1024-QAM, OFDMA, TWT | Fokus pada efisiensi spektrum, kepadatan perangkat tinggi, dan hemat daya. |
| **802.11be** | Wi-Fi 7 | 2.4 GHz, 5 GHz, 6 GHz | Hingga 46 Gbps | 4096-QAM, MLO (*Multi-Link Operation*), kanal 320 MHz | Latensi sangat rendah dan throughput sangat tinggi untuk *real-time/cloud networking*. |

---

### 3. Detail Sejarah dan Garis Waktu (Timeline) Internet
Internet berkembang dari proyek riset komunikasi paket militer/akademik menjadi interkoneksi global yang sepenuhnya terdistribusi:

| Periode | Peristiwa Penting | Lembaga Kunci | Signifikansi Teknis |
| :--- | :--- | :--- | :--- |
| **1960-an** | Gagasan & Riset Packet Switching | Paul Baran, Donald Davies, Leonard Kleinrock | Menemukan cara pemecahan data menjadi paket independen sebagai alternatif *circuit switching* telepon. |
| **1969** | Peluncuran Jaringan ARPANET | DARPA (Departemen Pertahanan AS), 4 Node Awal (UCLA, SRI, UCSB, Utah) | Interkoneksi komputer jarak jauh pertama berbasis paket data. |
| **1970-an** | Desain Arsitektur Internetworking | Vinton Cerf, Robert Kahn | Merancang konsep protokol TCP yang kemudian dipisahkan menjadi TCP dan IP demi modularitas arsitektur. |
| **1 Januari 1983** | Migrasi ke TCP/IP (*Flag Day*) | Komunitas ARPANET / IETF | Standarisasi keluarga protokol TCP/IP menggantikan NCP; disepakati sebagai kelahiran resmi Internet modern. |
| **1983–1984** | Pengenalan Domain Name System (DNS) | Paul Mockapetris (RFC 882/883) | Menggantikan pemetaan tabel file `HOSTS.TXT` manual dengan sistem basis data nama terdistribusi hierarkis. |
| **1989–1991** | Kelahiran World Wide Web (WWW) | Tim Berners-Lee (CERN) | Memperkenalkan format dokumen HTML, protokol transfer HTTP, dan URI; Web menjadi antarmuka aplikasi di atas Internet. |
| **1990-an** | Komersialisasi & Peramban Grafis | Netscape, NCSA Mosaic, ISP Komersial | ARPANET resmi dinonaktifkan (1990); jaringan dibuka untuk kepentingan komersial dan publik, memicu era *dot-com bubble*. |
| **2000-an** | Era Broadband dan Jaringan Nirkabel | Operator Telekomunikasi, IEEE 802.11 | Akses *dial-up* tergantikan oleh koneksi pita lebar berkecepatan tinggi seperti ADSL, serat optik (FTTH), dan Wi-Fi massal. |
| **2010-an** | Komputasi Awan, Seluler, dan IoT | Cloud Providers (AWS/GCP/Azure), 4G/LTE, APNIC/IETF | Lalu lintas bergerak masif ke infrastruktur awan dan perangkat *mobile/smartphone*; habisnya alokasi IPv4 memicu percepatan adopsi IPv6. |
| **2020-an** | Era Modern & Otomasi Terdistribusi | IETF, Operator Satelit LEO, Industri Jaringan | Standardisasi protokol QUIC/HTTP/3, rute BGP terotomasi, konstelasi satelit orbit rendah, dan integrasi kecerdasan buatan (AI) pada operasional jaringan. |

---

### 4. Interpretasi Metrik pada Fast.com
Fast.com (layanan uji performa kecepatan dari Netflix) menampilkan metrik kinerja jaringan nyata yang mengukur lapisan transportasi (*transport layer*) dan lapisan aplikasi:

| Parameter Metrik | Satuan | Definisi Operasional | Analisis / Arti Kondisi Jaringan |
| :--- | :--- | :--- | :--- |
| **Download Speed** | Mbps | Laju pemindahan muatan data dari server uji CDN menuju perangkat pengguna. | Menunjukkan goodput/throughput aktual untuk konsumsi streaming video, pengunduhan berkas, dan penjelajahan web harian. |
| **Upload Speed** | Mbps | Laju pemindahan data yang dikirim dari perangkat pengguna menuju server penampung. | Krusial untuk panggilan video interaktif dua arah, pencadangan file ke cloud, dan pengiriman berkas besar; umumnya diset lebih rendah pada paket rumahan asimetris (ADSL/kabel). |
| **Latency — Unloaded** | ms | Waktu bolak-balik (*Round-Trip Time* / RTT) dasar ketika jaringan sedang dalam kondisi tenang (tidak memproses transfer data berat). | Menggambarkan batas latensi ideal jalur fisik murni (penjumlahan dari delay propagasi media transmisi dan pemrosesan router lokal menuju server). |
| **Latency — Loaded** | ms | Waktu bolak-balik (RTT) saat jaringan sedang berada dalam beban puncak aktivitas unduh atau unggah. | Mengukur tingkat ketahanan terhadap fenomena **bufferbloat**. Jika angka ini melonjak drastis dibandingkan *unloaded*, berarti router/modem mengalami penumpukan antrean (*queuing delay*) yang parah di buffer-nya. |
| **Client Info (IP & ISP)** | Teks / Alamat IP | Identitas alamat jaringan publik dan nama penyedia layanan Internet (ISP) yang terdeteksi. | Memverifikasi apakah perangkat terkoneksi secara langsung melalui alamat rute IPv4 publik atau IPv6 asli, atau berada di balik translasi Carrier-Grade NAT (CGNAT) operator. |
| **Server Location** | Kota / Negara | Lokasi geografis titik node server edge/CDN terdekat yang melayani sesi pengujian tersebut. | Membantu memastikan apakah routing ISP mengarahkan lalu lintas melalui simpul pertukaran internet lokal (IXP terdekat) atau justru mengambil rute transit internasional yang memutar (*tromboning*). |
