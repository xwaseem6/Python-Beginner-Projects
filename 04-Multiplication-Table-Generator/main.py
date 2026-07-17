print("===== Multiplication Table Generator =====")

def table(number, table_limit):
    for i in range(1, table_limit + 1):
        print(number, "x", i, "=", number*i)

number = int(input("Enter a number: "))
table_limit = int(input("Enter the range of the multiplication table: "))

table(number, table_limit)