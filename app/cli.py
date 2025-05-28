from models import session, Crop, Market, PriceEntry
from datetime import datetime


#CROP
def add_crop():
    name = input("Enter crop name: ")
    description = input("Enter crop description: ")
    crop = Crop(name=name, description=description)
    session.add(crop)
    session.commit()
    print("Crop added!")

def view_crops():
    crops = session.query(Crop).all()
    for crop in crops:
        print(f"{crop.id}. {crop.name} - {crop.description}")

def update_crop():
    view_crops()
    crop_id = int(input("Enter Crop ID to update: "))
    crop = session.get(Crop, crop_id)
    if crop:
        new_name = input("Enter new crop name: ")
        crop.name = new_name
        session.commit()
        print("Crop updated.")
    else:
        print("Crop not found.")

def delete_crop():
    view_crops()
    crop_id = int(input("Enter Crop ID to delete: "))
    crop = session.get(Crop, crop_id)
    if crop:
        session.delete(crop)
        session.commit()
        print("Crop deleted.")
    else:
        print("Crop not found.")


#MARKET

def add_market():
    name = input("Enter market name: ")
    location = input("Enter market location: ")
    market = Market(name=name, location=location)
    session.add(market)
    session.commit()
    print("Market added.")

def view_markets():
    markets = session.query(Market).all()
    for market in markets:
        print(f"{market.id}. {market.name} - {market.location}")

def update_market():
    view_markets()
    market_id = int(input("Enter Market ID to update: "))
    market = session.get(Market, market_id)
    if market:
        market.name = input("Enter new name: ")
        market.location = input("Enter new location: ")
        session.commit()
        print("Market updated.")
    else:
        print("Market not found.")

def delete_market():
    view_markets()
    market_id = int(input("Enter Market ID to delete: "))
    market = session.get(Market, market_id)
    if market:
        session.delete(market)
        session.commit()
        print("Market deleted.")
    else:
        print("Market not found.")


#PRICE_ENTRY
def add_price_entry():
    view_crops()
    crop_id = int(input("Enter Crop ID: "))
    view_markets()
    market_id = int(input("Enter Market ID: "))
    price = float(input("Enter price per kg: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    entry_date = datetime.strptime(date_str, "%Y-%m-%d")
    entry = PriceEntry(price_per_kg=price, entry_date=entry_date, crop_id=crop_id, market_id=market_id)
    session.add(entry)
    session.commit()
    print("Price entry recorded.")

def view_price_entries():
    print("1. View all\n2. Filter by crop\n3. Filter by market\n4. Filter by date")
    choice = input("Choose an option: ")
    query = session.query(PriceEntry)

    if choice == "2":
        view_crops()
        crop_id = int(input("Enter Crop ID: "))
        query = query.filter_by(crop_id=crop_id)
    elif choice == "3":
        view_markets()
        market_id = int(input("Enter Market ID: "))
        query = query.filter_by(market_id=market_id)
    elif choice == "4":
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        query = query.filter(PriceEntry.entry_date == date)

    entries = query.all()
    for entry in entries:
        print(f"{entry.id}. {entry.crop.name} @ {entry.market.name} - {entry.price_per_kg} KES on {entry.entry_date.date()}")

def update_price_entry():
    view_price_entries()
    entry_id = int(input("Enter Price Entry ID to update: "))
    entry = session.get(PriceEntry, entry_id)
    if entry:
        entry.price_per_kg = float(input("Enter new price per kg: "))
        date_str = input("Enter new date (YYYY-MM-DD): ")
        entry.entry_date = datetime.strptime(date_str, "%Y-%m-%d")
        session.commit()
        print("Price entry updated.")
    else:
        print("Entry not found.")

def delete_price_entry():
    view_price_entries()
    entry_id = int(input("Enter Price Entry ID to delete: "))
    entry = session.get(PriceEntry, entry_id)
    if entry:
        session.delete(entry)
        session.commit()
        print("Entry deleted.")
    else:
        print("Entry not found.")


#MAIN MENU
def menu():
    while True:
        print("******Agricost Tracker Menu*******")
        print("1. Add Crop")
        print("2. View Crops")
        print("3. Update Crop")
        print("4. Delete Crop")
        print("5. Add Market")
        print("6. View Markets")
        print("7. Update Market")
        print("8. Delete Market")
        print("9. Record Price Entry")
        print("10. View Price Entries")
        print("11. Update Price Entry")
        print("12. Delete Price Entry")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1": add_crop()
        elif choice == "2": view_crops()
        elif choice == "3": update_crop()
        elif choice == "4": delete_crop()
        elif choice == "5": add_market()
        elif choice == "6": view_markets()
        elif choice == "7": update_market()
        elif choice == "8": delete_market()
        elif choice == "9": add_price_entry()
        elif choice == "10": view_price_entries()
        elif choice == "11": update_price_entry()
        elif choice == "12": delete_price_entry()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()

