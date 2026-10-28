#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VLSM Calculator and Visualizer
Mata Kuliah : Konsep Jaringan (TI043102) - PENS 2026
Penulis     : Shevanka Bagus Dwiyudi Kurniawan (NRP: 3125600044)
Dosen       : Dr. Ferry Astika Saputra, ST, M.Sc

Skrip ini melakukan:
1. Perhitungan matematis Variable Length Subnet Mask (VLSM) untuk blok 10.252.108.0/24.
2. Validasi bitwise, pencegahan overlap, dan perhitungan efisiensi alokasi host.
3. Analisis ruang alamat cadangan (unallocated address space).
4. Pembuatan visualisasi grafis resolusi tinggi (300 DPI):
   - Partisi blok ruang alamat (Address Block Partitioning)
   - Komparasi efisiensi kebutuhan vs kapasitas usable
   - Diagram topologi interkoneksi jaringan (Lab A, Lab B, Administrasi, Link P2P)
"""

import os
import math
import ipaddress
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Konfigurasi visual matplotlib
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8


class VLSMSubnet:
    def __init__(self, name, required_hosts):
        self.name = name
        self.required_hosts = required_hosts
        
        # Hitung bit host yang dibutuhkan: 2^h - 2 >= required_hosts
        # Catatan: Jika required_hosts == 2, h = 2 (2^2 - 2 = 2 host usable, subnet /30)
        h = 1
        while (2**h - 2) < required_hosts:
            h += 1
        self.host_bits = h
        self.prefix = 32 - h
        self.block_size = 2**h
        self.usable_hosts = 2**h - 2
        
        self.network = None
        self.broadcast = None
        self.first_usable = None
        self.last_usable = None
        self.netmask = None
        self.wildcard = None

    def allocate(self, start_ip_int):
        net_addr = ipaddress.IPv4Address(start_ip_int)
        self.network = ipaddress.IPv4Network(f"{net_addr}/{self.prefix}", strict=False)
        self.broadcast = self.network.broadcast_address
        self.first_usable = self.network.network_address + 1
        self.last_usable = self.broadcast - 1
        self.netmask = self.network.netmask
        self.wildcard = ipaddress.IPv4Address(int(self.network.hostmask))
        return start_ip_int + self.block_size


class VLSMPlanner:
    def __init__(self, base_cidr, subnet_specs):
        self.base_network = ipaddress.IPv4Network(base_cidr)
        # Urutkan subnet secara descending berdasarkan kebutuhan host
        self.subnets = [VLSMSubnet(name, hosts) for name, hosts in subnet_specs]
        self.subnets.sort(key=lambda x: x.required_hosts, reverse=True)
        self.unallocated_blocks = []
        self.total_allocated_ip = 0
        self.total_required_hosts = sum(s.required_hosts for s in self.subnets)
        self.total_usable_capacity = 0

    def compute(self):
        current_ip_int = int(self.base_network.network_address)
        base_end_int = int(self.base_network.broadcast_address)
        
        print("=" * 80)
        print(f"PERHITUNGAN VLSM UNTUK NETWORK INDUK: {self.base_network}")
        print(f"Total Kapasitas Blok Induk: {self.base_network.num_addresses} Alamat IP")
        print("=" * 80)
        
        for s in self.subnets:
            # Pastikan alamat mulai selaras dengan batas blok kelipatan block_size
            remainder = current_ip_int % s.block_size
            if remainder != 0:
                current_ip_int += (s.block_size - remainder)
                
            next_ip_int = s.allocate(current_ip_int)
            self.total_allocated_ip += s.block_size
            self.total_usable_capacity += s.usable_hosts
            current_ip_int = next_ip_int
            
        # Analisis sisa ruang alamat
        if current_ip_int <= base_end_int:
            remaining_ips = (base_end_int - current_ip_int) + 1
            start_rem = ipaddress.IPv4Address(current_ip_int)
            end_rem = ipaddress.IPv4Address(base_end_int)
            print(f"Ruang Alamat Tersisa (Unallocated): {remaining_ips} Alamat ({start_rem} - {end_rem})")
            
            # Subdivisi blok tersisa ke dalam CIDR valid
            curr = current_ip_int
            while curr <= base_end_int:
                # Cari blok CIDR terbesar yang muat
                max_size = base_end_int - curr + 1
                # Bit alignment
                alignment = curr & (-curr) if curr > 0 else 256
                # Cari pangkat 2
                sz = 1
                while sz * 2 <= max_size and sz * 2 <= alignment:
                    sz *= 2
                p = 32 - int(math.log2(sz))
                net = ipaddress.IPv4Network(f"{ipaddress.IPv4Address(curr)}/{p}")
                self.unallocated_blocks.append(net)
                curr += sz
        
        self.print_summary()

    def print_summary(self):
        print("\nHASIL ALOKASI SUBNET:")
        header = f"{'Subnet Name':<15} | {'Req':<5} | {'Prefix':<7} | {'Netmask':<15} | {'Network Address':<18} | {'Usable Host Range':<31} | {'Broadcast':<15}"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for s in self.subnets:
            usable_str = f"{s.first_usable} - {s.last_usable}"
            print(f"{s.name:<15} | {s.required_hosts:<5} | /{s.prefix:<6} | {str(s.netmask):<15} | {str(s.network.network_address) + '/' + str(s.prefix):<18} | {usable_str:<31} | {str(s.broadcast):<15}")
        print("-" * len(header))
        
        print("\nBLOK CADANGAN (UNALLOCATED BLOCKS):")
        for b in self.unallocated_blocks:
            print(f" - {b} ({b.num_addresses} IP: {b.network_address} s/d {b.broadcast_address})")
        
        efficiency = (self.total_allocated_ip / self.base_network.num_addresses) * 100
        host_eff = (self.total_required_hosts / self.total_usable_capacity) * 100
        print(f"\nMETRIK EFISIENSI:")
        print(f" - Total Kebutuhan Host Riil     : {self.total_required_hosts} host")
        print(f" - Total Kapasitas Usable Diberi : {self.total_usable_capacity} host")
        print(f" - Total IP Teralokasi (Subnet)  : {self.total_allocated_ip} / {self.base_network.num_addresses} ({efficiency:.2f}%)")
        print(f" - Efisiensi Host Usable         : {host_eff:.2f}%")


def generate_visualizations(planner, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # --------------------------------------------------------------------------
    # VISUALISASI 1: Partisi Ruang Alamat IP (Address Space Allocation Treemap/Bar)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    
    # Koordinat x dimulai dari 0 sampai 256
    colors = {
        'Lab A': '#2b5c8f',       # Biru elegan
        'Lab B': '#2d8a68',       # Hijau toska
        'Administrasi': '#d97724',# Oranye hangat
        'End-point': '#7c3aed',   # Ungu
        'Reserved': '#94a3b8'     # Abu-abu
    }
    
    current_x = 0
    y_pos = 0.5
    bar_height = 0.4
    
    for s in planner.subnets:
        width = s.block_size
        c = colors.get(s.name, '#3b82f6')
        rect = patches.Rectangle((current_x, y_pos - bar_height/2), width, bar_height,
                                 linewidth=1.5, edgecolor='#1e293b', facecolor=c, alpha=0.9)
        ax.add_patch(rect)
        
        # Label tengah
        cx = current_x + width / 2
        cy = y_pos
        ax.text(cx, cy + 0.05, f"{s.name}\n/{s.prefix}", ha='center', va='center',
                color='white', fontweight='bold', fontsize=11)
        ax.text(cx, cy - 0.12, f"{s.block_size} IP\n({s.usable_hosts} host)", ha='center', va='center',
                color='#f1f5f9', fontsize=8.5)
        
        # Tanda batas bawah
        ax.text(current_x, y_pos - bar_height/2 - 0.08, f".{current_x}", ha='center', va='top',
                fontsize=9, fontweight='semibold', color='#0f172a')
        
        current_x += width

    # Unallocated block
    rem_width = 256 - current_x
    if rem_width > 0:
        rect = patches.Rectangle((current_x, y_pos - bar_height/2), rem_width, bar_height,
                                 linewidth=1.5, edgecolor='#1e293b', facecolor=colors['Reserved'],
                                 linestyle='--', alpha=0.8)
        ax.add_patch(rect)
        cx = current_x + rem_width / 2
        ax.text(cx, y_pos + 0.05, "Unallocated / Cadangan", ha='center', va='center',
                color='white', fontweight='bold', fontsize=11)
        ax.text(cx, y_pos - 0.12, f"{rem_width} IP Bebas\n(.212 – .255)", ha='center', va='center',
                color='#f1f5f9', fontsize=8.5)
        ax.text(current_x, y_pos - bar_height/2 - 0.08, f".{current_x}", ha='center', va='top',
                fontsize=9, fontweight='semibold', color='#0f172a')
        ax.text(256, y_pos - bar_height/2 - 0.08, ".255", ha='center', va='top',
                fontsize=9, fontweight='semibold', color='#0f172a')

    ax.set_xlim(-5, 265)
    ax.set_ylim(0, 1.1)
    ax.axis('off')
    
    plt.title("Partisi Ruang Alamat VLSM IPv4: 10.252.108.0/24 (Total 256 Alamat)",
              fontsize=14, fontweight='bold', pad=25, color='#0f172a')
    
    # Subtitle / keterangan
    plt.figtext(0.5, 0.86,
                "Alokasi blok berdasarkan hukum pengurutan desending untuk mencegah fragmentasi internal",
                ha='center', fontsize=10, style='italic', color='#475569')
    
    plt.tight_layout()
    p1 = os.path.join(output_dir, 'vlsm_address_block_tree.png')
    plt.savefig(p1, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Visualisasi 1 tersimpan: {p1}")

    # --------------------------------------------------------------------------
    # VISUALISASI 2: Komparasi Kebutuhan Host vs Kapasitas Usable & Total Blok
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    categories = [s.name for s in planner.subnets] + ['Cadangan (Free)']
    req_hosts = [s.required_hosts for s in planner.subnets] + [0]
    usable_hosts = [s.usable_hosts for s in planner.subnets] + [44]  # 44 IP cadangan
    block_sizes = [s.block_size for s in planner.subnets] + [44]
    
    x = np.arange(len(categories))
    w = 0.25
    
    rects1 = ax.bar(x - w, req_hosts, w, label='Kebutuhan Host Riil', color='#3b82f6', edgecolor='#1d4ed8')
    rects2 = ax.bar(x, usable_hosts, w, label='Kapasitas Host Usable', color='#10b981', edgecolor='#047857')
    rects3 = ax.bar(x + w, block_sizes, w, label='Total Alokasi Blok (IP)', color='#6366f1', edgecolor='#4338ca')
    
    ax.set_ylabel('Jumlah Alamat IP / Host', fontsize=11, fontweight='semibold', color='#1e293b')
    ax.set_title('Analisis Kapasitas dan Efisiensi Alokasi VLSM (10.252.108.0/24)', fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{s.name}\n(/{s.prefix})" for s in planner.subnets] + ['Cadangan\n(Unallocated)'], fontsize=10)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)
    
    # Tambah angka di atas batang
    for rect in rects1:
        h = rect.get_height()
        if h > 0:
            ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1e40af')
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#065f46')
    for rect in rects3:
        h = rect.get_height()
        ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#3730a3')

    plt.tight_layout()
    p2 = os.path.join(output_dir, 'vlsm_host_efficiency_chart.png')
    plt.savefig(p2, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Visualisasi 2 tersimpan: {p2}")

    # --------------------------------------------------------------------------
    # VISUALISASI 3: Skema Topologi Jaringan Lengkap (Interkoneksi Kampus / Lab)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Background card
    bg = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=1,rounding_size=2",
                                facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1.5)
    ax.add_patch(bg)
    
    # Header box
    hdr = patches.FancyBboxPatch((5, 87), 90, 9, boxstyle="round,pad=0.5,rounding_size=1",
                                 facecolor="#1e293b", edgecolor="#0f172a")
    ax.add_patch(hdr)
    ax.text(50, 91.5, "TOPOLOGI ARSITEKTUR JARINGAN KAMPUS TERDISTRIBUSI BERBASIS VLSM",
            color="white", fontsize=13, fontweight="bold", ha="center", va="center")
    
    # Perangkat Router Utama (Core Router)
    r_core = patches.FancyBboxPatch((25, 62), 22, 14, boxstyle="round,pad=0.5,rounding_size=1.5",
                                    facecolor="#0284c7", edgecolor="#0369a1", linewidth=2)
    ax.add_patch(r_core)
    ax.text(36, 71, "ROUTER PUSAT (R1)", color="white", fontsize=11, fontweight="bold", ha="center")
    ax.text(36, 67, "G0/0.10: 10.252.108.1/25 (Lab A)\nG0/0.20: 10.252.108.129/26 (Lab B)\nG0/0.30: 10.252.108.193/28 (Admin)",
            color="#f0f9ff", fontsize=7.5, ha="center")

    # Perangkat Router Cabang (Edge / Remote Router)
    r_edge = patches.FancyBboxPatch((72, 62), 20, 14, boxstyle="round,pad=0.5,rounding_size=1.5",
                                    facecolor="#0284c7", edgecolor="#0369a1", linewidth=2)
    ax.add_patch(r_edge)
    ax.text(82, 71, "ROUTER CABANG (R2)", color="white", fontsize=11, fontweight="bold", ha="center")
    ax.text(82, 67, "S0/1/0: 10.252.108.210/30\n(Gedung Riset Jarak Jauh)",
            color="#f0f9ff", fontsize=7.5, ha="center")

    # Link P2P Antar Router (End-point / WAN link)
    ax.annotate('', xy=(72, 69), xytext=(47, 69),
                arrowprops=dict(arrowstyle="<->", color="#7c3aed", lw=3, ls="--"))
    ax.text(59.5, 73, "LINK POINT-TO-POINT (/30)", color="#6d28d9", fontsize=9, fontweight="bold", ha="center")
    ax.text(59.5, 70.5, "Network: 10.252.108.208/30", color="#4c1d95", fontsize=8, ha="center")
    ax.text(49, 66.5, ".209 (S0/1/0)", color="#7c3aed", fontsize=7.5, fontweight="bold")
    ax.text(67, 66.5, ".210 (S0/1/0)", color="#7c3aed", fontsize=7.5, fontweight="bold")

    # Trunk Switch Utama (Distribution Switch)
    sw_core = patches.FancyBboxPatch((28, 42), 16, 9, boxstyle="round,pad=0.5,rounding_size=1",
                                     facecolor="#334155", edgecolor="#1e293b", linewidth=1.5)
    ax.add_patch(sw_core)
    ax.text(36, 47.5, "SWITCH DISTRIBUSI", color="white", fontsize=9, fontweight="bold", ha="center")
    ax.text(36, 44, "IEEE 802.1Q Trunking", color="#cbd5e1", fontsize=7.5, ha="center")

    # Link Trunk R1 ke Switch Distribusi
    ax.plot([36, 36], [62, 51], color="#0f172a", lw=2.5)
    ax.text(38, 56.5, "Trunk 802.1Q (G0/0)", color="#0f172a", fontsize=7.5, fontweight="semibold")

    # Subnet 1: Lab A
    sw_laba = patches.FancyBboxPatch((6, 22), 24, 13, boxstyle="round,pad=0.5,rounding_size=1",
                                     facecolor="#eff6ff", edgecolor="#2563eb", linewidth=1.5)
    ax.add_patch(sw_laba)
    ax.text(18, 31, "SUBNET LAB A (VLAN 10)", color="#1d4ed8", fontsize=9.5, fontweight="bold", ha="center")
    ax.text(18, 27.5, "Kebutuhan: 90 Host\nPrefix: 10.252.108.0/25\nRange: .1 s/d .126 | Bcast: .127",
            color="#1e3a8a", fontsize=7.2, ha="center")
    ax.plot([30, 18], [42, 35], color="#2563eb", lw=1.8)

    # Subnet 2: Lab B
    sw_labb = patches.FancyBboxPatch((35, 22), 24, 13, boxstyle="round,pad=0.5,rounding_size=1",
                                     facecolor="#f0fdf4", edgecolor="#16a34a", linewidth=1.5)
    ax.add_patch(sw_labb)
    ax.text(47, 31, "SUBNET LAB B (VLAN 20)", color="#15803d", fontsize=9.5, fontweight="bold", ha="center")
    ax.text(47, 27.5, "Kebutuhan: 60 Host\nPrefix: 10.252.108.128/26\nRange: .129 s/d .190 | Bcast: .191",
            color="#14532d", fontsize=7.2, ha="center")
    ax.plot([36, 47], [42, 35], color="#16a34a", lw=1.8)

    # Subnet 3: Administrasi
    sw_admin = patches.FancyBboxPatch((64, 22), 28, 13, boxstyle="round,pad=0.5,rounding_size=1",
                                      facecolor="#fff7ed", edgecolor="#ea580c", linewidth=1.5)
    ax.add_patch(sw_admin)
    ax.text(78, 31, "SUBNET ADMINISTRASI (VLAN 30)", color="#c2410c", fontsize=9.5, fontweight="bold", ha="center")
    ax.text(78, 27.5, "Kebutuhan: 14 Host\nPrefix: 10.252.108.192/28\nRange: .193 s/d .206 | Bcast: .207",
            color="#7c2d12", fontsize=7.2, ha="center")
    ax.plot([42, 75], [42, 35], color="#ea580c", lw=1.8)

    # Client representations di bagian bawah
    ax.text(18, 14, "[ PC Client Lab A: 10.252.108.2 – 10.252.108.126 ]",
            ha="center", fontsize=7.5, color="#1e40af", bbox=dict(boxstyle="square,pad=0.3", fc="#dbeafe", ec="#93c5fd"))
    ax.plot([18, 18], [22, 17], color="#2563eb", lw=1, ls=":")

    ax.text(47, 14, "[ PC Client Lab B: 10.252.108.130 – 10.252.108.190 ]",
            ha="center", fontsize=7.5, color="#166534", bbox=dict(boxstyle="square,pad=0.3", fc="#dcfce7", ec="#86efac"))
    ax.plot([47, 47], [22, 17], color="#16a34a", lw=1, ls=":")

    ax.text(78, 14, "[ PC & Server Staf: 10.252.108.194 – 10.252.108.206 ]",
            ha="center", fontsize=7.5, color="#9a3412", bbox=dict(boxstyle="square,pad=0.3", fc="#ffedd5", ec="#fed7aa"))
    ax.plot([78, 78], [22, 17], color="#ea580c", lw=1, ls=":")

    # Footer note
    ftr = "Total Alamat Teralokasi: 212 IP | Sisa Cadangan (Unallocated): 44 IP (10.252.108.212 s/d 10.252.108.255)"
    ax.text(50, 6, ftr, ha="center", fontsize=9, fontweight="bold", color="#475569")

    plt.tight_layout()
    p3 = os.path.join(output_dir, 'vlsm_network_topology.png')
    plt.savefig(p3, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Visualisasi 3 tersimpan: {p3}")


if __name__ == '__main__':
    base_network = "10.252.108.0/24"
    subnets_demand = [
        ("Lab A", 90),
        ("Lab B", 60),
        ("Administrasi", 14),
        ("End-point", 2)
    ]
    
    planner = VLSMPlanner(base_network, subnets_demand)
    planner.compute()
    
    # Simpan ke folder asset di Tugas 6
    script_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(script_dir, "asset")
    os.makedirs(asset_dir, exist_ok=True)
    generate_visualizations(planner, asset_dir)
