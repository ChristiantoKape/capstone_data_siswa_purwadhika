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
    inputData = input('Masukkan Nisn/Nama Siswa: ')
    if(inputData.isdigit()):
      for i in range(len(dataSiswa)) :
        if(dataSiswa[i]['Nisn'] == inputData):
          print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
          break
        else:
          print('Data Siswa Tidak Ditemukan!')
    else:
      for i in range(len(dataSiswa)) :
        if(dataSiswa[i]['Nama'] == inputData):
          print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
          break
        else:
          print('Data Siswa Tidak Ditemukan!')
  
  while True:
    pilihanData = input('\n---- Record Data Siswa ----\n\nList Menu: \n1. Menampilkan Data Semua Siswa \n2. Menampilkan Data Siswa Berdasarkan Nama / Nisn \n3. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-3]: ')

    if(pilihanData == '1'):
      menampilkanSemuaSiswa()
    elif(pilihanData == '2'):
      menampilkanSiswaTertentu()
    elif(pilihanData == '3'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

def menambahDataSiswa():
  def addSiswaRecord():
    nisnSiswa = input('Masukkan Nisn Siswa: ')

    # jika nisn tidak angka maka akan diulang
    while(not nisnSiswa.isdigit()):
      print('NISN Harus Angka! Masukkan NISN Ulang!')
      nisnSiswa = input('Masukkan Nisn Siswa: ')

    #validasi nisn agar tidak ada yang sama
    for i in range(len(dataSiswa)):
      if(dataSiswa[i]['Nisn'] == nisnSiswa):
        print('*****Nisn Siswa Sudah Terdaftar!*****')
        return

    namaSiswa = input('Masukkan Nama Siswa: ')
    alamatSiswa = input('Masukkan Alamat Siswa: ')
    tanggalLahirSiswa = input('Masukkan Tanggal Lahir Siswa: ')

    # split data siswa untuk capitalize sebelum append ke directory
    namaSiswa = namaSiswa.split()
    for i in range(len(namaSiswa)):
      namaSiswa[i] = namaSiswa[i].capitalize()
    namaSiswa = ' '.join(namaSiswa)

    # split alamat untuk capitalize sebelum append ke directory
    alamatSiswa = alamatSiswa.split()
    for i in range(len(alamatSiswa)):
      alamatSiswa[i] = alamatSiswa[i].capitalize()
    alamatSiswa = ' '.join(alamatSiswa)

    # check apakah ingin menambahkan data siswa
    checker = input('Apakah anda ingin menambahkan data siswa? [Y/N]: ')

    #jika memilih selain N dan Y maka akan diulang
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda ingin menambahkan data siswa? [Y/N]: ')
      if(checker == 'N'):
        return

    dataSiswa.append({
      'Nisn': nisnSiswa,
      'Nama': namaSiswa,
      'Alamat': alamatSiswa,
      'Tanggal Lahir': tanggalLahirSiswa
    })

    print('---Data Siswa Berhasil Ditambahkan!---')

  while True:
    pilihanData = input('\n---- Menambahkan Data Siswa ----\n\nList Menu: \n1. Menambah Data Siswa \n2. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-2]: ')

    if(pilihanData == '1'):
      addSiswaRecord()
    elif(pilihanData == '2'):
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