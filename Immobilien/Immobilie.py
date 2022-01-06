class Wohnung(object):
    def __init__(self, kaufpreis:float=None,kaltmiete:float=None, gebuehren:[float]=None, zusatzkosten:float=0, hausgeld:float=None):
        self.netto_monat = kaltmiete
        self.kaufpreis = kaufpreis
        self.kosten_jahr = hausgeld * 12

        self.netto_kalt_jahr = self.netto_monat * 12
        self.kaufpreis_ges = self.kaufpreis + sum([kaufpreis * i for i in gebuehren]) + zusatzkosten

        self.gew_monat = self.netto_monat - hausgeld
        self.gew_jahr  = self.netto_kalt_jahr - self.kosten_jahr

    def mietpreismultiplikator(self):
        """ Der Mietpreismultiplikator gibt an, wie viele Jahresnettokaltmieten erfordelich sind um die Immobilie zu finanzieren.
        :return: Mietpreismultiplikator [float]
        """
        return round(self.kaufpreis_ges / self.netto_kalt_jahr,2)

    def nettomietrendite(self):
        """ Die Nettomietrendite zwigt an, wie hoch die Rendite unter Berücksichtigung der Werwerbsnebenkoste, Instanhaltungsrücklagen
            und Verwaltungs/ nicht umlegbaren Nebenkosten ausfällt.
        :return: Nettomietrendite in Prozent pro Jahr
        """
        return round((self.netto_kalt_jahr - self.kosten_jahr) * 100 / self.kaufpreis_ges,2)

    def bruttomietrendite(self):
        """ Verhältnis der jährlichen Bruttokaltmiete zum Kaufpreis.
        :return: Bruttomietrendite in Prozent pro Jahr
        """
        return round((self.netto_kalt_jahr) * 100 / self.kaufpreis, 2)

    def report(self):
        print(f"Netto Gewinn Monat: {self.gew_monat} € [vor Steuern]")
        print(f"Netto Gewinn Jahr:  {self.gew_jahr} €")
        #print(f"Brutto Rendite: {self.bruttomietrendite()} %")
        print("__________________________________________________________")
        print(f"Netto Rendite: {self.nettomietrendite()} %", "| Idealwert: 3.5-4 %")
        print("__________________________________________________________")
        print(f"Mietpreismultiplikator: {self.mietpreismultiplikator()} ", "| Standartwert: 25.0 ")