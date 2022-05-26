# My first Python code
# После знака # можно оставлять комментарии или выключать (комментировать) часть кода

# Загрузка библиотеки mcpi для коммуникации с сервером Minecraft
import mcpi.minecraft as minecraft

# Создаем объект, через который будем общаться с Майнкрафтом
# Объект - это несколько переменных в одной
mcraft = minecraft.Minecraft.create()
# Получаем координаты игрока из объекта, созданного выше
myCoord = mcraft.player.getTilePos()

# Печатаем сообщения в чат в игре Майнкрафт
mcraft.postToChat ("Hello world!")
# Из объекта myCoord печатаем координаты игрока в чат
mcraft.postToChat ("I'm here: x=" + str(myCoord.x) + " y=" + str(myCoord.y) + " z=" + str(myCoord.z))

# Печатаем сообщения в терминале
print ("My coordinate in Minecraft: x=" + str(myCoord.x) + " y=" + str(myCoord.y) + " z=" + str(myCoord.z))
