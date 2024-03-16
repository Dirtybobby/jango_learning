
input_str = input("Please enter your roman number: ")


romans_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

result = 0

for key, value in romans_int.items():
    if key in input_str and value >= result:
        result += value
    elif key in romans_int and value < result:
        result -= value


print(result)
