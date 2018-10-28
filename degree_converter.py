# A degree converter from (C) to (F) and from (F) to (C)

c = int(input("Enter a Celsius degree as an integer to convert it in Fahrenheit: "))
f = int(input("Enter a Fahrenheit degree as an integer to convert it in Celsius: "))

# Celsius to Fahrenheit
def cels(c):
    res_1 = "Fahrenheit: " + str(c*1.8 +32)
    return res_1
    
print(cels(c))
    
# Fahrenheit to Celsius
def fahr(f):
    res_2 = "Celsius: " + str((f - 32) * 5/9)
    return res_2
    
print(fahr(f))
