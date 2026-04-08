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
    },
    "S_SNEHA": {
        "shop_name": "Sneha Premium Store",
        "pincode": "411007",
        "city": "Pune",
        "contact_number": "+91-9876543210",
        "address": "Aundh Market"
    }
}

# global_inventory: Stores products. 
# KEY FEATURE: Each product has a 'seller_id' which creates a relational 
# link back to the sellers_registry.

global_inventory = {
    # SHIRDI INVENTORY
    "P01": {"seller_id": "S_SAI", "category": "phone", "brand": "Samsung", "model": "Galaxy S24", "price": 79000, "specs": "AI Features, 256GB"},
    "P02": {"seller_id": "S_SAI", "category": "laptop", "brand": "Apple", "model": "MacBook Air", "price": 82000, "specs": "M2 Chip, 8GB"},
    "P03": {"seller_id": "S_SAI", "category": "tv", "brand": "Sony", "model": "Bravia 4K", "price": 55000, "specs": "55-inch, Google TV"},
    "P14": {"seller_id": "S_SAI", "category": "phone", "brand": "OnePlus", "model": "12", "price": 44999, "specs": "Snapdragon 8 Gen 2"},
    "P15": {"seller_id": "S_SAI", "category": "laptop", "brand": "Lenovo", "model": "ThinkPad", "price": 58000, "specs": "Intel i7, 512GB SSD"},
    "P24": {"seller_id": "S_SAI", "category": "headphones", "brand": "Sony", "model": "WH-1000XM5", "price": 29999, "specs": "ANC, 30hrs Battery"},
    "P25": {"seller_id": "S_SAI", "category": "camera", "brand": "Canon", "model": "EOS R6", "price": 195000, "specs": "20MP, 4K Video"},
    "P26": {"seller_id": "S_SAI", "category": "monitor", "brand": "Dell", "model": "UltraSharp 27", "price": 35000, "specs": "4K, IPS Panel"},
    
    # RAHATA INVENTORY 
    "P04": {"seller_id": "S_KIRAN", "category": "fridge", "brand": "Whirlpool", "model": "Neo Fresh", "price": 26000, "specs": "265L, 3 Star"},
    "P05": {"seller_id": "S_KIRAN", "category": "ac", "brand": "Voltas", "model": "Adjustable Inverter", "price": 34000, "specs": "1.5 Ton, 5 Star"},
    "P06": {"seller_id": "S_KIRAN", "category": "microwave", "brand": "LG", "model": "Convection", "price": 12500, "specs": "28L, Charcoal Lighting"},
    "P07": {"seller_id": "S_KIRAN", "category": "washing machine", "brand": "Samsung", "model": "Top Load", "price": 19500, "specs": "7kg, Fully Automatic"},
    "P16": {"seller_id": "S_KIRAN", "category": "fridge", "brand": "LG", "model": "Door-in-Door", "price": 42000, "specs": "625L, Inverter"},
    "P17": {"seller_id": "S_KIRAN", "category": "ac", "brand": "Daikin", "model": "Smart Inverter", "price": 39000, "specs": "2 Ton, 5 Star"},
    "P27": {"seller_id": "S_KIRAN", "category": "gaming console", "brand": "PlayStation", "model": "PS5 Slim", "price": 49999, "specs": "1TB, Disc Edition"},
    "P28": {"seller_id": "S_KIRAN", "category": "monitor", "brand": "ASUS", "model": "ProArt PA248QV", "price": 26000, "specs": "24-inch, 100% sRGB"},
    
    # NASHIK INVENTORY
    "P08": {"seller_id": "S_RAHUL", "category": "laptop", "brand": "HP", "model": "Victus", "price": 62000, "specs": "RTX 3050, 16GB RAM"},
    "P09": {"seller_id": "S_RAHUL", "category": "phone", "brand": "iPhone", "model": "15", "price": 71000, "specs": "128GB, Blue"},
    "P10": {"seller_id": "S_RAHUL", "category": "tv", "brand": "LG", "model": "OLED C3", "price": 115000, "specs": "48-inch, 4K Smart"},
    "P18": {"seller_id": "S_RAHUL", "category": "laptop", "brand": "ASUS", "model": "VivoBook", "price": 45000, "specs": "Ryzen 5, 8GB RAM"},
    "P19": {"seller_id": "S_RAHUL", "category": "phone", "brand": "Google", "model": "Pixel 8", "price": 64999, "specs": "AI Magic Eraser"},
    "P29": {"seller_id": "S_RAHUL", "category": "headphones", "brand": "Bose", "model": "QuietComfort 45", "price": 26990, "specs": "ANC, Comfortable Fit"},
    "P30": {"seller_id": "S_RAHUL", "category": "camera", "brand": "Nikon", "model": "Z6II", "price": 165000, "specs": "24MP, 4K 60fps"},
    "P31": {"seller_id": "S_RAHUL", "category": "gaming console", "brand": "Xbox", "model": "Series X", "price": 54999, "specs": "1TB, 4K Gaming"},
    
    # PUNE INVENTORY
    "P11": {"seller_id": "S_SNEHA", "category": "fridge", "brand": "Samsung", "model": "Double Door", "price": 31000, "specs": "345L, Convertible"},
    "P12": {"seller_id": "S_SNEHA", "category": "ac", "brand": "Daikin", "model": "Premium Inverter", "price": 42000, "specs": "1 Ton, 3 Star"},
    "P13": {"seller_id": "S_SNEHA", "category": "washing machine", "brand": "IFB", "model": "Front Load", "price": 38000, "specs": "8kg, Steam Wash"},
    "P20": {"seller_id": "S_SNEHA", "category": "tv", "brand": "Samsung", "model": "QN75QN90D", "price": 125000, "specs": "75-inch 4K QLED"},
    "P21": {"seller_id": "S_SNEHA", "category": "phone", "brand": "Realme", "model": "12 Pro", "price": 28999, "specs": "Periscope Zoom"},
    "P22": {"seller_id": "S_SNEHA", "category": "microwave", "brand": "Whirlpool", "model": "Magicook", "price": 14999, "specs": "25L, Sensor Cook"},
    "P23": {"seller_id": "S_SNEHA", "category": "washing machine", "brand": "LG", "model": "AI DD", "price": 45000, "specs": "10kg, AI Diagnosis"},
    "P32": {"seller_id": "S_SNEHA", "category": "headphones", "brand": "JBL", "model": "Tour Pro 2", "price": 24999, "specs": "ANC, True Wireless"},
    "P33": {"seller_id": "S_SNEHA", "category": "camera", "brand": "Sony", "model": "A6700", "price": 155000, "specs": "26MP, Real-Time Eye AF"},
    "P34": {"seller_id": "S_SNEHA", "category": "monitor", "brand": "LG", "model": "Ultrawide 38", "price": 65000, "specs": "3840x1600, 144Hz"},
    "P35": {"seller_id": "S_SNEHA", "category": "gaming console", "brand": "Nintendo", "model": "Switch OLED", "price": 35999, "specs": "64GB, Portable Gaming"}
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
        
        # Display available categories in tabular format
        categories = ["Laptop", "Phone", "Fridge", "AC", "TV", "Washing Machine", 
                     "Microwave", "Headphones", "Camera", "Monitor", "Gaming Console"]
        
        print("\n--- AVAILABLE CATEGORIES ---")
        print("=" * 70)
        for i, cat in enumerate(categories, 1):
            print(f"{i:<3} {cat:<25}")
        print("=" * 70)
        
        cat_choice = input("Select category number (1-11): ").strip()
        
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            cat_query = categories[int(cat_choice) - 1].lower()
            
            print(f"\n--- {cat_query.upper()} in {LOCATION_MAP[choice]['name']} ---")
            print("=" * 130)
            print(f"{'Brand':<15} {'Model':<20} {'Price':<12} {'Specs':<35} {'Shop Name':<25} {'Contact':<15}")
            print("=" * 130)
            
            found = False
            
            for p_id, p_info in global_inventory.items():
                seller = sellers_registry.get(p_info['seller_id'])
                
                if seller and seller['pincode'] == target_pin and p_info['category'] == cat_query:
                    print(f"{p_info['brand']:<15} {p_info['model']:<20} ₹{p_info['price']:<10} {p_info['specs']:<35} {seller['shop_name']:<25} {seller['contact_number']:<15}")
                    found = True
            
            if found:
                print("=" * 130)
            else:
                print("No items found in this category.")
        else:
            print("Invalid category selection.")
    else:
        print("Invalid Selection.")

# --- 4. MAIN INTERFACE (Execution Loop) ---

def main():
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
            
        elif choice == '3': 
            add_new_product()
            
        elif choice == '4':
            print("\nID        | SHOP NAME            | CITY")
            print("-" * 40)
            for sid, info in sellers_registry.items():
                print(f"{sid:<9} | {info['shop_name']:<20} | {info['city']}")

        elif choice == '5': 
            print("Shutting down LATTICE...")
            break
            
        else: 
            print("Invalid Input. Please enter 1-5.")
            # We don't want to pause on an invalid input, just loop back.
            continue 
        input("\n--- Press Enter to return to main menu ---")

if __name__ == '__main__':
    main()
