try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# vector class from other file, as provided
from Vector import *
import time



CANVAS_HEIGHT = 400
CANVAS_WIDTH = 800


CAT_WALK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/068008ff.16016059-9a27-4c74-a1a2-8dd3b06749c1.png"
CAT_WALK_WIDTH = 128
CAT_WALK_HEIGHT = 128
CAT_WALK_COLUMNS = 4
CAT_WALK_ROWS = 4

CAT_BLINK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/06800915.142a41b4-174c-43d8-8f28-6db9fa15e11d.png"
CAT_SLEEP_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/06800895.04705fb5-eb86-4050-a0d3-3666ce282794.png"

BACKGROUND_LIBINT_URL = "https://i.ibb.co/61mZMKm/library-scene-v2.jpg"
BACKGROUND_LIBEXT_URL = "https://i.ibb.co/XCNP8vT/lib-external.jpg"
BACKGROUND_EXTWALL_URL = "https://i.ibb.co/fY3HL8L/ext-wall.jpg"
BACKGROUND_SUNSET_URL = "https://i.ibb.co/wcTxbVT/extsunset.jpg"

# BACKGROUND_PLAIN_IMG = simplegui.load_image(BACKGROUND_PLAIN_URL)
# overall size of source img
BACKGROUND_PLAIN_IMG_DIMS = (1920, 885)
# center of source img
BACKGROUND_PLAIN_IMG_CENTRE = (960,442)
# destination size, scaling from center
BACKGROUND_PLAIN_img_dest_dim = (CANVAS_WIDTH,CANVAS_HEIGHT)
BACKGROUND_PLAIN_img_rot = 0




CAT_STATUS = "sit" #walk_right, walk_left, sit
ground = 235
terrain_block = False
scene = 1





class catSprite:
    def __init__(self, imgurl, width, height, columns, rows, frame_duration, pos):
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.frame_duration = frame_duration #sprite speed, smaller is faster
        
        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frame_clock = 0

        self.pos = pos
        self.vel = Vector()



        
    def update_index(self): #iterate to next frame, dependant on cat status
        if (CAT_STATUS == "sit"):
            self.img = simplegui.load_image(CAT_BLINK_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            self.frame_index[1] = 0
            self.frame_duration = 18 #blink slower than walk
        else:
            self.img = simplegui.load_image(CAT_WALK_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            if (CAT_STATUS == "walk_right"):
                self.frame_index[1] = 2 #sprite sheet row changes
            if (CAT_STATUS == "walk_left"):
                self.frame_index[1] = 1
            self.frame_duration = 10

        

    def draw(self, canvas):
        global ground, terrain_block, scene
        x1,y1 = self.pos.get_p()
        if (x1 > CANVAS_WIDTH):
            if scene < 4:
                scene += 1
                x1 = 0
        if (x1 < 0):
            if scene > 1:
                scene -= 1
                x1 = CANVAS_WIDTH

        # gravity, if sprite off ground, return to ground at below rate
        if (y1 < ground):
            CAT_FALLING = True
            y1 += 5
        else:
            CAT_FALLING = False
        # specific terrain modifier for Scene 1
        if (scene == 1 ):
            # new ground height allows for the cat to fall to new level with existing gravity
            if (x1 < 350): #ledge down at this coord
                ground = 235
                if (y1 > 238):# if glitched underground (sofa)
                    terrain_block = True
                else:
                    terrain_block = False
            elif ( 450 <= x1 <= 520 ):
                ground = 225
                if (y1 > 225):# if glitched underground (table)
                    terrain_block = True
                else:
                    terrain_block = False
            else:
                ground = 275
                terrain_block = False
        # rebuild pos vector and apply to object
        self.pos = Vector(x1, y1)

        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            self.update_index()
    
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        
        source_size = (self.frame_width, self.frame_height)
        dest_centre = (300, (CANVAS_HEIGHT-self.frame_centre_y-5))
        # cat size
        dest_size = (80, 80)
        canvas.draw_image(self.img, source_centre, source_size, (x1,y1), dest_size)                      

    def on_ground(self):
        x1,y1 = self.pos.get_p()
        # return true if sprite on the ground
        return (y1 >= ground)

    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.down = False
        self.up = False
        self.space = False
        
    def keyDown(self, key):
        global CAT_STATUS
        if key == simplegui.KEY_MAP['right']:
            self.right = True
            CAT_STATUS = "walk_right"
        if key == simplegui.KEY_MAP['left']:
            self.left = True
            CAT_STATUS = "walk_left"
        if key == simplegui.KEY_MAP['down']:
            self.down = True
            CAT_STATUS = "sit"
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
        


class Background:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, canvas):
        x1,y1 = self.pos.get_p()
        # generate img for background of that scene, all same dims
        if scene == 1:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_LIBINT_URL)
        elif scene == 2:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_LIBEXT_URL)
        elif scene == 3:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_EXTWALL_URL)
        elif scene == 4:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_SUNSET_URL)   
        canvas.draw_image(SCENE_BACKGROUND, BACKGROUND_PLAIN_IMG_CENTRE, BACKGROUND_PLAIN_IMG_DIMS, (x1,y1), BACKGROUND_PLAIN_img_dest_dim, BACKGROUND_PLAIN_img_rot)


class Interaction:
    def __init__(self, cat, keyboard, background):
        self.cat = cat
        self.keyboard = keyboard
        self.background = background
    
    def update(self):   
        x1,y1 = self.cat.pos.get_p()
        if self.keyboard.right:
            self.cat.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.cat.vel.add(Vector(-1, 0))
        # space and down key only work if sprite is on ground
        if self.cat.on_ground() == True:
            if self.keyboard.down:
                self.cat.vel.add(Vector(0, 0))
            # jump alternatives, up or space
            if (self.keyboard.space and not terrain_block):
                # single jump only, set size
                self.cat.vel.add(Vector(0, -30))
            if (self.keyboard.up and not terrain_block):
                # single jump only, set size
                self.cat.vel.add(Vector(0, -30))
        if scene == 1 and terrain_block and x1 < 350:
            self.cat.pos = Vector(352, 275) #reset to bottom of sofa



bg = Background(Vector(CANVAS_WIDTH/2,CANVAS_HEIGHT/2))
kbd = Keyboard()
# last param is where cat spawns initially
cat = catSprite(CAT_WALK_URL, CAT_WALK_WIDTH, CAT_WALK_HEIGHT, CAT_WALK_COLUMNS, CAT_WALK_ROWS, 10, Vector(55, 235))
interaction = Interaction(cat, kbd, bg)

def draw(canvas):
    interaction.update()
    bg.draw(canvas)
    cat.update()
    cat.draw(canvas)

frame = simplegui.create_frame("Campus Cat", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_canvas_background("Grey")

frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
