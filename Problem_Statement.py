#Problem Statement 
'''Develop a Shopping List Manager using Python that allows a user to manage 
items required for shopping. The program should allow users to add items, 
remove items, display the list, search items, and count the total number of items 
using a list data structure. 

Functional Requirements 
    The system should provide the following operations: 
        1. Add Item – Add a new item to the shopping list. 
        2. Display Items – Display all items in the list. 
        3. Search Item – Search an item in the list. 
        4. Remove Item – Remove an item from the list. 
        5. Count Items – Display total number of items in the shopping 
            list. 
        6. Exit – Exit the program.
'''
Shopping_list = []

while True:
    print("\n1.Add Item")
    print("2.Display Items")
    print("3.Search Item")
    print("4.Remove Item")
    print("5.Count Items")
    print("6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        item = input("Enter item: ")
        Shopping_list.append(item)
        print("Item added")

    elif ch == 2:
        print("Shopping List:")
        for i in Shopping_list:
            print(i)

    elif ch == 3:
        item = input("Enter item to search: ")
        if item in Shopping_list:
            print("Item found")
        else:
            print("Not found")

    elif ch == 4:
        item = input("Enter item to remove: ")
        if item in Shopping_list:
            Shopping_list.remove(item)
            print("Item removed")
        else:
            print("Not found")

    elif ch == 5:
        print("Total items:", len(Shopping_list))

    elif ch == 6:
        print("Exit")
        break

    else:
        print("Invalid choice")


#Output:----->
'''1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 1
    Enter item: pen
    Item added

    1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 2
    Shopping List:
    pen

    1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 3
    Enter item to search: pen
    Item found

    1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 4
    Enter item to remove: pen
    Item removed

    1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 5
    Total items: 0

    1.Add Item
    2.Display Items
    3.Search Item
    4.Remove Item
    5.Count Items
    6.Exit
    Enter choice: 6
    Exit
    '''