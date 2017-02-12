def connect():
    dbAddr = "sqlite:///db/gurps.db"

    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///db/gurps.db", echo=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    return engine, Session()
