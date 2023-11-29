#MATCH statement
# a = int( input("Entet the number:"))

# def matchfun(a):
#     match a:
#         case 1:
#              print("welcome 1")
#         case 2:
#             print("welcome 2")
#         case _://this is similar to default case
#             print("nothing")
# matchfun(a)


b = input("Enter name:")
def wel(b):
    print("welcome "+b)
def namematch(b):
    match b:
        case "aa":
            wel(b)
        case "bb" :
            wel(b)
        case _:
            print("not")
namematch(b)
