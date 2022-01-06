class Wohnung(object):
    def __init__(self, kaufpreis:float=None,kaltmiete:float=None, gebuehren:[float]=None, zusatzkosten:float=None, ruecklagen:float=None):

        self.netto_monat = kaltmiete
        self.kaufpreis = kaufpreis
        self.kosten_jahr = ruecklagen * 12

        self.netto_kalt_jahr = self.netto_monat * 12
        self.kaufpreis_ges = self.kaufpreis + sum([kaufpreis * i for i in gebuehren]) + zusatzkosten

        self.gew_monat = self.netto_monat - self.kosten_jahr/12
        self.gew_jahr  = self.netto_kalt_jahr - self.kosten_jahr

    def mietpreismultiplikator(self):
        return round(self.kaufpreis_ges / self.netto_kalt_jahr,2)

    def nettomietrendite(self):
        return round((self.netto_kalt_jahr - self.kosten_jahr) * 100 / self.kaufpreis_ges,2)

    def bruttomietrendite(self):
        return round((self.netto_kalt_jahr) * 100 / self.kaufpreis, 2)

    def report(self):
        print(f"Netto Gewinn Monat: {self.gew_monat} € [vor Steuern]")
        print(f"Netto Gewinn Jahr: {self.gew_jahr} €")
        print(f"Brutto Rendite: {self.bruttomietrendite()} %")
        print(f"Netto Rendite: {self.nettomietrendite()} %")
        print(f"Mietpreismultiplikator: {self.mietpreismultiplikator()} ")