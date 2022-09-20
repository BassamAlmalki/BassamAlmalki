print("""((programmed by bassam almalki‏))
My ig : 5ndh •••••••••••••
[1] binary to decimal
[2] decimal to binary
•••••••••••••
""")
nu = int(input("select number "))

if nu ==1:
	ex = int(input("Enter the number binary : "))
	num=number=0
	while ex !=0:
		number=number+(ex%10)*(2**num)
		ex=ex//10
		num+=1
	print("Result = " , number)

if nu ==2:
	ex = int(input("Enter the number decimal : "))
	num=nur=0
	while ex !=0:
		nur=nur+(ex%2)*(10**num)
		ex=ex//2
		num+=1
	print("result binary number : " , nur)
