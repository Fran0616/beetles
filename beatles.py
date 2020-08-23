#The beatles line up
#empty list name beetles
beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("The beatles consist of ", beatles)
print("Both name must be enter as written below\n")

for i in beatles:
    i = input("Enter the name \"Stu Sutcliffe\": ")
    x = input("Enter the name \"Pete Best\": ")
    if i == "Stu Sutcliffe" and x == "Pete Best" :
        beatles.append(i)
        beatles.append(x)
        print("The beatles consist of ", beatles)
        break 
print("Will now remove Peter Best and Stu Sutcliffe from the group")
#Deleting Stu Sutcliffe
del beatles[3]
#Deleting Pete Best
del beatles[3]
print("The beatles consist of ", beatles)
print("Lets add Ringo Starr to the list ")
beatles.insert(0, "Ringo Starr")
print("The beatles now consist of: ", beatles)
