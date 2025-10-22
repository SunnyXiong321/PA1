my_schedule = open("schedule.txt") #by default opens in read mod, can open in write or append mode

my_schedule = open("schedule.txt", "w") #write mode
my_schedule.write ("Changing content!") #overwrites all files contents

my_schedule.open ("schedule.txt", "a")#append mode
my_schedule.write ("adding content!") #adds to the end of the file content


'''
to create a new file in python, just open one that doesn't exist in an edit mode or "x" mode
'''

new_file = open("new_file.txt", "w") #just creates new file
new_file.write ("YO")

new_file.close()

new_file.write()
'''
#writes a while loop that looks for "Mod 2"
#then write a for loop that prints out Mod 2 schedule

line = my_schedule.readline() #control variable for while loop

while my_schedule.read(6) !="Mod 2\n":
    my_schedule.readline() #advance cursor until we find mod:2

print (line) #print the mod 2 label

for i in range (3):
    print (my_schedule.readline()) #print the next 3 lines
'''