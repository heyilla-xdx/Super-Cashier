Super Cashier Project
 
 
Latar Belakang
 
Seorang pemilik Supermarket besar memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu membuat sistem kasir self-service di Supermarket miliknya. Dimana Customer dapat langsung memasukkan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli.
Sehingga customer yang tidak berada di kota tersebut 
 
Super Cashier App adalah sistem kasir self-service sederhana yang dibuat untuk usaha Supermarket. Dimana pada aplikasi ini memiliki fitur-fitur seperti menambahkan barang, jumlah, dan harga barang. Aplikasi ini dibuat dengan menggunakan bahasa pemrograman python.
 
Features
User dapat memasukkan nama item, jumlah item dan harga/item
User dapat mengedit nama item, jumlah item dan harga/item jika mengalami kesalahan pada saat penginputan sebelumnya.
User dapat menghapus pesanan yang tidak diinginkan
User dapat menghapus semua pesanan yang telah dimasukkan ke keranjang / mereset semua transaksi
User dapat mengecek ulang pesanan yang telah dimasukkan ke dalam keranjang
User dapat melihat total harga pesanan yang telah dibeli dan mendapatkan diskon jika memenuhi minimal pembelian pesanan yang berlaku.
 
Flow Chart












Function untuk menambahkan nama item, jumlah item dan harga/item
def add_item():
   """
   Function untuk menambahkan item pesanan
   """
   try:
     item = str(input("Masukkan Item yang ingin dibeli : "))
     jumlah = int(input(f"Berapa Jumlah {item} yang ingin dibeli : "))
     harga = int(input(f"Masukkan Harga {item} yang ingin dibeli : Rp. "))
     clear_screen()


     # Masukkan variabel ke dictionary baru, dan update ke dictionary keranjang
     order_name = {item : [jumlah, harga, jumlah * harga]}
     keranjang.update(order_name)


     # Menampilan tabel pesanan yang baru saja ditambahkan
     Transaction.show_order()
     print(f"{item} berhasil ditambahkan !\n")
     back_menu()


   except:
     print("Format yang Anda masukkan salah, harus Angka !")
     back_menu()

 Function untuk mengedit nama item jika mengalami kesalahan dala penginputan
def update_item_name():
   """
   Function untuk mengubah atau mengedit nama item
   """
  
   try:
     # Buat variabel untuk memasukkan nama item yang akan di update
     item= str(input("Nama item : "))
     item_update = str (input("Nama item (update) : "))
  
     # Masukkan variabel yang sudah diinput ke dictionary baru, dan update ke dictionary keranjang
     item_baru = {item_update : keranjang[item]}
     keranjang.update(item_baru)
     keranjang.pop(item)


     # Menampilan tabel pesanan setelah update nama item
     Transaction.show_order()
     print(f"{item} berhasil diganti menjadi {item_update} !\n")
     back_menu()


   except:
     print("Gagal update nama item pada data belanja Anda")
     back_menu()



Function untuk mengupdate / mengedit jumlah item 
def update_item_qty():
   """
   Function untuk mengubah atau mengedit jumlah item yang sudah diinput sebelumnya
   """
  
   try:
     # Buat variabel untuk memasukkan item qty yang akan di update
     item = str(input("Masukkan nama item yang akan diganti jumlahnya : "))
     item_qty_new = int(input("Jumlah item (update) : "))


     # Masukkan variabel yang sudah diinput ke dictionary baru, dan update ke dictionary keranjang
     keranjang[item][0] = item_qty_new
     keranjang[item][2] = keranjang[item][0] * keranjang[item][1]


     # Menampilan tabel pesanan setelah update jumlah item
     Transaction.show_order()
     print(f"{item} berhasil diganti jumlahnya menjadi {item_qty_new} !\n")
     back_menu()


   except ValueError:
     print("Gagal update jumlah item pada data belanja Anda")
     back_menu()



