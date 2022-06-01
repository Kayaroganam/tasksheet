import os

def help():
	print("0. exit")
	print("h. help")
	print("1. runserver")
	print("2. create new task sheet")

def main():

	flag = True
	while flag:
		select = input("select >> ")

		if select =='1':
			os.system("gnome-terminal -e \"python3 manage.py runserver\"")
			
		if select =='2':
			os.system("bash createuser.sh ")

		if select =='0':
			flag = False
			print("Bye")

		if select == 'h':
			help()

		if select =='clear':
			os.system("clear")

		else:
			pass


if __name__ == '__main__':
	main()