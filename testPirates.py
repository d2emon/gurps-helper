def savePC(session):
    import pc
    from pirates.pc import Default, Monk

    rooster = [
        Monk(),
        Default(),
    ]

    for c in rooster:
        print(c)
        print("ST\t{}".format(c.attributes["ST"]))
        print("DX\t{}".format(c.attributes["DX"]))
        print("IQ\t{}".format(c.attributes["IQ"]))
        print("HT\t{}".format(c.attributes["HT"]))
        pc.save(c, session)
    return rooster


def main():
    import sqlalchemy
    print("Версия SQLAlchemy:", sqlalchemy.__version__)
    print("="*80)

    import db
    e, s = db.connect(True)

    import pc
    s.query(pc.PlayerCharacter).delete()
    s.commit()

    rooster = savePC(s)

    import sqlalchemy.orm.exc
    try:
        c = pc.load(s, 10)
        r = c.fill(s, 10)
        print(r)
    except sqlalchemy.orm.exc.NoResultFound:
        print("No result")

    chars = [pc.load(s, c.id) for c in rooster]
    for c in chars:
        print("="*80)
        c.afterLoad()

        thrust = c.attributes["ST"].thrust()
        swing = c.attributes["ST"].swing()

        print("-"*80)
        print("LOAD:")
        print(c)

        print("ST\t{}".format(c.attributes["ST"]))
        print("DX\t{}".format(c.attributes["DX"]))
        print("IQ\t{}".format(c.attributes["IQ"]))
        print("HT\t{}".format(c.attributes["HT"]))

        print("Thrust\t{}".format(thrust))
        print("Swing\t{}".format(swing))

        print("-"*80)
        print("SAVED:")
        print(c)

        print("="*80)

    print("ST\t{}".format(chars[0].attributes["ST"]))
    print("DX\t{}".format(chars[0].attributes["DX"]))
    print("IQ\t{}".format(chars[0].attributes["IQ"]))
    print("HT\t{}".format(chars[0].attributes["HT"]))


if __name__ == "__main__":
    main()
