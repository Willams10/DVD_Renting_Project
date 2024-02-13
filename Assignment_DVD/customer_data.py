class Customerdata:
    def __init__(self, first_name, last_name, account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number

    def get_acc_no(self):
        return self.account_number

    def __lt__(self, other):
        return self.account_number < other.account_number

    def __str__(self):
        output = "| {0:<20} | {1:<20} | {2:<20} |".format(
            self.first_name, self.last_name, self.account_number)
        return output


if __name__ == '__main__':
    customers = []
    customers.append(Customerdata("Ashley", "Lisa", "C123456789"))
    customers.append(Customerdata("Steven", "Margaret", "C234567891"))
    customers.append(Customerdata("Benjamin", "Smith", "C345678912"))
    customers.append(Customerdata("Douglas", "Samantha", "C123456789"))
    customers.append(Customerdata("Daniel", "Joyce", "C234567891"))
    customers.append(Customerdata("Benjamin", "Jennie", "C345678912"))

    header = "+----------------------+----------------------+----------------------+"
    print(header)
    print("| First Name           | Last Name            | Account Number       |")
    print(header)
    for customer in customers:
        print(customer)
    print(header)
