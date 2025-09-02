import os 


# Select the directory whose contant you want list
direction_path = '/'

# Use the os module to list the directory contant
contents = os.listdir(direction_path)


#  print the contants of the direction   
print(contents)
