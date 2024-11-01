def get_car(**kwargs):
    print(kwargs)
    return kwargs


get_car(brand="BMW",
        model="M5",
        price=80000,
        max_speed=270)
