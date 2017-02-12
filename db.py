engine = None
dbAddr = "sqlite:///db/gurps.db"

def connect(echo=False):
    global engine, dbAddr

    if engine is None:
        from sqlalchemy import create_engine
        engine = create_engine("sqlite:///db/gurps.db", echo=echo)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    return engine, Session()
