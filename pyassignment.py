#---------------------------------------------------------Import Module-------------------------------------------------------------------
import datetime
#----------------------------------------------------------End Import---------------------------------------------------------------------
#---------------------------------------------------Open text file and assign data--------------------------------------------------------
#==== Open member file and read data ====#
def read_member_data():
    member_list = open("member.txt", 'r')
    member_data = member_list.readlines()
    username = []
    password = []
    customer_id = []
    name = []
    age = []
    gender = []
    phone_number = []
    current_rented_car_id = []
    customer_payment = []
    customer_credit_card = []
    member_list.close()

    for member_details in member_data:
        user_data = member_details.split(",")
        username.append(user_data[0])
        password.append(user_data[1])
        customer_id.append(user_data[2])
        name.append(user_data[3])
        age.append(user_data[4])
        gender.append(user_data[5])
        phone_number.append(user_data[6])
        current_rented_car_id.append(user_data[7])
        customer_payment.append(user_data[8])
        customer_credit_card.append(user_data[9])

    return username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card

#==== Open Car file and read data ====#
def read_car_data():
    car_list = open("car_details.txt","r")
    car_data = car_list.readlines()
    car_id = []
    car_platno = []
    car_year = []
    car_brand = []
    car_model = []
    car_type = []
    car_capacity = []
    car_colour = []
    car_price_per_day = []
    car_availability = []
    car_list.close()

    for car_details in car_data:
        car_info = car_details.split(",")
        car_id.append(car_info[0])
        car_platno.append(car_info[1])
        car_year.append(car_info[2])
        car_brand.append(car_info[3])
        car_model.append(car_info[4])
        car_type.append(car_info[5])
        car_capacity.append(car_info[6])
        car_colour.append(car_info[7])
        car_price_per_day.append(car_info[8])
        car_availability.append(car_info[9])

    return car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability

#==== Open record file and read data ====#
def read_record_data():
    record_list = open("record.txt","r")
    record_data = record_list.readlines()
    record_customer_id = []
    record_car_id = []
    start_date = []
    end_date = []
    duration_rent = []
    total_price = []
    payment_info = []
    record_list.close()

    for record_details in record_data:
        record_info = record_details.split(",")
        record_customer_id.append(record_info[0])
        record_car_id.append(record_info[1])
        start_date.append(record_info[2])
        end_date.append(record_info[3])
        duration_rent.append(record_info[4])
        total_price.append(record_info[5])
        payment_info.append(record_info[6])
    
    return record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info

#-------------------------------------------------------End open text file----------------------------------------------------------------
#----------------------------------------------------General Function for program---------------------------------------------------------
#==== Display day, month, date, time, year ====#
def time():
    today = datetime.datetime.today()
    print(f">>>{today: %c}")

#==== Menu Interface for all user (Admin, Guest, Member) ====#
def main_menu(): #interface for all user to proceed
    print("==============================================================")
    time()
    print(">>> Welcome :)")
    print(">>> This is an Online car rental system.")
    print(">>> Enter your option with number below.")
    print("[1] = Admin User")
    print("[2] = Members")
    print("[3] = Non-member")
    print("[0] = Exit")
    print("==============================================================")
    # User input their option
    while True:
        no = choice()
        if no == 1:
            admin_login()
            break
        elif no == 2:
            member_login()
            break
        elif no == 3:
            guest()
            break
        elif no == 0:
            exit()
        else:
            print(">>> Invalid Input !!")
            print(">>> Please Enter Again ..")
            print("==============================================================")

#==== Display available car for Guest, member, admin ====# 
def available_car_list_for_rent():
    #Call the return value from the function to be a local function
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    #Loop through all the list
    for x in range(len(car_id)):
        #When it is yes then display
        if car_availability[x].replace("\n","") == "YES":
            print("Car ID = " + car_id[x] + ", Car Brand = " + car_brand[x] + ", Car Model = " + car_model[x]+ "\n")

#==== For rent_car to check the date format ====#
def check_date_input():
    while True:
            date_start = input("->")
            try:
                #To split multiple interget input
                year, month, day = map(int, date_start.split('-'))
                date_start = datetime.date(year, month, day)
            except (ValueError, TypeError):
                print(">>> Please Use the Format (YYYY-MM-DD)")
                continue
            return date_start

#==== For option and no in function ====#
def choice():
    #infinite loop
    while True:
        try:
            number = int(input("->"))
        except ValueError: #except value error from integer
            print(">>> Sorry, please Enter A VALID Number.")
            continue # back to looping if user input string
        return number

#-------------------------------------------------------Admin Function-------------------------------------------------------------------
#==== Admin Login Interface ====#
def admin_login():
    #Get admin data
    admin_list = ["admin","adminpass"]
    #admin input
    while True:
        print(">>> Please insert your username.")
        admin_input_username = input("->")
        if admin_input_username == admin_list[0]:
            print(">>> Please insert your password.")
            admin_input_password = input("->")
            if admin_input_password == admin_list[1]:
                print(">>> Success Logged in!!")
                print(">>> Welcome Admin!")
                print(">>> Please Enter Your Option To Proceed..")
                print("==============================================================") 
                action_of_admin()
        # Either 1 info error then invalid
        print("==============================================================")
        print(">>> Username or Password Invalid!")
        print("[1] = Login again.")
        print("[0] = Back to main menu")
        print("==============================================================")
        option=choice()
        if option == 1:
            continue
        elif option == 0:
            main_menu()
        else:
            print(">>> Invalid Entry..")
            print(">>> Redirecting to main menu..")
            main_menu()

#==== Admin Menu Interface ====#
def action_of_admin():
    while True:
        print("[1] = Register car to be rent")
        print("[2] = Modify Car Details")
        print("[3] = Display records of Cars and Customers")
        print("[4] = Search specific record of Customer Booking or Payment")
        print("[5] = Return a Rented Car")
        print("[0] = Exit")
        print(">>> Please Enter the action you want to proceed")
        print("==============================================================")
        option = choice()
        if option == 1:
            register_car()
            #assign a main page for confirming register a car or back to action of admin
        elif option == 2:
            modify_car_details() #modify the details of a car
        elif option == 3:
            interface_of_record() #types of record for view
        elif option == 4:
            search_specific_record() #use member id to search either they have booking(carid if got then id if no then none) or unpay payment
        elif option == 5:
            return_car() #return a rented car
        elif option == 0:
            exit()
        else:
            print(">>> Invalid Option !!")
            print(">>> Please Enter Again !!")
            print("==============================================================")
            continue

