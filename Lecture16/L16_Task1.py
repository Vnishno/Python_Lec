class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        
        MovieTicket.total_tickets_sold += 1

    def display_ticket_info(self):
        print(f"კინოთეატრი: {MovieTicket.cinema_name}")
        print(f"ფილმი: {self.movie_title}")
        print(f"ადგილი: {self.seat_number}")
        print(f"ფასი: {self.price} ლარი")
        print("=" * 40)


ticket1 = MovieTicket("უდიპლომო სასიძო", 12, 20)
ticket1.display_ticket_info()

ticket2 = MovieTicket("შერეკილები", 5, 25)
ticket2.display_ticket_info()

ticket3 = MovieTicket("ცისფერი მთები", 8, 18)
ticket3.display_ticket_info()

print(f"სულ გაყიდული ბილეთების რაოდენობა: {MovieTicket.total_tickets_sold}")