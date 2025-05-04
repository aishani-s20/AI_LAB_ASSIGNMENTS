def calculate_compound_interest(principal, rate, time):
    """
    Calculate compound interest.

    :param principal: Principal amount (float)
    :param rate: Annual interest rate (percentage as float)
    :param time: Time period in years (float)
    :return: Compound interest (float)
    """
    compound_interest = principal * ((1 + rate / 100) ** time) - principal
    return compound_interest
