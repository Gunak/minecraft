import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

class Clear(object):
    """Sets all block in each direction except down, for 50 blocks from x,y,z."""

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.clearArea()

    def  clearArea(self):
        mc.setBlocks(self.x-50, self.y, self.z-50, self.x+50, self.y+50, self.z+50, block.AIR.id)


