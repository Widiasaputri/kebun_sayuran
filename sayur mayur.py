class Kebun:
    def __init__(self):
        self.list_sayuran = {}
        self.banyak_jenis_sayur = 0

    def create_sayuran(self, nama, teknik, jumlah, hari, harga):
        self.banyak_jenis_sayur += 1
        nomor_sayuran = self.banyak_jenis_sayur
        self.list_sayuran[nomor_sayuran] = {
            'nama': nama,
            'teknik': teknik,
            'jumlah': jumlah,
            'hari': hari,
            'harga': harga
        }
        print(f"Sayuran {nama} berhasil ditambahkan")
        print()

    def read_sayuran(self, nomor_sayuran):
        if nomor_sayuran in self.list_sayuran:
            sayuran = self.list_sayuran[nomor_sayuran]
            print(f"Nama: {sayuran['nama']}")
            print(f"teknik: {sayuran['teknik']}") 
            print(f"Jumlah: {sayuran['jumlah']}")
            print(f"Hari: {sayuran['hari']}")
            print(f"harga: {sayuran['harga']}")
            print()
        else:
            print(f"sayuran dengan nomor {nomor_sayuran} tidak ditemukan")

    def update_sayuran(self, nomor_sayuran, nama, teknik, jumlah, hari, harga):
        if nomor_sayuran in self.list_sayuran:
            self.list_sayuran[nomor_sayuran] = {
                    'nama': nama,
                    'teknik': teknik,
                    'jumlah': jumlah,
                    'hari': hari,
                    'harga': harga
                    }
            print(f"Sayuran dengan nomor {nomor_sayuran} berhasil diperbarui")
            print()
        else:
            print(f"sayuran dengan nomor {nomor_sayuran} tidak ditemukan")

    def delete_sayuran(self, nomor_sayuran):
        if nomor_sayuran in self.list_sayuran:
            del self.list_sayuran[nomor_sayuran]
            print(f"Sayuran dengan nomor {nomor_sayuran} berhasil dihapus")
            print()
        else:
            (f"sayuran dengan nomor{nomor_sayuran}tidak ditemukan")

kebun = Kebun()
kebun.create_sayuran("selada", "hidroponik", 20, "15 hari", 12000)
kebun.read_sayuran(1)
kebun.update_sayuran(1, "selada", "hidroponik", 35, "20 hari", 12000)
kebun.read_sayuran(1)
kebun.update_sayuran(1, "wortel", "tanam pot", 25, "50 hari", 18000)
kebun.read_sayuran(1)
kebun.delete_sayuran(1)