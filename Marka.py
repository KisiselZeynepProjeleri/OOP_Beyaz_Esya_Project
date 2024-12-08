class Base:
    def __init__(self,ürün_id=0,ürün_ismi=""):
        self.ürün_id=ürün_id
        self.ürün_ismi=ürün_ismi

    def ürün_kaydet(self):
        #kullanıcıdan id ve isim bilgilerini alır ve sınıfın özelliklerine atar.
        self.ürün_id=int(input("ürün id:"))
        self.ürün_ismi=input("ürün ismi:")    

class Urun(Base):
    def __init__(self, ürün_id=0, ürün_ismi="",ürün_fiyatı=0):
        super().__init__(ürün_id, ürün_ismi)
        self.ürün_fiyatı=ürün_fiyatı
    
    def ürün_kaydet(self):
        super().ürün_kaydet()
        self.ürün_fiyatı=float(input("ürün fiyatı:"))
    
    def ürün_silme(self,ürün_listesi:list):
        #parametre olarak verilen ürün listesini siler
        for i in ürün_listesi:
            print(f"{i.ürün_id} IDsi olan ismi {i.ürün_ismi}")

            #silmesini istediğimiz ürünlerin id'sini alalım
            id=int(input("silinecek id: "))
            #liste üzerinde gezinerek silinecek ürünü bulup kaldıralım
            for i in ürün_listesi:
                if (i.ürün_id==id):
                    ürün_listesi.remove(i)
    
    def Update(self,ürün_listesi:list):
        #parametre olarak girilmiş ürün listesini görelim

        for i in ürün_listesi:
            print(f"ID si {i.ürün_id} olan ürünün ismi: {i.ürün_ismi}")

            #güncellemek istediği ürün id'sini soralım
            id=int(input("GÜNCELLENECEK ID: "))

            #liste üzerinde gezinerek güncellenecek ürünün isim ve fiyatını kullanıcıdan alarak ürünü günceller
            for i in ürün_listesi:
                
                    i.ürün_ismi=input("YENİ ÜRÜN İSMİ: ")
                    i.ürün_fiyatı=input("GÜNCEL FİYAT: ")
                
class Kategori(Base):
    def __init__(self, ürün_tanımı=""):
        self.ürün_tanımı=ürün_tanımı
        
    def ürün_kaydet(self):
        super().ürün_kaydet()
        self.ürün_tanımı=input("ÜRÜN AÇIKLAMASI: ")

class Marka(Base):
    def __init__(self,ürün_marka=""):
        self.ürün_marka=ürün_marka
    def ürün_kaydet(self):
        super().ürün_kaydet()     
        self.ürün_marka=input("ÜRÜN MARKASI: ")

#ürün,kategori ve marka listelerini oluşturuyoruz

ürünler=[]
kategoriler=[]
markalar=[]

#örnek bir ürün oluşturarark bilgilerini kullanıcıdan alalım

ürün=Urun()
ürün.ürün_kaydet()
ürünler.append(ürün)
for i in ürünler:
    print(f"Ürün ID: {i.ürün_id}\nÜrün İsmi: {i.ürün_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")

ürün.Update(ürünler)
for i in ürünler:
 print(f"Ürün ID: {i.ürün_id}\nÜrün İsmi: {i.ürün_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")
        
