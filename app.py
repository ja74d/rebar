import math

As = int(input('ENTER As:'))

list_of_standard_reber = [6, 8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 50]

#sqrt = math.sqrt(f)

# 3фx
def three():

    a = 4*As
    b = 3*math.pi

    d = math.sqrt(a/b)

    print(d)

    p = []

    for i in list_of_standard_reber:
        f = i - d
        p.append(f)

    for j in p:
        if j >= 0 and j <=3:
            indx3 = p.index(j)
            #print(indx)

    print(list_of_standard_reber[indx3])


# 4фx

def four():

    a = As
    b = math.pi

    d = math.sqrt(a/b)

    print(d)

    p = []

    for i in list_of_standard_reber:
        f = i - d
        p.append(f)

    for j in p:
        if j >= 0 and j <=3:
            idx4 = p.index(j)
            #print(indx)

    print(list_of_standard_reber[idx4])

three()
four()