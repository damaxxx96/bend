class Instrument:
    def __init__(self):
        self.zemlja_porekla = "Srbija"

    def __init__(self, zemlja_porekla: str):
        self.zemlja_porekla = zemlja_porekla

    def sviraj(self):
        pass

    def ispisi(self):
        pass


class Gitara(Instrument):
    def __init__(self):
        super().__init__()

    def __init__(self, zemlja_porekla: str, elektricna: bool):
        super().__init__(zemlja_porekla)
        self.elektricna = elektricna

    def sviraj(self):
        if self.elektricna == True:
            print("ZING")
        else:
            print("TING")

    def ispisi(self):
        if self.elektricna == True:
            print("Električna gitara -  Zemlja porekla: " + self.zemlja_porekla)
        else:
            print("Akustična gitara - Zemlja porekla: " + self.zemlja_porekla)


class Bubanj(Instrument):
    def __init__(self):
        super().__init__()

    def __init__(self, zemlja_porekla: str):
        super().__init__(zemlja_porekla)
        self.broj_udaraca = 0

    def sviraj(self):
        self.broj_udaraca += 1

        if self.broj_udaraca % 3 == 0:
            print("TSS")
        else:
            print("BUM")

    def ispisi(self):
        (
            "Bubanj - Zemlja porekla: "
            + self.zemlja_porekla
            + "Broj udaraca: "
            + str(self.broj_udaraca)
        )


class Bend:
    def __init__(self):
        self.naziv = "Bezimeni"

    def __init__(
        self,
        naziv: str,
        prva_gitara: Gitara,
        druga_gitara: Gitara,
        bubanj: Bubanj,
    ):
        self.naziv = naziv
        self.prva_gitara = prva_gitara
        self.druga_gitara = druga_gitara
        self.bubanj = bubanj

    def sviraj(self):
        self.prva_gitara.sviraj()
        self.druga_gitara.sviraj()
        self.bubanj.sviraj()

    def predstavi_se(self):
        self.prva_gitara.ispisi()
        self.druga_gitara.ispisi()
        self.bubanj.ispisi()