#==== To make sure input of year is 4 digit====#
def check_4_digit():
    while True:
        year = choice()
        #convert to string to check length
        str_year=str(year)
        if year < 0:
            print(">>> Sorry, your input should not be negative number.")
            continue
        elif len(str_year) != 4: #to make sure it is 4 digit
            print(">>> Sorry, please Enter A VALID 4 Number year digit.")
            continue
        else:
            return year

#==== Available for Admin to Register Car ====#
def register_car():
    #Read car data
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    
    car_list_register = open("car_details.txt","a+") # a+ for read and write
    car_list_data = car_list_register.readlines()
    i = 1
    for x in car_id:
        i += 1
    auto_car_id = 0 + i #auto generate a new id
    new_car_id = ("ID"+str(auto_car_id))

    #Request input from the user (string)
    print(">>> Please Enter the car platnumber.")
    new_car_platno = str(input("->")).upper()
    print(">>> Please Enter the car made year.")
    print(">>> Please only insert number such as '2021'")
    new_car_year = check_4_digit()
    print(">>> Please Enter the brand of the car.")
    new_car_brand = str(input("->")).upper()
    print(">>> Please Enter the car model name.")
    new_car_model = str(input("->")).upper()
    print(">>> Please Enter the type of the car.")
    new_car_type = str(input("->")).upper()
    print(">>> Please Enter the car capacity with number.")
    new_car_capacity = choice()
    print(">>> Please Enter the car colour.")
    new_car_colour = str(input("->")).upper()
    print(">>> Please Enter the car price per day with number.")
    print(">>> If 100, then insert 100.")
    new_car_price_per_day = choice()
    print(">>> Please Enter the car availability with YES.")
    new_car_availability = str(input("->")).upper()
    if new_car_availability == "YES":
        #add data to txt file
        car_list_data.append(new_car_id +",")
        car_list_data.append(new_car_platno + ",")
        car_list_data.append(str(new_car_year) + ",")
        car_list_data.append(new_car_brand +",")
        car_list_data.append(new_car_model + ",")
        car_list_data.append(new_car_type + ",")
        car_list_data.append(str(new_car_capacity) + ",")
        car_list_data.append(new_car_colour + ",")
        car_list_data.append(str(new_car_price_per_day) + ",")
        car_list_data.append(new_car_availability + "\n")
        car_list_register.writelines(car_list_data)
        car_list_register.close()
        #Display success message
        print("==============================================================")
        print(">>> Register success!!")
        print(">>> Redirecting to main menu..")
        print("==============================================================")
        action_of_admin()
    else:
        print("==============================================================")
        print(">>> Invalid Input !!")
        print(">>> Please double check your info.")
        print("[1] = Enter again")
        print("[2] = Back to previous page")
        print("[3] = Exit")
        print("==============================================================")
        option=choice()
        if option == 1:
            register_car()
        elif option == 2:
            action_of_admin()
        elif option == 3:
            exit()
        else:
            print(">>> Invalid Option !!")
            print(">>> Redirecting to Admin Menu !!")
            print("==============================================================")
            action_of_admin()

#==== Admin to modify car details ====#
def modify_car_details():
    # read car data
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability=read_car_data()
    #User input the car ID of the car wanted to modify
    print("==============================================================")
    print(">>>Please Enter the car ID of the car (ID1).")
    modify_car_id = str(input("->")).replace(" ","").upper()
    for x in range(len(car_id)):
        if modify_car_id == car_id[x]:
            #Display current details of the car
            print("==============================================================")
            print(">>> Your current details is shown below.")
            print(">>> [1] = Car ID = " + car_id[x])
            print(">>> [2] = Car Plat number = " + car_platno[x]) 
            print(">>> [3] = Year of Made = " + car_year[x])  
            print(">>> [4] = Brand of Car = """ + car_brand[x])
            print(">>> [5] = Car model = """ + car_model[x]) 
            print(">>> [6] = Type of car = """ + car_type[x]) 
            print(">>> [7] = Capacity of car = """ + car_capacity[x]) 
            print(">>> [8] = Colour of car = """ + car_colour[x]) 
            print(">>> [9] = Price per day = """ + car_price_per_day[x])
            print("==============================================================")
            break
        
    if modify_car_id == car_id[x]:  
        print(">>> Please Enter the car platnumber.\n>>> Press Enter for remaining the same platnumber.")
        modified_car_platno = str(input("->")).upper()
        print("==============================================================")
        if modified_car_platno != "":
            car_platno[x] = modified_car_platno
        else:
            car_platno[x] = car_platno[x]

        print(">>> Please Enter the car made year.\n>>> Please only insert number such as 2021\n>>> Press Enter for remaining the same car made year.")
        modified_car_year = str(input("->")).upper()
        print("==============================================================")
        if modified_car_year != "":
            car_year[x] = modified_car_year
        else:
            car_year[x] = car_year[x]
            
        print(">>> Please Enter the brand of the car.\n>>> Press Enter for remaining the same brand.")
        modified_car_brand = str(input("->")).upper()
        print("==============================================================")
        if modified_car_brand != "":
            car_brand[x] = modified_car_brand
        else:
            car_brand[x] = car_brand[x]
        
        print(">>> Please Enter the car model name.\n>>> Press Enter for remaining the same car model.")
        modified_car_model = str(input("->")).upper()
        print("==============================================================")
        if modified_car_model != "":
            car_model[x] = modified_car_model
        else:
            car_model[x] = car_model[x]

        
        print(">>> Please Enter the type of the car.\n>>> Press Enter for remaining the same type of the car.")
        modified_car_type = str(input("->")).upper()
        print("==============================================================")
        if modified_car_type != "":
            car_type[x] = modified_car_type
        else:
            car_type[x] = car_type[x]

        print(">>> Please Enter the car capacity with number.\n>>> Press Enter for remaining the same capacity.")
        modified_car_capacity = str(input("->")).upper()
        print("==============================================================")
        if modified_car_capacity != "":
            car_capacity[x] = modified_car_capacity
        else:
            car_capacity[x] = car_capacity[x]

        print(">>> Please Enter the car colour.\n>>> Press Enter for remaining the same colour.")
        modified_car_colour = str(input("->")).upper()
        print("==============================================================")
        if modified_car_colour != "":
            car_colour[x] = modified_car_colour
        else:
            car_colour[x] = car_colour[x]
            
        print(">>> Please Enter the car price per day with number.\n>>> If 100, then insert 100.\n>>> Press Enter for remaining the same price per day.")
        modified_car_price_per_day = str(input("->")).upper()
        if modified_car_price_per_day != "":
            car_price_per_day[x] = modified_car_price_per_day
        else:
            car_price_per_day[x] = car_price_per_day[x]
        
        #Modify each elements in car details except car ID and car availability 
        modified_car_list = open("car_details.txt","w")
        for x in range(len(car_id)):
            #replace data inside the car details textfile
            modified_car_list.write(car_id[x]+",")
            modified_car_list.write(car_platno[x] +",")
            modified_car_list.write(car_year[x]+",")
            modified_car_list.write(car_brand[x]+",")
            modified_car_list.write(car_model[x]+ ",")
            modified_car_list.write(car_type[x]+",")
            modified_car_list.write(car_capacity[x]+",")
            modified_car_list.write(car_colour[x]+",")
            modified_car_list.write(car_price_per_day[x]+",")
            modified_car_list.write(car_availability[x])
            
            
        modified_car_list.close()
        print("==============================================================")
        print(">>> Modify success!!")
        print(">>> Redirecting to Admin menu..")
        print("==============================================================")
        action_of_admin()
            
        
    else:
        print("==============================================================")
        print(">>> Sorry :(")
        print(">>> This Car ID is not available.")
        print("[1] = Enter again")
        print("[2] = Back to previous page")
        print("[3] = Exit")
        print("==============================================================")
        option=choice()
        if option == 1:
            modify_car_details()
        elif option == 2:
            action_of_admin()
        elif option == 3:
            exit()
        else:
            print(">>> Invalid Option !!")
            print(">>> Redirecting to Admin Menu !!")
            print("==============================================================")
            action_of_admin()

