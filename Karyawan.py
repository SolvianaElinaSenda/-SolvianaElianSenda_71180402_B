class Karyawan:
    _nama=""
    _umur=None
    _jenisKelamin=""
    _upahPerHari=None

    #Constructor 
    def __init__(self,nama,umur):
        self._nama=nama
        self._umur=umur
    # Getter
    def getNama(self):
        return self._nama
    def getUmur(self):
        return self._umur
    def getJenisKelamin(self):
        return self._jenisKelamin
    def getUpahPerHari(self):
        return self._upahPerHari
    # setter

    def setNama(self,nama):
        self._nama=nama
    def setUmur(self,umur):
        self._umur=umur
    def setJenisKelamin(self,jenisKelamin):
        self._jenisKelamin=jenisKelamin
    def setUpahPerHari(self,upahPerHari):
        self._upahPerHari=upahPerHari
    
    #Fungsi Printinfo
    def printInfo(self):
        print("========INFO========")
        print("Nama: ",self.getNama())
        print("Umur: ",self.getUmur())
        print("Jenis Kelamin: ",self.getJenisKelamin())
        print("Upah Per Hari: ",self.getUpahPerHari())
    #Fungsi hitungGajiBulanan
    def hitungGajiBulanan(self,_hariKerja):
        if _hariKerja <=0:
            print("Error!! Upah Perhari Belum Diinputkan")
        else:
            self._upahPerHari * _hariKerja

#test case
if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()
    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()
    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)
        
