import os
from turtle import clear
from tabulate import tabulate
import pandas as pd


# Membuat dictionary kosong
keranjang = {}

def clear_screen():
  """
  Function untuk membersihkan layar dari aktifitas yang telah dilakukan sebelumnya
  """
  os.system ("cls" if os.name == "nt" else "clear")

# Memasukkan identitas user
username = input("Please enter your name: ")
clear_screen()

def back_menu():
  """
  Function untuk kembali ke menu awal
  """
  print("-"*50)
  input("Tekan Enter untuk kembali")
  clear_screen()
  Transaction.menu()
  
  
class Transaction:
  # Menampilkan cart order
  def show_order ():
    """ 
    Function untuk menampilkan tabel pesanan
    """
    
    # Mengubah dictionary menjadi dataframe
    df = pd.DataFrame(keranjang)
    header = ["Nama Item", "Jumlah Item", "Harga/item", "Total Harga"]
    
    # Menampilkan pesanan dalam bentuk tabel
    print(tabulate(df.T, header, tablefmt="fancy_grid"))
    

  # Membuat menu
  def menu():
    """
    Function ini berfungsi sebagai menu utama (navigasi) dalam aplikasi ini
    """
    
    welcome_Msg = f"Hai, {username}!\nWelcome to Self Service SuperMarket App"
    len_WCMsg = len(welcome_Msg)
    print("\n")
    print("="*len_WCMsg)
    print(welcome_Msg)
    print("="*len_WCMsg)
    print("1. Input My Order to Shopping Cart")
    print("2. Change My Order to Shopping Cart")
    print("3. Delete My Order from Shopping Cart")
    print("4. Check My Order")
    print("5. Delete All My Order from Shopping Cart")
    print("6. Check Total Payment and Discount")
    print("0. Exit\n")

    choice = int(input("Masukkan Pilihan Anda :"))
    clear_screen()

    while choice != 0:
      try:
        if choice == 1 :
          Transaction.add_item()
        elif choice == 2 :
          Transaction.update_item()
        elif choice == 3 :
          Transaction.delete_item()
        elif choice == 4 :
          Transaction.check_order()
        elif choice == 5 :
          Transaction.reset_transaction()
        elif choice == 6 :
          Transaction.total_price()
        else:
          print("Pilih nomor yang tertera pada menu : ")
          clear_screen()
      except ValueError :
          print("Error Input!")
          clear_screen()

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
      
    clear_screen()

  # Mengupdate orderan
  def update_item():
    """
    Function utama dengan pilihan untuk mengubah nama, jumlah dan harga item yang telah diinput sebelumnya
    ketika mengalami kesalahan input 
    """
    # Menu pilihan untuk edit nama, jumlah dan harga item
    print("-"*50)
    print("Transaksi apa yang ingin anda update?")
    print("1. Ubah Nama Item")
    print("2. Ubah Jumlah Item")
    print("3. Ubah Harga Item\n")

    choose = int(input("Masukkan jenis transaksi yang ingin di update :"))
    try:
      if choose == 1:
        Transaction.update_item_name()
      elif choose == 2:
        Transaction.update_item_qty()
      elif choose == 3:
        Transaction.update_item_price()
      else:
        print("Masukkan angka yang tertera di atas!")
    except:
      print("Sepertinya angka yang anda masukkan salah")
      
      back_menu()

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
  
  # Menghapus orderan
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

      print("\n")
      print (f"Item belanja {item} berhasil di delete !")
      print ("\n")

      back_menu()
    
    except:
      print("Gagal hapus data belanja anda:{}")
      back_menu()

  # Check order
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

    back_menu()


  # Reset transaction
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

  # Check out
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

    back_menu()

Transaction.menu()
