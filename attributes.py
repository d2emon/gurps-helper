class Attribute:
    defValue = 10
    cost = 10

    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self.value = self.defValue

    def valueDesc(self):
        if self.value <= 6:
            return "Cripping"
        if self.value <= 7:
            return "Low"
        if self.value <= 9:
            return "Below Average"
        if self.value <= 10:
            return "Normal"
        if self.value <= 12:
            return "Above Average"
        if self.value <= 14:
            return "Excellent"
        return "Unbeliveable"

    def countCost(self):
        delta = self.value - self.defValue
        return delta * self.cost


class ST(Attribute):
    cost = 10

    def getThrustDice(self):
        if self.value <= 10:
            return 1
        if self.value < 40:
            return (self.value - 11) // 8 + 1
        if self.value < 60:
            return (self.value - 5) // 10 + 1
        return (self.value) // 10 + 1

    def getTrustModifier(self):
        if self.value <= 10:
            return (self.value - 11) // 2 - 1
        if self.value < 40:
            return (self.value - 11) // 2 % 4 - 1
        if self.value < 60:
            return 1 + (self.value - 40) // 10 * 5 - (self.value - 40) // 5 * (self.value // 10 - 3)
        if self.value < 70:
            return (self.value - 60) // 5 * 2 - 1
        if self.value < 100:
            return (self.value - 60) // 5 % 2 * 2
        return 0

    def thrust(self):
        import dice
        return dice.d(self.getThrustDice(), modifier=self.getTrustModifier())

    def getSwingDice(self):
        if self.value <= 10:
            return 1
        if self.value < 27:
            return (self.value - 9) // 4 + 1
        if self.value < 40:
            return (self.value - 7) // 8 + 3
        return (self.value) // 10 + 3

    def getSwingModifier(self):
        if self.value < 9:
            return (self.value - 11) // 2
        if self.value < 27:
            return (self.value - 9) % 4 - 1
        if self.value < 40:
            g = (self.value - 9) // 2 + 1
            return g % 4 - 1
        if self.value < 60:
            return (self.value - 40) // 5 % 2 * 2 - 1
        if self.value < 100:
            return (self.value - 60) // 5 % 2 * 2
        return 0

    def swing(self):
        import dice
        return dice.d(self.getSwingDice(), modifier=self.getSwingModifier())

    def BL(self):
        BL = self.value * self.value / 5

        if BL > 10:
            return int(BL)
        return BL


class DX(Attribute):
    cost = 20


class IQ(Attribute):
    cost = 20


class HT(Attribute):
    cost = 10


class Secondary(Attribute):
    def __init__(self, Primary, modifier=0):
        Attribute.__init__(self, value=Primary.value + modifier)

        self.Primary = Primary
        self.modifier = modifier

    def getValue(self):
        return self.Primary.value + self.modifier

    def getCost(self):
        return self.modifier * self.cost


class HP(Secondary):
    cost = 2


class Will(Secondary):
    cost = 5


class Perc(Secondary):
    cost = 5
