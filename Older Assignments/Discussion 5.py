class Example:
    def __init__(self):
        #"private" variable
        self._number = 0
        #"mangled name" variable
        self.__sum = 0

    def check(self):
        print("Your number is:",self._number)
        print("Your sum is:",self.__sum)

Ex = Example()
Ex.check()

#generator example
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")
    #Warning, you WILL need to force this to quit.