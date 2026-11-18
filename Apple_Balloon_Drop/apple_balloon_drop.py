rows = int(input("Enter row : "))
columns = int(input("Enter column : "))
matrix = []
global runs
runs = True
obj = ""
column = int()

def table_creation():
    for _ in range(rows):
        row_creation = []
        for _ in range(columns):
            row_creation.append(".")
        matrix.append(row_creation)
        row_creation = []

def show_table():
    for row in matrix:
        for col in row:
            print(col,end=" ")
        print()

table_creation()
show_table()

def getuser_choice():

    try:
        print(f"""User Choices : 
        1. Drop Apple in Column no: 
        2. Drop Balloon in Column no : 
        3. Exit""")


        global runs,obj,column

        user_input = input("Enter your choice and column no: ")
        user_choice = user_input.strip().split()
        print(user_input)
        print(user_choice)

        if len(user_choice) == 1 or len(user_choice)>2:
            if user_choice[0] == "3":
                print("Thank you..Visit again !!")
                runs = False
                return
            else:
                print("Enter valid Object and column no : ")
                return

        obj,column = user_choice
        column = int(column)
        obj = str(obj)

        if len(user_choice) == 2:
            print("I am here")

            if 0 < column <= columns:
                column = int(column)-1
            else:
                print(f"Enter column Number between 1 to {columns} ")
                return
            
            if obj == "1":
                obj = "A"

            elif obj == "2":
                obj = "B"
            else:
                print("Enter Valid details")
                return

    except ValueError:
        print("Enter Object name and Column number with spaces: ")



def drop_object(obj,column):

    for row in range(-1,-len(matrix)-1,-1):
        print(row)
        if "." in matrix[row][column]:
            matrix[row][column] = obj
            break

    else:
        print("Table full")
        global runs
        runs = False
        
while runs:
    getuser_choice()
    if runs:
        drop_object(obj,column)
    show_table()
