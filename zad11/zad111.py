def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name},  кухня:  {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан сейчас открыт.")


    newRestaurant = Restaurant("'У Морио'","итальянская")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name} Кухня: {self.cuisine_type}.")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")


    restaurant1 = Restaurant("'Луи'", "Итальянская")
    restaurant2 = Restaurant("'Мама'", "Домашняя")
    restaurant3 = Restaurant("'Хаттори Ханзо'", "Японская")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}кухня: {self.cuisine_type}.")

        def open_restaurant(self):
            print("Ресторан сейчас открыт.")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} Был обновлен до  {self.rating}.")

    restaurant1 = Restaurant("'Итальяно'", "Итальянская", 3)

    print(f"Изначальынй рейтинг ресторана {restaurant1.restaurant_name}   {restaurant1.rating} ." )

    restaurant1.update_rating(5)
    print(f"Новый, обновленный рейтинг  {restaurant1.restaurant_name} : {restaurant1.rating}.")
z1()
z2()
z3()