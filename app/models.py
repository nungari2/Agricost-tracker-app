from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text, nullable=False)

    price_entries = relationship("PriceEntry", back_populates="crop")

class Market(Base):
    __tablename__ = 'markets'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    location = Column(String(100), nullable=False)

    price_entries = relationship("PriceEntry", back_populates="market")

class PriceEntry(Base):
    __tablename__ = 'price_entries'

    id = Column(Integer, primary_key=True)
    price_per_kg = Column(Float, nullable=False)
    entry_date = Column(DateTime, default=datetime.utcnow)

    crop_id = Column(Integer, ForeignKey("crops.id"), nullable=False)
    market_id = Column(Integer, ForeignKey("markets.id"), nullable=False)

    crop = relationship("Crop", back_populates="price_entries")
    market = relationship("Market", back_populates="price_entries")

# Create DB connection and session
engine = create_engine("sqlite:///agricost.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
