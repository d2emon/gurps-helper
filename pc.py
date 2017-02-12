from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy import event

Base = declarative_base()

import attributes


class PlayerCharacter(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Unicode)
    st = Column(Integer, default=10)
    dx = Column(Integer, default=10)
    iq = Column(Integer, default=10)
    ht = Column(Integer, default=10)
    attributes = {
        "ST": attributes.HT(),
        "DX": attributes.DX(),
        "IQ": attributes.IQ(),
        "HT": attributes.HT(),
    }

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

        self.st = self.attributes["ST"]
        self.dx = self.attributes["DX"]
        self.iq = self.attributes["IQ"]
        self.ht = self.attributes["HT"]

    def __repr__(self):
        return "<User#{}\t'{}'>".format(self.id, self.name)

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

    def beforeSave(self):
        self.st = self.attributes.get("ST", 10).getValue()
        self.dx = self.attributes.get("DX", 10).getValue()
        self.iq = self.attributes.get("IQ", 10).getValue()
        self.ht = self.attributes.get("HT", 10).getValue()

    def afterLoad(self):
        self.setST(self.st)

        self.attributes = {
            "ST": attributes.ST(),
            "DX": attributes.DX(),
            "IQ": attributes.IQ(),
            "HT": attributes.HT(),
        }
        self.attributes["DX"].value = self.dx
        self.attributes["IQ"].value = self.iq
        self.attributes["HT"].value = self.ht


@event.listens_for(PlayerCharacter, 'before_insert')
@event.listens_for(PlayerCharacter, 'before_update')
def receive_before_insert(mapper, connection, target):
    print("INSERT")
    print(mapper)
    print(connection)
    print(target)


# event.listen(PlayerCharacter, 'before_insert', receive_before_insert)
# event.listen(PlayerCharacter, 'before_update', receive_before_insert)


def save(pc, session):
    pc.beforeSave()
    print("BEFORE SAVE")
    session.add(pc)
    session.flush()
    # session.commit()
    print("+"*80)


def load(session, id):
    return session.query(PlayerCharacter).filter_by(id=id).one()
