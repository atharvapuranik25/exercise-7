room_type = int(input("Type of room booked (Enter 1 for Deluxe and 2 for Non AC): "))
days = int(input("Total no. of days: "))
food = float(input("Total amount spent on food: "))

if room_type == 1:
    gst = (0.18 * food)
    cgst = sgst = gst / 2
    room = 7500 * days
    tip = 0.10 * food
    bill = room + food + gst + tip

elif room_type == 2:
    gst = (0.05 * food)
    cgst = sgst = gst / 2
    room = 4500 * days
    tip = 0.10 * food
    bill = room + food + gst + tip

else:
    print("Enter a valid input.")

print("\nTotal room tariff: %.2f" % room)
print("Total amount on food (excluding gst): %.2f" % food)
print("GST: %.2f" % gst)
print("CGST: %.2f" % cgst)
print("SGST: %.2f" % sgst)
print("Tip: %.2f" % tip)
print("Total amount to be paid: %.2f" % bill)
