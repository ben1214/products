# 讀取檔案
products = []
with open('products.csv', 'r', encoding='big5') as f:
	for line in f:
		if '商品,價格,數量,小計金額' in line:
			continue
		name, price, quality, total = line.strip().split(',')
		products.append([name,price,quality,total])
print(products)

# 請使用者輸入
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

# 印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1],'數量',p[2],'小計金額',p[3])
#寫入檔案	
with open('products.csv','w' , encoding='big5') as f:
	f.write('商品,價格,數量,小計金額\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')






