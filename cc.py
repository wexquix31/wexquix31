from faker import Faker


l = '\033[32m________________\ncc olusturucu \n________________\n________________\nt.me/wexquix / t.me/wexquixpython\n________________\n\n'

print(l)

soru = int(input('Kac tane cece olusturulsun:     '))

f = Faker()


for i in range(soru):
	cece = f.credit_card_full()
	print(f'cc olusturuldu\n{cece}\nt.me/wexquixpython / t.me/wexquix\n\n')


