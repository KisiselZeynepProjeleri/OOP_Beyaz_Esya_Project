from BeyazEsya import BeyazEsya

class Buzdolabı(BeyazEsya):
    def __init__(self,marka,model,enerji,fiyat,hacim,kapak_sayısı):
        super().__init__(marka,model,enerji,fiyat)
        self.hacim=hacim
        self.kapak_sayısı=kapak_sayısı
    def bilgileriGöster(self):
        super().bilgileriGöster()
        print(f"""
            Hacim:{self.hacim}
            Kapak sayısı:{self.kapak_sayısı}
        """)

buzdolabı=Buzdolabı("beko","dn123","A++",30000,350,2)
buzdolabı.bilgileriGöster()