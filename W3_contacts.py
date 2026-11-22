contacts=[]
while True:
  print("1.添加联系人")
  print("2.查找全部")
  print("3.退出")
  choice = int(input("选一个:"))
  if choice == "1":
    name = input("请输入要添加的名字:")
    phone = input("请输入添加的对话:")
    contacts.append({"name":name,"phone":phone})
    print("添加成功!")
  elif choice == "2":
    for c in contacts:
      print(c["name"],c["phone"])
  elif choice == "3":
    print("退出")
    break
  else:
    print("输入错误，请重试")


#原理很简单 就是添加字典在列表中 查找时通过字典的键值查找对应的值