#==== Display types of record ====#
def interface_of_record():
    print("==============================================================")
    print("[1] = Cars Rented Out")
    print("[2] = Cars available for Rent")
    print("[3] = Customer Bookings")
    print("[4] = Customer Payment for a specific time duration")
    print("[5] = Back to Previous Page")
    print("[0] = Exit")
    print(">>> Which record you want to view?")
    print("==============================================================")
    option=choice()
    if option == 1:
        car_rented_out()
    elif option == 2:
        available_car_list_for_rent()
        print("==============================================================")
        print("[1] = Back to previous page.")
        print("[2] = Admin menu")
        print("[0] = Exit..")
        print("==============================================================")
        option=choice()
        if option == 1:
            interface_of_record()
        elif option == 2:
            action_of_admin()
        elif option == 0:
            exit()
        else:
            print(">>> Invalid Option !!")
            print(">>> Redirecting to previous page !!")
            print("==============================================================")
            interface_of_record()
    elif option == 3:
        customer_booking()
    elif option == 4:
        customer_payment_for_a_specific_time_duration()
    elif option == 5:
        action_of_admin()
    elif option == 0:
        exit()
    else:
        print(">>> Invalid Option !!")
        print(">>> Please Enter Again !!")
        print("==============================================================")
        interface_of_record()

#==== Display rented out car for admin ====#
def car_rented_out():
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability=read_car_data()
    for x in range(len(car_id)):
        if car_availability[x].replace("\n","") == "NO":
            print("==============================================================")
            print(">>>Car ID = " + car_id[x] + ", Car Brand = " + car_brand[x] + ", Car Model = " + car_model[x])

    print("==============================================================")
    print("[1] = Back to previous page.")
    print("[2] = Admin menu")
    print("[0] = Exit..")
    print("==============================================================")
             
    option=choice()
    if option == 1:
        interface_of_record()
    elif option == 2:
        action_of_admin()
    elif option == 0:
        exit()
    else:
        print(">>> Invalid Option !!")
        print(">>> Redirecting to previous page !!")
        print("==============================================================")
        interface_of_record()

#==== Display current customer booking to admin ====#
def customer_booking():
    #Read member data to display ID and current booking car 
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card=read_member_data()
    #Read record data to display start date and end date
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info=read_record_data()
    booking_info=False
    for x in range(len(username)):
        #when the data is not null 
        if current_rented_car_id[x].replace("\n","") != "null":
            for y in range(len(record_customer_id)):
                #When the current booking car is same as the data in record data then booking info is True
                if record_car_id[y] == current_rented_car_id[x]:
                    booking_info=True
        
    if booking_info == True:
        #when the data is not null then display current booking car and customer ID
        for x in range(len(username)):
            if current_rented_car_id[x].replace("\n","") != "null":
                record_customer=(">>>Customer ID = " + customer_id[x] + ", Car = " + current_rented_car_id[x])
                for y in range(len(record_customer_id)):
                    #When the current booking car is same as the data in record data then display start date and end date
                    if record_car_id[y] == current_rented_car_id[x]:
                        record_date = (", Start Date= "+ start_date[y] 
                        +", End date = " + end_date[y])
                        record = record_customer + record_date
                        #combine both data display the result
                        print("==============================================================")
                        print(record)
    elif booking_info == False:
        print("==============================================================")
        print("There is no customer booking any car.")
    
    print("==============================================================")
    print("[1] = Back to previous page.")
    print("[2] = Admin menu")
    print("[0] = Exit..")
    print("==============================================================")
    option=choice()

    if option == 1:
        interface_of_record()
    elif option == 2:
        action_of_admin()
    elif option == 0:
        exit()
    else:
        print(">>> Invalid Option !!")
        print(">>> Redirecting to previous page !!")
        print("==============================================================")
        interface_of_record()

#==== Display customer payment for a given time duration ====#
def customer_payment_for_a_specific_time_duration():
    #read record data
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info=read_record_data()
    #User input start date of the specific time duration
    print(">>> Enter the start of the time duration (Format = YYYY-MM-DD)")
    specific_time_duration_start_date=check_date_input()
    #User input end date of the specific time duration
    print(">>> Enter the End of the time duration (Format = YYYY-MM-DD)")
    specific_time_duration_end_date=check_date_input()
    for x in range(len(record_customer_id)):
        year, month, day = map(int, start_date[x].split('-'))
        start_date[x]=datetime.date(year, month, day)
        year, month, day = map(int, end_date[x].split('-'))
        end_date[x] = datetime.date(year, month, day)
    
    
    if specific_time_duration_start_date <= start_date[x] and specific_time_duration_end_date >= end_date[x]:
        print("The records of customer payment between " + str(specific_time_duration_start_date) + " and " + str(specific_time_duration_end_date) + ":")
        for x in range(len(record_customer_id)):
            if specific_time_duration_start_date <= start_date[x] and specific_time_duration_end_date >= end_date[x]:
                #Display the record between the specific time duration
                print("==============================================================")
                print(">>>Customer ID =" + record_customer_id[x] + ", Car = " + record_car_id[x]+ ", Start date of rent="+ str(start_date[x])+
                ", End date of rent =" + str(end_date[x])+ ", Total payment=" + total_price[x]+ ", Payment status=" + payment_info[x])
    
    else:
        print("==============================================================")
        print("There is no customer payment record during this time duration")

    print("==============================================================")
    print("[1] = Check for another time duration")
    print("[2] = Back to previous page.")
    print("[3] = Admin menu")
    print("[0] = Exit..")
    print("==============================================================")
    option=choice()
    if option == 1:
        customer_payment_for_a_specific_time_duration()
    elif option == 2:
        interface_of_record()
    elif option == 3:
        action_of_admin()
    elif option == 0:
        exit()
    else:
        print(">>> Invalid Option !!")
        print(">>> Redirecting to previous page !!")
        print("==============================================================")
        interface_of_record()

