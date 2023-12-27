from Operations import Databases



Databases.CreateTable_KlineData('BTCUSDT','1m')



#print(Databases.GetLastTime_PlusOne('BTCUSDT_1m'))
#print(Databases.DeleteLastOne('BTCUSDT_1m'))



# def pause():
#     programPause = input("Press the <ENTER> key to continue...")
    
# pause()

#Databases.get_KlineData_2_MsSql('BTCUSDT','1d',0)