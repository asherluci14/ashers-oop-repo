class Temperature:
    def __init__(self):
        self.celsius = 1.0

    def convert_to_fahrenheit(self):
        converted = (self.celsius * 9 / 5) + 32
        print(converted)

    def check_is_freezing(self):
        message = "It's freezing!" if self.celsius <= 0 else "It's not freezing."
        print(message)

    def check_weather(self):
        temp = self.celsius
        if temp <= 0:
            print(f"{temp}°C. brrrr it's freezing.")
        elif 0 < temp < 10:
            print(f"{temp}°C. Grab a jacket.")
        elif 10 <= temp < 18:
            print(f"{temp}°C. It's cool out.")
        elif 18 <= temp < 25:
            print(f"{temp}°C. Yesss, the sun <3.")
        elif 25 <= temp < 35:
            print(f"{temp}°C. Classic Australia.")
        else:
            print(f"{temp}°C. Heat wave time :(")


temperature = Temperature()
temperature.convert_to_fahrenheit()
temperature.check_is_freezing()
temperature.check_weather()

temperature.celsius = -10.0
temperature.convert_to_fahrenheit()
temperature.check_is_freezing()
temperature.check_weather()

temperature.celsius = 25.0
temperature.convert_to_fahrenheit()
temperature.check_is_freezing()
temperature.check_weather()

temperature.celsius = 35.0
temperature.check_weather()