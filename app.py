class Pul:
    def __init__(self, reng):
        self.reng = reng

    def hərəkət_et(self):
        raise NotImplementedError("Alt siniflərdə bu metod tətbiq olunmalidir.")


class Şah(Pul):
    def __init__(self, reng):
        super().__init__(reng)

    def hərəkət_et(self):
        return "Şah hərəkət edir."


class top(Pul):
    def __init__(self, reng):
        super().__init__(reng)

    def hərəkət_et(self):
        return "Top hərəkət edir."


class Fil(Pul):
    def __init__(self, reng):
        super().__init__(reng)

    def hərəkət_et(self):
        return "Fil hərəkət edir."



şah1 = Şah("Ağ")
top1 = top("Qara")
fil1 = Fil("Ağ")


print(şah1.hərəkət_et()) 
print(top1.hərəkət_et())  
print(fil1.hərəkət_et())  
