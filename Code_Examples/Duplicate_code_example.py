
#Duplicate code example
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

def calculate_surface_area(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

'''
# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
def calculate_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
'''

def calculate_shape_measurement(measurement, length, width, height=0):
    area = length * width
    measurement = measurement.lower()
    match measurement:
        case "area":
            return area
        case "perimeter":
            return 2 * (length + width)
        case "volume":
            return area * height
        case "surface area":
            return 2 * (area + length * height + width * height)
        case _:
            return "Please specify a valid shape measurement, such as area, perimeter, volume or surface area."