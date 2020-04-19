# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
firstname= input('enter your first name')
name= firstname[0]
print(name)
if name =='A' or name == 'B':
    print('go room AB')
elif name == 'C':
       print('go to room CD')
else:
    lastname= input('enter your last name')
    name2=lastname[0]
    if name =='Z':
        print('go room z')
    else:
        print('go to other room')