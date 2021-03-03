def print_menu():       

    print ("1. Что собрать на пуджа")
    print ("2. Самая мужская песня")
    print ("3. Стоит ли жить в Беларуси")
    print ("4. Жесть(")
    print ("5. Exit")


loop =True

while loop:        
    print_menu()    
    choice = input("Enter your choice [1-5]: ")

    if choice=="1":
        print ("Мом + рапира + бф норм")
        
    elif choice=="2":
        print ("Валим гачи ремикс")
       
    elif choice=="3":
        print ("не")
        
    elif choice=="4":
        print ("ряльна")
  
    elif choice=="5":
        print ("Menu 5 has been selected")
      
        loop=False 
    else:
       
        print("Wrong option selection. Enter any key to try again..")