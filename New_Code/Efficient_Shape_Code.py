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