import sqlite3
from bst import BinarySearchTree
from customer_data import Customerdata


def database_connection():
    return sqlite3.connect("dvd_Store.db")


class Customer_BST:
    def __init__(self):
        self.bst = BinarySearchTree()

    def load_all_customer(self):
        conn = database_connection()
        try:
            cursor = conn.cursor()
            sql = "SELECT * FROM customer;"
            cursor.execute(sql)
            c_data = cursor.fetchall()
            c_data =[list(t) for t in c_data]
            for cust in c_data:
                self.bst.insert(Customerdata(cust[0], cust[1], cust[2]))

        except sqlite3.Error as error:
            print(f"Something went wrong!!!! {error}")
        finally:
            if conn:
                conn.close()

    def display_data(self):
        print("+----------------------+----------------------+----------------------+")
        print("| First Name           | Last Name            | Account Number       |")
        print("+----------------------+----------------------+----------------------+")
        self.bst.in_order_traversal(self.bst.root)
        print("+----------------------+----------------------+----------------------+")

    def add_cust(self):
        conn = database_connection()
        print()
        first_name = input("Your First Name --> ")
        last_name = input("Your Last Name --> ")
        while True:
            try:
                account_number = int(input("Account Number: "))
                cursor = conn.cursor()
                query = "INSERT into customer values (?,?,?)"
                cursor.execute(query, [first_name, last_name, account_number])
                conn.commit()
                self.bst.insert(Customerdata(first_name, last_name, account_number))
                print("Customer added!")
                break
            except sqlite3.Error as error:
                print(f"Something went wrong!!!! {error}")
            finally:
                if conn:
                    conn.close()


if __name__ == '__main__':
    customer = Customer_BST()
    customer.load_all_customer()
    customer.display_data()
    customer.add_cust()
    customer.display_data()
