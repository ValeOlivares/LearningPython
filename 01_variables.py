#Variables
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 3 
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#concatenación de variables
print(my_string_variable, my_int_variable, my_bool_variable)

#pasar una var a string
my_int_to_str = str(my_int_variable)
print(type(my_int_to_str))

#length
print(len(my_string_variable))

#variables en una sola linea (hoy en pésimas ideas)
name, surname, alias, age = "Vale", "Olivares", "hamster" , 37
print("Me llamo", name, surname, "tengo" , age, "años", "y me dicen", alias)

#Inputs
name = input("Cómo te llamas?? ")
print(name)

#Forzar el tipo de la variable
address: str = "Mi dirección 123"
address("32")
print(address)