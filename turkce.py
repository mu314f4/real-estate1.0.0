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

os.system('title Emlak Uygulaması')
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
		print(f"Uygulamayı {round(now)} saniye boyunca kullandınız.")
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
			raise TypeError("\a programcıdan kullanıcıya mesaj :\tBu geçerli bir giriş değil.")
	def __iter__(self):
		return(self) 

	def __next__(self):
		try:
			self.choise = input('Yılı doğrularmısınız. ör:2000\n==>')
			self.choise = add(self.choise)
			if os.path.isfile(self.choise) and os.path.exists(self.choise):

				with open(self.choise,mode='r',encoding='utf-8') as self.f:
					self.f_r = self.f.readlines()
				for self.i in self.f_r :
					print(self.i)
				print(f"\n\t\tBonus: \nDosyanın boyutu: {os.stat(self.choise).st_size}\nDosyaya son erişim tarihi:{time.asctime(time.localtime(os.stat(self.choise).st_atime))}\nDosyanın oluşturulma tarihi:{time.asctime(time.localtime(os.stat(self.choise).st_ctime))}\nDosyada son işlemin yapılma tarihi:{time.asctime(time.localtime(os.stat(self.choise).st_mtime))}\n")
			else:
				print('Kusura bakmayın bu dosya geçerli değil.\a')
		except Exception:
			print("Hata yaptınız")
			sleep(4)

	@staticmethod
	def help():
		helpo = """
Bu bir Emlak uygulamasıdır.Bu uygulama Mustafa Şahin Karğın tarafından kodlanmıştır.\t\tBu uygulamanın hikayesi şöyle Mustafanın babası emlakçıydı.Ve o işinde
Python ile kodlanmıştır. Ve amacı emlakçılara yardımdır.\t\tzorlanıyordu.Bunun üzerine Mustafa babasına programlama bilgisiyle yardımcı olmak istedi.


		Seçtiğiniz yıl kaç iş yaptığınızı kolayca öğrenebilirsiniz.

		Geçmiş yıllara ait arşiv oluşturabilirsiniz.

		Seçtiğiniz yıl yaptıklarınızı satırı satırına görüntüleyebilirsiniz.

		Bilgi girebilirsiniz.

		Yıllara göre ortalama alabilirsiniz.

		"""	
		return helpo

	@staticmethod
	def data_write(choise):
		choise = add(choise)
		choise2 = input("Lütfen müşteri adını girin.(Müşteri adı sadece alfabetik karakter içerebilir)\n==>")
		choise2 = choise2.strip()
		choise2 = choise2.lower()
		choise2 = translate(choise2)
		choise_a = input('Lütfen yaptığınız işin türünü girin. ör:(rent ,sale)  \n==>')
		choise_a = choise_a.strip()
		if choise2.isalpha() and choise_a.isalpha():
			choise2 = choise2.capitalize()
			choise_a = choise_a.lower()
			try:
				choise3 = float(input("Lütfen bu işten kaç para kazandığınızı yazın.\n==>"))
				conform = input('İşlemi yapmak istediğinize eminmisiniz çünkü yaptığınız hataları bu uygulama ile düzeltemezsiniz Y/N\n==>')
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
					print('Bilgi Eklendi.\n\n\n')						
				else:
					time.sleep(4)	
					exit()

			except ValueError :
				print('\aBir yerde talimatlara uymadın')
				time.sleep(2)	
		else:
			print(f'\aÜzgünüm ama bu "{choise2}" sadece alfabetik karakter olabilir.')

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
							print('Dosya oluşturuldu.')
							time.sleep(4)
							exit()
					else:
						print('\aBu dosya zaten var.')
						time.sleep(4)
						exit()
				else:
					print(f'{year} yılını 2000 yılından öncesine ait ve {year} yılından öncesine ait dosya oluşturamazsınız.\a')
					time.sleep(4)
					exit()
			except Exception :
				print(f'\a2000 yılı ve yılından sonrası için ve {year} yılndan öncesi için arşiv kaydı oluşturabilirsiniz ör: 2010 ve arşiv tutacağınız yılın önceden olmaması gerek.')
				time.sleep(4)
				exit()
		else:
			print("'.txt' de yazmalısınız örneğin: 2000.txt")
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
		print(f'Bu yıl toplamda {sum(result)} lira kazandınız.')
		print(f"{file[:4]} yılının ortalaması: {sum(result)//Real_Estate.how_many_work_to_year(file)}")

