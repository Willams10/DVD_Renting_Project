class Dvddata:
    def __init__(self, movie_name, stars, producer, director, production_company, number_copies):
        self.movie_name = movie_name
        self.stars = stars
        self.producer = producer
        self.director = director
        self.production_company = production_company
        self.number_copies = number_copies

    def __str__(self):
        print("=== DVD Detail ===")
        output = f"Movie Name: {self.movie_name}\n" \
                 f"Movie stars: {self.stars}\n" \
                 f"Producer: {self.producer}\n" \
                 f"Director: {self.director}\n" \
                 f"Production Company: {self.production_company}\n" \
                 f"Number of copies: {self.number_copies}\n\n"
        return output


if __name__ == '__main__':
    print()
    m1 = Dvddata("Schindler's List", "Liam NeesonRalph, FiennesBen, Kingsley", "Thomas Keneally", "Steven Spielberg", "Universal", "50")
    m2 = Dvddata("The Godfather", "Marlon Brando", "Mario Puzo", "Francis Ford Coppola", "Paramount", "100")
    print(m1, m2)
