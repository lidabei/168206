flag=0;
for thief in range(ord('A'),ord('D')+1):
	print("假设",chr(thief),"偷了钻石，那么")
	if thief!=ord('A'):
		print("A说了真话")
	else:
		print("A说了假话")
	if thief!=ord('D'):
		print("B说了真话")
	else:
		print("B说了假话")
	if thief!=ord('B'):
		print("C说了真话")
	else:	
		print("C说了假话")
	if thief!=ord('D'):
		print("D说了真话")
	else:	
		print("D说了假话")
	result=(thief!=ord('A'))+(thief!=ord('D'))+(thief!=ord('B'))+(thief!=ord('D'))
	print(result,"人说了真话")
	if result==1:
		print("偷走钻石的人：",chr(thief)\n)
		flag=1
	else:
		print("假设不成立\n")
	if(flag==0):
		print("谁都不是小偷")