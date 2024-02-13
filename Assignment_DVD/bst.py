from customer_data import Customerdata
import sqlite3


class Node:
    def __init__(self, customer_data):
        self.left = None
        self.right = None
        self.data = customer_data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, customer_data):
        new_node = Node(customer_data)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root

        while True:
            if customer_data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

    def search(self, customer_data):
        current_node = self.root
        while current_node is not None:
            if customer_data == current_node.data:
                return True
            elif customer_data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def c_search(self, acc_no):
        current_node = self.root
        while current_node:
            if acc_no == current_node.data.get_acc_no():
                return current_node.data
            elif acc_no < current_node.data.get_acc_no():
                current_node = current_node.left
            else:
                current_node = current_node.right

    def in_order_traversal(self, current_node):
        if current_node:
            self.in_order_traversal(current_node.left)
            print(current_node.data)
            self.in_order_traversal(current_node.right)


    def show_customer_data(self):
        conn = sqlite3.connect("dvd_Store.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM customer;"

        cursor.execute(sql)
        customers = BinarySearchTree()
        c_data = cursor.fetchall()
        for cust in c_data:
            customers.insert(Customerdata(cust[0], cust[1], cust[2]))


if __name__ == '__main__':
    customers = BinarySearchTree()

    customer1 = Customerdata("Test1", "test1", "00001")
    customer2 = Customerdata("Test2", "test2", "00002")
    customer3 = Customerdata("Vulgar", "Bin", "00003")
    customer4 = Customerdata("Test4", "test4", "00004")
    customer5 = Customerdata("Test5", "test5", "00005")

    customers.insert(customer1)
    customers.insert(customer2)
    customers.insert(customer3)
    customers.insert(customer4)
    customers.insert(customer5)
    print(customers.c_search("00003"))
    print()
    customers.in_order_traversal(customers.root)




