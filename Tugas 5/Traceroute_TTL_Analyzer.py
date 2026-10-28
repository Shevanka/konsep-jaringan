#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traceroute and TTL Analyzer & Simulator
Mata Kuliah: Konsep Jaringan (TI043102) - PENS 2026
Penulis: Shevanka Bagus Dwiyudi Kurniawan (NRP: 3125600044)

Modul ini menyediakan:
1. Simulasi matematis dan biner dekrementasi TTL serta pembaruan Header Checksum IPv4
   berdasarkan RFC 791, RFC 1071, dan RFC 1624 (Incremental Checksum Update).
2. Parsing data telemetri riil traceroute ke target publik (1.1.1.1 dan 8.8.8.8).
3. Analisis anomali jaringan (timeout asterisk, spike latency, slow path vs fast path).
4. Visualisasi grafis profil latensi hop-by-hop dan diagram arsitektur router.
"""

import os
import struct
import shutil
import matplotlib.pyplot as plt
import numpy as np

# Set font and visual styling
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8


# ==============================================================================
# 1. SIMULASI DEKREMENTASI TTL & KALKULASI CHECKSUM RFC 791 / RFC 1624
# ==============================================================================

class IPv4HeaderSimulator:
    """
    Mensimulasikan pembuatan header IPv4, kalkulasi checksum 16-bit (RFC 1071),
    dekrementasi TTL per hop router, dan algoritma incremental update (RFC 1624).
    """

    def __init__(self, src_ip="192.168.110.100", dst_ip="8.8.8.8", protocol=1, initial_ttl=64):
        self.version = 4
        self.ihl = 5  # 5 * 32 bit = 20 byte
        self.tos = 0
        self.total_length = 60  # misal paket probe 60 byte
        self.identification = 0x4A2B
        self.flags = 0  # no fragmentation
        self.fragment_offset = 0
        self.ttl = initial_ttl
        self.protocol = protocol  # 1 = ICMP, 17 = UDP
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def _ip_to_int(self, ip_str):
        parts = [int(p) for p in ip_str.split('.')]
        return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

    def build_header(self, ttl=None, checksum=0):
        if ttl is None:
            ttl = self.ttl
        ver_ihl = (self.version << 4) | self.ihl
        flags_offset = (self.flags << 13) | (self.fragment_offset & 0x1FFF)
        src_int = self._ip_to_int(self.src_ip)
        dst_int = self._ip_to_int(self.dst_ip)

        header_bytes = struct.pack(
            "!BBHHHBBHII",
            ver_ihl,
            self.tos,
            self.total_length,
            self.identification,
            flags_offset,
            ttl,
            self.protocol,
            checksum,
            src_int,
            dst_int
        )
        return header_bytes

    @staticmethod
    def calculate_rfc1071_checksum(header_bytes):
        """Kalkulasi 16-bit One's Complement Sum (RFC 1071)."""
        if len(header_bytes) % 2 != 0:
            header_bytes += b'\x00'

        total = 0
        for i in range(0, len(header_bytes), 2):
            word = (header_bytes[i] << 8) + header_bytes[i + 1]
            total += word

        # Lipat carryover 32-bit ke 16-bit
        while (total >> 16) > 0:
            total = (total & 0xFFFF) + (total >> 16)

        # One's complement
        checksum = ~total & 0xFFFF
        return checksum

    @staticmethod
    def incremental_checksum_update(old_checksum, old_word, new_word):
        """
        Pembaruan checksum incremental sesuai RFC 1624:
        HC' = ~(~HC + ~m + m')
        Di mana:
        HC  = checksum lama
        m   = 16-bit word lama yang memuat TTL dan Protocol (misal [TTL, Protocol])
        m'  = 16-bit word baru dengan TTL yang telah dikurangi 1
        """
        # Dalam one's complement arithmetic:
        # ~HC = -HC, ~m = -m
        # Formula RFC 1624 Eq. 3: HC' = ~(~HC + ~m + m')
        c = (~old_checksum) & 0xFFFF
        m = (~old_word) & 0xFFFF
        m_prime = new_word & 0xFFFF

        total = c + m + m_prime
        while (total >> 16) > 0:
            total = (total & 0xFFFF) + (total >> 16)

        new_checksum = (~total) & 0xFFFF
        return new_checksum

    def simulate_hop_decrement(self, max_hops=10):
        print(f"{'='*75}")
        print(f"SIMULASI DEKREMENTASI TTL & PEMBARUAN CHECKSUM HEADER IPv4")
        print(f"Sumber: {self.src_ip} -> Tujuan: {self.dst_ip} | Protokol: {self.protocol} (ICMP)")
        print(f"{'='*75}")
        print(f"{'Hop':<5} | {'TTL':<5} | {'Word [TTL,Prot]':<16} | {'RFC 1071 Checksum':<18} | {'RFC 1624 Incr':<14} | {'Status'}")
        print(f"{'-'*75}")

        current_ttl = self.ttl
        # Hitung checksum awal dengan field checksum = 0
        raw_header = self.build_header(ttl=current_ttl, checksum=0)
        current_checksum = self.calculate_rfc1071_checksum(raw_header)

        old_word = (current_ttl << 8) | self.protocol
        print(f"{0:<5} | {current_ttl:<5} | 0x{old_word:04X}           | 0x{current_checksum:04X}             | {'(Host Awal)':<14} | Paket dibuat")

        for hop in range(1, max_hops + 1):
            prev_ttl = current_ttl
            current_ttl -= 1
            if current_ttl < 0:
                print(f"{hop:<5} | 0     | Paket dibuang (TTL Expired in Transit) -> Kirim ICMP Type 11 Code 0")
                break

            old_word = (prev_ttl << 8) | self.protocol
            new_word = (current_ttl << 8) | self.protocol

            # 1. Hitung ulang dari awal menggunakan RFC 1071
            raw_new = self.build_header(ttl=current_ttl, checksum=0)
            rfc1071_cs = self.calculate_rfc1071_checksum(raw_new)

            # 2. Hitung cepat menggunakan RFC 1624 Incremental Update
            rfc1624_cs = self.incremental_checksum_update(current_checksum, old_word, new_word)

            match = "MATCH (Valid)" if rfc1071_cs == rfc1624_cs else "MISMATCH"
            print(f"{hop:<5} | {current_ttl:<5} | 0x{new_word:04X}           | 0x{rfc1071_cs:04X}             | 0x{rfc1624_cs:04X}         | {match}")

            current_checksum = rfc1624_cs
        print(f"{'='*75}\n")


