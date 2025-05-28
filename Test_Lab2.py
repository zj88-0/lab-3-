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

def test_calc_average_temperature4():
    temp_values = [19.6,23.5,36.9,41.2,25.0]
    expected_average = 29.24
    average_temp= lab2.calc_average_temperature(temp_values)
    assert average_temp == expected_average
def test_calc_average_temperature5():
    temp_values = [20.0, 20.0, 20.0]
    expected_average = 20.0
    average_temp = lab2.calc_average_temperature(temp_values)
    assert average_temp == expected_average
def test_calc_average_temperature6():
    temp_values = [15.0]
    expected_average = 15.0
    average_temp = lab2.calc_average_temperature(temp_values)
    assert average_temp == expected_average
def test_calc_median_temperature7():
    temp_values = [19.6, 23.5, 36.9, 41.2, 25.0]
    expected_median = 25.0
    median_temp = lab2.calc_median_temperature(temp_values)
    assert median_temp == expected_median

def test_calc_median_temperature9():
    temp_values = [20.0, 20.0, 20.0]
    expected_median = 20.0
    median_temp = lab2.calc_median_temperature(temp_values)
    assert median_temp == expected_median
def test_calc_median_temperature10():
    temp_values = [15.0]
    expected_median = 15.0
    median_temp = lab2.calc_median_temperature(temp_values)
    assert median_temp == expected_median
def test_calc_median_temperature8():
    temp_values = [19.6, 23.5, 36.9, 41.2, 25.0, 20.0]
    expected_median = 24.25
    median_temp = lab2.calc_median_temperature(temp_values)
    assert median_temp == expected_median
