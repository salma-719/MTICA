def kelvinToFarenheit(Temperature):
    assert (Temperature >=0),"colder than zero to MTICA!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print (kelvinToFarenheit(-50))
except Exception as ob:
    print(ob)
try:
    print (kelvinToFarenheit(273))
except Exception as ob:
    print(ob)
try:
    print (kelvinToFarenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print (kelvinToFarenheit(-5))
except Exception as ob:
    print(ob)
print("Thank you")
    
    