# ==============================================================================
# 2. DATA TELEMETRI RIIL EKSPERIMEN TRACEROUTE
# ==============================================================================

TRACERT_DATA_1111 = [
    {"hop": 1, "ip": "192.168.110.1", "name": "Local AP / Router", "rtts": [9.0, 5.0, 53.0], "type": "Private LAN"},
    {"hop": 2, "ip": "192.168.10.1", "name": "Distribution Router", "rtts": [22.0, 25.0, 15.0], "type": "Private LAN"},
    {"hop": 3, "ip": "192.168.1.1", "name": "ONT / Home Gateway", "rtts": [3.0, 3.0, 3.0], "type": "Private LAN/ONT"},
    {"hop": 4, "ip": "36.81.160.1", "name": "Telkom BNG / Aggregation", "rtts": [4.0, 8.0, 5.0], "type": "ISP Edge Gateway"},
    {"hop": 5, "ip": "125.160.0.125", "name": "Telkom Backbone Surabaya", "rtts": [20.0, 7.0, 19.0], "type": "ISP Core/Backbone"},
    {"hop": 6, "ip": "180.240.196.40", "name": "Telkom Core Jakarta", "rtts": [39.0, 32.0, 35.0], "type": "ISP Core/Backbone"},
    {"hop": 7, "ip": "180.240.196.40", "name": "Telkom Core/Interconnect", "rtts": [38.0, 42.0, 67.0], "type": "ISP Core/Peering"},
    {"hop": 8, "ip": "*", "name": "Firewalled / Rate-limited Router", "rtts": [None, None, None], "type": "ICMP Filtered"},
    {"hop": 9, "ip": "162.158.160.248", "name": "Cloudflare Peering Edge", "rtts": [31.0, 33.0, 34.0], "type": "CDN / Cloudflare Peering"},
    {"hop": 10, "ip": "172.69.117.60", "name": "Cloudflare Edge Node (1.1.1.1 Anycast)", "rtts": [29.0, 32.0, 29.0], "type": "Destination Target"},
]

