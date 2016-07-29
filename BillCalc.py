def Tip(total, tip_percentage):
	return total*tip_percentage

def Total_Bill(bill_amount, Tip):
	return (Tip+bill_amount)

def Split(bill_amount, party):
	return(bill_amount/party)

def Calc_Bill(param1, param2, param3 = bill_amount):
	return bill_amount * user_tip * .01

global 

def main():
	user_split=1
	choice = raw_input("1-calculate tip 2-split the bill ")
	if choice == "1" :
		user_bill = float(raw_input("What is the Bill amount? "))
		user_tip =int(raw_input("What is tip percent?")) * .01
		print Tip (user_bill, user_tip)

		# print user_bill, "is the user bill"
		# print user_tip, "is the tip percent"

	elif choice == "2":
		user_bill = float(raw_input("What is the Bill amount? "))
		user_split = int (raw_input("Split how many ways?"))
        print Split (user_bill,user_split) 

	# quest=raw_input("Split the bill?")

	# print Total_Bill(100,25)

	# print Split (125,2)

	# print Tip(100, 0.25)

if __name__ == '__main__':
	main()
