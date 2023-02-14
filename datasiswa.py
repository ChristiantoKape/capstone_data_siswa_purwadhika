dataSiswa = [
]

def hasil(i):
    print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')
    print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))

def menampilkanSemuaSiswa():
  print('--- Daftar Siswa ---\n')
  if (len(dataSiswa) == 0):
    print('\t\tTidak Ada Data Siswa!')

  for i in range(len(dataSiswa)) :
    hasil(i)

def menampilkanSiswaTertentu():
  inputData = input('Masukkan Nisn/Nama Siswa: ')
  if(inputData.isdigit()):
    for i in range(len(dataSiswa)) :
      if(dataSiswa[i]['Nisn'] == inputData):
        print('--- Data Siswa ---\n')
        hasil(i)
        break
      else:
        print('Data Siswa Tidak Ditemukan!')
  else:
    for i in range(len(dataSiswa)) :
      if(dataSiswa[i]['Nama'] == inputData):
        print('--- Data Siswa ---\n')
        hasil(i)
        break
      else:
        print('Data Siswa Tidak Ditemukan!')

def menampilkanDataSiwa() :  
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

def mengubahDataSiswa():
  def changeSiswaRecord():
    # input nisn siswa yang akan diubah
    inputData = input('Masukkan Nisn/Nama Siswa: ')

    # jika inputan berupa angka maka akan dicari berdasarkan nisn jika tidak ditemukan maka akan diulang inputan
    if(inputData.isdigit()):
      for i in range(len(dataSiswa)) :
        if(dataSiswa[i]['Nisn'] == inputData):
          print('--- Data Siswa ---\n')
          print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')
          print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
          break
        else:
          print('Data Siswa Tidak Ditemukan!')
          return
    else:
      for i in range(len(dataSiswa)) :
        if(dataSiswa[i]['Nama'] == inputData):
          print('--- Data Siswa ---\n')
          print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')
          print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
          break
        else:
          print('Data Siswa Tidak Ditemukan!')
          return

    # checker untuk mengecek apakah ingin mengubah data siswa
    checker = input('Apakah anda ingin mengubah data siswa? [Y/N]: ')

    #jika memilih selain N dan Y maka akan diulang
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda ingin mengubah data siswa? [Y/N]: ')
      if(checker == 'N'):
        return

    # input data baru
    nisnSiswa = input('Masukkan Nisn Siswa: ')
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

    # check apakah ingin mengubah data siswa
    checker = input('Apakah Data Sudah Benar? [Y/N]: ')

    #jika memilih selain N dan Y maka akan diulang
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah Data Sudah Benar? [Y/N]: ')
      if(checker == 'N'):
        return

    # jika input kosong menggunakan data lama siswa
    if(nisnSiswa == ''):
      nisnSiswa = dataSiswa[i]['Nisn']
    if(namaSiswa == ''):
      namaSiswa = dataSiswa[i]['Nama']
    if(alamatSiswa == ''):
      alamatSiswa = dataSiswa[i]['Alamat']
    if(tanggalLahirSiswa == ''):
      tanggalLahirSiswa = dataSiswa[i]['Tanggal Lahir']

    # mengubah data siswa pada directory
    dataSiswa[i]['Nisn'] = nisnSiswa
    dataSiswa[i]['Nama'] = namaSiswa
    dataSiswa[i]['Alamat'] = alamatSiswa
    dataSiswa[i]['Tanggal Lahir'] = tanggalLahirSiswa

    print('---Data Siswa Berhasil Diubah!---')

    
  while True:
    pilihanData = input('\n---- Mengubah Data Siswa ----\n\nList Menu: \n1. Mengubah Data Siswa \n2. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-2]: ')

    if(pilihanData == '1'):
      changeSiswaRecord()
    elif(pilihanData == '2'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

def menghapusDataSiswa():
  menampilkanSemuaSiswa()

  # input nisn siswa yang akan dihapus
  inputData = input('Masukkan Nisn/Nama Siswa yang Ingin di Hapus: ')

  # check apakah data siswa ada
  if(inputData.isdigit()):
    for i in range(len(dataSiswa)) :
      if(dataSiswa[i]['Nisn'] == inputData):
        print('--- Data Siswa ---\n')
        print('Nisn\t| Nama  \t\t\t\t| Alamat\t\t| Tanggal Lahir')
        print('{}\t| {} \t| {}\t| {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Alamat'],dataSiswa[i]['Tanggal Lahir']))
        break
      else:
        # jika data siswa tidak ditemukan maka mengulang input
        print('Data Siswa Tidak Ditemukan!')
        inputData = input('Masukkan Nisn/Nama siswa Dengan Benar!: ')

  # checker apakah yakin menghapus data siswa
  checker = input('Apakah anda yakin ingin menghapus data siswa? [Y/N]: ')

  #jika memilih selain N dan Y maka akan diulang
  while(checker.upper() != 'Y' and checker.upper() != 'N'):
    checker = input('Apakah anda yakin ingin menghapus data siswa? [Y/N]: ')
    if(checker == 'N'):
      return

  # menghapus data siswa
  del dataSiswa[i]
  print('---Data Siswa Berhasil Dihapus!---')

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