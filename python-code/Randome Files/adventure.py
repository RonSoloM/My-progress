carsBrand = ['Honda', 'Black', 'BMW', 'Ferrari']

Picker = input()

if Picker in carsBrand:
    print("We got this car and it's number {} in our list".format(len(Picker)))
else:
    print("We don't have this car")
