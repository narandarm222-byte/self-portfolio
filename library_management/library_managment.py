import json

library = []

try:
	with open("/home/david/json_files/library.json","r") as file:
		library = json.load(file)
except FileNotFoundError:
	print("File not found or never existed")
except json.JSONDecodeError:
	print("The file was broken")

def add_book(library):
	bid = len(library) + 1
	title = input("Enter the title: ")
	author = input("Enter the author name: ")
	try:
		year = int(input("Enter the year: "))
	except ValueError:
		print("Please enter just year by numbers")
		return
	available = True
	borrowed_by = None
	book = {
		"id" : bid,
		"title" : title,
		"author" : author,
		"year" : year,
		"available" : available,
		"borrowed_by" : borrowed_by
	}
	for book in library:
		if title == book["title"] and author == book["author"] and year == book["year"]:
			print("There are already that book")
		else:
			library.append(book)
			print("Book added successfully")
			break
	
def remove_book(library):
	print("Please enter the book id which you wanna delete")
	try:
		rem = int(input("")) 
	except ValueError:
		print("Please enter the id")
		
	for book in library:
		if rem == book["id"]:
			library.remove(book)
			break
		elif book["available"] == False and book["borrowed_by"] != None and rem == book["id"]:
			print("You cant now delete that book")
			break
		else:
			print("There is no such book")
			break
			
def stats(library):
	for book in library:
		print("-" * 121)
		print(book)
		print("-" * 121)
		
def borrow(library):
	book_name = int(input("please enter books id: "))
	for book in library:
		if book_name == book["id"]:
			name = input("please enter your name: ")
			book["borrowed_by"] = name
			book["available"] = False
			print("Have a good time")
			break
		else:
			print("There is no such book")
			break
			
			
def book_return(library):
	book_name = int(input("please enter books id: "))
	for book in library:
		if book["id"] == book_name and book["available"] == False:
			book["borrowed_by"] = None
			book["available"] = True
			print("Thanks for books returning")
			break

def search(library):
	book = input("search: ")
	for item in library:
		if book == item["title"] or book == item["id"]:
			return item
			break
		elif book == item["title"] or book == item["id"] and item["available"] == False:
			print("Sorry but in this moment there is not such book")
	
run = True
while run:
	try:
		act = int(input("""==============================
Choose the action
1. add a book
2. remove a book
3. borrow a book
4. return the book
5. search a book
6. show stats
7. quit
==============================
|"""))
	except ValueError:
		print("Please choose action by the number")
		continue
	
	if act == 1:
		add_book(library)
	elif act == 2:
		remove_book(library)
	elif act == 3:
		borrow(library)
	elif act == 4:
		book_return(library)
	elif act == 5:
		print(search(library))
	elif act == 6:
		stats(library)
	elif act == 7:
		with open("/home/david/json_files/library.json","w") as file:
			json.dump(library,file)
		run = False
	else:
		print("Please choose one of the actions")
