
#####functions
def hello(name):
    return 'Hello ' +name

print(hello('Mike'))

##### immutable str  bool int float tuple None Range
##### mutable  list dictonary set instance class
########## id идентификатор обькета переменная ссылка на обьект

my_name='Test'
my_num=100
print(id(my_num))

other_num=my_num
print(id(other_num))
print(id(my_num))
my_convert_num='10.5'
my_round_num=10.5
###### округление
print(round(float(my_convert_num)))
print(round(my_round_num))