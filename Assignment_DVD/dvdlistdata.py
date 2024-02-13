import sqlite3
from dvd_data import Dvddata


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # null


class LinkedlistDVD:
    def __init__(self):
        self.head = None
        self.dvds = []

    def load_dvds(self):

        try:
            conn = sqlite3.connect("dvd_Store.db")
            sql = "SELECT * FROM dvd;"
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            dvd_records = cursor.fetchall()

            for dvddata in dvd_records:
                movie_name = dvddata[0]
                stars = dvddata[1]
                producer = dvddata[2]
                director = dvddata[3]
                production_company = dvddata[4]
                number_copies = dvddata[5]
                new_dvd = Dvddata(movie_name, stars, producer, director, production_company, number_copies)
                self.add_dvd(new_dvd)
        except sqlite3.Error as error:
            print(f"Something went wrong!!!{error}")
        finally:
            if conn:
                conn.close()

    def add_dvd(self, dvd):
        next_node = Node(dvd)
        if self.head is None:
            self.head = next_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = next_node

    def remove_dvd(self, movie_name):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.movie_name == movie_name:
                found = True
            else:
                previous = current
                current = current.next

            if found:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
            else:
                print(f"The Movie '{movie_name}' is not found. ")

    def display_dvd(self):
        current = self.head
        header = "+-------------------------------------+-----------------------------------------------+----------------------+----------------------+--------------------+-------------------+"
        print(header)
        print("| Movie Name                          | Stars                                         | Producer             | Director             | Production Company | Number of Copies  |")
        print(header)
        while current is not None:
            output = f"| {current.data.movie_name:<35} | {current.data.stars:<45} | {current.data.producer:<20} | {current.data.director:<20} | {current.data.production_company:<19}|" \
                     f"{current.data.number_copies:<19}|"
            print(output)
            current = current.next
        print(header)

    def search_dvd(self, movie_name):
        conn = sqlite3.connect('dvd_Store.db')
        cursor = conn.cursor()
        query = "SELECT * FROM dvd WHERE movie_name = ?"
        cursor.execute(query, (movie_name, ))
        result = cursor.fetchall()

        conn.close()
        for row in result:
            return row

        conn.close()

    def find_dvd(self, movie_name):
        current = self.head
        while current is not None:
            if current.data.movie_name == movie_name:
                # print(current.data)
                return current.data
            current = current.next

    def insert_dvd(self):
        movie_name = input("Enter Movie Name -> ")
        stars = input("Enter Stars -> ")
        producer = input("Enter Producer -> ")
        director = input("Enter Director -> ")
        production_company = input("Enter Production Company -> ")
        number_copies = input("Enter Number copies -> ")
        while True:
            try:
                conn = sqlite3.connect('dvd_Store.db')
                cursor = conn.cursor()
                query = "INSERT INTO dvd VALUES (?,?,?,?,?,?)"
                cursor.execute(query, [movie_name, stars, producer, director, production_company, number_copies])
                conn.commit()
                self.add_dvd(Dvddata(movie_name, stars, producer, director, production_company, number_copies))
                print("Movie is added successfully!!!")
                break
            except sqlite3.Error as error:
                print(f"Error{error}")
            finally:
                if conn:
                    conn.close()


if __name__ == '__main__':
    d1 = LinkedlistDVD()
    d1.load_dvds()

    d1.display_dvd()

    #d1.insert_dvd()
    #d1.search_dvd("Empire of Light")
    #movie_name = input("movie name")
    #print(d1.find_dvd(movie_name))

