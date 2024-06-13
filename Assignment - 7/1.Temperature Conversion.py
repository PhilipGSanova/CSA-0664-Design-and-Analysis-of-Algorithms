def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [round(kelvin, 5), round(fahrenheit, 5)]

# Example usage:
celsius_input_1 = 36.50
celsius_input_2 = 122.11

output_1 = convert_temperature(celsius_input_1)
output_2 = convert_temperature(celsius_input_2)

print(f"Input: {celsius_input_1} => Output: {output_1}")
print(f"Input: {celsius_input_2} => Output: {output_2}")
