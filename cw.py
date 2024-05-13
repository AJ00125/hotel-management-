# Importing required libraries
from datetime import datetime

# Singleton class for managing user input prompts
class UserInputPromptManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserInputPromptManager, cls).__new__(cls)
            cls._instance.arrival_prompt = "Enter arrival date (YYYY-MM-DD): "
            cls._instance.departure_prompt = "Enter departure date (YYYY-MM-DD): "
            cls._instance.breakfast_prompt = "Do you want breakfast during your stay? (yes/no): "
            cls._instance.num_rooms_prompt = "Enter the number of rooms you want to book: "
        return cls._instance

    def get_arrival_prompt(self):
        return self.arrival_prompt

    def get_departure_prompt(self):
        return self.departure_prompt

    def get_breakfast_prompt(self):
        return self.breakfast_prompt

    def get_num_rooms_prompt(self):
        return self.num_rooms_prompt

# Factory Method pattern for creating instances of HotelBooking
class HotelBookingFactory:
    @staticmethod
    def create_booking(arrival_date, departure_date, breakfast, num_rooms):
        return HotelBooking(arrival_date, departure_date, breakfast, num_rooms)

# HotelBooking class with encapsulation, inheritance, polymorphism, and abstraction
class HotelBooking:
    def __init__(self, arrival_date, departure_date, breakfast, num_rooms):
        self._arrival_date = arrival_date
        self._departure_date = departure_date
        self._breakfast = breakfast
        self._num_rooms = num_rooms

    def calculate_total_cost(self):
        room_cost_per_night = 100  # Cost of each room per night
        breakfast_cost_per_person = 10  # Cost of breakfast per person per day

        num_nights = (self._departure_date - self._arrival_date).days

        total_room_cost = self._num_rooms * room_cost_per_night * num_nights

        total_breakfast_cost = 0
        if self._breakfast:
            total_breakfast_cost = self._num_rooms * breakfast_cost_per_person * num_nights

        total_cost = total_room_cost + total_breakfast_cost
        return total_cost

    # Abstraction - Display booking details without revealing internal details
    def display_booking_details(self):
        print("\nBooking Details:")
        print("Arrival Date:", self._arrival_date)
        print("Departure Date:", self._departure_date)
        print("Breakfast Option:", "Yes" if self._breakfast else "No")
        print("Number of Rooms Booked:", self._num_rooms)
        print("Total Cost: $", self.calculate_total_cost())

# User input functions
def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in {'yes', 'y'}:
            return True
        elif choice in {'no', 'n'}:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_integer_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function
def main():
    print("Welcome to Hotel Booking System!")
    prompt_manager = UserInputPromptManager()

    # Get user input
    arrival_date = get_date_input(prompt_manager.get_arrival_prompt())
    departure_date = get_date_input(prompt_manager.get_departure_prompt())
    breakfast_option = get_yes_no_input(prompt_manager.get_breakfast_prompt())
    num_rooms_booked = get_integer_input(prompt_manager.get_num_rooms_prompt())

    # Create booking using Factory Method
    booking = HotelBookingFactory.create_booking(arrival_date, departure_date, breakfast_option, num_rooms_booked)

    # Display booking details
    booking.display_booking_details()

if __name__ == "__main__":
    main()