@time_calculater_decarotor
def main():

	def Have_to():
		real = Real_Estate()
		iteration = iter(real)
		while True :
			global need
			need += 1
			choise = input('Şu an okuma menüsündesiniz istediğiniz yıla ait verileri okuyabilirsiniz ör:2000 çıkmak için q ya basvilirsiniz. örneğin:q veya Q\n==>')	
			if choise == 'q' or choise == 'Q':
				exit()		
			else:
				choise = add(choise)
				if need == Real_Estate.how_many_work_to_year(choise)+1 :
					break
				else:
					print(next(iteration))

	print("\tUygulamamıza hoş geldiniz.")

	while True : 

		if "Real_Estate" not in os.listdir(os.curdir):
				os.mkdir('Real_Estate')
				print("Ana klasor oluşturuldu. Programı yeniden çalıştırın.")
				time.sleep(random.randrange(3,9))
				exit()

		if f_year not in os.listdir('Real_Estate'):
			os.chdir('Real_Estate')
			with open(f_year,mode='w+',encoding="utf-8") as f:
				rg = f.read()
				print("Yıl dosyası oluşturuldu file. Programı yeniden çalıştırın.")
				time.sleep(random.randrange(3,9))
				quit()
		os.chdir('Real_Estate')	
		while True :

			choise = input('Lütfen seçimizi yapın.\n   Eğer yılda kaç iş yaptığınızı görmek istiyorsanız:"1" e tıklayın.\n Seçtiğiniz yıl yapmış olduğunuz işleri görmek için :"2"ye tıklayın.\n\t   Eğer veri girişinde bulunmak istiyorsanız:"3" e tıklayın.\nEğer eski yıllara ait arşiv oluşturmak istiyorsanız :"A"ya tıklayın.\n     Eğer yıllara göre ortalama almak istiyorsanız  :"Equated"yazın.\n     Eğer yardım sayfasını görüntülemek istiyorsanız:"--help" yazın.\n\t\t\t    Eğer çıkmak istiyorsanız:"q"ya tıklayın.\n==>')

			if choise == '1':
				choise = input('Hangi yılı görmek istiyorsanız yazın.\n==>')
				choise = add(choise)
				print(f'Bu yıl sadece {Real_Estate.how_many_work_to_year(choise)} iş yaptınız.')
				time.sleep(3) 

			elif choise == 'q' or choise == 'Q':
				return True

			elif choise == '--help':
				print(Real_Estate.help())
				time.sleep(10)
				exit()

			elif choise == 'A' or choise == 'a':
				choise = input("Lütfen tarih girin ör:2000\n==>") 
				choise = add(choise) 
				Real_Estate.manuel_create_year_file(choise)

			elif choise == '2':
				Have_to()
				global need
				need=0

			elif choise == '3':
				choise = input('Lütfen yılı girin. ör: 2000\n==>')
				choise = add(choise)
				Real_Estate.how_many_work_to_year(choise)# I added it because this function already control is it availible so I havent want check myself
				Real_Estate.data_write(choise)

			elif choise.startswith('Equated') or choise.startswith('equated'):
				choise2 = input('Ortalamasını almak istediğiniz yılı girin. ör:2021\n==>')
				choise2 = add(choise2)
				Real_Estate.Equated(choise2)

			else:
				print('\aYanlış seçim lütfen tekrar seçim yapın.')

if __name__ == '__main__':
	main()