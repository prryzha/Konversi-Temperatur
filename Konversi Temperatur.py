def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Masukkan suhu dalam derajat Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} derajat Celcius = {fahrenheit} derajat Fahrenheit")

if __name__ == "__main__":
    main()
