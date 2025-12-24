class Stelezhka:
    def __init__(self, kod_stelezhki, nomer, kolichestvo_yacheek, dopustimaya_massa):
        self.kod_stelezhki = kod_stelezhki
        self.nomer = nomer
        self.kolichestvo_yacheek = kolichestvo_yacheek
        self.dopustimaya_massa = dopustimaya_massa
        self.zanyatye_yacheiki = set()
        self.obschaya_massa = 0.0