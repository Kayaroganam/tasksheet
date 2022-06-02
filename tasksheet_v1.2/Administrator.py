import os

def help():
	print("-----------------------------------")
	print("| h. help                         |")
	print("| 0. exit                         |")
	print("| 1. runserver                    | ")
	print("| 2. create new task sheet        |")
	print("| 3. create superuser             |")
	print("| 4. install (For the first time) |")
	print("-----------------------------------")

def main():

	help()
	flag = True
	while flag:
		select = input("select >> ")

		if select =='1':
			os.system("gnome-terminal -e \"python3 manage.py runserver\"")
			
		if select =='2':
			os.system("bash createuser.sh ")

		if select =='3':
			os.system("python3 manage.py createsuperuser")

		if select =='4':
			os.system("sudo apt update -y")
			os.system("sudo apt upgrade -y")
			os.system("sudo apt install python3 python3-pip python3-django libmysqlclient-dev default-libmysqlclient-dev ")
			os.system("pip3 install Django")
			os.system("pip3 install wheel")
			os.system("pip3 install mysqlclient")
			os.system("python3 manage.py makemigrations")
			os.system("python3 manage.py migrate")


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