class MobilePhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self, percent):
        self.battery_percentage += percent
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print("Charged. Battery now:", self.battery_percentage, "%")

    def use_phone(self, minutes):
        drain = minutes // 10
        if drain <= self.battery_percentage:
            self.battery_percentage -= drain
            print("Used phone for", minutes, "minutes")
        else:
            print("Battery too low for that usage!")
        print("Battery now:", self.battery_percentage, "%")

    def show_status(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery_percentage, "%")

phone1 = MobilePhone("Apple", "Iphone 17 Pro Max", 78)

phone1.show_status()
phone1.charge(30)
phone1.use_phone(120)
phone1.show_status()
phone1.use_phone(500)
