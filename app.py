class Kitab:
    def __init__(self, ad, yazar, janr):
        self.ad = ad
        self.yazar = yazar
        self.janr = janr
 

    def adi_deyisdir(self, yeni_ad):
        self.ad = yeni_ad
        print("Kitabın adı ugurlu deyisdirildi.")

    def melumatlari_goster(self):
        print(f"{self.ad} - {self.yazar}")


kitab1 = Kitab("Səfillər", "Victor Hugo", "Roman")
kitab1.melumatlari_goster()


kitab1.adi_deyisdir("Notr Dam")
kitab1.melumatlari_goster()


