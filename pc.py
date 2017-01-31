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

    def setST(self, value):
        self.attributes["ST"].value = value
