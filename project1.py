#Author: 
#Sahil Gulati
'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")


vehicles = dealer.initialize()

# This While loop will keep asking for user inputs until they simply press enter.
while True:
    dealer.display_menu()  
    option = input("Command (Enter to exit): ")
    
    if option == "":
        break
    
    if option == "1":

        #vehicles = dealer.initialize()
        dealer.display(vehicles)
    elif option == "2":
        #vehicles = dealer.initialize()
        dealer.info(vehicles)
    elif option == "3":
        #vehicles = dealer.initialize()
        vehicle_id = input("Enter the ID of the vehicle to remove: ")
        dealer.remove_vehicle(vehicles, vehicle_id)
    elif option == "4":
        #vehicles = dealer.initialize()
        vehicles=dealer.add_new_vehicle(vehicles)
    elif option == "5":
        #vehicles = dealer.initialize()
        vehicle1_id = input("Enter the ID of the first vehicle: ")
        vehicle2_id = input("Enter the ID of the second vehicle: ")
        dealer.compare(vehicles, vehicle1_id, vehicle2_id)
    elif option == "6":
        #vehicles = dealer.initialize()
        min_price = int(input("Enter the minimum price: "))
        max_price = int(input("Enter the maximum price: "))
        dealer.search(vehicles, min_price, max_price)
    elif option == "7":
        #vehicles = dealer.initialize()
        vehicle_id = input("Enter the ID of the vehicle to discount: ")
        discount_percent = int(input("Enter the discount percentage: "))
        dealer.discount(vehicles, vehicle_id, discount_percent)
    else:
        print("Invalid option. Please select again.")

# Code reaches here after the loop ends
print("\nThanks for using this tool!\nCome back soon!\n")