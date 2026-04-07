import json

# =======================================================
# PROJECT: Onliine Marketplace for Local Shops
# NAME: LATTICE 
# =======================================================

# --- 1. DATA ARCHITECTURE (The Database) ---

# LOCATION_MAP: Acts as a lookup table to pincodes across the app.
LOCATION_MAP = {
    "1": {"name": "Shirdi", "pin": "423109"},
    "2": {"name": "Rahata", "pin": "423107"},
    "3": {"name": "Nashik", "pin": "422001"},
    "4": {"name": "Pune", "pin": "411007"}
}

# sellers_registry: Stores shop details using a Unique ID as the key.
# This is equivalent to a 'Sellers' table in a real SQL database.
sellers_registry={
    "S_SAI": {
        "shop_name": "Sai Digital Shirdi",
        "pincode": "423109",
        "city": "Shirdi",
        "contact_number": "+91-9822012345",
        "address": "Opp. Temple Gate No. 2"
    },
    "S_KIRAN": {
        "shop_name": "Kiran Home Appliances",
        "pincode": "423107",
        "city": "Rahata",
        "contact_number": "+91-9422055667",
        "address": "Rahata Market Yard"
    },
    "S_RAHUL": {
        "shop_name": "Rahul Electronics",
        "pincode": "422001",
        "city": "Nashik",
        "contact_number": "+91-9850011223",
        "address": "College Road"
    }
}

# global_inventory: Stores products. 
# KEY FEATURE: Each product has a 'seller_id' which creates a relational 
# link back to the sellers_registry.

global_inventory = {
    "P01": {"seller_id": "S_SAI", "category": "phone", "brand": "Samsung", "model": "Galaxy S24", "price": 79000, "specs": "AI Features, 256GB"},
    "P02": {"seller_id": "S_KIRAN", "category": "fridge", "brand": "Whirlpool", "model": "Neo Fresh", "price": 26000, "specs": "265L, 3 Star"},
    "P03": {"seller_id": "S_SAI", "category": "laptop", "brand": "Apple", "model": "MacBook Air", "price": 82000, "specs": "M2 Chip, 8GB"},
    "P04": {"seller_id": "S_KIRAN", "category": "laptop", "brand": "HP", "model": "Victus", "price": 62000, "specs": "RTX 3050, 16GB RAM"},
    "P05": {"seller_id": "S_RAHUL", "category": "phone", "brand": "iPhone", "model": "15", "price": 71000, "specs": "128GB, Blue"}
}

# --- 2. SELLER FUNCTIONS (Backend Management) ---

def add_new_seller():
    #"""Allows a new business to register their shop location and contact info."""
    print("\n--- REGISTER NEW SHOP ---")
    # Convert input to uppercase to keep IDs consistent (S_AMIT)
    s_id = input("Create a unique Seller ID (e.g., S_AMIT): ").upper()
    name = input("Enter Shop Name: ")
    
    print("\nSelect Location:")
    for key, loc in LOCATION_MAP.items():
        print(f"{key}. {loc['name']}")
    
    choice = input("Choice: ")
    if choice in LOCATION_MAP:
        loc_data = LOCATION_MAP[choice]
        contact = input("Contact Number: ")
        addr = input("Area/Address: ")
        
        # Adding the new entry to our dictionary-based database
        sellers_registry[s_id] = {
            "shop_name": name,
            "pincode": loc_data['pin'],
            "city": loc_data['name'],
            "contact_number": contact,
            "address": addr
        }
        print(f"\n✅ Success: {name} ({loc_data['name']}) is now on LATTICE!")
    else:
        print("❌ Invalid selection.")

def add_new_product():
    #"""Allows an existing seller to list a new item in the global inventory."""
    print("\n--- ADD PRODUCT TO INVENTORY ---")
    s_id = input("Enter your Seller ID: ").upper()
    
    # Check if the seller exists before allowing them to add products (Foreign Key Check)
    if s_id in sellers_registry:
        # Generate a new Product ID based on current dictionary length
        new_id = f"P{len(global_inventory) + 1:02d}" 
        
        #covert category input to lowercase for easier searching later
        cat = input("Category (Laptop/Phone/Fridge): ").lower()
        brand = input("Brand: ")
        model = input("Model: ")
        price = int(input("Price (₹): "))
        specs = input("Key Specs: ")
        
        global_inventory[new_id] = {
            "seller_id": s_id, "category": cat, "brand": brand, 
            "model": model, "price": price, "specs": specs
        }
        print(f"✅ Success: Item listed under {sellers_registry[s_id]['shop_name']}")
    else:
        print("❌ Error: Seller ID not found. Register your shop first.")

# --- 3. CUSTOMER FUNCTIONS (Frontend Logic) ---

def search_products():
#    """Fetches local products by joining Inventory and Seller data based on Pincode."""
    print("\n--- BROWSE BY LOCATION ---")
    for key, loc in LOCATION_MAP.items():
        print(f"{key}. {loc['name']} ({loc['pin']})")
    
    choice = input("Select City (1-4): ")
    if choice in LOCATION_MAP:
        target_pin = LOCATION_MAP[choice]['pin']
        cat_query = input("Search for (Laptop/Phone/Fridge): ").lower() 
        
        print(f"\n--- Fetching {cat_query}s in {LOCATION_MAP[choice]['name']} ---")
        found = False
        
        # Iterate through all items in the inventory
        for p_id, p_info in global_inventory.items():
            # Retrieve the seller object for the current product
            seller = sellers_registry.get(p_info['seller_id'])
            
            # THE FILTER : Match the pincode AND the category
            if seller and seller['pincode'] == target_pin and p_info['category'] == cat_query:
                print(f"[{p_info['brand']} {p_info['model']}]")
                print(f"Price: ₹{p_info['price']} | Features: {p_info['specs']}")
                print(f"Shop: {seller['shop_name']} | Call: {seller['contact_number']}")
                print(f"Location: {seller['address']}")
                print("-" * 45)
                found = True
                
        if not found:
            print(f"No {cat_query} items found here yet.")
    else:
        print("Invalid Selection.")

# --- 4. MAIN INTERFACE (Execution Loop) ---

def main():
#    """Main loop to keep the program running until the user chooses to exit."""
    while True:
        print("\n" + "="*40)
        print("         LATTICE: Seamless Shopping.")
        print("="*40)
        print("1. [Customer] Browse Local Market")
        print("2. [Seller]   Register Your Shop")
        print("3. [Seller]   Add Item to Inventory")
        print("4. [Admin]    List All Active Sellers")
        print("5. Exit")

        choice = input("\nAction: ")
        if choice == '1': 
            search_products()
        elif choice == '2': 
            add_new_seller()
             # --- PAUSE FOR REVIEW ---
            input("\nPress Enter to return to menu...")
        elif choice == '3': 
            add_new_product()
             # --- PAUSE FOR REVIEW ---
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            # Formatted list of sellers for admin view
            print("\nID        | SHOP NAME            | CITY")
            print("-" * 40)
            for sid, info in sellers_registry.items():
                print(f"{sid:<9} | {info['shop_name']:<20} | {info['city']}")
                # --- PAUSE FOR REVIEW ---
            input("\nPress Enter to return to menu...")
        elif choice == '5': 
            print("Shutting down LATTICE...")
            break
        else: 
            print("Invalid Input. Please enter 1-5.")

#ensure code runs only when executed directly
if __name__ == "__main__":
    main()
