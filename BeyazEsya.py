class BeyazEsya():
    def __init__(self,marka,model,enerji,fiyat):
        self.marka=marka
        self.model=model
        self.enerji=enerji
        self.fiyat=fiyat
    def bilgileriGöster(self):
        print(f"""
        Marka:{self.marka}
        Model:{self.model}
        Enerji:{self.enerji}
        Fiyat:{self.fiyat}
        """)
beyaz_esya=BeyazEsya("samsung","abc-d","A",25000)
print(beyaz_esya)