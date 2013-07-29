#! usr/bin/env python

'''
--------------------------------------------
POLITEL CONSOLE v.0.1

twitter : @adiyatmubarak
usage   : Politel.py <username> <password>
--------------------------------------------

LICENSE

Copyright (C) <2013>  <Keda87>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from urllib import urlencode
from urllib2 import urlopen
from urllib2 import URLError
from json import loads
from os import sys
from sys import argv

class Politel(object):

    login_url = "http://politekniktelkom.ac.id/politeldroid.php/main/login"
    data_url = "http://politekniktelkom.ac.id/politeldroid.php/main/index"
    param = {}

    '''
    fungsi create instance dengan parameter username & password
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    '''
    fungsi validasi login, jika {status:1} == True (login sukses)
    selain itu bernilai False (login gagal)
    '''
    def is_login_auth(self):

        self.param["nim"] = self.username
        self.param["pass"] = self.password
        self.param["tipe"] = "login"

        try:

            login_param = urlencode(self.param)
            response = urlopen(self.login_url, login_param).read()
            data = loads(response)

            if data['status'] == 1:
                return True
            else:
                print "Kombinasi username & password salah"
                return False
                sys.exit(1)

        except URLError:
            print "Terjadi kesalahan pada jaringan"
            return False
        except KeyboardInterrupt:
            print "Aborted.."
            return False
            sys.exit(1)

    '''
    fungsi menampilkan data TAK
    '''
    def fetch_tak(self):

        self.param["tipe"] = "tak"
        tak_acumulate = 0

        try:

            tak_param = urlencode(self.param)
            response = urlopen(self.data_url, tak_param).read()
            data = loads(response)

            for raw in data:
                print "+ Nama bagian   : " + raw['nama_bagian']
                print "  Jenis kegiatan: " + raw['nama_jenisKegiatan']
                print "  Poin          : " + raw['poin']
                print "  Tahun         : " + raw['TAHUN']
                print "  Semester      : " + raw['semester']
                print "  Nim           : " + raw['nim']
                print
                tak_acumulate += int(raw['poin'])
            print "[+] Total TAK: %d poin" % tak_acumulate

        except URLError:
            print "Terjadi kesalahan pada jaringan"
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

    '''
    fungsi menampilkan biodata user
    '''
    def fetch_biodata(self):

        self.param["tipe"] = "biodata"

        try:

            profile_param = urlencode(self.param)
            response = urlopen(self.data_url, profile_param).read()
            data = loads(response)

            for profil in data:
                print "Nama                    : %s" % profil['NAMA']
                print "Tempat/Tanggal lahir    : %s, %s" % (profil['TEMPAT_LAHIR'], profil['TANGGAL_LAHIR'])
                print "Alamat                  : %s - %s" % (profil['ALAMAT'], profil['KOTA'])
                print "Jenis kelamin           : %s" % profil['JENIS_KELAMIN']
                print "Golongan darah          : %s" % profil['GOLONGAN_DARAH']
                print "Warga negara            : %s" % profil['WARGA_NEGARA']
                print "Agama                   : %s" % profil['AGAMA']
                print "Nim                     : %s" % profil['NIM']
                print "Email                   : %s" % profil['EMAIL']
                print "Telepon                 : %s" % profil['TELEPON']
                print "Ayah                    : %s" % profil['AYAH']
                print "Ibu                     : %s" % profil['IBU']

        except URLError:
            print "Terjadi kesalaan pada jaringan"
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

    '''
    fungsi menampilkan nilai mentah
    '''
    def fetch_nilai_mentah(self):

        self.param['tipe'] = "nilai"

        try:

            nilai_param = urlencode(self.param)
            response = urlopen(self.data_url, nilai_param).read()
            data = loads(response)

            for score in data:
                print "+ Kelas            : %s" % score['kd_kelas']
                print "  Mata Kuliah      : %s" % score['MK']
                print "  Kode dosen       : %s" % score['kd_dosen']
                print "  Jumlah SKS       : %s" % score['sks']
                print "  Nilai            : - Dasar        : %s" % score['ndasar']
                print "                     - Menengah     : %s" % score['ntengah']
                print "                     - Mahir        : %s" % score['nmahir']
                print "  Index            : %s" % score['nilai_indek']
                print

        except URLError:
            print "Terjadi kesalahan pada jaringan"
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

    '''
    fungsi menampilkan persentase & detail kehadiran
    '''
    def fetch_absensi(self):

        self.param["tipe"] = "absensi"

        try:

            absensi_param = urlencode(self.param)
            response = urlopen(self.data_url, absensi_param).read()
            data = loads(response)

            for absen in data:
                print "Mata Kuliah  : %s" % absen['MK']
                print "Persentase   : %s : %s%s" % (int(absen['PERSENTASE']) / 2 * "#", absen['PERSENTASE'], "%")
                print "Alpa         : %s hari" % absen['ALPA']
                print "Hadir        : %s hari" % absen['HADIR']
                print "Total        : %s hari" % absen['TOTAL']
                print

        except URLError:
            print "Terjadi kesaahan pada jaringan"
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

    '''
    fungsi menampilkan data kalender akademik
    '''
    def fetch_kalender_akademik(self):

        self.param["tipe"] = "kalender"

        try:

            kalender_param = urlencode(self.param)
            response = urlopen(self.data_url, kalender_param).read()
            data = loads(response)

            for x in data:
                print "+ Nama kegiatan: " + x['KEGIATAN']
                print "  Tanggal mulai: " + x['TANGGAL_MULAI']
                print "  Tanggal akhir: " + x['TANGGAL_AKHIR']
                print "  Tahun ajaran : " + x['TAHUN_AJARAN']
                print "  Unit         : " + x['UNIT']
                print

        except URLError:
            print "Terjadi kesalahan pada jaringan"
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

    def navigation_menu(self):
        print '''
--------------------------------------------
POLITEL CONSOLE v.0.1

twitter : @adiyatmubarak
usage   : Politel.py <username> <password>
      eg: Politel.py 30123456 qwerty
--------------------------------------------

    [1] Biodata
    [2] Absensi
    [3] Nilai Mentah
    [4] TAK
    [5] Kalender Akademik
    [6] Exit
'''


other, nim, pwd = argv
politel = Politel(nim, pwd)

if politel.is_login_auth():

    while True:

        politel.navigation_menu()

        try:

            pilihan = int(raw_input('Politel Console@Pilih > '))
            print

            if pilihan == 1:
                politel.fetch_biodata()
            elif pilihan == 2:
                politel.fetch_absensi()
            elif pilihan == 3:
                politel.fetch_nilai_mentah()
            elif pilihan == 4:
                politel.fetch_tak()
            elif pilihan == 5:
                politel.fetch_kalender_akademik()
            elif pilihan == 6:
                print "Bye.."
                sys.exit(1)
            else:
                print "Menu tidak tersedia.."

        except ValueError:
            print "Bad command.."
        except KeyboardInterrupt:
            print "Aborted.."
            sys.exit(1)

else:
    print "Opps..an error occured.."