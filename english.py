#usr/bin/python

import os
import datetime 
import time 
import random
import json
import sys 

if sys.platform == 'win32':
	os.system('cls')
else:
	os.system('clear')

os.system('title Real_Estate')
os.system('color 2')

year = datetime.datetime.now().year
s_year = str(year)
f_year = s_year+'.txt'
need = 0

def add(pag:str):
	if not pag.endswith('.txt'):
		pag = pag.strip()
		pag += '.txt'
		return pag
	else:
		return pag

def translate(paragraph:str):
	t = {'ü':'u','ö':'o','ğ':'g','ş':'s','ç':'c','ı':'i','İ':'i'}
	t2 = ''
	for i in paragraph :
		if i in t.keys() :
			t2 += t[i]
		else:
			t2 += i
	return t2

def time_calculater_decarotor(func):
	def wrapper():
		second = time.time()
		func()
		now = time.time()-second 
		print(f"The App Used For {round(now)} seconds")
		time.sleep(3)
	return wrapper

class Real_Estate:
	def __init__ (self):
		pass

	@classmethod
	def how_many_work_to_year(cls ,data:str):	
		data = add(data)
		if os.path.isfile(data) and data in os.listdir(os.curdir) :
			with open(data,mode='r',encoding="utf-8") as f:
				file = f.readlines()
			return len(file)

		else  :
			raise TypeError("\a message from programmer to user :\tsorry but it is not possible entrance")
	def __iter__(self):
		return(self) 

	def __next__(self):
		try:
			self.choise = input('can you confirm file ex:2000.txt\n==>')
			self.choise = add(choise)
			if os.path.isfile(self.choise) and os.path.exists(self.choise):

				with open(self.choise,mode='r',encoding='utf-8') as self.f:
					self.f_r = self.f.readlines()
				for self.i in self.f_r :
					print(self.i)
				print(f"\n\t\tBonus: \nByte of file: {os.stat(self.choise).st_size}\nLast entrance date:{time.asctime(time.localtime(os.stat(self.choise).st_atime))}\nFile born date:{time.asctime(time.localtime(os.stat(self.choise).st_ctime))}\nLast Changing date:{time.asctime(time.localtime(os.stat(self.choise).st_mtime))}\n")
			else:
				print('sorry but that file available.\a')
		except Exception:
			print("you made a fault")
			sleep(4)

	@staticmethod
	def help():
		helpo = """
This is Real-Estate app.This app coded by Mustafa Şahin Karğın.\t\t   The story of this such Mustafa's father is Real-Estate an he difficulting 
Made with Python. And purpose of that app is help for real-estate.\t\tWhile he make work.and Mustafa want help him with hisself programming information


		You can make with this app that you can learn easily how many work did you to years.

		You can make file for old years.

		You can see Real-Estate file line to line.

		You can enter data.

		You can equated to years.

		"""	
		return helpo

	@staticmethod
	def data_write(choise):
		choise = add(choise)
		choise2 = input("Please enter customer name (but it cannot content except alphabet character)\n==>")
		choise2 = choise2.strip()
		choise2 = choise2.lower()
		choise2 = translate(choise2)
		choise_a = input('you should write type of that work ex:( rent ,sale) ex:sale \n==>')
		choise_a = choise_a.strip()
		if choise2.isalpha() and choise_a.isalpha():
			choise2 = choise2.capitalize()
			choise_a = choise_a.lower()
			try:
				choise3 = float(input("Please write how many money you got it\n==>"))
				conform = input('are you sure if you enter false data you cannot adjust it with that program Y/N\n==>')
				conform = conform.strip()
				if conform == 'Y' or conform == 'y':
					if choise == f_year :
						data = {choise2:[datetime.datetime.strftime(datetime.datetime.now(),"%A %d-%B"),choise_a, choise3]}
						time.sleep(3)
					else:
						data = str({choise2:['',choise_a, choise3]})
					veri = json.dumps(data)
					with open(choise,mode="a",encoding="utf-8") as file :
						file.write(veri+'\n')
					print('Data added.\n\n\n')						
				else:
					time.sleep(4)	
					exit()

			except ValueError :
				print('\ayou should enter encounter')
				time.sleep(2)	
		else:
			print(f'\aSorry but it "{choise2}" it cannot content character but alfa')

	@staticmethod
	def manuel_create_year_file(file) :
		file = add(file)
		if file.endswith('.txt'):
			try :
				i_file = int(file[:4])

				if i_file < year and i_file >= 2000:
					if i_file not in os.listdir(os.curdir):
						with open(file,'x+') as f :
							rg = f.read()
							print('created file')
							time.sleep(4)
							exit()
					else:
						print('\athis file already there is')
						time.sleep(4)
						exit()
				else:
					print(f'you can not create file for before 2000 year and {year} and after {year}\a')
					time.sleep(4)
					exit()
			except Exception :
				print(f'\aYou must enter year after from 2000 year and before {year} ex: 2010 and that file shouldnt be before')
				time.sleep(4)
				exit()
		else:
			print("you should write '.txt' ex: 2000.txt")
			time.sleep(4)
			exit()

	@staticmethod
	def Equated(file:str=0,typle:str=0):
		file = add(file)
		Real_Estate.how_many_work_to_year(file)
		file = file 
		file3 = []
		customers = []
		result = []
		with open(file,mode='r',encoding='utf-8') as f :
			file2 = f.readlines()
		for i in file2 :
			if i.isdecimal():
				continue
			else:
				file3.append(eval(i))
		for i in file3 :
			customers.extend(list(i.keys()))
		for k,j in enumerate(file3):
			result.append(float(j[customers[k]][2]))
		print(f'You got {sum(result)} in total this year.')
		print(f"Equated of {file[:4]} is {sum(result)//Real_Estate.how_many_work_to_year(file)}")

