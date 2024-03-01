import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

    def show_information(self):
        logging.info(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


# Creating an instance of the Car class
my_car = Car('Toyota', 'Corolla', 2020)

# Printing the object
logging.info(my_car)
my_car.show_information()
