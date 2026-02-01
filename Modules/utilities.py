def add_tax(price, tax):
    """
    Returns the tax to add as a percentage to the price argument.
    Follows the formula of: Total = Price * Tax

    For example with a price of $1 and tax 0.06

    Total = $1 * 0.06
    Total = $0.06
    """

    return tax * price


def apply_discount(price, discount):
    """
    Return the discount argument as a percentage of the price argument.
    Follows the formula of: Total = Price * Discount

    For example with a price of $1 and discount of 20%

    Total = $1 * 0.20
    Total = $0.20
    """
    return price * discount


def calculate_tip(price, tip):
    """
    Calculated the tip as a total of the price argument, given a percentage.
    Follows the formula of: Total Tip = Price * Tip

    For example with a price of $1 and tip of 20%

    Total Tip = $1 * 0.20
    Total Tip = $0.20
    """
    return price * tip


def input_validator(price, discount, tax, tip):
    """
    Validates if any inputs are negative or non-valid characters.
    Returns True if the inputs are valid, False otherwise.
    """
    try:
        price = float(price)
        discount = float(discount)
        tax = float(tax)
        tip = float(tip)
    except ValueError:
        return False
    if price < 0:
        return False
    elif discount < 0:
        return False
    elif tip < 0:
        return False
    elif tax < 0:
        return False
    else:
        return True
