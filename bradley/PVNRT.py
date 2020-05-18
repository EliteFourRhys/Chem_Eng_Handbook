

def main():
    try:
        param = user_input()
        if param == "pressure" or param == "p":
            calculate_p()
        elif param == "temperature" or param == "t":
            calculate_t()
        elif param == "volume" or param == "v":
            calculate_v()
        elif param == "moles" or param == "n":
            calculate_n()
        elif param == "gas constant" or param == "R":
            print("That would be 8.314 J/(mol*K), please stop being silly")
        else:
            print("that didn't work, try entering a letter from PV=nRT")
    except:
        print("that didn't work, try entering a letter from PV=nRT")


def user_input():
    param = input("Which parameter in PV=nRT are you trying to find? (e.g. enter 'Pressure' or 'P'):\n").lower()
    return param

def calculate_p():
    p_value = (moles() * 8.314472 * temperature()) / volume()
    print("The value for pressure is " + str(p_value) + " kPa")

def calculate_n():
    mol_value = (pressure() * volume()) / ( 8.314472 * temperature())
    print("The answer is " + str(mol_value) + " moles")

def calculate_v():
    v_value = (moles() * 8.314472 * temperature()) / pressure()
    print("The value for volume is " + str(v_value) + " L")

def calculate_t():
    t_value = (pressure() * volume()) / (8.314472 * moles())
    print("The value for pressure is " + str(t_value) + " K")

def pressure():
    P = print(input("Enter the pressure value followed by its units (e.g. 101325 kPa): ")).lower()
    pressure_value = [int(word) for word in P.split() if word.isdigit()]
    if 'atm' in P:
        pressure_value = pressure_value * 101.325
    elif 'pa' in P:
        pressure_value = pressure_value * 0.001
    elif 'mmhg' or 'torr' in P:
        pressure_value = pressure_value * 0.133322
    elif 'bar' in P:
        pressure_value = pressure_value * 100
    elif 'mmhg' in P:
        pressure_value = pressure_value * 0.133322
    elif 'kpa' in P:
        return pressure_value
    else:
        print("try entering a pressure in either: atm, Pa, kPa, mmHg, bar, or torr")
    return pressure_value

def volume():
    V = print(input("Enter the volume value followed by its units (e.g. 12 m^3, 12 m3, 12 L): ")).lower()
    volume_value = [int(word) for word in V.split() if word.isdigit()]
    if 'm3' or 'm^3' in V:
        volume_value = volume_value * 1000
    elif 'cm3' or 'cm^3' in V:
        volume_value = volume_value * 0.001
    elif 'ft3' or 'ft^3' in V:
        volume_value = volume_value * 28.3168
    elif 'in3' or 'in^2' in V:
        volume_value = volume_value * 0.0163871
    elif 'gal' or 'gallons' in V:
        volume_value = volume_value * 4.54609
    elif 'ml' or 'millilitres' in V:
        volume_value = volume_value * 0.001
    elif 'l' or 'litres' in V:
        return volume_value
    else:
        print("try entering a volume in either: m3, cm3, ft3, in3, gal, mL, L")
    return volume_value

def temperature():
    T = print(input("Enter the temperature value followed by its units (e.g. 12 C, 12 Celcius, 12 degrees celcius): ")).lower()
    temperature_value = [int(word) for word in T.split() if word.isdigit()]
    if 'c' or 'degrees celcius' or 'celcius' in T:
        temperature_value = temperature_value + 273.15
    elif 'f' or 'degrees fahrenheit' or 'fahrenheit' in T:
        temperature_value = (temperature_value - 32) * (5/9) + 273.15
    elif 'k' or 'kelvin' or 'kelvins' in T:
        return temperature_value
    else:
        print("try entering a temperature in either: C, F, or K")
    return temperature_value

def moles():
    n = print(input("Enter the value for the amount of moles. If not stated in the question, assume 1 mol (only enter the value): ")).lower()
    return n

main()

