# prints meal receipt based on input
def ticketBuild(menuType, item1, item2, item3):
    """
    Depending on the menu type included, will produce a ticket for either the lunch or dinner menu

    The included item parameters will be listed on the receipt of the ticket.
    A total amount will be returned for the meal portion of the ticket.
    """
    if menuType == "LNC":
        print("\n")
        print("RECEIPT")
        print("-------------------------")
        print("\n")
        print("LUNCH SERVICE")
        total = 0
        if item1 > 0:
            line1 = item1 * 12.25
            print(f"{item1} Braised Pork Sliders x $12.25:  ${line1:.2f}")
            total += line1
        if item2 > 0:
            line2 = item2 * 15.50
            print(f"{item2} Crab Mac & Cheese x $15.50: ${line2:.2f} ")
            total += line2
        if item3 > 0:
            line3 = item3 * 7.50
            print(f"{item3} Roasted Brussels Sprouts x $7.50:  ${line3:.2f} ")
            total += line3
        return total
    elif menuType == "DIN":
        print("\n")
        print("RECEIPT")
        print("-------------------------")
        print("\n")
        print("DINNER SERVICE")
        total = 0
        if item1 > 0:
            line1 = item1 * 14.00
            print(f"{item1} Bacon & Brie Flatbread x $14.00  ${line1:.2f}")
            total += line1
        if item2 > 0:
            line2 = item2 * 12.50
            print(f"{item2} House Caesar Salad x $12.50: ${line2:.2f} ")
            total += line2
        if item3 > 0:
            line3 = item3 * 22.50
            print(f"{item3} Filet Mignon x $22.50:  ${line3:.2f} ")
            total += line3
        return total
    else:
        print("Invalid menu type")
        return 0


def ticketDrink(item1, item2, item3):
    """
    Will produce a ticket for the drink portion of the ticket.

    The included item parameters will be listed on the receipt of the ticket.
    A total amount will be returned for the drink portion of the ticket.
    """
    print("\n")
    print("-------------------------")
    print("\n")
    total = 0
    if item1 > 0:
        line1 = item1 * 2.25
        print(f"{item1} Soft drink x2.25: ${line1:.2f}")
        total += line1
    if item2 > 0:
        line2 = item2 * 3.50
        print(f"{item2} House Lemonade x $3.50: ${line2:.2f}")
        total += line2
    if item3 > 0:
        line3 = item3 * 12.00
        print(f"{item3} House wine x12.00: ${line3:.2f}")
        total += line3
    return total
