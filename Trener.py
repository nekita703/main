#Данная программа поможет людям пытающимся изменить вес и привести себя в форму
import pymysql #Базы данных 
import datetime as DT #Для получения текущей даты(дневник веса)

save=3
opcion=10
while opcion != 0:
    print("""
    Личный тренер
    0 - Выйти
    1 - Расчитать количество калорий которое вам необходимо потреблять
    2 - Узнать тип вашего телосложения
    3 - Дневник веса

    """)
    opcion = int(input("Baш выбор: "))
    

    if opcion==1:
        #Эта часть программы расчитывает необходимую суточную норму калорий человека
        #Ввод необходимых данных для формулы
        print("Данная программа позволит посчитать количество калорий которое вам необходимо потреблять, чтобы привести ваш вес на нужную вам отметку \n",
        "Выберите вашу цель: \n",
        "1 - Я хочу похудеть \n",
        "2 - Я хочу потолстеть \n",
        "3 - Я хочу удержать свой вес ")
        objetive= int(input())                #Цель пользователя

        if (save==1) or (save==2):
            gender=save
        else:
            print("\nВведите ваш пол: \n",
            "1 - М\n",
            "2 - Ж")
            gender= int(input())             #Пол пользователя
            save=gender

        print("\nВведите ваш вес: ")
        weight=int(input())             #Вес  

        print("\nВведите ваш рост: ")
        height= int(input())             #Рост 

        print("\nВведите ваш возраст: ")
        age= int(input())               #Возраст

        print("\nВведите уровень вашей активности: ",
        "\n1 - Низкая активность \n",
        "2 - Средняя активность \n",
        "3 - Высокая активность \n",
        "4 - Очень высокая активность\n")
        activity= int(input())

        #Эта часть кода преабразует параметры для правильной работы формулы
        if gender==1:
            gender=5
        else:
            gender=-161

        if activity==1:
            activity=1.2
        elif activity==2:
            activity=1.4
        elif activity==3:
            activity=1.6
        elif activity==4:
            activity=1.8

        if objetive==1:
            objetive=-500
        elif objetive==2:
            objetive=500
        elif objetive==3:
            objetive==0

        #Расчёт дневной нормы калорий по формуле
        dcu=(weight*10+height*6.25-age*5)*activity+objetive
        print("Вам необходимо потреблять: ",dcu," калорий")

    elif opcion==2:
        #Эта часть программы расчитывает тип тела человека
        print("Данная программа позволит узнать тип вашего телосложения \n")
        if (save==1) or (save==2):
            gender=save
        else:
            print("\nВведите ваш пол: \n",
            "1 - М\n",
            "2 - Ж")
            gender= int(input())             #Пол пользователя
            save=gender

        print("Измерьте сантиметром окружность самого тонкого места на запястье: ")
        zap=float(input())                  #Ширина запястья

        if gender==1:
            if (zap<18):
                print("Ваше телосложение: эктоморф, вы склонные к худобе")
            if (zap<=18) and (zap<20):
                print("Ваше телосложение: мезоморф, у вас самое лучий тип телосложения")
            if (zap>=20):
                print("Ваше телосложение: эндоморф, вы склонны к полноте")
    
    elif opcion==3:
        #Эта часть программы выводит последний ваш введёный вес и находится в доработке
        #Позже она будет выводить историю веса пользователя 
        print("Данная часть программы ещё не закончена")
        #print("Введите ваш нынешний вес: ")
        #ves=int(input())
        #date=0
        #now = DT.datetime.utcnow()
        #datetime.date.now(date)
        #db = pymysql.connect("localhost","root","","projpy" )   
        #cursor = db.cursor()
        #sql = "INSERT INTO diary(daytime,result) VALUES ('%s', '%d')" % (now, ves)
        #print(now)


        #try:
        #    cursor.execute(sql)
        #    db.commit()
        #except:
        #    db.rollback()

        #cursor.execute(sql)
        #results = cursor.fetchall()

        #for row in results:
        #    now = row[0]
        #    ves = row[1]
        

        #print ("Ваш вес %s был %d кг" % (now, ves))

        #db.close()
        
  
 
    elif opcion==0:
        print("Досвидания!")
        #print(DT.datetime.utcnow())
    


