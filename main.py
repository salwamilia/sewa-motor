from data_manager import init_file
from sewa_motor import tampilkan_data, tambah_data, edit_data, hapus_data

def menu():
    init_file()
    while True:
        print("\n=== Aplikasi Sewa Motor ===")
        print("1. Lihat Data Sewa Motor")
        print("2. Tambah Data Sewa Motor")
        print("3. Edit Data Sewa Motor")
        print("4. Hapus Data Sewa Motor")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            edit_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()