TRACERT_DATA_8888 = [
    {"hop": 1, "ip": "192.168.110.1", "name": "Local AP / Router", "rtts": [1.0, 1.0, 3.0], "type": "Private LAN"},
    {"hop": 2, "ip": "192.168.10.1", "name": "Distribution Router", "rtts": [6.0, 36.0, 4.0], "type": "Private LAN"},
    {"hop": 3, "ip": "192.168.1.1", "name": "ONT / Home Gateway", "rtts": [164.0, 10.0, 6.0], "type": "Private LAN/ONT"},
    {"hop": 4, "ip": "36.81.160.1", "name": "Telkom BNG / Aggregation", "rtts": [7.0, 31.0, 23.0], "type": "ISP Edge Gateway"},
    {"hop": 5, "ip": "125.160.0.125", "name": "Telkom Backbone Surabaya", "rtts": [15.0, 27.0, 24.0], "type": "ISP Core/Backbone"},
    {"hop": 6, "ip": "180.240.196.40", "name": "Telkom Core Jakarta", "rtts": [53.0, 42.0, 34.0], "type": "ISP Core/Backbone"},
    {"hop": 7, "ip": "180.240.196.40", "name": "Telkom Peering (Slow Path ICMP)", "rtts": [91.0, 69.0, 223.0], "type": "ISP Interconnect"},
    {"hop": 8, "ip": "*", "name": "Filtered Core / CoPP Shield", "rtts": [None, None, None], "type": "ICMP Filtered"},
    {"hop": 9, "ip": "72.14.217.34", "name": "Google Peering Edge", "rtts": [48.0, 30.0, 27.0], "type": "Google AS15169 Gateway"},
    {"hop": 10, "ip": "172.253.70.41", "name": "Google Internal Backbone", "rtts": [29.0, 27.0, 29.0], "type": "Google Backbone"},
    {"hop": 11, "ip": "209.85.245.51", "name": "Google Internal Backbone", "rtts": [27.0, 28.0, 29.0], "type": "Google Backbone"},
    {"hop": 12, "ip": "8.8.8.8", "name": "Google DNS Anycast (Target)", "rtts": [26.0, 27.0, 27.0], "type": "Destination Target"},
]


# ==============================================================================
# 3. GENERASI GRAFIK PROFIL LATENSI HOP-BY-HOP
# ==============================================================================

