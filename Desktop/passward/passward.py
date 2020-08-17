x = 0
passward = "jimmylo123"
while x < 3:
	pwd = input("請輸入密碼")
	if pwd == passward:
		print ("登入成功")
		break
	else:
		x = x + 1
		print ("登入失敗 還有", 3 - x ,"次機會")