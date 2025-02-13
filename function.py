#method overlaoding ,python doesnot support it
#arbitary arguments (*parametername)
#keyword arguments(**parameter name)
def profiledata(**information):
    for key,value in information.items():#.items() it is method used for abstracting values from the ductionary in key-value pair,because the keyword arguments data is stored in dictionary format
        print(key,'=',value)

profiledata(name='mvenkat',batch='30r',password=123456,mail='maddineni@gamil')


