import pymysql.cursors
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

class printer():
    def show_beautifully(array):
        print()
        for x in array:
            for y in x:
                if(type(y)==type("test") and len(y)<9):
                    print(y, "\t\t", end=" ")
                elif(type(y)==type("test") and len(y)<17):
                    print(y, "\t\t", end=" ")
                elif(type(y)==type("test") and len(y)>17):
                    print(y, "\t", end=" ")
                elif(type(y)==type(type_test)):
                    print(y, "\t\t", end=" ")
                else:
                    print(y, "\t\t", end=" ")
            print("\n", end=" ")

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

class operand():
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

    def get_opperation():
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


class main():
    def get_table(table_name):
        chose={"consultant" : operand.get_consultant,
               "opperation" : operand.get_opperation,
               "polis" : operand.get_polis}
        printer.show_beautifully(printer.adapter(chose[table_name]()))




print("available tables: \n consultant\n polis\n operation\nchose needed one:")

main.get_table('consultant')