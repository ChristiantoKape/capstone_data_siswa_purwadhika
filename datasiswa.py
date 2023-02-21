dataSiswa = [
]  

def menampilkanSemuaSiswa():
  print('--- Daftar Siswa ---\n')
  if (len(dataSiswa) == 0):
    print('Tidak Ada Data Siswa!')

  for i in range(len(dataSiswa)) :
    print('Nisn: {}, Nama: {}, Kota: {}, Jenis Kelamin: {}, Tanggal Lahir: {}'.format(dataSiswa[i]['Nisn'],dataSiswa[i]['Nama'],dataSiswa[i]['Kota'],dataSiswa[i]['Jenis Kelamin'],dataSiswa[i]['Tanggal Lahir']))

def mencariDataSiswa():
  # input data siswa
  inputData = input('Masukkan Nisn Siswa: ')

  # check nisn angka atau bukan
  result = None
  for sub in dataSiswa:
    if sub['Nisn'] == inputData.capitalize():
      result = sub
      break

  print("-- Data Siswa yang Dicari --\n")
  if(result):
    print('Nisn: {}, Nama: {}, Kota: {}, Jenis Kelamin: {}, Tanggal Lahir: {}'.format(result['Nisn'],result['Nama'],result['Kota'],result['Jenis Kelamin'],result['Tanggal Lahir']))
  else:
    print('Tidak Ada Data Siswa!')

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
    alamatSiswa = input('Masukkan Kota Siswa: ')
    jenisKelamin = input('Masukkan Jenis Kelamin Siswa: ')
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

    # split jenis kelamin untuk capitalize sebelum append ke directory
    jenisKelamin = jenisKelamin.split()
    for i in range(len(jenisKelamin)):
      jenisKelamin[i] = jenisKelamin[i].capitalize()
    jenisKelamin = '-'.join(jenisKelamin)

    # check apakah ingin menambahkan data siswa
    checker = input('Apakah anda ingin menambahkan data siswa? [Y/N]: ')

    #jika memilih selain N dan Y maka akan diulang
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda ingin menambahkan data siswa? [Y/N]: ')
    
    if(checker.upper() == 'N'):
      print('---Data Siswa Gagal Ditambahkan!---')
    else:
      dataSiswa.append({
        'Nisn': nisnSiswa,
        'Nama': namaSiswa,
        'Kota': alamatSiswa,
        'Jenis Kelamin': jenisKelamin,
        'Tanggal Lahir': tanggalLahirSiswa
      })
      print('---Data Siswa Berhasil Ditambahkan!---')

def changeDataSiswa():
  menampilkanSemuaSiswa()

  if(len(dataSiswa) == 0):
    return

  inputData = input('Masukkan Nisn Siswa yang Ingin di Ubah: ')

  res = None
  for sub in dataSiswa:
      if sub['Nisn'] == inputData:
          res = sub
          break

  if(res == None):
    print('Tidak Ada Data Siswa!')
    return
  else:
    print("-- Data Siswa yang Dicari --\n")
    print('Nisn: {}, Nama: {}, Kota: {}, Jenis Kelamin: {}, Tanggal Lahir: {}'.format(res['Nisn'],res['Nama'],res['Kota'],res['Jenis Kelamin'],res['Tanggal Lahir']))
    
  checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')

  while(checker.upper() != 'Y' and checker.upper() != 'N'):
    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
  
  if(checker.upper() == 'N'):
    return

  inputData = input('Masukkan Kolom yang Ingin di Ubah: ')

  inputData = inputData.split()
  for i in range(len(inputData)):
    inputData[i] = inputData[i].capitalize()
  inputData = ' '.join(inputData)

  if(inputData == 'Nisn'):
    nisnSiswa = input('Masukkan Nisn Siswa: ')

    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')

    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
      
    if(checker.upper() == 'N'):
      print('---Data NISN Gagal Diubah!---')
      return
    else:
      res['Nisn'] = nisnSiswa
      print('---Data NISN Berhasil Diubah!---')

  elif(inputData == 'Nama'):
    namaSiswa = input('Masukkan Nama Siswa: ')

    namaSiswa = namaSiswa.split()
    for i in range(len(namaSiswa)):
      namaSiswa[i] = namaSiswa[i].capitalize()
    namaSiswa = ' '.join(namaSiswa)

    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')

    if(checker.upper() == 'N'):
      print('---Data Nama Gagal Diubah!---')
      return
    else:
      res['Nama'] = namaSiswa
      print('---Data Nama Berhasil Diubah!---')

  elif(inputData == 'Kota'):
    alamatSiswa = input('Masukkan Kota Siswa: ')

    alamatSiswa = alamatSiswa.split()
    for i in range(len(alamatSiswa)):
      alamatSiswa[i] = alamatSiswa[i].capitalize()
    alamatSiswa = ' '.join(alamatSiswa)

    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    
    if(checker.upper() == 'N'):
      print('---Data Kota Gagal Diubah!---')
      return
    else:
      res['Kota'] = alamatSiswa
      print('---Data Kota Berhasil Diubah!---')

  elif(inputData == 'Jenis Kelamin'):
    jenisKelamin = input('Masukkan Jenis Kelamin Siswa: ')

    jenisKelamin = jenisKelamin.split()
    for i in range(len(jenisKelamin)):
      jenisKelamin[i] = jenisKelamin[i].capitalize()
    jenisKelamin = '-'.join(jenisKelamin)

    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    
    if(checker.upper() == 'N'):
      print('---Data Jenis Kelamin Gagal Diubah!---')
      return
    else:
      res['Jenis Kelamin'] = jenisKelamin
      print('---Data Jenis Kelamin Berhasil Diubah!---')

  elif(inputData == 'Tanggal Lahir'):
    tanggalLahirSiswa = input('Masukkan Tanggal Lahir Siswa: ')

    tanggalLahirSiswa = tanggalLahirSiswa.split()
    for i in range(len(tanggalLahirSiswa)):
      tanggalLahirSiswa[i] = tanggalLahirSiswa[i]
    tanggalLahirSiswa = ' '.join(tanggalLahirSiswa)

    checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')
    while(checker.upper() != 'Y' and checker.upper() != 'N'):
      checker = input('Apakah anda yakin ingin mengubah data siswa? [Y/N]: ')

    if(checker.upper() == 'N'):
      print('---Data Tanggal Lahir Gagal Diubah!---')
      return
    else:
      res['Tanggal Lahir'] = tanggalLahirSiswa
      print('---Data Tanggal Lahir Berhasil Diubah!---')