#==== Admin choose the specific record to search ====#
def search_specific_record():
    print("==============================================================")
    print("[1] = Customer Booking")
    print("[2] = Customer Payment")
    print("[3] = Back to Previous Page")
    print("[0] = Exit")
    print(">>> Which specific record you want to search?")
    print("==============================================================")
    option=choice()
    if option == 1:
        specific_record_customer_booking()
    elif option == 2:
        specific_record_customer_payment()
    elif option == 3:
        action_of_admin()
    elif option == 0:
        exit()
    else:
        print("==============================================================")
        print(">>> Invalid Option !!")
        print(">>> Please Enter Again !!")
        print("==============================================================")
        search_specific_record()

#==== Admin search specific record of customer booking ====#
def specific_record_customer_booking():
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card=read_member_data()
    #read record data
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info=read_record_data()
    record_info=False
    #User input customer ID to search for booking
    print("==============================================================")
    print(">>> Please Enter the customer ID.")
    input_customer_id = str(input("->")).replace(" ","")
    
    for x in range(len(username)):
        #when the input ID is same with customer ID in member textfile then display the customer ID with current booking car
        if input_customer_id == customer_id[x] and current_rented_car_id[x] != "null":
            record_customer=("Customer ID = " + customer_id[x] + ", Car = " + current_rented_car_id[x])
            record_info=True
            for y in range(len(record_customer_id)):
                #when the input ID is same with record customer ID in record textfile then display start date and end date
                if input_customer_id == record_customer_id[y] and current_rented_car_id[x]==record_car_id[y]:
                    record_date=(", Start Date= "+ start_date[y] 
                        +", End date = " + end_date[y])
                    #combine both record then display
                    record=record_customer+record_date
                    print(record)

        elif input_customer_id == customer_id[x] and current_rented_car_id[x] == "null":
            print(">>> This customer is not booking any car.")
            record_info=True
    
    if record_info == True:
        print("==============================================================")
        print(">>> Which option you want to proceed?")
        print("[1] = Search for another customer ")
        print("[2] = Back to previous page")
        print("[0] = Exit")
        
        option=choice()
    
        if option == 1:
            specific_record_customer_booking()
        elif option == 2:
            search_specific_record()
        elif option == 0:
            exit()
        else:
            print("==============================================================")
            print(">>> Sorry :( ")
            print(">>> This option is not available.")
            print(">>> Redirecting to Admin menu..")
            print("==============================================================")
            action_of_admin()

    
    elif record_info==False:
        print("==============================================================")
        print(">>> Invalid customer ID!")
        print("[1] = Enter again")
        print("[2] = Back to Previous Page")
        print("[0] = Exit")
        print(">>> Which option you want to proceed?")
        print("==============================================================")
        option=choice()       
        if option == 1:
            specific_record_customer_booking()
        elif option == 2:
            search_specific_record()
        elif option == 0:
            exit()
        else:
            print("==============================================================")
            print(">>> Sorry :( ")
            print(">>> This option is not available.")
            print(">>> Redirecting to Admin menu..")
            print("==============================================================")
            action_of_admin()

#==== Admin search specific record of customer payment ====#
def specific_record_customer_payment():
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card=read_member_data()

    record_info=False
    #User input customer ID to search for payment
    print("==============================================================")
    print(">>> Please Enter the customer ID.")
    record_customer_id = str(input("->")).replace(" ","")
    for x in range(len(username)):
        #When the customer payment is not null then display payment has not completed and its leftover
        if record_customer_id == customer_id[x] and customer_payment[x] != "null":
            print(">>> The payment of the customer has not completed.")
            print(">>> The amount of payment that has not completed = "+ customer_payment[x])
            record_info=True
            break
        #When the customer payment is null then display payment has completed
        elif record_customer_id == customer_id[x] and customer_payment[x] == "null":
            print(">>> The payment of the customer has completed")
            record_info=True
            break
    
    if record_info == True:
        print("==============================================================")
        print("[1] = Search for another customer ")
        print("[2] = Back to previous page")
        print("[0] = Exit")
        print(">>>Which option you want to proceed?")
        print("==============================================================")
        option=choice()
        if option == 1:
            specific_record_customer_payment()
        elif option == 2:
            search_specific_record()
        elif option == 0:
            exit()
        else:
            print("==============================================================")
            print(">>> Sorry :( ")
            print(">>> This option is not available.")
            print(">>> Redirecting to Admin menu..")
            print("==============================================================")
            action_of_admin()

    
    elif record_info==False:
        print("==============================================================")
        print(">>> Invalid customer ID!")
        print("[1] = Enter again")
        print("[2] = Back to Previous Page")
        print("[0] = Exit")
        print(">>> Which option you want to proceed?")
        print("==============================================================")
        option=choice()     
        if option == 1:
            specific_record_customer_payment()
        elif option == 2:
            search_specific_record()
        elif option == 0:
            exit()
        else:
            print("==============================================================")
            print(">>> Sorry :( ")
            print(">>> This option is not available.")
            print(">>> Redirecting to Admin menu..")
            print("==============================================================")
            action_of_admin()