def generate_latency_chart(output_paths):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 10), sharex=False)
    fig.patch.set_facecolor('#FDFDFD')

    # Color palette
    color_primary = '#1A5276'
    color_accent = '#D9534F'
    color_cloud = '#2E7D32'
    color_grid = '#E0E0E0'

    # --- Plot 1: Target Cloudflare 1.1.1.1 ---
    hops_1 = [d["hop"] for d in TRACERT_DATA_1111]
    avg_rtts_1 = [np.mean(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_1111]
    min_rtts_1 = [min(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_1111]
    max_rtts_1 = [max(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_1111]

    ax1.plot(hops_1, avg_rtts_1, marker='o', markersize=8, color=color_primary, linewidth=2.2, label='Average RTT (ms)')
    ax1.fill_between(hops_1, min_rtts_1, max_rtts_1, color=color_primary, alpha=0.18, label='Min-Max RTT Range')

    # Highlight timeout asterisk at hop 8
    ax1.plot(8, 0, marker='X', markersize=12, color=color_accent, label='Hop 8: Timeout (* * *) - ICMP Rate Limit / Filter')
    ax1.annotate('Hop 8: Rate-Limited (* * *)\nRouter Control Plane blocks ICMP', 
                 xy=(8, 5), xytext=(6.5, 30),
                 arrowprops=dict(arrowstyle="->", color=color_accent, lw=1.5),
                 fontsize=9.5, fontweight='bold', color=color_accent,
                 bbox=dict(boxstyle="round,pad=0.4", fc="#FFF0F0", ec=color_accent, lw=1))

    # Annotation destination
    ax1.annotate(f'Target Cloudflare: 10 hops\nAvg RTT: {avg_rtts_1[-1]:.1f} ms', 
                 xy=(10, avg_rtts_1[-1]), xytext=(9.2, 55),
                 arrowprops=dict(arrowstyle="->", color=color_cloud, lw=1.5),
                 fontsize=9.5, fontweight='bold', color=color_cloud,
                 bbox=dict(boxstyle="round,pad=0.4", fc="#F0FFF0", ec=color_cloud, lw=1))

    ax1.set_title('Traceroute Telemetry: Local Host -> 1.1.1.1 (Cloudflare DNS)', fontsize=13, fontweight='bold', pad=12)
    ax1.set_ylabel('Round-Trip Time (RTT) [ms]', fontsize=11, fontweight='bold')
    ax1.set_xticks(hops_1)
    ax1.set_xticklabels([f"Hop {h}\n({TRACERT_DATA_1111[h-1]['ip']})" for h in hops_1], fontsize=8.5, rotation=25)
    ax1.set_ylim(-5, 80)
    ax1.grid(True, linestyle='--', alpha=0.6, color=color_grid)
    ax1.legend(loc='upper left', frameon=True, facecolor='#FFFFFF', framealpha=0.9)

    # --- Plot 2: Target Google DNS 8.8.8.8 ---
    hops_2 = [d["hop"] for d in TRACERT_DATA_8888]
    avg_rtts_2 = [np.mean(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_8888]
    min_rtts_2 = [min(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_8888]
    max_rtts_2 = [max(d["rtts"]) if d["rtts"][0] is not None else np.nan for d in TRACERT_DATA_8888]

    ax2.plot(hops_2, avg_rtts_2, marker='s', markersize=8, color='#7B1FA2', linewidth=2.2, label='Average RTT (ms)')
    ax2.fill_between(hops_2, min_rtts_2, max_rtts_2, color='#7B1FA2', alpha=0.18, label='Min-Max RTT Range')

    # Highlight Latency Spike at Hop 7
    ax2.annotate('Hop 7 Spike: Max 223 ms!\nControl Plane (Slow Path CPU)\nForwarding downstream tetap cepat!', 
                 xy=(7, max_rtts_2[6]), xytext=(4.3, 160),
                 arrowprops=dict(arrowstyle="->", color=color_accent, lw=1.6),
                 fontsize=9.5, fontweight='bold', color=color_accent,
                 bbox=dict(boxstyle="round,pad=0.4", fc="#FFF0F0", ec=color_accent, lw=1))

    # Highlight timeout asterisk at hop 8
    ax2.plot(8, 0, marker='X', markersize=12, color=color_accent, label='Hop 8: Timeout (* * *) - ICMP Rate Limit / Filter')

    # Annotation destination
    ax2.annotate(f'Target Google: 12 hops\nAvg RTT: {avg_rtts_2[-1]:.1f} ms\n(Downstream normal!)', 
                 xy=(12, avg_rtts_2[-1]), xytext=(10.2, 80),
                 arrowprops=dict(arrowstyle="->", color=color_cloud, lw=1.5),
                 fontsize=9.5, fontweight='bold', color=color_cloud,
                 bbox=dict(boxstyle="round,pad=0.4", fc="#F0FFF0", ec=color_cloud, lw=1))

    ax2.set_title('Traceroute Telemetry: Local Host -> 8.8.8.8 (Google DNS Anycast)', fontsize=13, fontweight='bold', pad=12)
    ax2.set_xlabel('Nomor Hop & Alamat IP Router Perantara', fontsize=11, fontweight='bold', labelpad=10)
    ax2.set_ylabel('Round-Trip Time (RTT) [ms]', fontsize=11, fontweight='bold')
    ax2.set_xticks(hops_2)
    ax2.set_xticklabels([f"Hop {h}\n({TRACERT_DATA_8888[h-1]['ip']})" for h in hops_2], fontsize=8, rotation=30)
    ax2.set_ylim(-10, 250)
    ax2.grid(True, linestyle='--', alpha=0.6, color=color_grid)
    ax2.legend(loc='upper left', frameon=True, facecolor='#FFFFFF', framealpha=0.9)

    plt.tight_layout()
    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        plt.savefig(p, dpi=300)
        print(f"[OK] Diagram profil latensi tersimpan di: {p}")
    plt.close()


# ==============================================================================
# 4. DIAGRAM ARSITEKTUR ROUTER: FAST PATH VS SLOW PATH
# ==============================================================================

def generate_router_architecture_diagram(output_paths):
    fig, ax = plt.subplots(figsize=(12, 7.5))
    fig.patch.set_facecolor('#FDFDFD')
    ax.set_facecolor('#F7F9FB')

    # Title & Subtitle
    ax.text(0.5, 0.96, "Arsitektur Router: Fast Path (Data Plane) vs Slow Path (Control Plane)",
            fontsize=14, fontweight='bold', ha='center', va='top', transform=ax.transAxes, color='#1A365D')
    ax.text(0.5, 0.91, "Mengapa ICMP Time Exceeded (Traceroute) Dapat Mengalami Latency Spike Tanpa Mempengaruhi Forwarding",
            fontsize=10, fontstyle='italic', ha='center', va='top', transform=ax.transAxes, color='#4A5568')

    # Box 1: Ingress Line Card
    rect_ingress = plt.Rectangle((0.05, 0.35), 0.22, 0.42, facecolor='#EBF8FF', edgecolor='#3182CE', lw=2, zorder=2)
    ax.add_patch(rect_ingress)
    ax.text(0.16, 0.73, "Ingress Interface\n(Line Card)", ha='center', va='center', fontweight='bold', fontsize=11, color='#2B6CB0')
    ax.text(0.16, 0.54, "• Terima Frame L2\n• Parse Header IPv4\n• Cek TTL > 1 ?\n• Cek FIB / TCAM", ha='center', va='center', fontsize=9.5, color='#2D3748')

    # Box 2: Fast Path (Data Plane)
    rect_fast = plt.Rectangle((0.37, 0.55), 0.30, 0.25, facecolor='#E6FFFA', edgecolor='#319795', lw=2.2, zorder=2)
    ax.add_patch(rect_fast)
    ax.text(0.52, 0.75, "FAST PATH (Data Plane)", ha='center', va='center', fontweight='bold', fontsize=11.5, color='#234E52')
    ax.text(0.52, 0.64, "• Dedicated ASIC / NPU / TCAM\n• Forwarding jutaan paket/detik\n• Dekrementasi TTL & Checksum\n• Line-rate throughput (< 1 ms)", ha='center', va='center', fontsize=9.5, color='#1D4044')

    # Box 3: Slow Path (Control Plane)
    rect_slow = plt.Rectangle((0.37, 0.12), 0.30, 0.32, facecolor='#FFF5F5', edgecolor='#E53E3E', lw=2.2, zorder=2)
    ax.add_patch(rect_slow)
    ax.text(0.52, 0.39, "SLOW PATH (Control Plane)", ha='center', va='center', fontweight='bold', fontsize=11.5, color='#9B2C2C')
    ax.text(0.52, 0.24, "• General CPU & Sistem Operasi\n• Eksepsi: TTL = 1 -> TTL Expired!\n• Bangkitkan ICMP Type 11 Code 0\n• Enkapsulasi paket baru & kirim balik\n• Dibatasi CoPP / Rate Limiter", ha='center', va='center', fontsize=9.5, color='#742A2A')

    # Box 4: Egress Line Card
    rect_egress = plt.Rectangle((0.77, 0.55), 0.19, 0.25, facecolor='#EDFDFD', edgecolor='#2B6CB0', lw=2, zorder=2)
    ax.add_patch(rect_egress)
    ax.text(0.865, 0.72, "Egress Interface", ha='center', va='center', fontweight='bold', fontsize=11, color='#2B6CB0')
    ax.text(0.865, 0.62, "• Forwarding Paket\n  Normal ke Hop Berikut\n  (Next Hop)", ha='center', va='center', fontsize=9.5, color='#2D3748')

    # Arrows and Flow Labels
    # Normal Forwarding Flow (Green Arrow)
    ax.annotate("", xy=(0.37, 0.68), xytext=(0.27, 0.68),
                arrowprops=dict(facecolor='#319795', edgecolor='#234E52', width=3, headwidth=9))
    ax.text(0.32, 0.72, "TTL > 1\n(Normal)", color='#234E52', fontsize=9, fontweight='bold', ha='center')

    ax.annotate("", xy=(0.77, 0.68), xytext=(0.67, 0.68),
                arrowprops=dict(facecolor='#319795', edgecolor='#234E52', width=3, headwidth=9))
    ax.text(0.72, 0.72, "Line Rate", color='#234E52', fontsize=9, fontweight='bold', ha='center')

    # TTL Expired Exception Flow (Red Arrow to Slow Path)
    ax.annotate("", xy=(0.37, 0.28), xytext=(0.27, 0.42),
                arrowprops=dict(facecolor='#E53E3E', edgecolor='#9B2C2C', width=3, headwidth=9))
    ax.text(0.31, 0.33, "TTL = 1 (Habis)\nCPU Exception!", color='#9B2C2C', fontsize=9, fontweight='bold', ha='center')

    # ICMP Reply Out Flow
    ax.annotate("", xy=(0.27, 0.22), xytext=(0.37, 0.22),
                arrowprops=dict(facecolor='#DD6B20', edgecolor='#C05621', width=2.5, headwidth=8))
    ax.text(0.32, 0.17, "ICMP Time Exceeded\nKirim ke Pengirim", color='#C05621', fontsize=9, fontweight='bold', ha='center')

    # Explanation Callout
    callout_text = (
        "KESIMPULAN OPERASIONAL:\n"
        "1. Paket data biasa melewati FAST PATH di hardware (ASIC), bebas antrean CPU.\n"
        "2. Probe Traceroute memaksa CPU masuk SLOW PATH untuk menyusun pesan ICMP.\n"
        "3. Bila CPU sibuk atau ada pembatasan CoPP, respon ICMP tertunda (Spike) atau didrop (* * *).\n"
        "4. Kinerja forwarding jaringan aktual tetap sempurna asalkan hop berikutnya kembali normal!"
    )
    ax.text(0.5, 0.03, callout_text, ha='center', va='bottom', transform=ax.transAxes,
            fontsize=9.5, color='#1A202C',
            bbox=dict(boxstyle="square,pad=0.6", fc="#FEFCBF", ec="#D69E2E", lw=1.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    for p in output_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        plt.savefig(p, dpi=300)
        print(f"[OK] Diagram arsitektur router tersimpan di: {p}")
    plt.close()


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    print("\n--- MENJALANKAN ANALISIS TRACEROUTE & MEKANISME TTL ---")

    # 1. Jalankan simulasi matematis TTL & Checksum
    sim = IPv4HeaderSimulator(src_ip="192.168.110.100", dst_ip="8.8.8.8", protocol=1, initial_ttl=64)
    sim.simulate_hop_decrement(max_hops=8)

    # 2. Definisikan jalur penyimpanan visualisasi
    script_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(script_dir, "asset")
    os.makedirs(asset_dir, exist_ok=True)
    base_dir_6 = r"C:\Kuliah\Mata Kuliah\[ 4 ] Konsep Jaringan\[ 6 ] 1 Oktober 2026\asset"

    chart1_paths = [
        os.path.join(asset_dir, "traceroute_latency_analysis.png")
    ]
    if os.path.exists(base_dir_6):
        chart1_paths.append(os.path.join(base_dir_6, "traceroute_latency_analysis.png"))

    chart2_paths = [
        os.path.join(asset_dir, "fast_vs_slow_path_architecture.png")
    ]
    if os.path.exists(base_dir_6):
        chart2_paths.append(os.path.join(base_dir_6, "fast_vs_slow_path_architecture.png"))

    # 3. Buat dan simpan grafik
    generate_latency_chart(chart1_paths)
    generate_router_architecture_diagram(chart2_paths)

    print("\n[SELESAI] Seluruh simulasi dan visualisasi aset berhasil dibuat!")
