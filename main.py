import os, time


gList=[]

try:
  f=open("Game.list","a")
  f.write(str(gList))
  f.close()
except:
  print("File Does Not Exist🤔 ")

def add():
  time.sleep(2)
  os.system("clear")
  while True:
    try:
      item=input("Add to inventory>> ").capitalize()
      break
    except:
      item=input("Add another item>> ").capitalize()
  gList.append(item)
  print()
  print("\033[32mItem added to list✨🎉\033[0m")
  time.sleep(1)
  os.system("clear")

def view():
  time.sleep(1)
  os.system("clear")
  for item in gList:
    freq=gList.count(item)
    print(f"You have {freq} {item}s in your game inventory😁😁 ")
    time.sleep(1)
    os.system("clear")
    
def remove():
  time.sleep(1)
  os.system("clear")
  removed=input("\033[31mEnter item to remove>>\033[0m ")
  if removed in gList:
    gList.remove(removed)
    print("\033[35mItem removed from inventory✂️ \033[0m")
  else:
    print("Oopsie! Item not in your inventory😅 ")
  time.sleep(1)
  os.system("clear")
  
while True:
  space=""
  print(f"\033[34m{space:^17}⭐⚡Kiprono Game.co Inventory⚡⭐\033[0m")
  print()
  
  menu=input("1. Add\n2. View\n3. Remove\n>>> ")
  if menu=="1" or menu=="Add":
    add()
  elif menu=="2" or menu=="View":
    view()
    f=open("Game.list","w")
    f.write(str(gList))
    f.close()
  else:
    remove()
    