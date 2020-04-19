# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name

# Ask the user for their last name


# if first name is < 10 characters and last name is < 10 characters

#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName
firstname= input('enter your first name')
lastname= input('enter your last name')
total1=0
for i in firstname:
    total1= total1 + 1
print(total1)

total2=0
for w in lastname:
    total2=total2+1
print(total2)

if total1 <10 and total2 <10 :
    print("" + firstname +" " +lastname)
elif total1>= 10  and  total2 < 10:
    name=firstname[0]
    print("" + name +" " +lastname)
elif total1 < 10  and  total2 >= 10:
    name2=lastname[0]
    print("" + name2 +" " +firstname)
else:
    print('mummy ko bolo naam chota kare')
