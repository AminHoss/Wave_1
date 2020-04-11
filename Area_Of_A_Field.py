length = float(input("What length is the field in feet? "))
width = float(input("What width is the field in feet? "))
area = (length * width) / 43560
if area == 1:
    print("The area of the field is {} acre".format(area))
else:
    print("The area of the field is {} acres".format(area))
