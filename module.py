#Modules -- file containing code you want to include in your program
            # use 'import' to include a module (built-in or your own)
            # useful to break up a large program reusable separate files
            
import math as m
import examplemodule as exampleMath

print(m.pi)
print(exampleMath.e(2))
print(exampleMath.pi)
print(f"{exampleMath.area(3):.2f}")
print(f"{exampleMath.circumference(3):.2f}")