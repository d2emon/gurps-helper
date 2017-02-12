def main():
    import sqlalchemy
    print("Версия SQLAlchemy:", sqlalchemy.__version__)
    print("="*80)

    import db
    e, s = db.connect()

    import pirates.pc as pc

    c = pc.Monk()

    import sqlalchemy.orm.exc
    try:
        r = c.fill(s, 10)
        print(r)
    except sqlalchemy.orm.exc.NoResultFound:
        print("No result")

    c.load(s, 1)
    c.save(s)

    thrust = c.attributes["ST"].thrust()
    swing = c.attributes["ST"].swing()

    print("-"*80)
    print("LOAD:")
    print("#{}\t{}".format(c.record.id, c.record))
    print("Thrust\t{}".format(thrust))
    print("Swing\t{}".format(swing))


    print("-"*80)
    print("SAVED:")
    print("#{}\t{}".format(c.record.id, c.record))


if __name__ == "__main__":
    main()
