import Lab2.BMI as bmi

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.75, 50)  # BMI ≈ 16.33
    assert result == -1

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.75, 68)  # BMI ≈ 22.2
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.75, 90)  # BMI ≈ 29.39
    assert result == 1
