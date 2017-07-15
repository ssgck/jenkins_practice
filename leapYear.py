class LeapYear:
    lst = []
    for i in range(1900,2021):
        if i%4 == 0 :
            if i%100 ==0:
                if i%400 ==0:
                    lst.append(str(i))
            else:
                lst.append(str(i))
    print 'Leap years between 1900 and 2020 are ', ' '.join(lst)