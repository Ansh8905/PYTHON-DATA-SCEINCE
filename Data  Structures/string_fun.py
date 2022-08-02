from cgi import print_environ
import string


name = "something serious is Noot HaPPening"

#formatting function
print(name)
print( name.upper() )
print( name.lower() )
print( name.capitalize() )
print( name.title() )
print( name.swapcase() )
print( name.casefold() )

word = "python"

#left align
print( word.ljust(80))
#right align
print( word.rjust(80))
#center align
print( word.center(80))

#fill char
print( word.ljust(80 , '-'))
print( word.rjust(80, '$'))
print( word.center(80, '~'))

#printing a formatted table of 3
print ('-'*40)
for i in range (1,11):
    r= 3 ** i 
    print(3,'x',str(i).rjust(2),'=',r)