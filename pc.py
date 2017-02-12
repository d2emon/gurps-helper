from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode

Base = declarative_base()

import attributes


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Unicode)
    st = Column(Integer, default=10)
    dx = Column(Integer, default=10)
    iq = Column(Integer, default=10)
    ht = Column(Integer, default=10)

    def __init__(self, name, attributes=[10, 10, 10, 10], description=""):
        self.name = name
        self.st = attributes[0]
        self.dx = attributes[1]
        self.iq = attributes[2]
        self.ht = attributes[3]
        self.description = description

    def __repr__(self):
        return "<User('{}')>".format(self.name)


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

        self.record = Character(name=self.name)

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

    def save(self, session):
        self.record.name = self.name
        self.record.ht = self.attributes.get("ST", 10).getValue()
        self.record.dx = self.attributes.get("DX", 10).getValue()
        self.record.iq = self.attributes.get("IQ", 10).getValue()
        self.record.ht = self.attributes.get("HT", 10).getValue()

        session.add(self.record)
        session.commit()

    def load(self, session, id):
        self.record = session.query(Character).filter_by(id=id).first()
