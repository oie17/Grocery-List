#Jalen Grimes and Oliver Greco 
# 01/10/2024
#Grocery List 

#Functions 

def grocerylistapp(): 
    glist=[]
    print(" 1. Add an item to the grocery list \n 2. View current list \n 3. Check item off \n 4. Remove item from list \n 5. Remove all items from list \n 6. Sort items alphabetically \n 7. Print # of items\n 8. Exit list ")
    while True:
        ans= int(input(" Insert the number corresponding to the option you choose"))
        
        if ans== 1:
            newitem= str(input("What item do you want to add to the list?"))
            glist.append(newitem)
        elif ans== 2: 
            print(glist)
        elif ans== 3: 
            checkitem= str(input("Which item do you want to check off?"))
            itemposition= (glist.index(checkitem))
            glist.pop(itemposition)
            glist.insert(itemposition, checkitem +"X")
        elif ans== 4: 
            olditem= str(input("Which item do you want to remove from the list?"))
            glist.remove(olditem)
        elif ans==5:
            clear=str(input("Are you sure you'd like to clear the list? (y/n)"))
            if clear=="y":
                glist.clear()
            else:
                grocerylistapp()
        elif ans==6:
            glist.sort()
            print(glist)
        elif ans==7:
            print(str(len(glist))+" items in your list.")
        elif ans== 8:
            break
        else: 
            print("Not valid selection")
            grocerylistapp()
#Main
grocerylistapp()