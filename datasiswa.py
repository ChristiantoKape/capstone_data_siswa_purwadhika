dataSiswa = [
]

def menampilkanDataSiwa() :
  def menampilkanSemuaSiswa():
    print('--- Daftar Siswa ---\n')
    print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')

    if (len(dataSiswa) == 0):
      print('\t\tTidak Ada Data Siswa!')

    for i in range(len(dataSiswa)) :
        print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
  
  def menampilkanSiswaTertentu():
    print('--- Daftar Siswa ---\n')
    print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')

    if (len(dataSiswa) == 0):
      print('\t\tTidak Ada Data Siswa!')
    else: 
      nisnSiswa = int(input('Masukkan Nisn Siswa: '))

    #print data sesuai index yang dicari

  while True:
    pilihanData = input('\n---- Record Data Siswa ----\n\nList Menu: \n1. Menampilkan Raport Semua Siswa \n2. Menampilkan Raport Siswa Tertentu \n3. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-3]: ')

    if(pilihanData == '1'):
      menampilkanSemuaSiswa()
    elif(pilihanData == '2'):
      menampilkanSiswaTertentu()
    elif(pilihanData == '3'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

while True:
  pilihanMenu = input('\n---- Data Raport Siswa ----\n\nList Menu: \n1. Menampilkan Data Siswa \n2. Menambah Data Siswa \n3. Mengubah Data Siswa \n4. Menghapus Data Siswa \n5. Exit Program \nSilahkan Pilih Menu [1-5]: ')

  if(pilihanMenu == '1'):
    menampilkanDataSiwa()
  elif(pilihanMenu == '2'):
    menambahDataSiswa()
  elif(pilihanMenu == '3'):
    mengubahDataSiswa()
  elif(pilihanMenu == '4'):
    menghapusDataSiswa()
  elif(pilihanMenu == '5'):
    print('Good Bye!')
    break
  else:  
    print('*****Pilihan yang anda masukkan salah!*****')