import pymysql.cursors

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
                    print(row)
                    ret.append(row)
        finally:
            connection.close()
        return ret
class operand2():
    def get_operation():
        connection = connect()
        try:
            with connection.cursor() as cursor:
                sql = "select * from operation"
                cursor.execute(sql)
                print()
                ret=[]
                for row in cursor:
                    print(row)
                    ret.append(row)
        finally:
            connection.close()
        return ret


class main():
    def decorator():
        first = operand1.get_consultant()
        print("operand 1 is being decorated:")
        print()
        print("idconsultant \t name \t\t level \t structure \t commission \t\n")
        for row in first:
            print(row["idconsultant"], " \t ", row["name"], " \t ", row["level"], " \t ", row["structure"], " \t ", row["commission"], " \t")
        print("\n")
        
        second = operand2.get_operation()
        print("operand 2 is being decorated:")
        print()
        print("idoperation \t data_start \t data_finish \t\n")
        for row in second:
            print(row["idoperation"], " \t\t ", row["data_start"], "\t", row["data_finish"], "\t")
        print("\n")
if __name__ == "__main__": 
    main.decorator()
