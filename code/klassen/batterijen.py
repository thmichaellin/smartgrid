class Batterijen:
    
    def __init__(self, i, x, y, capaciteit) -> None:
        """Neemt gegevens van batterijen uit district en slaat het op in batterij object."""

        self.batterij_id = i
        self.x_as = x
        self.y_as = y
        self.capaciteit = capaciteit
        self.resterende_capaciteit = capaciteit
        self.gelinkte_huizen = []
        self.afstand_huizen = {} 

    # def delink_output(self, huis):
    #     self.resterende_capaciteit -= huis.maxoutput
    #     nieuwe_lijst = set(self.gelinkte_huizen) - set(huis)
    #     self.gelinkte_huizen = list(nieuwe_lijst)

    def bereken_afstand(self, huizen) -> None:
        """Berekent afstand van batterijen tot huizen."""

        # itereer over ongekoppelde huizen, voeg deze toe aan dictionary en geef afstand tot batterij als waarde mee
        for huis in huizen:
            afstand = abs(huis.x_as - self.x_as) + abs(huis.y_as - self.y_as)
            self.afstand_huizen[huis.huis_id] = afstand
     

    def dichtstbijzijnde_huis(self) -> int:
        """Neemt het dichtstbijzijnde huis vanaf een batterij."""

        afstand = self.afstand_huizen
        return min(afstand, key=afstand.get)
    
    def update_verbruik(self, output) -> None:
        """Update de resterende capaciteit van de batterij na het aansluiten van een huis."""

        self.resterende_capaciteit -= output
