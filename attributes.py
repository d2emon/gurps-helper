class Attribute:
    defValue = 10
    cost = 10

    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self.value = self.defValue

    def getValue(self):
        return self.value

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

    def successRoll(self, modifier=0):
        modified = self.value + modifier

        import dice
        roll = dice.d(3)

        import logging
        logging.debug("%d vs. %d [%d(%d)]", roll, modified, self.value, modifier)
        return roll <= modified


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

    def pickUp(self):
        return self.BL() * 2

    def liftHead(self):
        return self.BL() * 8

    def maxWeight(self, loadClass):
        return self.BL() * (1 + loadClass * loadClass)

    def moveMdf(self, loadClass):
        return 1 - loadClass * 0.2

    def dodgeMdf(self, loadClass):
        return -loadClass


class DX(Attribute):
    cost = 20


class IQ(Attribute):
    cost = 20


class HT(Attribute):
    cost = 10


class Secondary(Attribute):
    def __init__(self, Primary, modifier=0):
        Attribute.__init__(self, value=Primary.getValue() + modifier)

        self.Primary = Primary
        self.modifier = modifier

    def getValue(self):
        return self.Primary.getValue() + self.modifier

    def countCost(self):
        return self.modifier * self.cost


class HP(Secondary):
    cost = 2


class Will(Secondary):
    cost = 5


class Perc(Secondary):
    cost = 5


class FP(Secondary):
    cost = 3


class BS(Attribute):
    cost = 20

    def __init__(self, DX=None, HT=None, modifier=0):
        Attribute.__init__(self, value=(DX.value + HT.value) / 4 + modifier)

        self.Primaries = [DX, HT]
        self.modifier = modifier

    def getValue(self):
        s = 0
        for i in self.Primaries:
            s += i.value
        return s / 4 + self.modifier

    def countCost(self):
        return self.modifier * self.cost

    def dodge(self):
        return int(self.getValue()) + 3


class Move(Secondary):
    cost = 5

    def getValue(self):
        return int(self.Primary.getValue()) + self.modifier