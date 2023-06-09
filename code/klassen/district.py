from .batterijen import Batterijen
from .huizen import Huizen
from typing import TextIO
import os


class District:

    def __init__(self, district: int) -> None:
        """Laad een wijk in aan de hand van opgegeven getal.

        In: wijknummer."""

        self.districtnummer = district
        self.batterijen = []
        self.losse_huizen = []
        self.gelinkte_huizen = []


        self.laad_batterijen(self.data_pad(district, 'batteries'))
        self.laad_huizen(self.data_pad(district, 'houses'))
        
        for batterij in self.batterijen:
            batterij.afstand_berekenen(self.losse_huizen)

    def laad_batterijen(self, bestand: str) -> None:
        """Neemt data van bestand en maakt daarmee batterijobjecten.
        deze worden ongebracht in batterijlijst.

        In: CSV bestand"""

    # neemt file eindigend op batteries.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan batterij-lijst toe.
                if data[0].isnumeric():
                    self.batterijen.append(Batterijen(i, int(data[0]), int(data[1]), float(data[2])))

    def laad_huizen(self, bestand: str) -> None:
        """Neemt data van bestand en maakt daarna huisobjecten.
        Deze worden ondergebracht in huislijst.

        In: CSV bestand"""    

        # neemt file eindigend op houses.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.losse_huizen.append(Huizen(i, int(data[0]), int(data[1]), float(data[2])))

    def data_inladen(self, b: TextIO):
        """Neemt bestandlijn en converteert het naar een lijst.

        In: CSV bestand.
        Uit: lijst met 3 variabelen."""

        line = b.readline()
        line = line.replace("\n", '')
        line = line.replace('\"','')

        return line.split(",")
    
    def data_pad(self, district, item) -> str:
        """Vind het juist bestandspad naar opgevraagde bestand.

        In: bestaandsnaam
        Uit: pad naar opgevraagde bestand."""

        cwd = os.getcwd()

        # hoofdfolder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # district_map = os.path.join(hoofdfolder, 'Huizen&Batterijen', f'district_{self.districtnummer}')
        # bestandnaam = f'district-{self.districtnummer}_{naam}.csv'
        sep = os.sep
        pad = f'{sep}Huizen&Batterijen{sep}district_{district}{sep}district-{district}_{item}.csv'
        return cwd + os.path.normpath(pad)

    def link_huis(self, id):
        for huis in self.losse_huizen:
            if huis.huis_id == id:
                self.losse_huizen.remove(huis)
                self.gelinkte_huizen.append(huis)
                huis.linked = True
                break


                    
    # def vind_los_huis(self, id):
    #     """Returnt een ongekoppeld huis."""
    #     for huis in self.losse_huizen:
    #         if huis.huis_id == id:
    #             return huis

    def creer_connectie(self, batterij, huis):
        huis.linked = True
        batterij.update_usage(huis.maxoutput)
        batterij.gelinkte_huizen.append(huis)

    def route_cable(self, batterij, huis):
        cursor_x, cursor_y = batterij.x_as, batterij.y_as
        while cursor_x < huis.x_as:
            huis.lay_cable((cursor_x), (cursor_y))
            cursor_x += 1
        while cursor_x > huis.x_as:
            huis.lay_cable((cursor_x), (cursor_y))
            cursor_x -= 1
        while cursor_y < huis.y_as:
            huis.lay_cable((cursor_x), (cursor_y))
            cursor_y += 1
        while cursor_y > huis.y_as:
            huis.lay_cable((cursor_x), (cursor_y))
            cursor_y -= 1
        huis.lay_cable((cursor_x), (cursor_y))
        self.creer_connectie(batterij, huis)