#==== return a car from customer ====#
def return_car():
    #read car data to make change to data 
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability=read_car_data()
    #read member data to make change to data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card=read_member_data()
    car_return_info=False
    #User input car ID of the returned car
    print("==============================================================")
    print(">>> Please Enter the car ID of the return car (ID1).")
    return_car_id = str(input("->")).replace(" ","").upper()

    for x in range(len(car_id)):
        if return_car_id == car_id[x]:
            car_return_info=True
            break
    if car_return_info==True:
        #rewrite the data and display availability as yes
        return_car_list = open("car_details.txt","w")
        car_availability[x]=("YES\n")
        for x in range(len(car_id)):
            return_car_list.write(car_id[x]+",")
            return_car_list.write(car_platno[x] +",")
            return_car_list.write(car_year[x]+",")
            return_car_list.write(car_brand[x]+",")
            return_car_list.write(car_model[x]+ ",")
            return_car_list.write(car_type[x]+",")
            return_car_list.write(car_capacity[x]+",")
            return_car_list.write(car_colour[x]+",")
            return_car_list.write(car_price_per_day[x]+",")
            return_car_list.write(car_availability[x])
        return_car_list.close()
    
    for y in range(len(username)):
        if return_car_id == current_rented_car_id[y]:
            car_return_info=True
            break
    if car_return_info==True:
        #rewrite the data and display current rented car id and payment as null
        return_car_from_member=open("member.txt","w")   
        current_rented_car_id[y]="null"
        customer_payment[y]="null"
        for y in range(len(username)):
            return_car_from_member.write(username[y]+",")
            return_car_from_member.write(password[y]+",")
            return_car_from_member.write(customer_id[y]+",")
            return_car_from_member.write(name[y]+",")
            return_car_from_member.write(age[y]+",") 
            return_car_from_member.write(gender[y]+",") 
            return_car_from_member.write(phone_number[y]+",")
            return_car_from_member.write(current_rented_car_id[y]+",")
            return_car_from_member.write(customer_payment[y]+",") 
            return_car_from_member.write(customer_credit_card[y])
        return_car_from_member.close()
        print("==============================================================")
        print(">>> The car has been returned!!")
        print(">>> Redirecting to main menu")
        print("==============================================================")
        action_of_admin()
    
        
    elif car_return_info==False:
        print("==============================================================")
        print(">>> Sorry :(  ")
        print(">>> This Car ID is not available.")
        print(">>> Redirecting to Admin menu..")
        print("==============================================================")
        action_of_admin()

#-----------------------------------------------------Guess User Function--------------------------------------------------------------
#==== Guest Menu Interface ====#
def guest():
    print("==============================================================")
    print(">>> Enter your option with number.")
    print("[1] = View car available currently for rent")
    print("[2] = Register to members")
    print("[0] = Exit")
    print("==============================================================")
    #user input
    option = choice() #Create a option for the user to choose which process they want.
    if option == 1:
        available_car_list_for_rent()
        # An option for guest user back to home page or register
        print("==============================================================")
        print("[1] = Register to be a member to rent the car")
        print("[2] = Back to main menu")
        print("[0] = Exit")
        print("==============================================================")
        no = choice()
        if no == 1:
            register_new_user()
        elif no == 2:
            main_menu()
        elif no == 0:
            exit()
        else:
            print("==============================================================")
            print(">>> Invalid Entry..")
            print(">>> Redirecting to main menu..")
            main_menu()
    elif option == 2:
        register_new_user()
    #To exit the system
    elif option == 0:
        exit()
    else:
        print("==============================================================")
        print(">>> Invalid Entry..")
        print(">>> Redirecting to main menu..")
        main_menu()

#==== Check for 16 digit card ====#
def check_16_digit():
    while True:
        card = choice()
        #convert to string to check length
        str_card = str(card)
        if card < 0:
            print(">>> Sorry, your input should not be negative number.")
            continue
        elif len(str_card) != 16: #to make sure it is 16 digit
            print(">>> Sorry, please Enter A VALID 16 Number card digit.")
            continue
        else:
            return card

#==== Check Male or Female ====#
def check_gender():
    while True:
        new_customer_gender = str(input("->")).upper()
        if new_customer_gender == "MALE" or new_customer_gender == "FEMALE":
            pass
        else:
            print(">>> Please enter your gender (MALE/ FEMALE) ")
            continue
        return new_customer_gender

#==== Register For New Member ====#
def register_new_user():
    #read customer data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    # Open file to append
    member_list_register = open("member.txt","a")

    # Create loop for auto cus id
    for x in range(len(customer_id)):
        x = x + 1 #(looping each cus id and +1) auto cus id
    auto_customer_id = x + 1
    # Request input from user and assign input to string
    # Username
    print(">>> Please Enter your Username for register.")
    new_member_username = unique_username()
    #Password
    print(">>> Please Enter your password for future login purpose.")
    new_member_password = str(input("->"))
    #CusID
    new_customer_id = ("Cus"+str(auto_customer_id))
    #Cus name
    print(">>> Please Enter your name.")
    new_customer_name = str(input("->"))
    #Cus age
    print(">>> Please Enter your age.")
    int_new_customer_age = choice()
    new_customer_age = str(int_new_customer_age)
    #Cus gender
    print(">>> Please Enter your gender. (MALE / FEMALE)")
    new_customer_gender = check_gender()
    #Cus phone number
    print(">>> Please Enter your phone number without (-).")
    print(">>> Please include a starting number 6 for Malaysia number")
    print(">>> Example : (601224536532)")
    int_new_customer_phone_no = choice()
    new_customer_phone_no = str(int_new_customer_phone_no)
    #Cus given details
    new_current_rented_car_id = "null"
    new_customer_payment = "null"
    #Cus credit card
    print(">>> Please Enter your credit card number. (XXXXXXXXXXXXXXXX) = 16digis")
    print(">>> Please Do not included any (space or -)")
    print(">>> We do not accept credit card start with number '0'.")
    int_new_customer_credit_card = check_16_digit()
    new_customer_credit_card = str(int_new_customer_credit_card)
    
    # append input to txt file
    member_list_register.write(new_member_username + "," + new_member_password + "," + new_customer_id + "," + 
    new_customer_name + "," + new_customer_age + "," + new_customer_gender + "," + new_customer_phone_no + "," +
    new_current_rented_car_id + "," + new_customer_payment + "," + new_customer_credit_card +"\n")
    member_list_register.close()
    #Display success message
    print("==============================================================")
    print(">>> Register success !!")
    print(">>> Glad to see you here !!")
    member_login()

