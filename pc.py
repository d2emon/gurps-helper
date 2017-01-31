import attributes


class PlayerCharacter:
    def __init__(self, name="UNNAMED"):
        self.name = name
        self.attributes = {
            "ST": attributes.ST(),
            "DX": attributes.DX(),
            "IQ": attributes.IQ(),
            "HT": attributes.HT(),
        }
        self.HP = attributes.HP(self.attributes["ST"])
        self.Will = attributes.Will(self.attributes["IQ"])
        self.Perc = attributes.Perc(self.attributes["IQ"])
        self.FP = attributes.FP(self.attributes["HT"])
        self.BS = attributes.BS(self.attributes["DX"], self.attributes["HT"])
        self.Move = attributes.Move(self.BS)

    def setST(self, value):
        self.attributes["ST"].value = value

    def countCost(self):
        cost = 0
        for title, a in self.attributes.items():
            cost += a.countCost()
        cost += self.HP.countCost()
        cost += self.Will.countCost()
        cost += self.Perc.countCost()
        cost += self.FP.countCost()
        return cost
