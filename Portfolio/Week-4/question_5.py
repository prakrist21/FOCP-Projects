'''
Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. Test both functions. (Google will find you the formulae).
'''
def convertCelcius(temp):
    '''
    This function takes fahrenheit temprature as argument,then converts and returns it into celcius temprature. 
    '''
    Celcius=round((temp - 32) * 5/9,2)
    print(Celcius)

def convertFahrenheit(temp):
    '''
    This function takes celcius temprature as argument,then converts and returns it into fahrenheit temprature. 
    '''
    fahrenheit=round((temp * 9/5) + 32,2)
    print(fahrenheit)


convertCelcius(20)
convertFahrenheit(20)

