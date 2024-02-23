"""
    Program Purpose: enabling users to input customer details like room type, number of rooms, and nights.
                    It computes the total reservation cost considering various conditions such as differing rates
                    for room types, discounts for reserving more than 5 rooms, a mandatory 3-night minimum stay for
                    Suites, and a complimentary breakfast voucher for Single rooms booked over 7 nights
    Programmer: Muhammad Muqry Bin Razaly
    Date 23 february 2024
"""

for i in range(1, 11):
    print(f"Customer {i}:")
    room_type = input("Enter room type (Single, Double, Suite): ").capitalize()
    num_rooms = int(input("Enter number of rooms to reserve: "))
    num_nights = int(input("Enter number of nights to stay: "))

    if room_type not in ["Single", "Double", "Suite"] or num_rooms <= 0 or num_nights <= 0:
        print("Error: Invalid room type, number of rooms, or number of nights. Please try again.")

# for suite, user need to book minimum 3 nights
    if room_type == "Suite" and num_nights < 3:
        print("Error: Minimum stay for a Suite is 3 nights.")

    #rates of the room types
    rates = {"Single": 100, "Double": 150, "Suite": 250}
    total_cost = rates[room_type] * num_rooms * num_nights

#if user choose any room's type more than 5 rooms, they will get discount
    if num_rooms > 5:
        total_cost *= 0.9

#if user choose single and number of nights more than 7 days, they will get complimentary breakfast voucher
    if room_type == "Single" and num_nights >= 7:
        print("Congratulations! You get a complimentary breakfast voucher.")

    print(f"Total cost for your reservation: RM{total_cost:.2f}\n")
