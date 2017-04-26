from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("Hello world, and welcome to Jackcraft. If can read this say hi.")
#x, y, z = mc.player.getPos()
#mc.player.setPos(x+10, y+10, z+10)
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)
from mcpi import block
mc.setBlock(x+3, y, z, block.STONE.id)
wool = 35
mc.setBlock(x, y, z, wool, 1)
stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

DIAMOND_BLOCK = 57

#while True:
 #   x, y, z = mc.player.getPos()
  #  mc.setBlock(x, y, z, DIAMOND_BLOCK)
   # sleep(0.1)
    #x, y, z = mc.player.getPos()  # player position (x, y, z)
#this_block = mc.getBlock(x, y, z)  # block ID
#print(this_block)
#x, y, z = mc.player.getPos()  # player position (x, y, z)
#block_beneath = mc.getBlock(x, y, z)  # block ID
#print(block_beneath)
#while True:
 #   x, y, z = mc.player.getPos()
  #  block_beneath = mc.getBlock(x, y, z)
  #  print(block_beneath)
   # grass = 2
#DIAMOND_BLOCK = 57


#while True:
#    x, y, z = mc.player.getPos()  # player position (x, y, z)
 #   block_beneath = mc.getBlock(x, y, z)  # block ID

 #   if block_beneath == DIAMOND_BLOCK:
  #      mc.setBlock(x, y, z, DIAMOND_BLOCK)
   # sleep(0.1)
#if block_beneath == DIAMOND_BLOCK:
 #   mc.setBlock(x, y, z, DIAMOND_BLOCK)
#else:
 #   mc.setBlock(x, y-1, z, DIAMOND_BLOCK)
  #  tnt = 46
#mc.setBlock(x, y, z, tnt, 1)
#tnt = 46
#mc.setBlocks(x+1, y+1, z+1, x+1, y+11, z+1, tnt, 1)
#from mcpi.minecraft import Minecraft

#mc = Minecraft.create()

#x, y, z = mc.player.getPos()

#lava = 10

#mc.setBlock(x+3, y+3, z, lava)
#from mcpi.minecraft import Minecraft
#from time import sleep

#mc = Minecraft.create()

#x, y, z = mc.player.getPos()

#lava = 10
#water = 8
#air = 0

#mc.setBlock(x+3, y+3, z, lava)
#sleep(20)
#mc.setBlock(x+3,y+5, z, water)
#sleep(4)
#mc.setBlock(x+3, y+5, z, air)
