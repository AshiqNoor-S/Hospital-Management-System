import time
import random
import datetime
import sys
import pyttsx3
import mysql.connector
import calendar
import webbrowser
import simpleaudio as sa
from clrprint import *
from tabulate import *

try:

    import nltk
    import numpy as np
    import random
    import string
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import TfidfVectorizer



except:
    print('')

while True:
    clrprint("\t\t***************************************************************", clr='r')
    clrprint("\t\t*                                                             *", clr='r')
    clrprint("\t\t*                   Metropolitan Hospital                     *", clr='r')
    clrprint("\t\t*                   Established in 1979                       *", clr='r')
    clrprint("\t\t*                  Your Health Is Our Concern                 *", clr='r')
    clrprint("\t\t***************************************************************", clr='r')

    # Making the database
    passwd = str(clrinput("\n Please enter the database password :", clr='b'))
    mysql = mysql.connector.connect(host="localhost", user="root", passwd=passwd)
    if mysql.is_connected() == True:
        print("\n Connection established Successfully  !! ")
    else:
        print("!!!!! Sorry could not be established !!!!!")

    mycursor = mysql.cursor()
    mycursor.execute("create database if not exists Metro_Hospital")
    mycursor.execute("use Metro_Hospital")
    mycursor.execute(
        "create table if not exists patient_details(patient_id varchar(25) primary key,name varchar(30) not null,sex varchar(10),age varchar(3),address varchar(50),contact_number varchar(25),specialization varchar(30))")
    mycursor.execute(
        "create table if not exists doctor_details(id varchar(10) primary key, name varchar(30), specialization varchar(40),sex varchar(3),age varchar(3),address varchar(30),contact varchar(15),fees varchar(10),Monthly_salary varchar(20))")
    mycursor.execute(
        "create table if not exists nurse_details(id varchar(10) primary key, name varchar(30),sex varchar(5), age varchar(3),address varchar(30),contact varchar(15),Monthly_salary varchar(10))")
    mycursor.execute("create table if not exists user_data(username varchar(30) primary Key,password varchar(30))")
    mycursor.execute(
        "create table if not exists facilities(serial_no varchar(10) primary key, services_available varchar(25))")
    mycursor.execute(
        "create table if not exists appointment(id varchar(10) , name_patient varchar(25), name_doctor varchar(25), age_patient varchar(4) ,date varchar(20) , time varchar(20))")
    mycursor.execute(
        "create table if not exists results(covid_id varchar(5) primary key not null, serial_no varchar(5), name varchar(20), result varchar(10))")
    mycursor.execute(
        "create table if not exists covid_ward(covid_id varchar(5) primary key not null,serial_no varchar(5) not null, name varchar(20), current_result varchar(13), status varchar(15))")

    # Sign in Music
    filename = 'metro intro.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    # Creating object for 'text-to-speech'
    engine = pyttsx3.init()


    def insert_values():
        mycursor.execute(
            "insert into patient_details values('1001', 'Koshi Vargheese', 'M','49','Birmingham','9712345678','Surgeon'), ('1002', 'Sameera Perisic', 'F','28','Tottenham','971987698','Urologist'), ('1003', 'Toshiba Samsung', 'M','22','Zayan','9723456878','Cardiology'), ('1004', 'Lava Daniels', 'M','20','Michigan','9712345999','Surgeon'), ('1005', 'John Rocks', 'M','20','South Dakota','9712345609','Pediatrician')")
        mycursor.execute(
            "insert into doctor_details values('1006', 'Aneesah Powers', 'Surgeon','F','33','Koulibaly,Milan', '10922388901', '135','13000'), ('1007', 'Fox Leblanc', 'Physicist','M','33','Manchester,England', '1092238800', '135','13000'), ('1008', 'Anis Boone', 'Gynecologist','M','39','Nerul, NaviMumbai', '1090088901', '175','13000'), ('1009', 'Anees Par', 'Dermatologist','M', '27','Kouli,Toronto', '1096678901', '105','13000'), ('1010', 'Amara Huffmann', 'Physician','F', '40','Rolla, UAE', '1667798231', '100','13000')")
        mycursor.execute(
            "insert into nurse_details values('1011', 'Joseline Jacobs', 'F','21','Somewolid, South Africa','9097654348','3500'),('1012', 'Marcus Rashlord', 'M','23','Sussex, England','9097456723','3500'), ('1013', 'Lionel Messi', 'M','33','Catalonia, Barcelona','9090098765','3500'), ('1014', 'Cristiano Ronaldo', 'M','35','Madiera, Portugal','909700988','3500'), ('1015', 'Melissa Cordon', 'F','29','Cincinatti, Ohio','987651234','3500')")
        mycursor.execute(
            "insert into user_data values('sis123', '1234'), ('lm10', '644'), ('cr7', '450'), ('ls09', '198'), ('vvd04', '50')")
        mycursor.execute(
            "insert into facilities values('1016', 'X-ray'), ('1017', 'Ambulatory'), ('1018', 'Blood-collection'), ('1019', 'Addiction-'), ('1020', 'Emergency')")
        mycursor.execute(
            "insert into appointment values('1001','Koshi Vargheese', 'Aneesah Powers', '49', '22/12/20', '10:00am - 11:00am'), ('1002', 'Sameera Perisic ', 'Fox Leblanc', '28', '19/11/20', '10:00am - 11:00am'),('1003','Toshiba Samsung', 'Anis boone', '22', '18/12/20', '10:00am - 11:00am'),('1005','John Rocks', 'Amara Huffmann', '20', '28/07/20', '10:00am - 11:00am')")
        mycursor.execute(
            "insert into results values('1636','1001', 'Koshi Vargheese', 'POSITIVE'), ('1639', '1002', 'Sameera Perisic', 'NEGATIVE'), ('1780','1003', 'Toshiba Samsung', 'POSITIVE'), ('4269', '1004', 'Lava Daniels', 'POSITIVE'), ('4270','1005', 'John Rocks', 'NEGATIVE')")
        mycursor.execute(
            "insert into covid_ward values('1636', '1001', 'Koshi Vargheese', 'POSITIVE', 'IN-WARD'), ('1639','1002', 'Sameera Perisic', 'NEGATIVE', 'NOT-IN-WARD'), ('1780','1003', 'Toshiba Samsung', 'POSITIVE', 'IN-WARD'), ('4269', '1004', 'Lava Daniels', 'POSITIVE', 'IN-WARD'), ('4279','1005', 'John Rocks', 'NEGATIVE', 'NOT-IN-WARD')")
        mysql.commit()


    # insert_values()
    # Run the above function only for the first time execution inorder to preload some default values to the dataset


    # main while loop(for signing in/ registering)
    while True:

        clrprint("""
               1.Sign in (login)
               2.Signup(register)
               """, clr='yellow')
        r = int(clrinput("Enter your choice: "))
        if r == 2:
            clrprint("""
                   =====================!!!!!!!please register yourself!!!!!===========
                   """, clr='magenta')
            username = clrinput("Enter your preffered username", clr='default')
            password = clrinput("Enter your preffered password", clr='default')
            mycursor.execute("select username from user_data where username = '{}'".format(username))
            user_record = mycursor.fetchall()
            if len(user_record) > 0:
                print("!!Invalid!!, username already exists")

            else:
                mycursor.execute("insert into user_data values('" + username + "','" + password + "')")
                mysql.commit()
                clrprint("""
                    =================================================================================
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!Registered Successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    =================================================================================
                    """, clr='magenta')

        x = clrinput("\nEnter any key to continue  : ")
        if r == 1:
            clrprint("""
                =================================================================================
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {{sign in }} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                =================================================================================
                """, clr='magenta')
            username = clrinput("\nEnter the username:", clr='default')
            password = clrinput("Enter the password:", clr='default')
            mycursor.execute("select password from user_data where username='" + username + "'")
            data = mycursor.fetchall()
            for i in data:
                a = list(i)
                if a[0] == str(password):
                    # while loop for the main menu

                    while True:
                        op = 'nN'
                        while op in 'nN':
                            clrprint("""                                   ========================== 
                                   | 1.Administration           |
                                   | 2.Patient                  |
                                   | 3.Covid - 19 Chatbot       |
                                   | 4.Covid - 19 Zone          |
                                   | 5.Help Desk                |
                                   | 6.Sign out                 |
                                   =============================
                                   """, clr='b')

                            o = int(clrinput("\n Enter your choice :", clr='default'))
                            if o == 1:
                                y = clrinput("Enter the database password   :", clr='default')
                                # asking for the database password(admin menu) , for authenticity
                                if y == str(passwd):
                                    ch = 'n'
                                    while ch in 'nN':
                                        # available options in admin menu
                                        print("""
                                                1. Add Doctors                              2. Add Nurses
                                                3. Add Patients                             4. See Doctor Details
                                                5. See Nurse Details                        6. See Patient Details
                                                7. Update Doctor Details                    8. Update Nurse Details
                                                9. Update Patient Details                   10. Deleting Nurse Details
                                                11. Deleting Doctor Details                 12. Deleting Patient Details
                                                13. Add Facilities                          14. Check Facilities
                                                15. Check Appointments                      16. Check COVID-19 Results
                                                17. Check COVID-19 ward details             18. Exit""")

                                        b = int(input("Enter your choice :"))

                                        # adding doctors
                                        if b == 1:
                                            doctor_id = random.randint(100, 9999)
                                            mycursor.execute("select id from doctor_details")
                                            data_id = mycursor.fetchall()
                                            while doctor_id in data_id:
                                                doctor_id = random.randint(100, 9999)
                                            name_doctor = input("Enter your name :")
                                            age_doctor = input("Enter your age :")
                                            sex = input("Enter your Sex : ")
                                            address = input("Enter your address please :")
                                            contact_no = input("Enter your contact number please :")
                                            monthly_salary = input("Enter your monthly salary :")
                                            specialization = input("Enter your specilization :")
                                            fees = input("Enter your fees :")
                                            mycursor.execute(
                                                "insert into doctor_details values('" + str(doctor_id) + "','" + str(
                                                    name_doctor) + "','" + str(specialization) + "','" + str(
                                                    sex) + "','" + str(age_doctor) + "','" + str(address) + "','" + str(
                                                    contact_no) + "','" + str(fees) + "','" + str(
                                                    monthly_salary) + "')")
                                            mysql.commit()
                                            print("Succesfully registered")
                                            mycursor.execute(
                                                "select * from doctor_details where id ='{}'".format(doctor_id))
                                            rec = mycursor.fetchall()
                                            print(tabulate(rec, headers=['Id', 'Name', 'specialization', 'Sex', 'Age',
                                                                         'Address', 'Contact Number', 'Fees',
                                                                         'Monthly Salary'], tablefmt='fancy_grid'))
                                            print("""
                                                 Please verify your details from the table displayed above,
                                                 if any changes, please visit update section
                                                 """)

                                        # adding nurses
                                        if b == 2:
                                            nurse_id = random.randint(100, 9999)
                                            mycursor.execute("select patient_id from patient_details")
                                            data_id = mycursor.fetchall()
                                            while nurse_id in data_id:
                                                nurse_id = random.randint(100, 9999)
                                            name_nurse = input("Enter your name :")
                                            age_nurse = input("Enter your age :")
                                            sex = input("Enter your Sex : ")
                                            address = input("Enter your address please :")
                                            contact_no = input("Enter your contact number please :")
                                            monthly_salary = input("Enter your monthly salary :")
                                            mycursor.execute(
                                                "insert into nurse_details values('" + str(nurse_id) + "','" + str(
                                                    name_nurse) + "','" + str(sex) + "','" + str(
                                                    age_nurse) + "', '" + str(address) + "','" + str(
                                                    contact_no) + "','" + str(monthly_salary) + "')")
                                            mysql.commit()
                                            print("Succesfully registered")
                                            mycursor.execute(
                                                "select * from nurse_details where id ='{}'".format(nurse_id))
                                            rec = mycursor.fetchall()
                                            print(tabulate(rec, headers=['Id', 'Name', 'Sex', 'age', 'Address',
                                                                         'Contact number', 'monthly salary'],
                                                           tablefmt='fancy_grid'))
                                            print("""Verfiy your details from the table displayed above .
                                                If any changes to be made , please visit the update section
                                                """)

                                        # adding patients
                                        if b == 3:
                                            patient_id = random.randint(100, 9999)
                                            mycursor.execute("select patient_id from patient_details")
                                            data_id = mycursor.fetchall()
                                            while patient_id in data_id:
                                                patient_id = random.randint(100, 9999)
                                            name_patient = input("Enter your name :")
                                            age_patient = input("Enter your age :")
                                            sex = input("Enter your sex please :")
                                            address = input("Enter your address please :")
                                            contact_no = input("Enter your contact number please :")
                                            specialization = input("Enter your specialization please :")
                                            mycursor.execute(
                                                "insert into patient_details values('" + str(patient_id) + "','" + str(
                                                    name_patient) + "', '" + str(sex) + "','" + str(
                                                    age_patient) + "', '" + str(address) + "','" + str(
                                                    contact_no) + "','" + str(specialization) + "')")
                                            mysql.commit()
                                            print("Succesfully registered")
                                            mycursor.execute(
                                                "select * from patient_details where patient_id ='{}'".format(
                                                    patient_id))
                                            rec = mycursor.fetchall()
                                            print(tabulate(rec, headers=['Id', 'Name', 'Sex', 'age', 'Address',
                                                                         'Contact number', 'specialization'],
                                                           tablefmt='fancy_grid'))
                                            print("""
                                                Please verify your details from the table displayed above,
                                                if any changes to be done, please visit the update section
                                                """)

                                        # display all the doctors
                                        if b == 4:
                                            mycursor.execute("select * from doctor_details")
                                            data = mycursor.fetchall()
                                            print(tabulate(data, headers=['Id', 'Name', 'Specialization', 'Sex', 'Age',
                                                                          'Address', 'Contact', 'Fees',
                                                                          'Monthly salary'], tablefmt='fancy_grid'))

                                        # display all the nurses
                                        if b == 5:
                                            mycursor.execute("select * from nurse_details")
                                            data = mycursor.fetchall()
                                            print(tabulate(data,
                                                           headers=['Id', 'Name', 'Sex', 'Age', 'Address', 'Contact',
                                                                    'Monthly salary'], tablefmt='fancy_grid'))

                                        # display all the patients
                                        if b == 6:
                                            mycursor.execute("select * from patient_details")
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(tabulate(data,
                                                               headers=['Patient ID', 'Name', 'Sex', 'Age', 'Address',
                                                                        'Contact_number', 'Specialisation'],
                                                               tablefmt='fancy_grid'))
                                            else:
                                                print("No results available at the moment")

                                        # updating doctor's details
                                        if b == 7:
                                            id = input("Enter the doctor's id: ")
                                            mycursor.execute("select * from doctor_details where id = '{}'".format(id))
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print("The data to be updated is: ")
                                                print(tabulate(data,
                                                               headers=['Doctor Id', 'Name', 'Specialization', 'Sex',
                                                                        'Age', 'Address', 'Contact No', 'Fees',
                                                                        'Monthly Salary']))
                                                print("""
                                                           1. Address
                                                           2. Contact number
                                                           3. Fees
                                                           4. Salary
                                                            """)
                                                update_field = int(input(
                                                    "Enter the field you want to update from the above listed menus : "))
                                                if update_field == 1:
                                                    new_address = input("Enter the new address please: ")
                                                    mycursor.execute(
                                                        "update doctor_details set address='{}' where id ='{}'".format(
                                                            new_address, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 2:
                                                    new_number = input("Enter the new number please: ")
                                                    mycursor.execute(
                                                        "update doctor_details set contact='{}' where id ='{}'".format(
                                                            new_number, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 3:
                                                    new_fees = input("Enter the new fees amount please: ")
                                                    mycursor.execute(
                                                        "update doctor_details set fees='{}' where id ='{}'".format(
                                                            new_fees, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 4:
                                                    new_salary = input("Enter the new salary please: ")
                                                    mycursor.execute(
                                                        "update doctor_details set monthly_salary='{}' where id ='{}'".format(
                                                            new_salary, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field not in (1, 2, 3, 4):
                                                    print("!!Invalid Choice!!  Please Try Again")

                                            else:
                                                print("No database present, Please Type Valid id")

                                        # update the nurse details
                                        if b == 8:
                                            id = input("Enter the nurse ID : ")
                                            mycursor.execute("select * from nurse_details where id = '{}'".format(id))
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print("The data to be updated is: ")
                                                print(tabulate(data,
                                                               headers=['Nurse Id', 'Name', 'Sex', 'Age', 'Address',
                                                                        'Contact No', 'Monthly Salary'],
                                                               tablefmt='fancy_grid'))
                                                print("""
                                                       1. Address
                                                       2. Contact number
                                                       3. Salary
                                                       """)
                                                update_field = int(input("Enter the field you want to update: "))
                                                print()
                                                if update_field == 1:
                                                    new_address = input("Enter the new address please: ")
                                                    mycursor.execute(
                                                        "update nurse_details set address='{}' where id ='{}'".format(
                                                            new_address, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 2:
                                                    new_number = input("Enter the new number please: ")
                                                    mycursor.execute(
                                                        "update nurse_details set contact='{}' where id ='{}'".format(
                                                            new_number, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 3:
                                                    new_salary = input("Enter the new salary please: ")
                                                    mycursor.execute(
                                                        "update doctor_details set monthly_salary='{}' where id ='{}'".format(
                                                            new_salary, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field not in (1, 2, 3):
                                                    print("!!INVALID CHOICE!!, please try again")
                                            else:
                                                print("No record found in the database")

                                        # update the patient details
                                        if b == 9:
                                            id = input("Enter the patient's ID: ")
                                            mycursor.execute(
                                                "select * from patient_details where patient_id = '{}'".format(id))
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print("The data to be updated is: ")
                                                print(tabulate(data,
                                                               headers=['Patient ID', 'Name', 'Sex', 'Age', 'Address',
                                                                        'Contact NO', 'Specialization'],
                                                               tablefmt='fancy_grid'))
                                                print("""
                                                       1. address
                                                       2. contact number
                                                       3. Specialisation
                                                       """)
                                                update_field = int(input("Enter the field you want to update: "))
                                                print()
                                                if update_field == 1:
                                                    new_address = input("Enter the new address please: ")
                                                    mycursor.execute(
                                                        "update patient_details set address='{}' where patient_id ='{}'".format(
                                                            new_address, id))
                                                    mysql.commit()
                                                    print()
                                                    print("The record has been updated successfully")

                                                if update_field == 2:
                                                    new_number = input("Enter the new number please: ")
                                                    mycursor.execute(
                                                        "update patient_details set contact_number='{}' where patient_id ='{}'".format(
                                                            new_number, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field == 3:
                                                    specialization = input("Enter the new salary please: ")
                                                    mycursor.execute(
                                                        "update patient_details set specialization='{}' where patient_id ='{}'".format(
                                                            specialization, id))
                                                    mysql.commit()
                                                    print("The record has been updated successfully")

                                                if update_field not in (1, 2, 3):
                                                    print("!!Invalid choice!!, Please try again")

                                            else:
                                                print("No record found in the database ")

                                        # deleting a nurse's details
                                        if b == 10:
                                            id = input("Enter nurse ID :")
                                            mycursor.execute("select * from nurse_details where id='" + id + "'")
                                            data = mycursor.fetchall()
                                            choice = input("you really want to delete this data? (y/n):")
                                            if len(data) > 0:
                                                if choice in "yY":
                                                    mycursor.execute("delete from nurse_details where id='" + id + "'")
                                                    mysql.commit()
                                                    print("Successfully deleted!!")
                                                else:
                                                    print("Not deleted")
                                            else:
                                                print('Sorry, no records available for deletion')

                                        # deleting a doctor's details
                                        if b == 11:
                                            id = input("Enter Doctor ID :")
                                            mycursor.execute("select * from doctor_details where id='" + id + "'")
                                            data = mycursor.fetchall()
                                            choice = input("you really want to delete this data? (y/n):")
                                            if len(data) > 0:
                                                if choice in "Yy":
                                                    mycursor.execute("delete from doctor_details where id='" + id + "'")
                                                    mysql.commit()
                                                    print("successfully deleted!!")
                                                else:
                                                    print("Not deleted")
                                            else:
                                                print("Sorry, no records available for deletion")

                                        # deleting a patient's details
                                        if b == 12:
                                            id = input("Enter patient ID : ")
                                            mycursor.execute(
                                                "select * from patient_details where patient_id='" + id + "'")
                                            data = mycursor.fetchall()
                                            choice = input("Do you really want to delete this data ? (y/n):")
                                            if len(data) > 0:
                                                if choice in "yY":
                                                    mycursor.execute(
                                                        "delete from patient_details where patient_id='" + id + "'")
                                                    mycursor.execute(
                                                        "delete from the appointment where id='" + id + "'")
                                                    mysql.commit()
                                                    print("Successfully deleted !!")
                                                else:
                                                    print("Not deleted")
                                            else:
                                                print("Sorry, no records available for deletion")

                                        # Adding Facilities
                                        if b == 13:
                                            serial_no = random.randint(100, 9999)
                                            mycursor.execute("select serial_no from facilities")
                                            data = mycursor.fetchall()
                                            while serial_no in data:
                                                serial_no = random.randint(100, 9999)
                                            facilities_available = input("Enter the facilities available")
                                            mycursor.execute(
                                                "insert into facilities values('" + str(serial_no) + "','" + str(
                                                    facilities_available) + "')")
                                            mysql.commit()
                                            print("Successfully Added ")

                                        # Check available facilities
                                        if b == 14:
                                            mycursor.execute("select * from facilities")
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(tabulate(data, headers=['Serial No', 'Services Available'],
                                                               tablefmt='fancy_grid'))
                                            else:
                                                print("Sorry, no facilities available at the moment")

                                        # displaying all the appointments
                                        if b == 15:
                                            mycursor.execute("select * from appointment")
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(tabulate(data,
                                                               headers=['Name of the patient', 'Name of the Doctor',
                                                                        'Age of the patient', 'Date', 'Time'],
                                                               tablefmt='fancy_grid'))
                                            else:
                                                print("Sorry no appointments available at the moment")

                                        # displaying COVID-19 test results
                                        if b == 16:
                                            mycursor.execute("select * from results")
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(
                                                    tabulate(data, headers=['COVID ID', 'Serial NO', 'Name', 'Result'],
                                                             tablefmt='fancy_grid'))
                                            else:
                                                print("No results available at the moment")

                                        # Check COVID-19 Ward details
                                        if b == 17:
                                            mycursor.execute("select * from covid_ward")
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(tabulate(data, headers=['COVID ID', 'Serial NO', 'Name',
                                                                              'Current_result', 'Status'],
                                                               tablefmt='fancy_grid'))
                                            else:
                                                print("The ward is Empty ")

                                        # Exiting Adminstration menu
                                        if b == 18:
                                            for n in ".....":
                                                sys.stdout.write(n)
                                                sys.stdout.flush()
                                                time.sleep(0.2)
                                            ch = input("\nAre You sure you want to exit(y/n):")
                                            print(n)

                                        # Invalid choice

                                        l = [i for i in range(1, 19)]
                                        if b not in l:
                                            print("!!INVALID CHOICE!!")

                                if y != str(passwd):
                                    clrprint("Password does not match, please try again later", clr='r')

                            if o == 2:
                                op = 'n'
                                while op in 'nN':
                                    # available options in patient menu
                                    print("""
                                           1. See your details
                                           2. Facilities
                                           3. See Doctor Details
                                           4. Appointment
                                           5. Exit
                                           """)

                                    j = int(input("\nEnter your choice: "))

                                    if j == 1:
                                        serial_no = input("Enter your Patient ID: ")
                                        mycursor.execute(
                                            "select * from patient_details where patient_id = '{}'".format(serial_no))
                                        data = mycursor.fetchall()
                                        if len(data) > 0:
                                            print(tabulate(data, headers=['Patient ID', 'Name', 'Sex', 'Age', 'Address',
                                                                          'Contact_number', 'Specialisation'],
                                                           tablefmt='fancy_grid'))
                                        else:
                                            print("Invalid Patient ID Please type in valid ID")

                                    # Display list of facilities avaialable

                                    if j == 2:
                                        mycursor.execute("select * from facilities")
                                        data = mycursor.fetchall()
                                        if len(data) > 0:
                                            print(tabulate(data, headers=['Serial_no', 'Services_available']))

                                        else:
                                            print("Sorry, no facilities available at the moment.")

                                    # displaying list of doctors available
                                    if j == 3:
                                        mycursor.execute("select name, age from doctor_details")
                                        data = mycursor.fetchall()
                                        if len(data) > 0:
                                            print(tabulate(data, headers=['Name', 'Age'], tablefmt='fancy_grid'))
                                        else:
                                            print("Sorry, no doctors available at the moment.")

                                    # Administartion (only for patients)
                                    if j == 4:
                                        id = input("Enter your patient ID : ")
                                        mycursor.execute(
                                            "Select * from patient_details where patient_id='{}'".format(id))
                                        patientrec = mycursor.fetchall()
                                        if len(patientrec) > 0:
                                            for i in patientrec:
                                                name_patient = i[1]
                                                print("\nWelcome to appointment menu ", name_patient)
                                            name_doctor = input("Enter the  doctor's name:")
                                            age_patient = input("Enter your age :")
                                            year = int(input("Enter the year you want to take appointment : "))
                                            month = int(input("Enter the Month you want to take appointment : "))
                                            print(calendar.month(year, month))
                                            print()
                                            date = input(
                                                "Enter the desired date for the appointment from the calendar in (YYYY/MM/DD) displayed above:  ")
                                            print("The dates booked up already for the Doctor selected is :")
                                            mycursor.execute(
                                                "select name_doctor,time from appointment where name_doctor='{}'".format(
                                                    name_doctor))
                                            data1 = mycursor.fetchall()
                                            if len(data1) > 0:
                                                print(tabulate(data1, headers=['Name of the Doctor', 'Time'],
                                                               tablefmt='fancy_grid'))

                                            if len(data1) == 0:
                                                print("No data present")
                                            time_dict = {1: '10.00am-11.00am', 2: '12.00am-1.00pm',
                                                         3: '1.00pm - 2.00pm', 4: '4.00pm - 5.00pm',
                                                         5: '5.00pm - 6.00pm'}
                                            for i in range(len(time_dict)):
                                                print(i + 1, '\t\t', time_dict[i + 1])
                                            ch = int(input(
                                                "Enter your choice from the list of time given above other than the once already booked : "))
                                            if ch == 1:
                                                tme = '10:00am - 11:00am'
                                            if ch == 2:
                                                tme = '12:00am - 1:00pm'
                                            if ch == 3:
                                                tme = '1:00pm - 2:00pm'
                                            if ch == 4:
                                                tme = '4:00pm - 5:00pm'
                                            if ch == 5:
                                                tme = '5:00pm - 6:00pm'
                                            if ch not in (1, 2, 3, 4, 5):
                                                print('Invalid Choice')
                                            if len(data1) > 0:

                                                for field in data1:
                                                    if field[1] != tme:
                                                        mycursor.execute(
                                                            "insert into appointment values(%s,%s,%s,%s,%s,%s)",
                                                            (id, name_patient, name_doctor, age_patient, date, tme))
                                                        mysql.commit()
                                                        print("The appointment is booked successfully")
                                                    else:
                                                        print(
                                                            "The time slot you have selected is already booked up , Please select a different time slot ")

                                            else:
                                                mycursor.execute("insert into appointment values(%s,%s,%s,%s,%s,%s)", (
                                                id, name_patient, name_doctor, age_patient, date, tme))
                                                mysql.commit()
                                                print("The appointment is booked successfully")


                                        else:
                                            print('Please register yourself into the hospital ')

                                    # Exiting out of patient menu

                                    if j == 5:
                                        for n in ".....":
                                            sys.stdout.write(n)
                                            sys.stdout.flush()
                                            time.sleep(0.2)
                                        print(n)
                                        op = input("\nAre you sure you want to exit(y/n):")
                                        if op == 'yY':
                                            break

                                    if j not in (1, 2, 3, 4, 5):
                                        print("!!INVALID CHOICE!!")

                                # The available options in covid 19 Menu

                            if o == 4:
                                op = 'n'
                                while op in 'nN':
                                    print("""
                                           1. Test For Covid
                                           2. Check Results
                                           3. Precautions to be taken
                                           4. Check Live COVID updates
                                           5. Book a room in ward
                                           6. Exit
                                           """)
                                    s = int(input("Enter your choice: "))

                                    # Test for Covid 19
                                    if s == 1:
                                        code = input("Enter your patient ID : ")
                                        mycursor.execute('Select patient_id from patient_details')
                                        data = mycursor.fetchall()
                                        found = False
                                        for b in data:
                                            for c in b:
                                                if c == code:
                                                    found = True
                                                    break
                                        if found == True:
                                            covid_id = random.randint(100, 9999)
                                            mycursor.execute("select covid_id from results")
                                            data_id = mycursor.fetchall()
                                            while covid_id in data_id:
                                                covid_id = random.randint(100, 9999)
                                            print("Your COVID_ID generated is: ", covid_id)
                                            print("Please use this COVID_ID for further references ")
                                            mycursor.execute(
                                                "select name from patient_details where patient_id='{}'".format(code))
                                            data = mycursor.fetchall()
                                            for i in data:
                                                name_patient = i[0]
                                                print("Welcome to Covid 19 - Zone", name_patient)
                                            age = int(input("Enter your age please: "))
                                            print("""
                                                   Type 'Y' if your answer is yes
                                                   'N' if your answer is no
                                                   if you have any of the conditions asked below, please 
                                                   respond accurately
                                                   """)
                                            a = input("any heart conditions: ")
                                            b = input("asthma: ")
                                            c = input("high blood pressure: ")
                                            d = input("bluish lips: ")
                                            e = input("Sore throat: ")
                                            f = input("nausea or vomiting: ")
                                            g = input("Loss of taste or smell: ")
                                            h = input("Nasal congestion or runny nose")
                                            l = [a, b, c, d, e, f, g]
                                            print("Thank you, please wait for your result")
                                            pos = 'POSITIVE'
                                            neg = 'NEGATIVE'
                                            count = 0
                                            for elements in l:
                                                if elements in 'yY':
                                                    count = count + 1
                                                else:
                                                    continue
                                            if count >= 5:
                                                mycursor.execute("insert into results values('" + str(
                                                    covid_id) + "','" + code + "', '" + name_patient + "','" + pos + "')")
                                                mysql.commit()
                                            else:
                                                mycursor.execute("insert into results values('" + str(
                                                    covid_id) + "','" + code + "', '" + name_patient + "','" + neg + "')")
                                                mysql.commit()

                                            mycursor.execute(
                                                "select result from results where serial_no='{}'".format(code))
                                            record = mycursor.fetchall()
                                            for i in record:
                                                if i == 'POSITVE':
                                                    fac = input("Do you have the facilites for isolation?(y/n): ")
                                                    if fac in "nN":
                                                        print("please visit menu number 5 for booking a ward")
                                                    else:
                                                        print("""
                                                               Please take care of yourself at home
                                                               Stay in Isolation for the next 14 days
                                                               """)

                                                else:
                                                    print("Stay home, stay safe")

                                        else:
                                            print("Invalid Patient Id, Please register yourself")
                                            os.system('say "Invalid Patient ID, Please register yourself"')
                                    # Check results

                                    if s == 2:
                                        code = input("Enter your COVID_ID please: ")
                                        mycursor.execute("select * from results where covid_id ={}".format(code))
                                        data = mycursor.fetchall()
                                        if len(data) > 0:
                                            print('          Metropolitan Hospital       ')
                                            print('             COVID-19 Result  ')

                                            print()
                                            print('Result generated : ', datetime.datetime.now())
                                            print("-" * 100)
                                            print(tabulate(data, headers=['Covid ID ', 'Serial no', 'Name', 'Result'],
                                                           tablefmt='fancy_grid'))
                                            print("\n ** This is a computer based test. The results may vary ** ")
                                            print("-" * 100)


                                        else:
                                            print("No results available at the Moment")

                                    # Precautions to be taken and useful links

                                    if s == 3:
                                        print("""
                                               *To prevent the spread of COVID-19:
                                               *Clean your hands often. Use soap and water, or an alcohol-based hand rub.
                                               *Maintain a safe distance from anyone who is coughing or sneezing.
                                               *Wear a mask when physical distancing is not possible.
                                               *Don’t touch your eyes, nose or mouth.Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
                                               *Stay home if you feel unwell.
                                               *If you have a fever, cough and difficulty breathing, seek medical attention.
                                               """)
                                        print()
                                        read = clrinput("Read aloud (Y/N)", clr='magenta')
                                        if read in 'Yy':
                                            print()
                                        else:
                                            pass
                                        choice = input("Do you want to know more COVID-19(Y/N): ")
                                        if choice in 'yY':
                                            webbrowser.open_new_tab(
                                                "https://www.google.com/search?q=covid+updates&rlz=1C5CHFA_enAE910AE910&oq=c"
                                                "ovid+updates&aqs=chrome..69i57j0j0i22i30l6.3382j1j7"
                                                "&sourceid=chrome&ie=UTF-8#wptab=s:H4sIAAAAAAA"
                                                "AAONgVuLVT9c3NMwySk6OL8zJecTozS3w8sc9YSmn"
                                                "SWtOXmO04eIKzsgvd80rySypFNLjYoOyVLgEpVB1ajBI"
                                                "8XOhCvHsYuLzSE3MKckIrswtKMnPLV7EKpKcX5Sfl1iW"
                                                "WVRarFAMFQYAHgCUcIcAAAA")
                                        if choice in 'nN':
                                            exit()

                                    # Opening the link for further details

                                    if s == 4:
                                        webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/?")

                                    # To book a room in a ward

                                    if s == 5:
                                        id_no = input("Please enter your Patient_id: ")
                                        mycursor.execute(
                                            "Select * from patient_details where patient_id ='{}'".format(id_no))
                                        data = mycursor.fetchall()
                                        if len(data) > 0:
                                            covid_id = input("Please enter your Covid_id: ")
                                            for i in data:
                                                name = i[1]
                                                print("Welcome to covid 19 Ward ", name)
                                            mycursor.execute(
                                                "select covid_id,serial_no, result from results where covid_id='{}'".format(
                                                    covid_id))
                                            data = mycursor.fetchall()
                                            if len(data) > 0:
                                                print(tabulate(data, headers=['COVID ID', 'PATIENT ID', 'RESULT'],
                                                               tablefmt='fancy_grid'))
                                                mycursor.execute(
                                                    "Select * from covid_ward where covid_id = '{}'".format(covid_id))
                                                data_new = mycursor.fetchall()
                                                if len(data_new) == 0:
                                                    for i in data:
                                                        if i[2] == 'POSITIVE':
                                                            print("""
                                                                   You are tested positive for COVID-19
                                                                   """)
                                                            current_result = i[2]
                                                            status = 'IN-WARD'
                                                            mycursor.execute("select * from covid_ward")
                                                            record = mycursor.fetchall()
                                                            if len(record) > 50:
                                                                print("""
                                                                       Sorry, the ward's are fully occupied 
                                                                       Please visit our website for further assistance
                                                                       or contact +4522402062
                                                                       """)
                                                            else:
                                                                mycursor.execute(
                                                                    "insert into covid_ward values('" + str(
                                                                        covid_id) + "','" + id_no + "', '" + name + "', '" + current_result + "', '" + status + "')")
                                                                mysql.commit()
                                                                print("Room booked Successfully")

                                                        if i[2] == 'NEGATIVE':
                                                            status = 'NOT-IN-WARD'
                                                            mycursor.execute("insert into covid_ward values('" + str(
                                                                covid_id) + "','" + id_no + "', '" + name + "', '" + current_result + "', '" + status + "')")
                                                            print("""
                                                                   You are tested NEGATIVE at present
                                                                   Please take care at your home
                                                                   """)
                                                if len(data_new) > 0:
                                                    print("Room already booked with the same Covid ID")

                                            else:
                                                print("Sorry, incorrect serial number")

                                    # Exiting the Covid 19 Ward

                                    if s == 6:
                                        for n in ".....":
                                            sys.stdout.write(n)
                                            sys.stdout.flush()
                                            time.sleep(0.2)
                                        print(n)
                                        op = input("\nAre you sure you want to exit(y/n):")
                                        if op in 'yY':
                                            break

                                    if s not in (1, 2, 3, 4, 5, 6):
                                        print("!!INVALID CHOICE!!")

                                # Exiting the main Menu

                            if o == 5:
                                ch = 'N'
                                while ch in 'Nn':
                                    clrprint("\t\t*****************************************************", clr='y')
                                    clrprint("\t\t    Welcome to Metropolitan hospital Help Desk       ", clr='y')
                                    clrprint("\t\t             Established In 1979                    ", clr='y')
                                    clrprint("\t\t          Your Health Is Our Concern                 ", clr='y')
                                    clrprint("""

                                        1. How to Register?
                                        2. How to book an appointment?
                                        3. How to take a COVID-19 test?
                                        4. How to get your test results?
                                        5. Why does the username you have typed in shows 'Invalid username'?
                                        6. Can I take a COVID-19 Test more than once?
                                        7. How to take a COVID-19 Test if you are a worker at the hospital?
                                        8. Further queries
                                        9. Exit 
                                        """, clr='g')

                                    choice_user = int(clrinput("Enter your choice :"))
                                    if choice_user == 1:
                                        print("""
                                             STEP 1 : Log in using your username and password
                                             STEP 2 : Go into the Adminstration Menu, and provide the necessary information to the admin
                                             STEP 3 : After you have successfully registered , you will be provided with a Patient ID which can be used for further refernces 
                                             """)
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            " STEP 1  Log in using your username and passwordSTEP 2  Go into the Adminstration Menu, and provide the necessary information to the admin STEP 3 : After you have successfully registered , you will be provided with a Patient I:D which can be used for further refernces")
                                        engine.runAndWait()
                                    if choice_user == 2:
                                        print("""
                                             STEP 1 : Log in using your username and password
                                             STEP 2 : Go into the Patient Menu, select appointment Sub Menu and provide the necessary information , Make sure you type in the Patient Id without any errors
                                             STEP 3 : Select a suitable time slot
                                             STEP 4 : Your appointment will be fixed successfully if the time slot is avaiable , else Please select a different time slot """)
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "STEP 1 Log in using your username and password STEP 2 Go into the Patient Menu, select appointment Sub Menu and provide the necessary information, Make sure you type in the Patient I:d without any errors STEP 3 : Select a suitable time slotSTEP 4 : Your appointment will be fixed successfully if the time slot is avaiable , else Please select a different time slot")
                                        engine.runAndWait()

                                    if choice_user == 3:
                                        print("""
                                              STEP 1 : Log in using your username and password
                                              STEP 2 : Go into the Covid - 19 Zone Menu , select covid test sub menu  and provide the informations accurately
                                              STEP 3 : You will be given a Covid ID which must be used for accessing the result once generated""")

                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "STEP 1  Log in using your username and password STEP 2  Go into the Covid  19 Zone Menu  select covid test sub menu  and provide the informations accurately STEP 3 : You will be given a Covid ID which must be used for accessing the result once generated")
                                        engine.runAndWait()

                                    if choice_user == 4:
                                        print("""
                                              STEP 1 : Log in using your username and password
                                              STEP 2 : Go into the Covid - 19 Zone Menu , Select Covid Result Sub Menu 
                                              STEP 3 : Provide the informations correctly , Make sure you type in the Covid ID correctly  """)

                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "STEP 1  Log in using your username and password STEP 2  Go into the Covid  19 Zone Menu  Select Covid Result Sub Menu STEP 3 : Provide the informations correctly , Make sure you type in the Covid ID correctly")
                                        engine.runAndWait()

                                    if choice_user == 5:
                                        print(
                                            "Username you have typed in does not exist or contains an error. Please type it in again carefully")
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "Username you have typed in does not exist or contains an error Please type it in again carefully")
                                        engine.runAndWait()

                                    if choice_user == 6:
                                        print(
                                            " Yes , you can take a covid test more than once , for each new test you will be provided with a new Covid Id ")
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "Yes  you can take a covid test more than once  for each new test you will be provided with a new Covid Id")
                                        engine.runAndWait()

                                    if choice_user == 7:
                                        print("""
                                            STEP 1 : Register yourself as a patient in the adminstration menu
                                            STEP 2 : Go into the Adminstration Menu, and provide the necessary information to the admin
                                            STEP 3 : After you have successfully registered, you will be provided with a Patient ID which can be used for further refernces 
                                             """)
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "STEP1  Register yourself as a patient in the adminstration menu STEP 2  Go into the Adminstration Menu, and provide the necessary information to the admin STEP 3 : After you have successfully registered, you will be provided with a Patient I:D which can be used for further references ")
                                        engine.runAndWait()

                                    if choice_user == 8:
                                        print(
                                            "Please contact our toll free +4522402062 for further queries or you can reach us at helpdesk@metrohospital.com")
                                        engine.setProperty('rate', 165)
                                        engine.say(
                                            "Please contact our toll free +4522402062 for further queries or you can reach us at helpdesk@metrohospital.com")
                                        engine.runAndWait()

                                    if choice_user == 9:
                                        for n in ".....":
                                            sys.stdout.write(n)
                                            sys.stdout.flush()
                                            time.sleep(0.2)
                                        print(n)
                                        ch = input("\nAre you sure you want to exit(y/n):")
                                        if ch in 'yY':
                                            break

                                    if choice_user not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                                        print("INVALID CHOICE !!!!")

                            if o == 6:
                                for n in ".....":
                                    sys.stdout.write(n)
                                    sys.stdout.flush()
                                    time.sleep(0.2)
                                print(n)
                                op = input("\nAre you sure you want to exit ? (y/n):")
                                if op in 'yY':
                                    exit()

                            if o==3:

                                try:

                                    filepath = 'corona 2.txt'
                                    corpus = open(filepath, 'r', errors='ignore')
                                    raw_data = corpus.read()

                                    x = raw_data.lower()

                                    sent_tokens = nltk.sent_tokenize(x)

                                    word_tokens = []
                                    for i in sent_tokens:
                                        word_tokens += (nltk.word_tokenize(i))

                                    lemmer = nltk.stem.WordNetLemmatizer()


                                    def LemTokens(tokens):
                                        return [lemmer.lemmatize(token) for token in tokens]


                                    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


                                    def LemNormalize(text):
                                        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


                                    GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey", "hey there","hi there"]
                                    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello",
                                                          "I am glad! You are talking to me","Hi , Glad to meet you !!"]


                                    def greeting(sentence):
                                        for word in sentence.split():
                                            if word.lower() in GREETING_INPUTS:
                                                return random.choice(GREETING_RESPONSES)


                                    def response(user_response):
                                        robo_response = ''
                                        sent_tokens.append(user_response)
                                        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
                                        tfidf = TfidfVec.fit_transform(sent_tokens)
                                        vals = cosine_similarity(tfidf[-1], tfidf)
                                        idx = vals.argsort()[0][-2]
                                        flat = vals.flatten()
                                        flat.sort()
                                        req_tfidf = flat[-2]

                                        if (req_tfidf == 0):
                                            robo_response = robo_response + "I am sorry !! I don't understand you"
                                            return robo_response
                                        else:
                                            robo_response = robo_response + sent_tokens[idx]
                                            return robo_response


                                    flag = True
                                    print(
                                        "MATRIX: My name is Matrix. I will answer your queries about Covid-19 Virus. If you want to exit, type Bye!")
                                    while (flag == True):
                                        user_response = input()
                                        user_response = user_response.lower()
                                        if (user_response != 'bye'):
                                            if (user_response == 'thanks' or user_response == 'thank you'):
                                                flag = False
                                                print("MATRIX: You are welcome..")

                                            if user_response == 'how are you' or user_response == 'how are you doing':
                                                print('I am great!! How are you?')

                                            if user_response == 'i am fine' or user_response == 'i am great' or user_response == 'fine' or user_response == 'good':
                                                print('Good to hear that')


                                            else :
                                                if (greeting(user_response) != None):
                                                    print("MATRIX: " + greeting(user_response))

                                                else:
                                                    print("MATRIX: ", end="")
                                                    print(response(user_response))
                                                    sent_tokens.remove(user_response)
                                        else:
                                            flag = False
                                            print("MATRIX: Bye! Have a good day ahead ")
                                except:
                                    print('')


                            if o not in (1, 2, 3, 4, 5,6):
                                print("!!INVALID CHOICE!!")



                    else:
                        clrprint("sorry the password is incorrect, try again", clr='r')
                        engine.setProperty('rate', 110)
                        engine.say("Sorry the password is incorrect, try again")
                        engine.runAndWait()
                else:
                    clrprint("sorry the password is incorrect, try again", clr='r')
                    engine.setProperty('rate', 110)
                    engine.say("Sorry the password is incorrect, try again")
                    engine.runAndWait()

# End of Code

