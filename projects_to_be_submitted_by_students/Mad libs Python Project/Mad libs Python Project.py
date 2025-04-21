name:str = input("Name: ")
surname:str = input("Surname: ")
age:int = input("Age:")
title:str = input("MR/MRS/MISS: ")
ticket_no:str = input("Ticket No: ")
Flight_Name:str = input("Flight Name: ")
Seat_No:int = input("Seat No: ")
From:str = input("From: ")
To:str = input("To: ")

Detail = f"Above is the Passenger DetaiL. Passenger name is {title} {name} {surname}. His/Her age is {age}. Having Ticket Number {ticket_no} and seat number {Seat_No}. \
Going To {To} From {From} through {Flight_Name}."
print(Detail)