#!/usr/bin/env python3
# by rog

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return (', '.join(cars['Jeep']))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [value[0] for value in cars.values()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    my_list = []
    for models in cars.values():
        for model in models:
            if grep.lower() in model.lower():
                my_list.append(model)
    return sorted(my_list)
    # return [model for model in models if grep.lower() in model.lower()] for models in cars.values()


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for key in cars.keys():
        cars[key] = sorted(cars[key])
    return cars

