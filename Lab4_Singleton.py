import pymysql.cursors

print_db_row = False
type_test = False


def connect():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="qwertyui",
        db="sys_analis",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("connected successfully!!!")
    return connection


class operand():
    def get_consultant():
        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = "select * from consultant"
                cursor.execute(sql)
                print()
                ret = []
                for row in cursor:
                    if (print_db_row == True):
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
                ret = []
                for row in cursor:
                    if (print_db_row == True):
                        print(row)
                    ret.append(row)
        finally:
            connection.close()
        global type_test
        type_test = ret[0]["name"]
        return ret


class printer():
    def show_beautifully(array):
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
        output = []
        a = []
        for b in dbarray[0]:
            a.append(b)
        output.append(a)
        for row in dbarray:
            elements = []
            for element in row:
                elements.append(row[element])
            output.append(elements)
        return output


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        print("here take your singleton inctance...\n")
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")

        else:
            Singleton.__instance = printer.adapter(operand.get_polis())
            printer.show_beautifully(Singleton.__instance)


o = Singleton()

s = Singleton.getInstance()
print(s, "\n")


def try_to_create():
    try:
        print("trying to create singleton instance once again...")
        t = Singleton()
    except Exception:
        print('we got Exception("This class is a singleton!")')
        print("Not able to create singleton instance twice. ")
        print("Trying to get singleton instance...")
        t = Singleton.getInstance()
        print(t, "\n")
        print("We got singleton instance!")


try_to_create()


