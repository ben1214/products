
import os
products = []

# 讀取檔案
def read_file(filename):
	
	with open(filename, 'r', encoding='big5') as f:
		for line in f:
			if '商品,價格,數量,小計金額' in line:
				continue
			name, price, quality, total = line.strip().split(',')
			products.append([name,price,quality,total])
	return products

# 請使用者輸入
def user_input(products):
	while True:
		name = input('輸入商品名稱:')
		if name == 'q':
			break
		price = input('輸入價格:')
		price = int(price)
		quality = input('輸入數量:')
		quality = int(quality)
		total = price * quality
		products.append([name,price,quality,total])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1],'數量',p[2],'小計金額',p[3])

#寫入檔案
def write_flie(filename,products):
	with open(filename,'w' , encoding='big5') as f:
		f.write('商品,價格,數量,小計金額\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + ',' + str(p[3]) + '\n')
def main():

	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yes')
		products = read_file(filename)
	else:
		print('no')
	products = user_input(products)
	print_products(products)
	write_flie('products.csv', products)
main()


