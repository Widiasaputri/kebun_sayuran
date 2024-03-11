class Node:
    def __init__(self, nomor_sayuran, nama, teknik, jumlah, hari, harga):
        self.nomor_sayuran = nomor_sayuran
        self.data = {
            'nama': nama,
            'teknik': teknik,
            'jumlah': jumlah,
            'hari': hari,
            'harga': harga
        }
        self.next = None

class Kebun:
    def __init__(self):
        self.head = None
        self.tail = None
        self.banyak_jenis_sayur = 0

    def create_sayuran(self, nama, teknik, jumlah, hari, harga, posisi='akhir', posisi_nomor=None):
        self.banyak_jenis_sayur += 1
        new_node = Node(self.banyak_jenis_sayur, nama, teknik, jumlah, hari, harga)
        
        if self.head is None or posisi == 'awal':
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        elif posisi == 'akhir':
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current is not None and current.nomor_sayuran != posisi_nomor:
                prev = current
                current = current.next
            if current is not None:
                new_node.next = current.next
                current.next = new_node
            else:
                print("Posisi nomor tidak ditemukan. Sayuran ditambah di akhir")
                self.tail.next = new_node
                self.tail = new_node
        
        print(f"Sayuran {nama} berhasil ditambahkan\n")

    def read_sayuran(self):
        current = self.head
        if current is None:
            print("Tidak ada sayuran di kebun\n")
            return
        print("Daftar Sayuran:")
        while current is not None:
            print(f"Nomor: {current.nomor_sayuran}")
            print(f"Nama: {current.data['nama']}")
            print(f"Teknik: {current.data['teknik']}") 
            print(f"Jumlah: {current.data['jumlah']}") 
            print(f"Hari: {current.data['hari']}")
            print(f"Harga: {current.data['harga']}\n")
            current = current.next
        print()
    
    def update_sayuran(self, nomor_sayuran, nama, teknik, jumlah, hari, harga):
        current = self.head
        while current is not None:
            if current.nomor_sayuran == nomor_sayuran:
                current.data = {
                    'nama': nama,
                    'teknik': teknik,
                    'jumlah': jumlah,
                    'hari': hari,
                    'harga': harga
                }
                print(f"Sayuran dengan nomor {nomor_sayuran} berhasil diperbarui\n")
                return
            current = current.next
        print(f"Sayuran dengan nomor {nomor_sayuran} tidak ditemukan\n")
    
    def delete_sayuran(self, posisi):
        if self.head is None:
            print("Tidak ada sayuran untuk dihapus\n")
            return

        if posisi == 'awal':
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        elif posisi == 'akhir':
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
        else:
            current = self.head
            prev = None
            while current is not None and current.nomor_sayuran != posisi:
                prev = current
                current = current.next
            if current is None:
                print(f"Sayuran dengan nomor {posisi} tidak ditemukan\n")
                return
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            if current.next is None:
                self.tail = prev

        print("Sayuran berhasil dihapus\n")
        
    def mergeSort(self, head, attribute, order):
        if head is None or head.next is None:
            return head
        
        middle = self.getMiddle(head)
        nextToMiddle = middle.next
        
        middle.next = None
        
        left = self.mergeSort(head, attribute, order)
        right = self.mergeSort(nextToMiddle, attribute, order)
        
        sortedList = self.sortedMerge(left, right, attribute, order)
        return sortedList
    
    def getMiddle(self, head):
        if (head == None):
            return head
        
        slow = head
        fast = head
        
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def sortedMerge(self, a, b, attribute, order):
        result = None
        
        if a == None:
            return b
        if b == None:
            return a
        
        if  (attribute == "harga" and ((a.data[attribute] <= b.data[attribute] and order == "ascending") or (a.data[attribute] > b.data[attribute] and order == "descending"))) or \
            (attribute != "harga" and ((a.data[attribute] <= b.data[attribute] and order == "ascending") or (a.data[attribute] > b.data[attribute] and order == "descending"))):
            result = a
            result.next = self.sortedMerge(a.next, b, attribute, order)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next, attribute, order)
        return result
    
    def sort_sayuran(self, attribute="harga", order="ascending"):
        if attribute not in ['nama', 'teknik', 'jumlah', 'hari', 'harga']:
            print(f"Attribute '{attribute}' tidak terdapat dalam pilihan")
            return
        if order not in ['ascending', 'descending']:
            print(f"Diorder dalam '{order}' tidak terdapat dalam pilihan")
            return

        self.head = self.mergeSort(self.head, attribute, order)
        current = self.head
        while current and current.next is not None:
            current = current.next
        self.tail = current
        print(f"Sayuran berhasil diurutkan berdasarkan {attribute} secara {order}\n")
        self.read_sayuran()


    def menu(self):
        while True:
            print("=== Menu Kebun Sayuran ===")
            print("1. Tambah Sayuran")
            print("2. Lihat Sayuran")
            print("3. Ubah Sayuran")
            print("4. Hapus Sayuran")
            print("5. Urutkan Sayuran")
            print("6. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                nama = input("Masukkan nama sayuran: ")
                teknik = input("Masukkan teknik penanaman: ")
                jumlah = int(input("Masukkan jumlah: "))
                hari = input("Masukkan lama tanam: ")
                harga = int(input("Masukkan harga: "))
                print("Pilih posisi penambahan: 1. Awal 2. Akhir 3. Di antara")
                posisi_pilihan = input("Masukkan pilihan (1/2/3): ")  
                if posisi_pilihan == '1':
                    posisi = 'awal'
                    self.create_sayuran(nama, teknik, jumlah, hari, harga, posisi)
                elif posisi_pilihan == '2':
                    posisi = 'akhir'
                    self.create_sayuran(nama, teknik, jumlah, hari, harga, posisi)
                elif posisi_pilihan == '3':
                    posisi = 'antara'
                    posisi_nomor = int(input("Masukkan nomor sayuran setelah penambahan: "))
                    self.create_sayuran(nama, teknik, jumlah, hari, harga, posisi, posisi_nomor)
                
            elif pilihan == '2':
                print()
                self.read_sayuran()
                
            elif pilihan == '3':
                print()
                nomor_sayuran = int(input("Masukkan nomor sayuran yang ingin diubah: "))
                nama = input("Masukkan nama sayuran: ")
                teknik = input("Masukkan teknik penanaman: ")
                jumlah = int(input("Masukkan jumlah: "))
                hari = input("Masukkan lama tanam: ")
                harga = int(input("Masukkan harga: "))
                self.update_sayuran(nomor_sayuran, nama, teknik, jumlah, hari, harga)
                
            elif pilihan == '4':
                print("Hapus sayuran di: 1. Awal 2. Akhir 3. Nomor khusus (Masukkan nomor yang ingin dihapus)")
                posisi = input("Pilih: ")
                if posisi == '1':
                    posisi = 'awal'
                elif posisi == '2':
                    posisi = 'akhir'
                else:
                    posisi = int(posisi)
                self.delete_sayuran(posisi)
                
            elif pilihan == '5':
                attribute = input("Urutkan berdasarkan (harga/nama): ").lower()
                order = input("Urutan (ascending/descending): ").lower()
                self.sort_sayuran(attribute, order)
                
            elif pilihan == '6':
                print("Terima kasih telah menggunakan menu kebun sayuran")
                break
            else:
                print("Pilihan tidak tersedia, silakan coba lagi\n")

kebun = Kebun()
kebun.menu()

