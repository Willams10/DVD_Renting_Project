import sqlite3
from dvdlistdata import LinkedlistDVD
import datetime
from customer_bst_all_data import Customer_BST


class Rent:

    def __init__(self):
        self.rental_id = None
        self.rental_list = self.get_rental_data()
        self.mov = LinkedlistDVD()
        self.mov.load_dvds()
        self.cbst = Customer_BST()
        self.cbst.load_all_customer()

    def get_rental_data(self):
        try:
            conn = sqlite3.connect("dvd_Store.db")
            cursor = conn.cursor()
            query = "SELECT * FROM rented_dvd_list ORDER BY rent_id;"
            cursor.execute(query)
            rental_data = cursor.fetchall()
            rental_data = [list(t) for t in rental_data]
            self.rental_id = max(rental_data)[0]
            return rental_data
        except sqlite3.Error as error:
            print(error)
        finally:
            if conn:
                conn.close()

    def __str__(self):
        output = ""
        output += "+----------------+---------------------------------+-------------------+-------------------+--------------------+\n"
        output += "| Rent ID        | Movie Name                      | Rented Date       | Returned Date     | Account Number     |\n"
        output += "+----------------+---------------------------------+-------------------+-------------------+--------------------+\n"
        for rental in self.rental_list:
            rent_id = rental[0]
            movie_name = rental[1]
            rented_date = rental[2]
            return_date = rental[3]
            account_number = rental[4]
            output += "|{:<14} | {:<32} | {:<17} |{:<18} |{:<19} |\n".format(rent_id, movie_name, rented_date,
                                                                             return_date if return_date is not None else "Not return yet!",
                                                                             account_number)
        output += "+----------------+---------------------------------+-------------------+-------------------+--------------------+"
        return output

    def check_dvd(self):
        movie_name = input("Movie Name: ")
        movie = self.mov.find_dvd(movie_name)
        if movie is not None:
            print(f"The movie {movie_name} is available.")
            print(f"The available copies in the store for this movie is {movie.number_copies}")
            return movie
        else:
            print(f"Sorry! The movie {movie_name} is not found.")
            return None

    def insert_rented_dvd_list(self):
        movie = self.check_dvd()
        if movie is None:
            return
        r_movie_name = movie.movie_name
        num_copies = movie.number_copies
        acc_number = None
        if num_copies <= 0:
            print(f"The movie {r_movie_name} is out of stock!")
        else:
            try:
                acc_number = int(input("What is your account number -> : "))
                if self.cbst.bst.c_search(acc_number) is None:
                    print("There is no customer account number in the system!")
                    return
            except ValueError:
                print("Account Number is Numeric number. Please check your data Again!!!")

        try:
            conn = sqlite3.connect("dvd_Store.db")
            c = conn.cursor()
            i_query = "INSERT INTO rented_dvd_list VALUES(?,?,?,?,?);"
            current_date = datetime.datetime.now().strftime("%d/%m/%Y")
            self.rental_id += 1
            c.execute(i_query, (self.rental_id, r_movie_name, current_date, None, acc_number))
            u_dvd_query = f"UPDATE dvd SET number_copies = {num_copies - 1} WHERE movie_name = '{r_movie_name}' "
            c.execute(u_dvd_query)
            conn.commit()
            self.rental_list.append([self.rental_id, r_movie_name, current_date, None, acc_number])
            movie.number_copies = num_copies - 1
            print(f"Your dvd rental with id - {self.rental_id} is Done successfully!!!")
        except sqlite3.Error as error:
            print(f"Error{error}")
        finally:
            if conn:
                conn.close()

    def return_rented_dvd_list(self):
        input_rental_id, index = None, None
        try:
            input_rental_id = int(input("Please enter your (Rent id) : ->"))
        except ValueError:
            print("Enter numeric value!")
        r_movie_name = None
        for i, rental in enumerate(self.rental_list):
            rental_id = rental[0]
            if input_rental_id == rental_id:  # rent table check
                r_movie_name = rental[1]
                index = i
        dvd_result = self.mov.find_dvd(r_movie_name)
        num_copies = dvd_result.number_copies
        try:
            conn = sqlite3.connect("dvd_Store.db")
            c = conn.cursor()
            return_date = datetime.datetime.now().strftime("%d/%m/%Y")
            u_query = f"UPDATE rented_dvd_list SET return_date = '{return_date}' WHERE rent_id = {input_rental_id} "
            u_dvd_query = f"UPDATE dvd SET number_copies = {num_copies + 1} WHERE movie_name = '{r_movie_name}'"
            c.execute(u_query)
            c.execute(u_dvd_query)
            conn.commit()
            self.rental_list[index][3] = return_date
            print("Thank you!!! Your have returned your dvd.")
        except sqlite3.Error as error:
            print(f"Error{error}")
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    rent = Rent()
    # rent.mov.load_dvds()
    # print(rent)
    # rent.insert_rented_dvd_list()
    # rent.insert_rented_dvd_list()
    # rent.insert_dvd()
