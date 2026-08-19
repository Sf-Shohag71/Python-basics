from city_function import location

def test_city_country():
    city_country = location('santiago', 'chilli')
    assert city_country == "Santiago Chilli"

def test_city_country_population():
    city_country_population = location('santiago', 'chilli', 5000000)
    assert city_country_population == "Santiago Chilli - 5000000"

# Run test case: python -m pytest