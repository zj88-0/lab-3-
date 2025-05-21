import Lab2.lab2 as lab2

def test_calc_min_max_temperature1():
    # Test case 1: Normal case with positive and negative temperatures
    temp_values = [30.5, 25.0, 15.0, 40.0, -5.0]
    expected_min = -5.0
    expected_max = 40.0
    min_temp, max_temp = lab2.calc_min_max_temperature(temp_values)
    assert min_temp == expected_min
    assert max_temp == expected_max

def test_calc_min_max_temperature2():
    # Test case 2: All temperatures are the same
    temp_values = [20.0, 20.0, 20.0]
    expected_min = 20.0
    expected_max = 20.0
    min_temp, max_temp = lab2.calc_min_max_temperature(temp_values)
    assert min_temp == expected_min
    assert max_temp == expected_max

def test_calc_min_max_temperature3():
    # Test case 3: Single temperature value
    temp_values = [15.0]
    expected_min = 15.0
    expected_max = 15.0
    min_temp, max_temp = lab2.calc_min_max_temperature(temp_values)
    assert min_temp == expected_min
    assert max_temp == expected_max
