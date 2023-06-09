from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

animal_feed = Table(
    'animal_feed', Base.metadata,
    Column("animal_id", Integer(), ForeignKey("animal.id")),
    Column("feed_id", Integer(), ForeignKey("feed.id"))
)


class Animal(Base):
    __tablename__ = "animal"

    id = Column(Integer, primary_key=True, autoincrement=True)

    animal_name = Column(String(128))
    date_of_birth = Column(Date(), default=datetime.now)
    gender = Column(String(128))

    kind_animal_id = Column(Integer, ForeignKey("kind_animal.id"))
    feeds = relationship("Feed", secondary=animal_feed, backref=backref('animals'))


class KindAnimal(Base):
    __tablename__ = "kind_animal"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128), unique=True)

    animals = relationship("Animal")


class Feed(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kind_feed = Column(String(128))
    manufacturer = Column(String(1024))
    title = Column(String(128))
    price = Column(Float)
