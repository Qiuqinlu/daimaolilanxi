import  random
secret=random.randrange(1,100)
while True:
  guess=int(input("请输入你猜的数:"))
  if guess>secret:
    print(“大了")
  elif guess<secret:
    print("小了")
  else:
    print("猜中了")
    break