#------------------------------------------------------Member Function------------------------------------------------------------------
#==== Member Login Interface ====#
def member_login():
    #Call return value from the function
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    while True:
        print("==============================================================")
        print(">>> Please insert your username.")
        user_input_username = str(input("->"))
        for x in username:
        #loop for all username (member)
            if user_input_username == x:
                # When user input same with the username in txt file
                index = username.index(x)
                # Get the username index for find the exact value of password
                user_password = password[index]
                # Find exact password with index
                print(">>> Please insert your password.")
                user_input_password = str(input("->"))
                if user_input_password == user_password:
                    # If input and exact password is same, direct to member interface
                    print("==============================================================")
                    print(">>> You are successfully logged in !")
                    print(">>> Welcome!! ")
                    print(">>> Glad to see you here !!")
                    member_interface(index)
                else:
                    # If program run here mean that username correct but password wrong
                    pass
            else:
                #this is the looping for the username, if the username is not in the txt file
                pass
        print("==============================================================")
        print(">>> Username or Password Invalid!")
        print("[1] = Login again.")
        print("[0] = Back to main menu")
        option = choice()
        if option == 1:
            continue
        elif option == 0:
            main_menu()
        else:
            print(">>> Invalid Entry..")
            print(">>> Redirecting to main menu..")
            main_menu()

#==== Member Menu Interface ====#
def member_interface(index):
    while True:
        #User interface action
        print("==============================================================")
        print(">>> Enter your option with number.")
        print("[1] = View car available currently for rent.")
        print("[2] = Rent a car (Now/Advance).")
        print("[3] = View details of rented car.")
        print("[4] = View personal rented history.")
        print("[5] = Complete payment to confirm booking.")
        print("[6] = Modify Personal details.")
        print("[0] = Exit..")
        print("==============================================================")
        # define option
        option = choice()
        if option == 1:
            available_car_list_for_rent() #after showing the list, request for user next action
            print("==============================================================")
            print("[1] = To view car details. (Required Car ID)")
            print("[2] = To rent a car. (Required Car ID)")
            print("[3] = Back to Previous Page.")
            print("[0] = Exit..")
            #define no
            no = choice()
            if no == 1:
                details_car(index) #Enter id and show details and ask want rent or not
            elif no == 2:
                rent_car(index)
            elif no == 3:
                continue
            elif no == 0:
                exit()
            else:
                print(">>> Invalid Entry..")
                print(">>> Redirecting to previous page..")
                continue
        elif option == 2:
            rent_car(index)
        elif option == 3:
            details_rented_car(index)
        elif option == 4:
            view_personal_rental_history(index)
        elif option == 5:
            complete_payment(index)
        elif option == 6:
            modify_personal_details(index)
        elif option == 0:
            exit()
        else:
            print(">>> Invalid Entry..")
            continue

#==== View Details of Available Car ====#
def details_car(index):
    #Check the details of the car availability
    car_availability_info, id_car = check_car_availability(index)

    # When the return value is true
    if car_availability_info == True:
        #User input
        print(">>> Please Enter Number for action to proceed.")
        print("[1] = Rent This Car (Required Car ID)")
        print("[2] = Back to Menu Page")
        print("[0] = Exit..")
        option = choice()
        if option == 1:
            rent_car(index)
        elif option == 2:
            member_interface(index)
        elif option == 0:
            exit()
        else:
            print(">>> Invalid Entry..")
            print(">>> Redirecting to previous page..")
            member_interface(index)

#==== Member View Current Rented Car ====#
def details_rented_car(index):
    # Read car data for display current member rented car details
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    
    # Read member data to check its current rented car id
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    
    #get the index form argument
    rented_id = current_rented_car_id[index]
    for x in range(len(car_id)):
        if rented_id == car_id[x].replace(" ", ""):
            print("==============================================================")
            print(">>> Car ID = " + car_id[x])
            print(">>> Car Brand = " + car_brand[x])
            print(">>> Car Model = " + car_model[x])
            print(">>> Car Plat No = " + car_platno[x])
            print(">>> Year of Car = " + car_year[x])
            print(">>> Type of Car = " + car_type[x])
            print(">>> Car Capacity = " + car_capacity[x])
            print(">>> Colour of Car = " + car_colour[x])
            print(">>> Car Price = " + car_price_per_day[x] + "/ Day")
            print("==============================================================")
            print("[1] = Back to previous page.")
            print("[0] = Exit..")
            option = choice()
            if option == 1:
                member_interface(index)
            elif option == 0:
                exit()
            else:
                print("==============================================================")
                print(">>> Invalid Entry !!")
                print(">>> Redirecting to previous page..")
                member_interface(index)
        
    print("==============================================================")
    print(">>>You have not rented any car currently.")
    print("[1] = Back to previous page.")
    print("[0] = Exit..")
    option = choice()
    if option == 1:
        member_interface(index)
    elif option == 0:
        exit()
    else:
        print("==============================================================")
        print(">>> Invalid Entry..")
        print(">>> Redirecting to previous page..")
        member_interface(index)

#==== Member To Modify Personal Details ====#
def modify_personal_details(index):
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    # Open txt file for read
    member_list_modify = open("member.txt","r")

    # Assign cusid to the user who use the username to login
    cus_id = customer_id[index]

    #loop all customer id and find the exact match
    for y in range(len(customer_id)):
        if cus_id == customer_id[y]:
            print("==============================================================")
            print(">>> Your current details is shown below.")
            print(">>> [1] = Username = " + username[y])
            print(">>> [2] = Password = " + password[y])
            print(">>> [3] = Name = " + name[y])
            print(">>> [4] = Age = " + age[y])
            print(">>> [5] = Gender = " + gender[y])
            print(">>> [6] = Phone Number = " + phone_number[y])
            print(">>> [7] = Credit Card Number = " + customer_credit_card[y])
            print("==============================================================")
    member_list_modify.close()

    
    # Another loop for the user to modify its data
    for x in range(len(customer_id)):
        if cus_id == customer_id[x]:
            print(">>> Please Enter number above to modify or Enter 0 Back to previous page.")
            option = choice()
            if option == 1:
                print(">>> Please Enter your New username.")
                new_username = unique_username()
                username[x] = new_username

            elif option == 2:
                print(">>> Please Enter your New password.")
                new_password = str(input("->"))
                password[x] = new_password

            elif option == 3:
                print(">>> Please Enter a new name to show up in your profile.")
                new_name = str(input("->"))
                name[x] = new_name
                
            elif option == 4:
                print(">>> Please Enter a number to update your age.")
                new_age = choice()
                age[x] = str(new_age)

            elif option == 5:
                print(">>> Please Enter 'MALE / FEMALE' to update your gender.")
                new_gender = check_gender()
                gender[x] = new_gender
            
            elif option == 6:
                print(">>> Please Enter your new phone number without symbol (-) and space.")
                print(">>> Please Include a ‘60’ as country number")
                new_phone_number = choice()
                phone_number[x] = str(new_phone_number)
            
            elif option == 7:
                print(">>> Please Enter your new credit card number. (XXXXXXXXXXXXXXXX) = 16digis")
                print(">>> Please Do not included any (space or -)")
                print(">>> Credit card number should not start with ‘0’")
                new_credit_card = check_16_digit()
                customer_credit_card[x] = str(new_credit_card) + "\n"
            
            elif option == 0:
                member_interface(index)
            
            else:
                print("==============================================================")
                print(">>> Invalid Entry..")
                print(">>> Redirecting to previous page..")

    member_list_modify = open("member.txt","w")
    print(">>> Your Changes had been updated.")
    for x in range(len(customer_id)):
        member_list_modify.write(username[x] + ",")
        member_list_modify.write(password[x] + ",")
        member_list_modify.write(customer_id[x] + ",")
        member_list_modify.write(name[x] + ",")
        member_list_modify.write(age[x] + ",")
        member_list_modify.write(gender[x] + ",")
        member_list_modify.write(phone_number[x] + ",")
        member_list_modify.write(current_rented_car_id[x] + ",")
        member_list_modify.write(customer_payment[x] + ",")
        member_list_modify.write(customer_credit_card[x])
    member_list_modify.close()
    member_interface(index)

