#Python Queue Simulation

names = []
for x in range(10):
    acceptedName = input('Enter name: ')
    names.append(acceptedName)
print(names)

for x in range(len(names)):
    print(names.pop(0))
print(names)
    



    
