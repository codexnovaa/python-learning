#  variable score = where a variable is visible and accessible
#  scope resolution = LEGB --- Local => Enclosed => Global => Built in


def func1():
    x = 1
    
    def func2():
        print(x)
    
    func2()
    
func1()