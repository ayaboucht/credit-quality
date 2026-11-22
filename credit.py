def calculate_risk(income, debt, age=None):
    """Calcule le niveau de risque de crédit basé sur le ratio dette/revenu."""
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
