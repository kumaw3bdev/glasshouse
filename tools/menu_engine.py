#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glass House Bar - Menu Search Tool
Allows users to search for menu items, categories, and sauces.
"""

# Glass House Master Menu Data
menu_data = [
    {
        "category": "Appetizers",
        "header_notes": "Add fries, onion rings or tots to any app for $3.50",
        "items": [
            {
                "name": "Mini Corn Dogs",
                "price": 9.75,
                "desc": "Bite-sized corn dogs"
            },
            {
                "name": "White Cheddar Cheese Curds",
                "price": 9.75,
                "desc": "Fried white cheddar curds."
            },
            {
                "name": "Mac & Cheese Bites",
                "price": 9.75,
                "desc": "Creamy Mac & Cheese, fried."
            },
            {
                "name": "Beer Battered Shrimp",
                "price": 11.75,
                "desc": "Served with cocktail or tartar sauce."
            },
            {
                "name": "Mozzarella Sticks",
                "price": 9.75,
                "desc": "Served with marinara."
            },
            {
                "name": "Fried Pickles",
                "price": 9.75,
                "desc": "Lightly breaded pickle slices."
            },
            {
                "name": "Pizza Puffs",
                "price": 8.00,
                "desc": "House-made pizza puffs served with marinara."
            },
            {
                "name": "Jalapeno Poppers",
                "price": 9.75,
                "desc": "Fried jalapenos stuffed with cream cheese."
            },
            {
                "name": "Fried Mushrooms",
                "price": 9.75,
                "desc": "Crispy fried mushrooms."
            },
            {
                "name": "Chips & Salsa",
                "price": 6.00,
                "desc": "Classic tortilla chips and house salsa."
            },
            {
                "name": "Basket of Fries, Tots or Onion Rings",
                "price": 7.00,
                "desc": "Add Chili: $9.00 | Add Cheese: $10.00"
            }
        ],
        "sauces": {
            "tier_1": {
                "price": 0.25,
                "list": ["Ranch", "Blue Cheese", "Honey Mustard", "Salsa"]
            },
            "tier_2": {
                "price": 0.50,
                "list": ["Glass House Sauce", "Pesto Mayo"]
            }
        }
    },
    {
        "category": "Wings & Tenders",
        "items": [
            {
                "name": "Traditional Wings",
                "price": 14.00,
                "desc": "8 Wings"
            },
            {
                "name": "Boneless Wings",
                "price": 11.00,
                "desc": "10 Wings"
            },
            {
                "name": "Chicken Tenders",
                "price": 11.00,
                "desc": "4 Tenders"
            },
            {
                "name": "Vegan Tenders",
                "price": 12.00,
                "desc": "4 Plant-Based Tenders"
            }
        ],
        "sauce_options": [
            "Asian Zing", "Buffalo", "BBQ", "Chipotle BBQ",
            "Garlic Parmesan", "Jamaican Jerk"
        ],
        "header_notes": "All wings and tenders can be tossed in or served with your choice of sauce. Additional side of sauce: $0.50"
    },
    {
        "category": "Soup & Salads",
        "items": [
            {
                "name": "Soup of the Day (Cup)",
                "price": 4.00,
                "desc": "Ask your server for today's selection."
            },
            {
                "name": "Soup of the Day (Bowl)",
                "price": 6.00,
                "desc": "Ask your server for today's selection."
            },
            {
                "name": "Caesar Salad",
                "price": 8.00,
                "desc": "Fresh romaine, onions, parmesan, croutons, and Caesar dressing. Add Grilled or Crispy Chicken: $3.00"
            },
            {
                "name": "GH House Salad",
                "price": 6.00,
                "desc": "Mixed greens, cucumbers, tomatoes, croutons, and cheddar cheese."
            },
            {
                "name": "GH Chef Salad",
                "price": 13.00,
                "desc": "Greens topped with turkey, ham, tomatoes, cucumbers, croutons, and cheddar."
            },
            {
                "name": "Grilled or Crispy Chicken Salad",
                "price": 13.00,
                "desc": "Your choice of chicken on a bed of greens with cucumbers, tomatoes, croutons, and cheddar."
            },
            {
                "name": "Side Salad",
                "price": 3.50,
                "desc": ""
            }
        ],
        "header_notes": "Dressings: Ranch, Blue Cheese, Thousand Island, Italian, French."
    },
    {
        "category": "Handhelds",
        "section_note": "Served with choice of fries, tots, onion rings, potato chips or side salad.",
        "items": [
            {
                "name": "BLT",
                "price": 13.00,
                "desc": "Bacon, lettuce, tomato, on grilled sourdough."
            },
            {
                "name": "Club",
                "price": 13.00,
                "desc": "Turkey, ham, bacon, lettuce, tomato, American cheese on grilled sourdough."
            },
            {
                "name": "Grilled Cheese",
                "price": 11.00,
                "desc": "Swiss, American cheese on sourdough. Add Ham or Turkey: $3.00."
            },
            {
                "name": "Reuben",
                "price": 14.00,
                "desc": "House-made corned beef, sauerkraut, Swiss, Thousand Island, swirl marble rye."
            },
            {
                "name": "Pulled Pork",
                "price": 13.00,
                "desc": "Shredded pork, cheddar, choice of regular or Chipotle BBQ on brioche bun."
            },
            {
                "name": "Dog Basket",
                "price": 8.00,
                "desc": "Two all beef dogs. Add cheddar: $0.50 | Add Chili: $0.50"
            },
            {
                "name": "Philly or French Dip",
                "price": 14.00,
                "desc": "Thinly sliced steak on sub bun. Includes choice of one cheese. Add Peppers, Onions, or Mushrooms: $0.50 ea."
            },
            {
                "name": "BYO Burger or Chicken Sandwich",
                "price": 14.00,
                "desc": "Beef, chicken, or veggie. Includes 3 toppings. Additional toppings: $1.00. Cheese: $2.00. Proteins: $3.00. Sauces: $0.50."
            }
        ]
    },
    {
        "category": "Wraps",
        "section_note": "Served with choice of fries, tots, onion rings, potato chips or side salad.",
        "items": [
            {
                "name": "Chicken Caesar",
                "price": 14.00,
                "desc": "Grilled or crispy chicken, romaine, parmesan, and Caesar dressing."
            },
            {
                "name": "Chicken, Bacon & Ranch",
                "price": 14.00,
                "desc": "Grilled or crispy chicken, bacon, lettuce, tomatoes, shredded cheddar, ranch."
            },
            {
                "name": "Buffalo Chicken",
                "price": 14.00,
                "desc": "Grilled or crispy chicken, buffalo sauce, lettuce, tomatoes, and cheddar. Sub Shrimp: $3.00"
            }
        ]
    },
    {
        "category": "Tex-Mex",
        "section_note": "Add salsa or sour cream: $0.25",
        "items": [
            {
                "name": "Chips & Cheese",
                "price": 9.50,
                "desc": "Tortilla chips, cheddar cheese blend."
            },
            {
                "name": "Quesadilla",
                "price": 11.50,
                "desc": "Choice of Chicken, House-made Taco Meat, Steak, or Pulled Pork. (Onions/Jalapenos on request)."
            },
            {
                "name": "Pulled Pork Nachos",
                "price": 14.00,
                "desc": "Onions, jalapenos, tortilla chips, cheese blend, chipotle BBQ. Add Bacon: $3.00."
            },
            {
                "name": "Ultimate Nachos",
                "price": 11.00,
                "desc": "Lettuce, tomatoes, onions, jalapenos, tortilla chips, cheese blend. Add Chicken, Housemade Steak, Taco Meat or Pulled Pork: $3.00."
            }
        ]
    },
    {
        "category": "Loaded Tots",
        "items": [
            {
                "name": "Nacho Tots",
                "price": 14.00,
                "desc": "Taco Meat, Tots, Onions, Lettuce, Tomatoes, Jalapeños, Cheese."
            },
            {
                "name": "Pork Tots",
                "price": 14.00,
                "desc": "Pulled Pork, Tots, Onions, Jalapeños, Cheese, Chipotle BBQ Sauce. Add Bacon: $2.00"
            }
        ]
    },
    {
        "category": "Pizza",
        "section_note": "14 inch medium crust pizza.",
        "items": [
            {
                "name": "BYO (Build Your Own)",
                "price": 14.00,
                "desc": "Includes 2 toppings. Options: Pepperoni, Sausage, Ham, Bacon, Mushrooms, Onions, Roasted Red Peppers, Green Olives. Additional Toppings: Protein $3 | Veggies $2"
            },
            {
                "name": "Glass House Pizza",
                "price": 16.00,
                "desc": "Taco meat, mozzarella, lettuce, tomato, onions, shredded cheese blend, house chipotle sauce."
            },
            {
                "name": "BBQ Chicken",
                "price": 14.00,
                "desc": "Grilled chicken, onions, cheese, BBQ sauce."
            },
            {
                "name": "BLT",
                "price": 14.00,
                "desc": "Bacon, lettuce, tomatoes, mayo."
            },
            {
                "name": "Pulled Pork",
                "price": 14.00,
                "desc": "Pulled pork, onions, cheese, chipotle BBQ."
            }
        ]
    }
]


def format_price(price):
    """
    Format a price value as a currency string.
    
    Args:
        price: Can be float, int, or string
        
    Returns:
        str: Formatted price string (e.g., "$9.75")
    """
    if isinstance(price, (float, int)):
        return f"${price:.2f}"
    return str(price)


def search_menu_items(search_term, category):
    """
    Search for menu items within a category.
    
    Args:
        search_term (str): The search query
        search_term_lower (str): Lowercase version for matching
        category (dict): Category data containing items
        
    Returns:
        bool: True if matches found, False otherwise
    """
    found = False
    search_term_lower = search_term.lower()
    cat_name = category.get("category", "Unknown")
    items_list = category.get("items", [])
    
    # Check if searching by category name
    category_match = search_term_lower in cat_name.lower()
    
    # Search through menu items
    for item in items_list:
        name_match = search_term_lower in item["name"].lower()
        
        if category_match or name_match:
            price_str = format_price(item.get("price", "Varies"))
            
            print(f"Found Item: {item['name']} -- {price_str}")
            print(f"   Category: {cat_name}")
            if item.get("desc"):
                print(f"   Desc: {item['desc']}")
            print("-" * 50)
            found = True
    
    return found


def search_sauce_options(search_term, category):
    """
    Search for sauce options in Wings & Tenders category.
    
    Args:
        search_term (str): The search query
        category (dict): Category data containing sauce_options
        
    Returns:
        bool: True if matches found, False otherwise
    """
    found = False
    search_term_lower = search_term.lower()
    cat_name = category.get("category", "Unknown")
    user_wants_all_sauces = "sauce" in search_term_lower
    
    if "sauce_options" in category:
        for sauce in category["sauce_options"]:
            # Match if user types exact sauce name OR if user types "sauce"
            if (search_term_lower in sauce.lower()) or user_wants_all_sauces:
                print(f"Found Sauce: {sauce}")
                print(f"   Category: {cat_name}")
                if category.get("header_notes"):
                    print(f"   Note: {category['header_notes']}")
                print("-" * 50)
                found = True
    
    return found


def search_tiered_sauces(search_term, category):
    """
    Search for tiered sauces in Appetizers category.
    
    Args:
        search_term (str): The search query
        category (dict): Category data containing tiered sauces
        
    Returns:
        bool: True if matches found, False otherwise
    """
    found = False
    search_term_lower = search_term.lower()
    cat_name = category.get("category", "Unknown")
    user_wants_all_sauces = "sauce" in search_term_lower
    
    if "sauces" in category:
        for tier_name, tier_data in category["sauces"].items():
            for sauce in tier_data.get("list", []):
                # Match if user types exact sauce name OR if user types "sauce"
                if (search_term_lower in sauce.lower()) or user_wants_all_sauces:
                    price = tier_data.get("price", 0)
                    print(f"Found Sauce: {sauce}")
                    print(f"   Category: {cat_name} (Tier: {tier_name}, Price: ${price:.2f})")
                    print("-" * 50)
                    found = True
    
    return found


def search_menu(search_term):
    """
    Main search function that searches across all menu categories.
    
    Args:
        search_term (str): The search query from user input
        
    Returns:
        bool: True if any matches found, False otherwise
    """
    if not search_term or not search_term.strip():
        print("Please enter a valid search term.")
        return False
    
    found = False
    
    for category in menu_data:
        # Search menu items
        if search_menu_items(search_term, category):
            found = True
        
        # Search sauce options (Wings & Tenders style)
        if search_sauce_options(search_term, category):
            found = True
        
        # Search tiered sauces (Appetizers style)
        if search_tiered_sauces(search_term, category):
            found = True
    
    return found


def main():
    """
    Main program loop for interactive menu search.
    """
    print("=" * 50)
    print("Glass House Bar - Menu Search")
    print("=" * 50)
    print("\nSearch by item name, category, or sauce type.")
    print("Type 'q' to quit.\n")
    
    while True:
        try:
            search_item = input("\nEnter food to search for (or 'q' to quit): ").strip()
            
            if search_item.lower() == 'q':
                print("\nThank you for using Glass House Menu Search!")
                break
            
            if not search_item:
                print("Please enter a search term.")
                continue
            
            print("\n" + "=" * 50)
            found = search_menu(search_item)
            
            if not found:
                print(f"Sorry, we couldn't find any items matching '{search_item}'.")
                print("Try searching by category (e.g., 'Pizza', 'Wings') or item name.")
            
            print("=" * 50)
            
        except KeyboardInterrupt:
            print("\n\nExiting menu search. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()