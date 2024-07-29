#Author: 
#Sahil Gulati

'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")



#### To complete (all functions below)
def initialize():
    """Create and return a list of vehicles"""
    vehicles = [
        ["Toyota", "Camry", "2018", "45000", "20000"],
        ["Ford", "Escape", "2019", "30000", "23500"],
        ["Honda", "Accord", "2017", "60000", "16200"],
        ["Chevrolet","Silverado", "2020", "25000", "41000",],
        ["BMW",   "3 Series", "2016", "60000", "20500",],
        ["Nissan", "Rogue", "2019", "40000", "17800",],
        ["Hyundai", "Sonata", "2018", "42000", "16500"],
        ["Jeep", "Wrangler", "2021", "15000", "32000"],
        ["Ford", "Mustang", "2015", "50000", "22000"],
        ["Volkswagen", "Golf", "2017", "38000", "17800"]
        
    ]
    
    return vehicles

def display(vehicles):
    """Display the information of vehicles"""
    print("\t\tMake\t\tModel\t\tYear\tMileage\tPrice\t")
    print("-----------------------------------------------------------------------------")
    i=1
    for vehicle in vehicles:
        print(i,end='\t\t')
        i=i+1
        print(vehicle[0], end='\t\t') 
        print(vehicle[1], end='\t\t')  
        print(vehicle[2], end='\t\t')  
        print(vehicle[3], end='\t\t')  
        print(vehicle[4], end='\t\t')
        print()


def info(vehicles):
   
    """Display vehicle statistics"""
    num_vehicles = len(vehicles)
    total_price = sum(int(vehicle[4]) for vehicle in vehicles)
    mean_price = total_price / num_vehicles
    min_price = min(int(vehicle[4]) for vehicle in vehicles)
    max_price = max(int(vehicle[4]) for vehicle in vehicles)
    price_ratio = (max_price - min_price) / max_price * 100
    
    print("Number of vehicles:", num_vehicles)
    print("Price ratio (highest/lowest): {:.2f}%".format(price_ratio))
    print("Mean price: ${:.2f}".format(mean_price))

def remove_vehicle(vehicles, vehicle_id):
    """Remove a vehicle from the list"""
    length=len(vehicles)
    index=int(vehicle_id)-1
    if 0 <= index < len(vehicles):
        vehicles.pop(index)  # Remove and return vehicle at the specified index
        print(f"Vehicle removed successfully.")
    else:
        print("Vehicle not found!")

def add_new_vehicle(vehicles):
    """Add a new vehicle to the list"""
    new_vehicle = [
        input("Enter Make: "),
        input("Enter Model: "),
        input("Enter Year: "),
        input("Enter Mileage: "),
        input("Enter Price ($): ")
    ]
    vehicles.append(new_vehicle)
    print("New vehicle added successfully.")
    return vehicles

def compare(vehicles, vehicle1_id, vehicle2_id):
    """Compare details between two vehicles"""
    vehicle1_index = int(vehicle1_id) - 1
    vehicle2_index = int(vehicle2_id) - 1

    if 0 <= vehicle1_index < len(vehicles) and 0 <= vehicle2_index < len(vehicles):
            vehicle1 = vehicles[vehicle1_index]
            vehicle2 = vehicles[vehicle2_index]
            
            make_match = "Yes" if vehicle1[0] == vehicle2[0] else "No"
            newer_year = max(int(vehicle1[2]), int(vehicle2[2]))
            higher_price = max(int(vehicle1[4]), int(vehicle2[4]))
            
            print("Make match:", make_match)
            print("Newer vehicle year:", newer_year)
            print("Vehicle with higher price:", higher_price)
    else:
        print("Invalid vehicle number.")

def search(vehicles, min_price, max_price):
    """Search for vehicles within a price range"""
    matching_vehicles = [vehicle for vehicle in vehicles if min_price <= int(vehicle[4]) <= max_price]
    print("Vehicles within price range:")
    for vehicle in matching_vehicles:
        print("\t".join(vehicle))
    print("Total number of vehicles within price range:", len(matching_vehicles))

def discount(vehicles, vehicle_id, discount):
    """Apply discount to a vehicle's price"""
    vehicle_index = int(vehicle_id) - 1
    if 0 <= vehicle_index < len(vehicles):
        current_price = int(vehicles[vehicle_index][4])
        discounted_price = current_price * (1 - discount / 100)
        vehicles[vehicle_index][4] = str(discounted_price)
        print("Discount applied successfully.")
    else:
        print("Invalid vehicle number.")

