from datetime import datetime
from data_manager import baca_data, simpan_data

HARGA_PER_HARI = 25000

def hitung_durasi(tgl_mulai, tgl_selesai):
    fmt = '%Y-%m-%d'
    start = datetime.strptime(tgl_mulai, fmt)
    end = datetime.strptime(tgl_selesai, fmt)
    durasi = (end - start).days + 1
    if durasi < 0:
        return 0
    return durasi

def hitung_biaya(durasi):
    return durasi * HARGA_PER_HARI

def tampilkan_data():
    data = baca_data()
    if not data:
        print("Data sewa motor kosong.")
        return
    print(f"{'No':<3} {'Jenis Motor':<15} {'No Polisi':<12} {'Nama Penyewa':<20} {'No Telp':<15} {'Mulai':<12} {'Selesai':<12} {'Durasi(hari)':<13} {'Biaya(Rp)':<10}")
    print("-"*120)
    for i, d in enumerate(data, start=1):
        durasi = hitung_durasi(d['Tanggal Mulai'], d['Tanggal Selesai'])
        biaya = hitung_biaya(durasi)
        print(f"{i:<3} {d['Jenis Motor']:<15} {d['No Polisi']:<12} {d['Nama Penyewa']:<20} {d['No Telp']:<15} {d['Tanggal Mulai']:<12} {d['Tanggal Selesai']:<12} {durasi:<13} {biaya:<10}")

def tambah_data():
    print("\nTambah Data Sewa Motor")
    jenis = input("Jenis Motor: ").strip()
    no_pol = input("No Polisi: ").strip()
    nama = input("Nama Penyewa: ").strip()
    no_telp = input("No Telp: ").strip()
    tgl_mulai = input("Tanggal Mulai (YYYY-MM-DD): ").strip()
    tgl_selesai = input("Tanggal Selesai (YYYY-MM-DD): ").strip()

    try:
        start_date = datetime.strptime(tgl_mulai, '%Y-%m-%d')
        end_date = datetime.strptime(tgl_selesai, '%Y-%m-%d')
        if end_date < start_date:
            print("Tanggal selesai tidak boleh lebih awal dari tanggal mulai.")
            return
    except ValueError:
        print("Format tanggal salah, harus YYYY-MM-DD.")
        return

    data = baca_data()
    data.append({
        'Jenis Motor': jenis,
        'No Polisi': no_pol,
        'Nama Penyewa': nama,
        'No Telp': no_telp,
        'Tanggal Mulai': tgl_mulai,
        'Tanggal Selesai': tgl_selesai
    })
    simpan_data(data)
    print("Data berhasil ditambahkan.")

def edit_data():
    data = baca_data()
    if not data:
        print("Data kosong, tidak bisa edit.")
        return
    tampilkan_data()
    try:
        idx = int(input("Pilih nomor data yang ingin diedit: ")) - 1
        if idx < 0 or idx >= len(data):
            print("Nomor tidak valid.")
            return
    except ValueError:
        print("Input harus angka.")
        return

    print("Masukkan data baru (kosongkan jika tidak ingin diubah):")
    jenis = input(f"Jenis Motor [{data[idx]['Jenis Motor']}]: ").strip() or data[idx]['Jenis Motor']
    no_pol = input(f"No Polisi [{data[idx]['No Polisi']}]: ").strip() or data[idx]['No Polisi']
    nama = input(f"Nama Penyewa [{data[idx]['Nama Penyewa']}]: ").strip() or data[idx]['Nama Penyewa']
    no_telp = input(f"No Telp [{data[idx]['No Telp']}]: ").strip() or data[idx]['No Telp']
    tgl_mulai = input(f"Tanggal Mulai [{data[idx]['Tanggal Mulai']}]: ").strip() or data[idx]['Tanggal Mulai']
    tgl_selesai = input(f"Tanggal Selesai [{data[idx]['Tanggal Selesai']}]: ").strip() or data[idx]['Tanggal Selesai']

    try:
        start_date = datetime.strptime(tgl_mulai, '%Y-%m-%d')
        end_date = datetime.strptime(tgl_selesai, '%Y-%m-%d')
        if end_date < start_date:
            print("Tanggal selesai tidak boleh lebih awal dari tanggal mulai.")
            return
    except ValueError:
        print("Format tanggal salah, harus YYYY-MM-DD.")
        return

    data[idx] = {
        'Jenis Motor': jenis,
        'No Polisi': no_pol,
        'Nama Penyewa': nama,
        'No Telp': no_telp,
        'Tanggal Mulai': tgl_mulai,
        'Tanggal Selesai': tgl_selesai
    }
    simpan_data(data)
    print("Data berhasil diupdate.")

def hapus_data():
    data = baca_data()
    if not data:
        print("Data kosong, tidak bisa hapus.")
        return
    tampilkan_data()
    try:
        idx = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(data):
            print("Nomor tidak valid.")
            return
    except ValueError:
        print("Input harus angka.")
        return

    konfirmasi = input(f"Yakin ingin menghapus data nomor {idx+1}? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        data.pop(idx)
        simpan_data(data)
        print("Data berhasil dihapus.")
    else:
        print("Hapus data dibatalkan.")