Function untuk mengupdate / mengedit harga/item
def update_item_price():
   """
   Function untuk mengubah atau mengedit harga item yang sudah diinput sebelumnya
   """
  
   try:
     # Buat variabel untuk memasukkan harga yang akan di update
     item = str(input("Masukkan nama item yang akan diganti harganya : "))
     item_price_new = int(input("Harga item (update) : Rp "))
     clear_screen()


     # Masukkan variabel yang sudah diinput ke dictionary baru, dan update ke dictionary keranjang
     keranjang[item][1] = item_price_new
     keranjang[item][2] = keranjang[item][0] * keranjang[item][1]


     # Menampilan tabel pesanan setelah update harga item
     Transaction.show_order()
     print(f"{item} berhasil diganti menjadi Rp. {item_price_new} !\n")
     back_menu()


   except ValueError:
     print("Gagal update nama item pada data belanja Anda:{}")
     back_menu()

Function untuk menghapus pesanan
 def delete_item():
   """
   Function untuk menghapus pesanan
   """
  
   print("Masukkan nama item yang ingin dihapus : ")


   try:
     #Buat variabel untuk memasukan nama item yang ingin diganti
     item = str(input("\n Nama Item : "))
     keranjang.pop(item)


     #Menampilkan daftar pesanan user
     Transaction.show_order()
    
     print (f"\nItem belanja {item} berhasil di delete !\n")
     back_menu()
  
   except:
     print("Gagal hapus data belanja anda:{}")
     back_menu()

Function untuk mengecek semua pesanan yang sudah diinput
 def check_order ():
   """
   Function untuk mengecek pesanan yang sudah ditambahkan ke dalam keranjang beserta total harganya
   """
   # Menampilan tabel pesanan user
   Transaction.show_order()


   total = 0
   for key in keranjang :
     total = total + keranjang [key][2]
   print(f"Total belanja Anda : Rp. {total}\n")



Function untuk menghapus semua transaksi / mereset semua transaksi yang sudah diinput
def reset_transaction():
   """
   Function untuk menghapus seluruh keranjang belanja / mereset transaksi
   """
   # Memastikan kembali kepada user apakah akan dihapus semua atau tidak?
   print(" Apakah Anda yakin ingin menghapus seluruh pesanan? ")
  
   try:
     ensure_key = (int(input("\n Tekan 1 untuk menghapus seluruh keranjang belanja atau any key untuk batal : ")))


     # Hapus dictionary dengan .clear
     keranjang.clear()
     Transaction.show_order()
     print(f"\nKeranjang kosong !\n")
     back_menu()
  
   except:
     print("Gagal hapus semua data belanja anda:{}")
     back_menu()

Function untuk menjumlahkan semua pesanan yang sudah diinput dan mengecek diskon yang didapat
def total_price():
   """
   Function untuk melihat jumlah semua pesanan yang telah dimasukkan ke dalam keranjang,
   melihat total pesanan dan melihat apakah mendapatkan diskon atau tidak
   """


   # Menghitung total belanjaan
   total = 0
   total_order = 0
   for key in keranjang:
     total = total + keranjang[key][2]
  
   Transaction.show_order()


   # Conditional for discount
   if total >= 500_000:
       print(f"\nTotal belanja Anda adalah : Rp. {total}")
       print("Selamat ! Anda mendapatkan diskon 10%")
       discount = int(total * 0.10)
       total_after_discount = total - discount 
       print(f"Total belanja Anda setelah diskon adalah: Rp. ({total_after_discount})\n")
   elif total >300_000:
       print(f"\nTotal belanja Anda adalah : Rp. {total}")
       print("Anda mendapatkan diskon 8%")
       discount = total * 0.08
       total_after_discount = total - discount
       print(f"Total belanja Anda setelah diskon adalah: Rp. ({total_after_discount})\n")
   elif total >=200_000:
       print(f"\nTotal belanja Anda adalah : Rp. {total}")
       print("Anda mendapatkan diskon 5%")
       discount = total * 0.05
       total_after_discount = total - discount
       print(f"Total belanja Anda setelah diskon adalah: Rp. ({total_after_discount})\n")
   else:
     print(f"\nTotal belanja Anda adalah: {total}")
     print("Maaf Anda belum mendapatkan diskon. Ayo belanja lagi !\n") 





Demonstration (Test Code)




Conclusion

Super Cashier App ini merupakan sistem yang sederhana dalam segi tampilan. diharapkan kedepannya view pada sistem ini lebih baik lagi seiring dengan berjalannya kemajuan teknologi.
  