#==== Unique Username for member ====#
def unique_username():
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    while True:
        unique = []
        for x in range(len(username)):
            unique.append(username[x])
            
        customer_username = str(input("->"))

        if customer_username in unique:
            print(">>> Sorry, this username had been registered.")
            print(">>> Please Enter again")
            continue
        else:
            return customer_username

#==== For function to check the car availability ====#
def check_car_availability(index):
    # Car availabitity as false
    car_availability_info = False
    
    # Get car data
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    # User Input
    print("==============================================================")
    print(">>> Please Enter the Car ID number to rent. (Example : ID1)")
    print("[0] = Enter to back to Main Menu.")
    id_car = str(input("->")).upper()
    
    for x in range(len(car_id)): #loop with range of car ID1 to ID5 = 0,4
        # In our txt file car_avaibility is YES\n so replace it
        if car_availability[x].replace("\n","") == "YES":
            if car_id[x] == id_car:
                car_availability_info = True
                print("==============================================================")
                print(">>> Car ID = " + car_id[x])
                print(">>> Car Brand = " + car_brand[x])
                print(">>> Car Model = " + car_model[x])
                print(">>> Car Plat No = " + car_platno[x])
                print(">>> Year of Car = " + car_year[x])
                print(">>> Type of Car = " + car_type[x])
                print(">>> Car Capacity = " + car_capacity[x])
                print(">>> Colour of Car = " + car_colour[x])
                print(">>> Car Price = " + car_price_per_day[x] + "/ Day")
                print("==============================================================")
            else:
                continue

    # When the info is true, return value for other function
    if car_availability_info == True:
        return car_availability_info, id_car

    else:
        # When the info is false, then back to main menu
        print("==============================================================")
        print(">>> Sorry :( ")
        print(">>> This Car ID is not available.")
        print(">>> Redirecting to main menu..")
        member_interface(index)

#==== For rent_car to check the duration ====#
def check_duration_rent():
    while True:
        try:
            print(">>> Enter the amount of day you want to rent with ' NUMBER '. ")
            date_duration = int(input("->"))
        except ValueError:
            print(">>> Sorry, please Enter A VALID Number for your duration rent.")
            continue
        return date_duration

#==== Check Valid number ====#
def valid_duration_rent():
    while True:
        date_duration = check_duration_rent()
        if date_duration < 0:
            print(">>> Sorry, your duration of rent car should not be negative number.")
            continue
        else:
            return date_duration

#==== For rent car to check the member availability====#
def rent_for_member(index):
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    #read car data
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    
    #Get user current rented id
    rented_id = current_rented_car_id[index]
    for x in range(len(car_id)):
        if rented_id == car_id[x].replace(" ", ""):
            print(">>> You are not allow to rent car")
            print(">>> Due to another renting in progress.")
            details_rented_car(index)
            break
        else:
            pass

#==== Check actual date ====#
def check_valid_date():
    while True:
        date_start = check_date_input()
        #find today date
        today = datetime.date.today()
        #make sure it is not passed date
        if today > date_start:
            print(">>> Please Enter the actual date. (YYYY-MM-DD)")
            continue
        else:
            return date_start