def menampilkanDataSiwa() :
  while True:
    pilihanData = input('\n---- Record Data Siswa ----\n\nList Menu: \n1. Menampilkan Data Semua Siswa \n2. Mencari Data Sesuai Nisn Siswa \n3. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-2]: ')

    if(pilihanData == '1'):
      menampilkanSemuaSiswa()
    elif(pilihanData == '2'):
      mencariDataSiswa()
    elif(pilihanData == '3'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

def menambahDataSiswa():
  while True:
    pilihanData = input('\n---- Menambahkan Data Siswa ----\n\nList Menu: \n1. Menambah Data Siswa \n2. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-2]: ')

    if(pilihanData == '1'):
      addSiswaRecord()
    elif(pilihanData == '2'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

def mengubahDataSiswa():        
  while True:
    pilihanData = input('\n---- Mengubah Data Siswa ----\n\nList Menu: \n1. Mengubah Data Siswa \n2. Kembali ke Menu Utama \nSilahkan Pilih Sub-Menu [1-2]: ')

    if(pilihanData == '1'):
      changeDataSiswa()
    elif(pilihanData == '2'):
      break
    else:
      print('*****Pilihan yang anda masukkan salah!*****')

def menghapusDataSiswa():
  menampilkanSemuaSiswa()

  if(len(dataSiswa) == 0):
    return

  inputData = input('Masukkan Nisn Siswa yang Ingin di Hapus: ')

  res = None
  for sub in dataSiswa:
      if sub['Nisn'] == inputData:
          res = sub
          break

  if(res == None):
    print('Tidak Ada Data Siswa!')
    return
  else:
    print("-- Data Siswa yang Dicari --\n")
    print('Nisn: {}, Nama: {}, Kota: {}, Jenis Kelamin: {}, Tanggal Lahir: {}'.format(res['Nisn'],res['Nama'],res['Kota'],res['Jenis Kelamin'],res['Tanggal Lahir']))

  checker = input('Apakah anda yakin ingin menghapus data siswa? [Y/N]: ')

  while(checker.upper() != 'Y' and checker.upper() != 'N'):
    checker = input('Apakah anda yakin ingin menghapus data siswa? [Y/N]: ')
  
  if(checker.upper() == 'N'):
    print('---Data Siswa Gagal Dihapus!---')
    return
  else:
    del dataSiswa[dataSiswa.index(res)]
    print('---Data Siswa Berhasil Dihapus!---')

while True:
  pilihanMenu = input('\n---- Record Data Siswa ----\n\nList Menu: \n1. Menampilkan Data Siswa \n2. Menambah Data Siswa \n3. Mengubah Data Siswa \n4. Menghapus Data Siswa \n5. Exit Program \nSilahkan Pilih Menu [1-5]: ')

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