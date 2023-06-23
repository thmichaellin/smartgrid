import copy
from code.klassen.district import Wijk
from .random_alg import random_alg

class Hill_climber:
    
    def __init__(self, wijk: Wijk) -> None:
        """Maak een hill_climber aan."""
        self.oude_wijk = wijk
        self.kosten = wijk.kosten_berekening()
        self.nieuwe_wijk = wijk

        self.counter = 0


    def check_uitkomst(self) -> None:
        """Checkt of the nieuwe staat goedkoper is dan de oude staat.
        zo ja, nieuwe staat = oude staat."""
        nieuwe_kosten = self.nieuwe_wijk.kosten_berekening()
        oude_kosten = self.kosten
        
        if nieuwe_kosten < oude_kosten:
            self.oude_wijk = self.nieuwe_wijk
            self.kosten = nieuwe_kosten
            self.counter = 0
            self.nieuwe_wijk = copy.deepcopy(self.oude_wijk)
        else: 
            self.counter += 1
            
    
    def draai_hillclimber(self) -> Wijk:
        """Run hill climber algoritme totdat de counter bereikt is."""
        while self.counter < 150:
            if self.nieuwe_wijk.hill_climber():
                self.check_uitkomst()
        self.oude_wijk.herleg_alle_kabels()
        return self.oude_wijk

def hillclimber_alg(wijk):
    wijk_kopie = copy.deepcopy(wijk)
    random_wijk = random_alg(wijk_kopie)
    hillclimber = Hill_climber(random_wijk)
    nieuw_wijk = hillclimber.draai_hillclimber()
    return nieuw_wijk
