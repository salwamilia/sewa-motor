import csv
import os

DATA_FILE = 'data_sewa.csv'

def init_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Jenis Motor', 'No Polisi', 'Nama Penyewa', 'No Telp', 'Tanggal Mulai', 'Tanggal Selesai'])

def baca_data():
    data = []
    if not os.path.exists(DATA_FILE):
        return data
    with open(DATA_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def simpan_data(data):
    with open(DATA_FILE, mode='w', newline='') as file:
        fieldnames = ['Jenis Motor', 'No Polisi', 'Nama Penyewa', 'No Telp', 'Tanggal Mulai', 'Tanggal Selesai']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
