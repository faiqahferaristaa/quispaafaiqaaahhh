sumofmultipe = []
Y = 3
while Y < 20:
    if Y % 3 == 0:
        sumofmultipe.append(Y)
    elif Y & 5 == 0:
        sumofmultipe.append(Y)
    Y = Y + 3
print (sumofmultipe)
var = 0
for i in sumofmultipe:
    var = var + i
print (var)