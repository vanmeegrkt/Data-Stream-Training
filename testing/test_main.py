from main import get_weather

def test_get_weather():
    assert get_weather(18) == "It's not that hot outside."
    assert get_weather(25) == "It's not that hot outside."
    assert get_weather(30) == "It's not that hot outside."
    assert get_weather(40) == "It's hot outside."
    assert get_weather(20) == "It's not that hot outside."