@time_calculater_decarotor
def main():

	def Have_to():
		real = Real_Estate()
		iteration = iter(real)
		while True :
			global need
			need += 1
			choise = input('you are in file_read menu at the moment you can enter file ex:2000 and read is or you can quit ex:q or Q\n==>')	
			if choise == 'q' or choise == 'Q':
				exit()		
			else:
				choise = add(choise)
				if need == Real_Estate.how_many_work_to_year(choise)+1 :
					break
				else:
					print(next(iteration))

	print("\tWelcome our app.")

	while True : 

		if "Real_Estate" not in os.listdir(os.curdir):
				os.mkdir('Real_Estate')
				print("Main file created. Return run the program.")
				time.sleep(random.randrange(3,9))
				exit()

		if f_year not in os.listdir('Real_Estate'):
			os.chdir('Real_Estate')
			with open(f_year,mode='w+',encoding="utf-8") as f:
				rg = f.read()
				print("Year file created.return run the program.")
				time.sleep(random.randrange(3,9))
				quit()
		os.chdir('Real_Estate')	
		while True :

			choise = input('Please make your choise \n if you want see how many work did you then click:   "1"\nif you want see Real-Estate file line to line click: "2"\n\t\t\tif you want enter data click:"3"\nif you want create archive own old years then click: "A"\n\t    If you want Equated to years write:"Equated"\n\t\tif you want see help page write:"--help"\n\t\t\tIf you want quit then click: "q"\n==>')

			if choise == '1':
				choise = input('Please enter file which want you see year\n==>')
				choise = add(choise)
				print(f'You done only {Real_Estate.how_many_work_to_year(choise)} work in that year')
				time.sleep(3) 

			elif choise == 'q' or choise == 'Q':
				return True

			elif choise == '--help':
				print(Real_Estate.help())
				time.sleep(10)
				exit()

			elif choise == 'A' or choise == 'a':
				choise = input("please enter date ex:2000\n==>") 
				choise = add(choise) 
				Real_Estate.manuel_create_year_file(choise)

			elif choise == '2':
				Have_to()
				global need
				need=0

			elif choise == '3':
				choise = input('Please enter year file ex: 2000\n==>')
				choise = add(choise)
				Real_Estate.how_many_work_to_year(choise)# I added it because this function already control is it availible so I havent want check myself
				Real_Estate.data_write(choise)

			elif choise.startswith('Equated') or choise.startswith('equated'):
				choise2 = input('Enter Year file ex:2021\n==>')
				choise2 = add(choise2)
				Real_Estate.Equated(choise2)

			else:
				print('\athat is false choise please try again')

if __name__ == '__main__':
	main()