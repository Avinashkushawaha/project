#Wap to check  if user enterd value is single value data type
value= eval(input("Enter a value : "))
type_of_value= type (value)
if type_of_value in [int, float, str, bool, complex]:
    print(f"The entered value is of single value data type")