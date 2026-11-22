from credit import calculate_risk


# --- Tests initiaux ---

def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100)
    assert result == "LOW"


# --- Tests des cas limites ---

def test_zero_income():
    """Cas limite 1 : Revenu nul (income = 0). Doit retourner -1."""
    result = calculate_risk(0, 500)
    assert result == -1

def test_negative_income():
    """Cas limite 2 : Revenu négatif (income = -1000). Doit retourner -1."""
    result = calculate_risk(-1000, 500, 30)
    assert result == -1

def test_zero_debt():
    """Cas limite 3 : Dette nulle (debt = 0). Ratio = 0.0 -> Doit retourner 'LOW'."""
    result = calculate_risk(1000, 0, 30)
    assert result == "LOW"

def test_exact_ratio_0_3():
    """Cas limite 4 : Ratio exactement égal à 0.3 (debt = 300, income = 1000).

    0.3 n'étant pas strictement supérieur à 0.3, la condition échoue et
    bascule dans else -> Doit retourner 'LOW'.
    """
    result = calculate_risk(1000, 300, 30)
    assert result == "LOW"

def test_exact_ratio_0_6():
    """Cas limite 5 : Ratio exactement égal à 0.6 (debt = 600, income = 1000).

    0.6 n'étant pas strictement supérieur à 0.6 mais supérieur à 0.3 -> Doit retourner 'MEDIUM'.
    """
    result = calculate_risk(1000, 600, 30)
    assert result == "MEDIUM"
