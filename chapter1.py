def creationOrder():
    print("1.\tBase Attributes")
    print("2.\tBody")
    print("3.\tSocial")
    print("4.\tAdvantages")
    print("5.\tDisadvantages")
    print("6.\tSkills")


def showPC(pc):
    print(pc.name)
    for title, a in pc.attributes.items():
        print("{} {}[{}]\t{}".format(title, a.value, a.countCost(), a.valueDesc()))

    a = pc.attributes["ST"]
    print("Thrust {}d+{}[{}]".format(a.getThrustDice(), a.getTrustModifier(), a.thrust()))
    print("Swing  {}d+{}[{}]".format(a.getSwingDice(), a.getSwingModifier(), a.swing()))
    print("BL {} p. = {} kg.".format(a.BL(), a.BL()/2))
    print("HP {}[{}]".format(pc.HP.getValue(), pc.HP.getCost()))
    print("Will {}[{}]".format(pc.Will.getValue(), pc.Will.getCost()))
    print("Perc {}[{}]".format(pc.Perc.getValue(), pc.Perc.getCost()))


def main():
    creationOrder()

    import dice
    import pc
    import testPC

    p = pc.PlayerCharacter("Random")
    p.setST(dice.d(3))
    p.attributes["DX"].value = dice.d(3)
    p.attributes["IQ"].value = dice.d(3)
    p.attributes["HT"].value = dice.d(3)
    p.HP.modifier = dice.d(modifier=-3)
    p.Will.modifier = dice.d(modifier=-2)
    p.Perc.modifier = dice.d(modifier=-2)

    players = [
        pc.PlayerCharacter(),
        p,
        testPC.TestCharacter(),
    ]

    for pl in players:
        print("-"*80)
        showPC(pl)

    # print("{}({}): {}".format(p.ST.value, p.ST.valueDesc(), p.ST.countCost()))
    # print("{}({}): {}".format(p.DX.value, p.DX.valueDesc(), p.DX.countCost()))
    # print("{}({}): {}".format(p.IQ.value, p.IQ.valueDesc(), p.IQ.countCost()))
    # print("{}({}): {}".format(p.HT.value, p.HT.valueDesc(), p.HT.countCost()))

    print("-"*80)


if __name__ == "__main__":
    main()
