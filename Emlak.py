#usr/bin/python

import os
import time

def language():
	m = 5
	print('İf you can understand english better than turkish then choise  english.')
	time.sleep(1)
	print('Eğer türkçeyi ingilizceden daha  iyi anlıyorsan türkçe yi  seç.')
	time.sleep(1)
	print('İf you choise turkish then you cannot adjust with that program.')
	time.sleep(1)
	print('Eğer ingilizceyi seçersen bu uygulamadan daha türkçe seçemezsin')
	time.sleep(1)
	print("for english click: e or E")
	time.sleep(1)
	print("Türkçe  için: T   veya  t")
	while m==5:
		choise = input('==>')
		choise = choise.strip()
		if choise.isalpha():
			choise = choise.lower()
			if choise == 'e':
				os.system('python english.py')
				m = 6
			elif choise == 't':
				os.system('python turkce.py')
				m = 6
			else:
				print('\aYou can not such choise.')
				time.sleep(1)
				print('Böyle bir işlem yapamazsın')
		else:
			print('That is not true choise.')
			time.sleep(1)
			print('Bu doğru bir seçim değil')
			time.sleep(1)
	else:
		quit()
		
language()