#Student Information Management

import time
import os
import getpass
import random
import sqlite3


#SETUP DATABASE
conn = sqlite3.connect('studdb.db')
mycursor = conn.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS students(studName TEXT, studLocation TEXT, studClass INTEGER, studPercentage REAL, randUser TEXT, randPass INTEGER)")
mycursor.execute("SELECT * FROM students");
for row in mycursor:
	print ("studName ", row[0])
	print ("studLocation ", row[1])
	print ("studClass ", row[2])
	print ("studPercentage ", row[3]) 
	print ("randUser ", row[4])
	print ("randPass ", row[5])
	print("")
	

conn.commit()


class Student:

	studName = None
	studLocation = None
	studClass = None
	studPercentage = None

		
	def studRegister(self):
		
		studName = str(input("Enter your name: "))
		studLocation = str(input("Enter your location: "))
		studClass = int(input("Enter your class: "))
		studPercentage = float(input("Enter your percentage: "))
		
		randNum = str(random.randint(1, 9999))
		randUser = studName+randNum
		randPass = random.randint(1, 999999999)
		
		mycursor.execute("INSERT INTO students(studName, studLocation, studClass, studPercentage, randUser, randPass) VALUES(?,?,?,?,?,?)",(studName, studLocation, studClass, studPercentage, randUser, randPass))
		conn.commit()
		

		
	def studLogin(self):
		studUsername = str(input("Enter username:"))
		studPassword = getpass.getpass("Enter password:")
		
		mycursor.execute('SELECT randPass FROM students WHERE randUser = "%s" AND randPass = "%s"' % (studUsername, studPassword))
		if mycursor.fetchone() is not None:
			print("Welcome "+studUsername+"! Select an operation: ")
			print("1. View Details")
			print("2. Update Details")
			print("3. Delete Details Completely")
			
			valOption = int(input())
			
			if valOption == 1:
				mycursor.execute('SELECT studName, studLocation, studClass, studPercentage FROM students WHERE randUser = "%s"' % (studUsername));
				for row in mycursor:
					print("Name: 		", row[0])
					print("Location: 	", row[1])
					print("Class: 		", row[2])
					print("Percentage: 	", row[3]) 
					
			elif valOption == 2:
				mycursor.execute('SELECT studName, studLocation, studClass, studPercentage FROM students WHERE randUser = "%s"' % (studUsername));
				for row in mycursor:
					print("Name: 		", row[0])
					print("Location: 	", row[1])
					print("Class: 		", row[2])
					print("Percentage: 	", row[3])
					
				
				print("1. Location")
				print("2. Class")
				print("3. Percentage")
				updateOption = int(input("Select the data to be updated: "))	
				if updateOption == 1:
					print("Old Location: ", row[1])
					newLocation = str(input("Enter new location: "))
					
					print("Updating Location... Please wait...")
					mycursor.execute('UPDATE students SET studLocation = "%s" WHERE randUser = "%s"' % (newLocation, studUsername))
					conn.commit()
					print("Successfully Updated!")
					mycursor.execute('SELECT studName, studLocation, studClass, studPercentage FROM students WHERE randUser = "%s"' % (studUsername));
					for row in mycursor:
						print("Name: 		", row[0])
						print("Location: 	", row[1])
						print("Class: 		", row[2])
						print("Percentage: 	", row[3])
				
				elif updateOption == 2:
					print("Old Class: ", row[2])
					newClass = str(input("Enter new class: "))
					
					print("Updating class... Please wait...")
					mycursor.execute('UPDATE students SET studClass = "%s" WHERE randUser = "%s"' % (newClass, studUsername))
					conn.commit()
					print("Successfully Updated!")
					mycursor.execute('SELECT studName, studLocation, studClass, studPercentage FROM students WHERE randUser = "%s"' % (studUsername));
					for row in mycursor:
						print("Name: 		", row[0])
						print("Location: 	", row[1])
						print("Class: 		", row[2])
						print("Percentage: 	", row[3])
						
				elif updateOption == 3:
					print("Old Percentage: ", row[3])
					newPercentage = str(input("Enter new percentage: "))
					
					print("Updating percentage... Please wait...")
					mycursor.execute('UPDATE students SET studPercentage = "%s" WHERE randUser = "%s"' % (newPercentage, studUsername))
					conn.commit()
					print("Successfully Updated!")
					mycursor.execute('SELECT studName, studLocation, studClass, studPercentage FROM students WHERE randUser = "%s"' % (studUsername));
					for row in mycursor:
						print("Name: 		", row[0])
						print("Location: 	", row[1])
						print("Class: 		", row[2])
						print("Percentage: 	", row[3])	

				else:
					print("Invalid Input!")
					
			elif valOption == 3:
				print("This will delete all your details permanently!")
				delOption = str(input("Do you want to continue?"))
				
				if delOption == 'Y':
					mycursor.execute('DELETE FROM students WHERE randUser = "%s"' % (studUsername))
					conn.commit()
					print("Successfully Deleted!")
					return
				elif delOption == 'N':
					print("Deletion Cancelled! Please login again!")
					return
					
				else:
					print("Invalid Input! Please login again!")
					return
					
		else:
			print("Login Failed!")
		
		
		
		
		
		
	def studOperation(self):
		print("Select Operation:")
		print("1. Register")
		print("2. Login")
		studChoice = int(input())
		if studChoice == 1:
			s1.studRegister()
		elif studChoice == 2:
			s1.studLogin()
		else:
			print("Invalid Input!")

			
class Admin:
	
	
	def adminOperation(self):
		print("Select Operation:")
		print("1. Login")
		print("2. Add Admin")
		adminChoice = int(input())
		if adminChoice == 1:
			a1.adminLogin()
		elif adminChoice == 2:
			a1.addAdmin()
		else:
			print("Invalid Input!")
	
print("Welcome to Student Info. Management\n")
print("Select your role:")
print("1. Student")
print("2. Admin")

choice = int(input())
if choice == 1:
	os.system('cls')
	s1 = Student()
	s1.studOperation()
	
elif choice == 2:
	os.system('cls')
	a1 = Admin()
	a1.adminOperation()
else:
	print("Invalid Input!")

def adminLogin():
	aUsername = str(input("Enter username:"))
	aPassword = getpass.getpass("Enter password:")



