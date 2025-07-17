# Define the menu of the cafe
menu = {
    	'Espresso':90,	
        'Cappuccino':120,	
        'Latte':130,	
        'Cold Coffee':140,	
        'Green Tea':80,	
        'Masala Chai':60,	
        'Hot Chocolate':150,	
        'Iced Americano':110,	
        'Lemon Iced Tea':90,
	    'Blueberry Smoothie':160,
	   'Veg Cheese Sandwich':100,
	    'Grilled Chicken Sandwich':150,
	    'Paneer Wrap':120,
	    'Chicken Mayo Wrap':150,
	    'Veggie Burger':130,
	    'Classic Chicken Burger':160,
	    'French Fries':90,
	    'Chocolate Brownie':80,
	    'Red Velvet Cupcake':70,
	    'Classic Waffles with Syrup':130,
}
# Greet
print("Welcome to THE CAFE")
print("Espresso: Rs90\nCappuccino: Rs120\n Latte: Rs130\nCold Coffee: Rs140\nGreen Tea: Rs80\nMasala Chai: Rs60\nHot Chocolate: Rs150\nIced Americano: Rs110\nLemon Iced Tea: Rs90\nBlueberry Smoothie: Rs160\nVeg Cheese Sandwich: Rs100\nGrilled Chicken Sandwich: Rs150\nPaneer Wrap: Rs120\nChicken Mayo Wrap: Rs150\nVeggie Burger: Rs130\nClassic Chicken Burger: Rs160\nFrench Fries: Rs90\nChocolate Brownie: Rs80\nRed Velvet Cupcake: Rs70\nClassic Waffles with Syru :130")

order_total = 0

item_1 = input("Enter the name of the item you wanted to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Sorry Order item{item_1}is not available yet!")

    another_order = input("Do you want to add another item?(YES/NO)")

    if another_order == "YES":
        item_2 = input("Enter the nae of the second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item{item_2}has been added to the order")
        else:
            print(f"Orderes item{item_2} is not available!")

            print(f"The total amount of item to pay is {order_total}")


