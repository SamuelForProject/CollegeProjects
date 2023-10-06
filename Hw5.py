
def display_welcome():
    print("Welcome to Feet and Meters Converter""\n")

def display_menu():
    print("Conversion Menu: ""\n""a.Feet to Meters""\n""b.Meters to Feet")
    answer = input("Select conversion(a/b): ")
    while answer != "a" and answer != "b":
        print("\n""You did not enter a valid selection""\n")
        qu = input("Would you like to perform another conversion (y/n): ")
        if qu == "n":
            print("Thanks!, Bye")
            quit()
        display_menu()
        return answer
    return answer

def feet_to_meters(num):
    meters = num * 0.3048
    return (f"{meters:.2f}")

def meters_to_feet(num):
    feet = num / 0.3048
    return (f"{feet:.2f}")

def mainfunc(num, ftmOrMtf):
        while num <0:
           num = float(input("Enter a postive number: "))
        if ftmOrMtf == "ftm":
            print(f"{feet_to_meters(num)} feet")
        elif ftmOrMtf =="mtf":
            print(f"{meters_to_feet(num)} feet")
        again = input("\n""Would you like to perform another conversion (y/n): ")
        return again

while True:
    display_welcome()
    while display_menu() == "a":
        break
    if mainfunc(float(input("\n""Enter the feet:")), "ftm")=="n":
        print("Thanks Bye!")
        break
    while display_menu() == "b":
        break  
    if mainfunc(float(input("\n""Enter the meters:")),"mtf") == "n":
        print("Thanks, Bye!")
        break



    
        
    


