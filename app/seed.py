#!/usr/bin/env python3

from models import Crop, Market, PriceEntry
from db import session

crop1 = Crop(name="Maize", description="Staple grain crop")
crop2 = Crop(name="Tomato", description="Perishable vegetable")

market1 = Market(name="Wakulima", location="Nairobi")
market2 = Market(name="Kibuye", location="Kisumu")

session.add_all([crop1, crop2, market1, market2])
session.commit()

entry1 = PriceEntry(price_per_kg=45.0, crop=crop1, market=market1)
entry2 = PriceEntry(price_per_kg=55.0, crop=crop2, market=market2)

session.add_all([entry1, entry2])
session.commit()

print("\U0001F331 Database seeded!")