#==== For customer to reserve a car ====#
def rent_car(index):
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    #read car data
    car_id, car_platno, car_year, car_brand, car_model, car_type, car_capacity, car_colour, car_price_per_day, car_availability = read_car_data()
    #read record data
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info = read_record_data()

    # This function is to check the member either can rent car or not
    rent_for_member(index)

    # Retreive data from the function to know the car availability and the id_car to be rent
    car_availability_info, id_car = check_car_availability(index)

    #Check the date start for renting format
    print(">>>Enter the Date to start rent (Format = YYYY-MM-DD)")
    date_start = check_valid_date()
    #Check the duration is number or not
    date_duration = valid_duration_rent()

    #Assign z to calculate with car price per day for total payment
    z = date_duration
    # transfer interger to days
    duration = datetime.timedelta(days = date_duration)
    # Calculate the end days
    end_date_for_rent = date_start + duration

    # Looping to find the index of car and the car price of the id car
    for b in range(len(car_id)):
        if id_car == car_id[b]:
            # Change data type from list to int to str
            price = int(car_price_per_day[b])
            int_total_payment = price * z
            total_payment = str(int_total_payment)

    # Open file for write
    car_list_modify = open("car_details.txt","w")
    # Get specific car id
    for y in range(len(car_id)):
        if id_car == car_id[y]:
            # Assign no to the specific id's car_availability
            car_availability[y] = str("NO\n")
    # Loop to rewrite
    for y in range(len(car_id)):
        car_list_modify.write(car_id[y] + ",")
        car_list_modify.write(car_platno[y] + ",")
        car_list_modify.write(car_year[y] + ",")
        car_list_modify.write(car_brand[y] + ",")
        car_list_modify.write(car_model[y] + ",")
        car_list_modify.write(car_type[y] + ",")
        car_list_modify.write(car_capacity[y] + ",")
        car_list_modify.write(car_colour[y] + ",")
        car_list_modify.write(car_price_per_day[y] + ",")
        car_list_modify.write(car_availability[y])
    car_list_modify.close()
    # Assign variable to rewrite the data

    # Open file
    member_list_modify = open("member.txt","w")
    # Get specific customer id based on login
    cus_id = customer_id[index]
    # loop x to find the same variable index in text file
    for x in range(len(customer_id)):
        if cus_id == customer_id[x]:
            # Modify data
            current_rented_car_id[x] = id_car
            customer_payment[x] = total_payment
    # Loop to rewrite data
    for x in range(len(customer_id)):
        member_list_modify.write(username[x] + ",")
        member_list_modify.write(password[x] + ",")
        member_list_modify.write(customer_id[x] + ",")
        member_list_modify.write(name[x] + ",")
        member_list_modify.write(age[x] + ",")
        member_list_modify.write(gender[x] + ",")
        member_list_modify.write(phone_number[x] + ",")
        member_list_modify.write(current_rented_car_id[x] + ",")
        member_list_modify.write(customer_payment[x] + ",")
        member_list_modify.write(customer_credit_card[x])
    member_list_modify.close()

    # Open file
    new_record_list = open("record.txt","a")
    # Assign variable to be append in record file
    record_cus_id = str(cus_id)
    record_car_id_data = str(id_car)
    record_start_date = str(date_start)
    record_end_date = str(end_date_for_rent)
    record_duration = str(date_duration)
    record_total_price = str(total_payment)
    record_payment_info = "Not"
    # Write variable to record file
    new_record_list.write(record_cus_id + "," + record_car_id_data + "," + 
    record_start_date + "," + record_end_date + "," + record_duration +
     "," + record_total_price + "," + record_payment_info + "\n")
    new_record_list.close()

    # After all data been updatedq
    print("==============================================================")
    print(">>> Your rent car total payment = " + total_payment)
    print(">>> You need to return the car on " + record_end_date)
    print(">>> Your car will be hold until you had complete your payment.")
    print("==============================================================")
    print("[1] = Back to Main Menu")
    print("[2] = Proceed to payment")
    print("[0] = Exit")
    print("==============================================================")
    option = choice()
    if option == 1:
        member_interface(index)
    elif option == 2:
        complete_payment(index)
    elif option == 0:
        exit()
    else:
        print("==============================================================")
        print(">>> Invalid Entry !!")
        print(">>> Redirecting to main menu..")
        member_interface(index)

#==== Update data when completed payment ====#
def update_data(index):
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    #read record data
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info = read_record_data()

    # Open file to write
    member_list_modify = open("member.txt","w")
    # Search for specific customer
    cus_id = customer_id[index]
    for x in range(len(customer_id)):
        if cus_id == customer_id[x]:
            # assign data
            customer_payment[x] = "null"
    # Loop to rewrite
    for x in range(len(customer_id)):
        member_list_modify.write(username[x] + ",")
        member_list_modify.write(password[x] + ",")
        member_list_modify.write(customer_id[x] + ",")
        member_list_modify.write(name[x] + ",")
        member_list_modify.write(age[x] + ",")
        member_list_modify.write(gender[x] + ",")
        member_list_modify.write(phone_number[x] + ",")
        member_list_modify.write(current_rented_car_id[x] + ",")
        member_list_modify.write(customer_payment[x] + ",")
        member_list_modify.write(customer_credit_card[x])
    member_list_modify.close()

    # Open file to write
    modify_record_list = open("record.txt","w")
    # Search for specific data
    cus_id = customer_id[index]
    customer_booked_car_id = current_rented_car_id[index]
    for i in range(len(record_customer_id)):
        if cus_id == record_customer_id[i]:
            if customer_booked_car_id == record_car_id[i]:
                # Assign data
                payment_info[i] = "Done\n"
    # Loop to rewrite
    for i in range(len(record_customer_id)):
        modify_record_list.write(record_customer_id[i] + ",")
        modify_record_list.write(record_car_id[i] + ",")
        modify_record_list.write(start_date[i] + ",")
        modify_record_list.write(end_date[i] + ",")
        modify_record_list.write(duration_rent[i] + ",")
        modify_record_list.write(total_price[i] + ",")
        modify_record_list.write(payment_info[i])
    modify_record_list.close

#==== Complete payment and update data ====#
def complete_payment(index):
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()

    # Specific the member
    cus_id = customer_id[index]
    for x in range(len(customer_id)):
        # If it match
        if cus_id == customer_id[x]:
            # If member's payment is null
            if customer_payment[x] == "null":
                print("==============================================================")
                print(">>> You has no payment need to be complete !!")
                print(">>> Redirecting to main menu..")
                member_interface(index)
                break
            else:
                print("==============================================================")
                print(">>> Do you want to complete your payment to confirm booking ??")
                print(">>> Total price = " + customer_payment[x])
                print("[1] = Confirm payment with Credit card : " + customer_credit_card [x].replace("\n",""))
                print("[2] = Back to main menu")
                print("[0] = Exit")

    # Option as choice function
    option = choice()
    if option == 1:
        print("==============================================================")
        print(">>> Your payment has done !! ")
        print(">>> Redirecting to main menu..")
        update_data(index)
        member_interface(index)
    elif option == 2:
        member_interface(index)
    elif option == 0:
        exit()
    else:
        print("==============================================================")
        print(">>> Invalid Entry..")
        print(">>> Redirecting to main menu..")
        member_interface(index)

#==== For member to view own rental history ====#
def view_personal_rental_history(index):
    #read record data
    record_customer_id, record_car_id, start_date, end_date, duration_rent, total_price, payment_info = read_record_data()
    #read member data
    username, password, customer_id, name, age, gender, phone_number, current_rented_car_id, customer_payment, customer_credit_card = read_member_data()
    
    # Search for specific user
    cus_id = customer_id[index]
    i = 0
    for x in range(len(record_customer_id)):
        # When the record had found
        if cus_id == record_customer_id[x]:
            i = i + 1
            no = str(i)
            # Display the founded record and continue
            print("=========================================================================================")
            print("["+no+"] Car ID = "+ record_car_id[x] + ", Start Date = " + start_date[x] 
            + ", End Date = " + end_date[x] + ", Total Price Paid = " + total_price[x])
            continue
    print("=========================================================================================")
    print(">>> Above is all your rental history.")
    print("[1] = Back to main menu")
    print("[0] = Exit")
    option = choice()
    if option == 1:
        member_interface(index)
    elif option == 0:
        exit()
    else:
        print(">>> Invalid Input !!")
        print(">>> Redirecting to main menu..")
        member_interface(index)

#--------------------------------------------------------------Call Function-------------------------------------------------------------
main_menu()
#------------------------------------------------------------------End------------------------------------------------------------------