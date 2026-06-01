#first os project that you said chat gpt. project of 1st day
import os

files = 0
directories = 0

while True:
		
	try:
		print(f"Your current direcory is {os.getcwd()}")
		path = input("Enter your path | ")
	except OSError as Error:
		print("Your doing something wrong with your input. there isnt any terminal device with that name")
		
	if os.path.exists(path):
		print(os.listdir(path))
		break
	else:
		print("There isnt any path like that")
		
		act = input("Would you like to check again | if YES type y / else type any symbole ")
		if act.lower() == "y":
			continue
		else:
			exit()

for item in os.listdir(path):
	full_path = os.path.join(path,item)
	if os.path.isfile(full_path):
		files += 1
	elif os.path.isdir(full_path):
		directories += 1
	else:
		print("There is something wrong")
			
print("\n" + "="*30)
print(f"Total files: {files}")
print(f"Total directories: {directories}")
print("="*30)
