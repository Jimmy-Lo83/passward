x = 3
passward = "jimmylo123"
while x > 0:
	x = x - 1
	pwd = input("請輸入密碼")
	if pwd == passward:
		print ("登入成功")
		break
	else:
		print ("登入失敗")
		if x > 0:
			print (" 還有", x ,"次機會")