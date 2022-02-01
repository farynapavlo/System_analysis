import pymysql.cursors
import os
import keyboard


print_db_row=True
type_test=False


def connect():

    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "qwertyui",
        db = "sys_analis",
        charset = "utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
        )
    print("connected successfully!!!")
    return connection

#######################################additional module##################
def cls():
    os.system(['clear','cls'][os.name == 'nt'])
cls()

stop=False
def stop():
    global stop
    stop=True
keyboard.add_hotkey('esc', stop)

def create_main_menu(menu):
    global show_menu
    for i in range(0, len(menu)):
        show_menu.append("  ")
        menu[i]+="\n"
        show_menu[i+1]+=menu[i]
    cls()
    for e in show_menu:
        print(e, end="")
        
def upchose():
    global show_menu
    global current
    global menu
    if (current>0):
        show_menu[current]=show_menu[current-1]
        show_menu[current-1]=">"
        current-=1
        cls()
        print()
        for e in show_menu:
            print(e, end="")
            
def downchose():
    global show_menu
    global current
    global menu
    if (current<len(menu)-1):
        show_menu[current]=show_menu[current+1]
        show_menu[current+1]=">"
        current+=1
        cls()
        print()
        for e in show_menu:
            print(e, end="")
            
def enter():
    global show_menu
    global current
    cls()
    print()
    for e in show_menu:
        print(e, end="")
    chose(show_menu[current+1])

menu=["consultant", "polis", "operation"]
show_menu=[">"]
current=0
output=["\n", " "]

create_main_menu(menu)

def chose(point):
    chose={"  consultant\n" : operand1.get_consultant,
           "  polis\n" : operand2.get_polis,
           "  operation\n" : operand3.get_operation
        }
    printer.show_beautifully(main.adapter(chose[point]()))
    chose[point]

#######################################################################
    
class printer():
    def show_beautifully(array):
        for x in array:
            for y in x:
                if(type(y)==type("test") and len(y)<9):
                    print(y, "\t\t\t", end=" ")
                elif(type(y)==type("test") and len(y)<17):
                    print(y, "\t\t", end=" ")
                elif(type(y)==type("test") and len(y)>17):
                    print(y, "\t", end=" ")
                elif(type(y)==type(type_test)):
                    print(y, "\t\t", end=" ")
                else:
                    print(y, "\t\t\t", end=" ")
            print("\n", end=" ")

class operand1():
    def get_consultant():
        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = "select * from consultant"
                cursor.execute(sql)
                print()
                ret=[]
                for row in cursor:
                    if (print_db_row==True):
                        print(row)
                    ret.append(row)
        finally:
            connection.close()
        return ret

class operand2():
    def get_polis():
        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = "select * from polis"
                cursor.execute(sql)
                print()
                ret=[]
                for row in cursor:
                    if (print_db_row==True):
                        print(row)
                    ret.append(row)
        finally:
            connection.close()
        global type_test
        type_test=ret[0]["name"]
        return ret

class operand3():
    def get_operation():
        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = "select * from operation"
                cursor.execute(sql)
                print()
                ret=[]
                for row in cursor:
                    if (print_db_row==True):
                        print(row)
                    ret.append(row)
        finally:
            connection.close()
        return ret

class main():
    def adapter(dbarray):
        output=[]
        a=[]
        for b in dbarray[0]:
            a.append(b)
        output.append(a)
        for row in dbarray:
            elements=[]
            for element in row:
                elements.append(row[element])
            output.append(elements)
        return output

keyboard.add_hotkey('up', upchose)
keyboard.add_hotkey('down', downchose)
keyboard.add_hotkey('enter', enter)

while True:
    if (stop==True):
        break


#####
