print("starting line")
a=[11,22,33]

try:
    a=10/0
    print(a[5])
    print(y)
except ZeroDivisionError:
    print("exception rised due to zero divion error")
except IndexError:
    print("exception rised due to index out of bound")
except NameError:
    print("expection rised due to undefined variable")
except:
    print("some exception raised")
else:
    print("No expection raised")
finally:
    print("This is a finally block")
print("outside try block")
