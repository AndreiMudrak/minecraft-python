import mcpi.minecraft as minecraft

mcraft = minecraft.Minecraft.create()
myCoord = mcraft.player.getTilePos()

mcraft.postToChat ("Hello world!")
mcraft.postToChat ("I'm here: x=" + str(myCoord.x) + " y=" + str(myCoord.y) + " z=" + str(myCoord.z))

print ("My coordinate: x=" + str(myCoord.x) + " y=" + str(myCoord.y) + " z=" + str(myCoord.z))
