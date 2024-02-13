from customer_bst_all_data import Customer_BST
from dvdlistdata import LinkedlistDVD
from dvd_rented_lists import Rent

MENU_RENT_DVD = "1"
MENU_RETURN_DVD = "2"
MENU_CREATE_lIST_OF_DVD = "3"
MENU_PRINT_DVD_LISTS = "4"
MENU_CHECK_DVD_AVAL = "5"
MENU_ADD_CUSTOMER_DATA = "6"
MENU_PRINT_RENTED_DVD = "7"
MENU_CUSTOMER_LIST = "8"
MENU_Quit = "9"


def main():
    menu = f"{MENU_RENT_DVD}.Rent a DVD ?\n" \
           f"{MENU_RETURN_DVD}.Return DVD ?\n" \
           f"{MENU_CREATE_lIST_OF_DVD}.Create list of DVDs ?\n" \
           f"{MENU_PRINT_DVD_LISTS}.print DVD lists ?\n" \
           f"{MENU_CHECK_DVD_AVAL}.Check DVD available ?\n" \
           f"{MENU_ADD_CUSTOMER_DATA}.Add Customer Data ?\n" \
           f"{MENU_PRINT_RENTED_DVD}.Print a list of all DVDs rented by Customer ?\n" \
           f"{MENU_CUSTOMER_LIST}.Show customer list ? \n" \
           f"{MENU_Quit}.Quit the system ?\n" \
           "------->    "
    customers = Customer_BST()
    customers.load_all_customer()
    rents = Rent()
    dvds = LinkedlistDVD()
    dvds.load_dvds()
    option = input(menu)
    while option != MENU_Quit:
        if option == MENU_RENT_DVD:
            rents.insert_rented_dvd_list()
        elif option == MENU_RETURN_DVD:
            rents.return_rented_dvd_list()
        elif option == MENU_CREATE_lIST_OF_DVD:
            dvds.insert_dvd()
        elif option == MENU_CHECK_DVD_AVAL:
            rents.check_dvd()
        elif option == MENU_PRINT_DVD_LISTS:
            dvds.display_dvd()
        elif option == MENU_ADD_CUSTOMER_DATA:
            customers.add_cust()
        elif option == MENU_PRINT_RENTED_DVD:
            print(rents)
        elif option == MENU_CUSTOMER_LIST:
            customers.display_data()
        else:
            print()
        option = input(menu)

    print(">>>>Bye Bye! Have A Good Day !<<<<")


if __name__ == '__main__':
    main()
