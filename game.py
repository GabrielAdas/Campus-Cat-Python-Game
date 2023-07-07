try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# vector class from other file, as provided
from Vector import *
import time

# # Code Skulptor Vector
# from user304_rsf8mD0BOQ_1 import Vector


CANVAS_HEIGHT = 400
CANVAS_WIDTH = 800

# CAT SPRITE RESOURCES
WCAT_WALK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/06800a25.efc3013d-35c0-4c3e-b6bb-649222b178c3.png"
WCAT_BLINK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/068008fb.5bab9e70-bc1e-4024-b600-21470b897006.png"
WCAT_SLEEP_URL = "https://i.ibb.co/kgr1h8T/WCSleep.png"
WCAT_YUCK_URL = "https://i.ibb.co/zN0nkGy/WC-yuck-right.png"

CCAT_WALK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/068008ff.16016059-9a27-4c74-a1a2-8dd3b06749c1.png"
CCAT_BLINK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/06800915.142a41b4-174c-43d8-8f28-6db9fa15e11d.png"
CCAT_SLEEP_URL = "https://i.ibb.co/2dbDyvW/CCSleep.png"
CCAT_YUCK_URL = "https://i.ibb.co/M255PFv/CC-yuck-right.png"

GCAT_WALK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/0680088d.a34807b8-a686-4035-80a0-372cfba46e8e.png"
GCAT_BLINK_URL = "https://assetstorev1-prd-cdn.unity3d.com/preview/06800866.44c5cd21-cd91-41a0-80e3-c9e657ce3d9a.png"
GCAT_SLEEP_URL = "https://i.ibb.co/h1nfR5r/GCSleep.png"
GCAT_YUCK_URL = "https://i.ibb.co/GJSK9Tm/GC-yuck-right.png"

# default to white cat
CAT_BLINK_URL = WCAT_BLINK_URL
CAT_SLEEP_URL = WCAT_SLEEP_URL
CAT_YUCK_URL = WCAT_YUCK_URL
CAT_WALK_URL = WCAT_WALK_URL

CAT_WALK_WIDTH = 128
CAT_WALK_HEIGHT = 128
CAT_WALK_COLUMNS = 4
CAT_WALK_ROWS = 4

HEART_ICON_URL = "https://i.ibb.co/LPbdDQg/My-project-1.png"
HEART_ICON_WIDTH = 50
HEART_ICON_HEIGHT = 50

# BACKGROUND RESOURCES
BACKGROUND_START_URL = "https://i.ibb.co/xgGc4cb/startq.jpg"
BACKGROUND_SELECT_URL = "https://i.ibb.co/Zh3JPrG/selectcat.jpg"
BACKGROUND_LIBINT_URL = "https://i.ibb.co/61pndWr/intlib.jpg"
BACKGROUND_LIBEXT_URL = "https://i.ibb.co/QpkP4Br/extlib-hole.jpg"
BACKGROUND_EXTWALL_URL = "https://i.ibb.co/k23fLvs/extwall.jpg"
BACKGROUND_EXTJUMP_URL = "https://i.ibb.co/30C1cnt/extjump.jpg"
BACKGROUND_GAZEBO_URL = "https://i.ibb.co/27Lkn7t/extgaz.jpg"
BACKGROUND_BED_URL = "https://i.ibb.co/njQwVGN/intbed-hole.jpg"


# MENU RESOURCES
BACKGROUND_HOWTOPLAY_URL = "https://i.ibb.co/RgyZ8NN/howtoplay-back.jpg"
BACKGROUND_FAIL_LIBINT_URL = "https://i.ibb.co/2PkBxQj/GO-intlib.jpg"
BACKGROUND_FAIL_LIBEXT_URL = "https://i.ibb.co/N7ycYd4/GO-extlib.jpg"
BACKGROUND_FAIL_EXTWALL_URL = "https://i.ibb.co/VTqWVqB/GO-extwall.jpg"
BACKGROUND_FAIL_EXTWALLJUMP_URL = "https://i.ibb.co/hX13g52/GOextjump.jpg"
BACKGROUND_FAIL_GAZEBO_URL = "https://i.ibb.co/8jdysJ2/GO-extgaz.jpg"
BACKGROUND_FAIL_BED_URL = "https://i.ibb.co/TcG8nQJ/GO-intbed.jpg"
BACKGROUND_PASS_URL = "https://i.ibb.co/BNj1mL4/complete-empty.jpg"
BACKGROUND_CLEAR_LIBEXT_URL = "https://i.ibb.co/SnCQ3CT/levelclear-libext.jpg"
BACKGROUND_CLEAR_EXTWALL_URL = "https://i.ibb.co/t4G3Mcn/Clear-EXTjump.jpg"


# overall size of source img
BACKGROUND_IMG_DIMS = (900, 415)
# center of source img
BACKGROUND_IMG_CENTRE = (450, 207.5)
# destination size, scaling from center
BACKGROUND_img_dest_dim = (CANVAS_WIDTH, CANVAS_HEIGHT)
BACKGROUND_img_rot = 0

# TREAT RESOURCES
BLUE_TREAT_URL = "https://i.ibb.co/Yc6tCqn/bluefish.png"
GOLD_TREAT_URL = "https://i.ibb.co/tKcJn6j/goldfish.png"
TREAT_HEIGHT = 384
TREAT_WIDTH = 384

# SPARKLE RESOURCES
SPARKLE_URL = "https://i.ibb.co/4NF6qPw/output-onlinepngtools.png"
SPARKLE_WIDTH = 128
SPARKLE_HEIGHT = 128

# CLOCK RESOURCES
CLOCK_URL = "https://i.ibb.co/BfZstVM/clock.png"
CLOCK_WIDTH = 384
CLOCK_HEIGHT = 384

# Enemy Resources
ENEMY_URL = "https://i.ibb.co/nRcYWYL/image1.png"
ENEMY_WIDTH = 138
ENEMY_HEIGHT = 128

# Enemy Smoke Resources
ENEMY_SMOKE_URL = "https://i.ibb.co/DDwcXgM/smoke-explode.png"
SMOKE_HEIGHT = 32
SMOKE_WIDTH = 160

# Score number resources
NUMBERS_URL = "https://i.ibb.co/xDK5k0v/clean-numbers.png"
NUMBERS_WIDTH = 318
NUMBERS_HEIGHT = 32

# end Score board resources
ENDSCORE_DISPLAY_URL = 'https://i.ibb.co/xzSsRvs/Score.png'
ENDSCORE_DISPLAY_WIDTH = 1280
ENDSCORE_DISPLAY_HEIGHT = 720

# Level complete score resources
LEVELSCORE_DISPLAY_URL = 'https://i.ibb.co/MSgDm1q/Levelcomplete.png'
LEVELSCORE_DISPLAY_WIDTH = 640
LEVELSCORE_DISPLAY_HEIGHT = 360

# bottom bar resources
BOTTOM_BAR_URL = 'https://i.ibb.co/TM4h9Fn/bottombarscore.jpg'
BOTTOM_BAR_WIDTH = 900
BOTTOM_BAR_HEIGHT = 31

# BUTTON PARAMS (corners of square)
# START
BUTTON_S0START_P1 = (225, 210)  # TL
BUTTON_S0START_P2 = (355, 210)  # TR
BUTTON_S0START_P3 = (225, 270)  # BL
BUTTON_S0START_P4 = (355, 270)  # BR
# EXIT
BUTTON_S0EXIT_P1 = (425, 210)  # TL
BUTTON_S0EXIT_P2 = (555, 210)  # TR
BUTTON_S0EXIT_P3 = (425, 270)  # BL
BUTTON_S0EXIT_P4 = (555, 270)  # BR
# Q BUTTON
BUTTON_S0Q_P1 = (760, 360)  # TL
BUTTON_S0Q_P2 = (795, 360)  # TR
BUTTON_S0Q_P3 = (760, 395)  # BL
BUTTON_S0Q_P4 = (795, 395)  # BR
# S0.2 PLAY button
BUTTON_S02PLAY_P1 = (640, 360)  # TL
BUTTON_S02PLAY_P2 = (760, 360)  # TR
BUTTON_S02PLAY_P3 = (640, 390)  # BL
BUTTON_S02PLAY_P4 = (760, 390)  # BR
# S0.2 BACK button
BUTTON_S02BACK_P1 = (46, 360)  # TL
BUTTON_S02BACK_P2 = (160, 360)  # TR
BUTTON_S02BACK_P3 = (46, 390)  # BL
BUTTON_S02BACK_P4 = (160, 390)  # BR
# all scene exit / quit
BUTTON_PLAYEXIT_P1 = (720, 370)  # TL
BUTTON_PLAYEXIT_P2 = (800, 370)  # TR
BUTTON_PLAYEXIT_P3 = (720, 400)  # BL
BUTTON_PLAYEXIT_P4 = (800, 400)  # BR
# replay button
BUTTON_REPLAY_P1 = (55, 310)  # TL
BUTTON_REPLAY_P2 = (265, 310)  # TR
BUTTON_REPLAY_P3 = (55, 350)  # BL
BUTTON_REPLAY_P4 = (265, 350)  # BR
# menu exit button
BUTTON_MENUEXIT_P1 = (630, 310)  # TL
BUTTON_MENUEXIT_P2 = (750, 310)  # TR
BUTTON_MENUEXIT_P3 = (630, 350)  # BL
BUTTON_MENUEXIT_P4 = (750, 350)  # BR
# menu exit button
BUTTON_SCORES_P1 = (290, 310)  # TL
BUTTON_SCORES_P2 = (580, 310)  # TR
BUTTON_SCORES_P3 = (290, 350)  # BL
BUTTON_SCORES_P4 = (580, 350)  # BR

# SELECT WHITE CAT
BUTTON_WCAT_P1 = (280, 210)  # TL
BUTTON_WCAT_P2 = (340, 210)  # TR
BUTTON_WCAT_P3 = (280, 300)  # BL
BUTTON_WCAT_P4 = (340, 300)  # BR
# SELECT CALICO CAT
BUTTON_CCAT_P1 = (360, 210)  # TL
BUTTON_CCAT_P2 = (430, 210)  # TR
BUTTON_CCAT_P3 = (360, 300)  # BL
BUTTON_CCAT_P4 = (430, 300)  # BR
# SELECT GREY CAT
BUTTON_GCAT_P1 = (460, 210)  # TL
BUTTON_GCAT_P2 = (520, 210)  # TR
BUTTON_GCAT_P3 = (460, 300)  # BL
BUTTON_GCAT_P4 = (520, 300)  # BR


# IMPORTANT GAME STATUS CHANGES
CAT_STATUS = "sit"  # walk_right, walk_left, sit, sleep, yuck
CAT_SELECT = "calico"  # grey, white
game_start = False
game_complete = False
ground = 235
terrain_block = False
scene = 0
btreat_count = 0
gtreat_count = 0


class Player:
    def __init__(self, imgurl, width, height, columns, rows, frame_duration, pos, lives):
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.frame_duration = frame_duration  # sprite speed, smaller is faster

        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frame_clock = 0

        self.pos = pos
        self.vel = Vector()

        self.lives = lives

    def lose_life(self):
        self.lives -= 1

    def update_index(self):  # iterate to next frame, dependant on cat status
        if (CAT_SELECT == "white"):
            CAT_BLINK_URL = WCAT_BLINK_URL
            CAT_SLEEP_URL = WCAT_SLEEP_URL
            CAT_YUCK_URL = WCAT_YUCK_URL
            CAT_WALK_URL = WCAT_WALK_URL

        elif (CAT_SELECT == "calico"):
            CAT_BLINK_URL = CCAT_BLINK_URL
            CAT_SLEEP_URL = CCAT_SLEEP_URL
            CAT_YUCK_URL = CCAT_YUCK_URL
            CAT_WALK_URL = CCAT_WALK_URL

        elif (CAT_SELECT == "grey"):
            CAT_BLINK_URL = GCAT_BLINK_URL
            CAT_SLEEP_URL = GCAT_SLEEP_URL
            CAT_YUCK_URL = GCAT_YUCK_URL
            CAT_WALK_URL = GCAT_WALK_URL

        if (CAT_STATUS == "sit"):
            self.img = simplegui.load_image(CAT_BLINK_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            self.frame_index[1] = 0
            self.frame_duration = 18  # blink slower than walk
        elif (CAT_STATUS == "sleep"):
            self.img = simplegui.load_image(CAT_SLEEP_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            self.frame_index[1] = 0
            self.frame_duration = 25  # sleep slower than blink
        elif (CAT_STATUS == "yuck"):
            self.img = simplegui.load_image(CAT_YUCK_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            self.frame_index[1] = 0
            self.frame_duration = 18
        else:
            self.img = simplegui.load_image(CAT_WALK_URL)
            self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
            if (CAT_STATUS == "walk_right"):
                self.frame_index[1] = 2  # sprite sheet row changes
            if (CAT_STATUS == "walk_left"):
                self.frame_index[1] = 1
            self.frame_duration = 10

    def draw(self, canvas):
        global ground, terrain_block, scene
        x1, y1 = self.pos.get_p()

        # Canvas wraps left and right h
        if (x1 > CANVAS_WIDTH):
            # midlevels to next scene
            if scene == 1 or scene == 3 or scene == 5:
                scene += 1
                x1 = 0
            # end levels to level clear
            elif scene == 2 or scene == 4:
                scene += 120
                x1 = 0
            elif scene == 6:
                x1 = CANVAS_WIDTH  # canvas wrap rhs of level 6

        if (x1 < 0):
            if scene == 2 or scene == 4 or scene == 6:
                scene -= 1
                x1 = CANVAS_WIDTH
            elif scene == 1 or scene == 3 or scene == 5:
                x1 = 0  # canvas wrap lhs where levels already cleared

        # gravity, if sprite off ground, return to ground at below rate
        if (y1 < ground):
            CAT_FALLING = True
            y1 += 5
        else:
            CAT_FALLING = False
        # specific terrain modifier for each scene
        if (scene == 1):
            # new ground height allows for the cat to fall to new level with existing gravity
            if (x1 < 350):  # ledge down at this coord
                ground = 235
                # if glitched underground (sofa)
                terrain_block = (y1 > (ground + 10))
            elif (440 <= x1 <= 540):  # table
                ground = 225
                # if glitched underground (table)
                terrain_block = (y1 > (ground + 10))
            else:
                ground = 275
                terrain_block = False
        if (scene == 2):
            if (0 < x1 < 160):  # if glitched in left ledge
                ground = 275
                terrain_block = (y1 > (ground + 10))
            elif (160 < x1 < 315):  # fall in hole
                ground = 490
                # if fallen in hole
                terrain_block = (y1 > (ground - 130))
            elif (x1 < 315):  # if glitched in right ledge
                ground = 275
                terrain_block = (y1 > (ground + 10))
            else:
                ground = 275
                terrain_block = False
        if (scene == 3):
            if (280 < x1 < 380):  # step1 low
                ground = 240
                # if glitched underground (step1)
                terrain_block = (y1 > (ground + 10))
            elif (380 < x1 < 630):  # step2 mid
                ground = 210
                # if glitched underground (step2)
                terrain_block = (y1 > (ground + 10))
            elif (630 < x1 < 800):  # step3 high
                ground = 156
                # if glitched underground (step3)
                terrain_block = (y1 > (ground + 10))
            else:
                ground = 275
                terrain_block = False
        if (scene == 4):
            if (0 < x1 < 160):  # if glitched in left ledge
                ground = 156
                terrain_block = (y1 > (ground + 10))
            elif (160 < x1 < 250):  # first gap
                ground = 490
                # if fallen in hole
                terrain_block = (y1 > (ground - 130))
            elif (250 < x1 < 350):  # first island
                ground = 190
                # if fallen in hole
                terrain_block = (y1 > (ground + 10))
            elif (350 < x1 < 430):  # second gap
                ground = 490
                # if fallen in hole
                terrain_block = (y1 > (ground - 130))
            elif (430 < x1 < 545):  # second island
                ground = 135
                # if fallen in hole
                terrain_block = (y1 > (ground + 10))
            elif (545 < x1 < 630):  # third gap
                ground = 490
                # if fallen in hole
                terrain_block = (y1 > (ground - 130))
            elif (x1 < 630):  # if glitched in right ledge
                ground = 156
                terrain_block = (y1 > (ground + 10))
            else:
                ground = 156
                terrain_block = False
        if (scene == 5):
            if (x1 < 125):
                ground = 156
                # if glitched underground (step)
                terrain_block = (y1 > (ground + 10))
            elif (125 < x1 < 180):  # step2
                ground = 210
                # if glitched underground (step)
                terrain_block = (y1 > (ground + 10))
            elif (180 < x1 < 230):  # step3
                ground = 240
                # if glitched underground (step)
                terrain_block = (y1 > (ground + 10))
            elif (501 < x1 < 600):  # bench
                ground = 240
                # if glitched underground (planter)
                terrain_block = (y1 > (ground + 10))
            else:
                ground = 275
                terrain_block = False
        if (scene == 6):
            if (0 < x1 < 120):  # if glitched in left ledge
                ground = 275
                terrain_block = (y1 > (ground + 10))
            elif (120 < x1 < 270):  # fall in hole
                ground = 490
                # if fallen in hole
                terrain_block = (y1 > (ground - 60))
            elif (270 < x1 < 670):  # if glitched in right ledge
                ground = 275
                terrain_block = (y1 > (ground + 10))
            elif (x1 > 670):
                ground = 220
                # if glitched underground (sofa)
                terrain_block = (y1 > (ground + 10))
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
        if ((0.5 < scene < 100) or scene == 110):
            canvas.draw_image(self.img, source_centre,
                              source_size, (x1, y1), dest_size)
        if (0.5 < scene < 100):
            # heart and lives display
            heart_icon = simplegui.load_image(HEART_ICON_URL)

            for i in range(self.lives):
                canvas.draw_image(heart_icon,
                                  (HEART_ICON_WIDTH/2, HEART_ICON_HEIGHT/2),
                                  (HEART_ICON_WIDTH, HEART_ICON_HEIGHT),
                                  ((640 + 50*i) + HEART_ICON_WIDTH /
                                      2, HEART_ICON_HEIGHT / 2),
                                  (HEART_ICON_WIDTH, HEART_ICON_HEIGHT))

    def on_ground(self):
        x1, y1 = self.pos.get_p()
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

    def keyDown(self, key):
        global CAT_STATUS
        if key == simplegui.KEY_MAP['right']:
            self.right = True
            if (game_complete != True):  # stop updating after game end
                CAT_STATUS = "walk_right"
        if key == simplegui.KEY_MAP['left']:
            self.left = True
            if (game_complete != True):
                CAT_STATUS = "walk_left"
        if key == simplegui.KEY_MAP['down']:
            self.down = True
            if (game_complete != True):
                CAT_STATUS = "sit"
        if key == simplegui.KEY_MAP['up']:
            self.up = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False


class Background:
    def __init__(self, pos):
        self.pos = pos

    def draw(self, canvas):
        x1, y1 = self.pos.get_p()
        # generate img for background of that scene, all same dims
        if scene == 0:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_START_URL)
        elif scene == 0.2:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_HOWTOPLAY_URL)
        elif scene == 0.5:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_SELECT_URL)
        elif scene == 1:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_LIBINT_URL)
        elif scene == 2:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_LIBEXT_URL)
        elif scene == 3:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_EXTWALL_URL)
        elif scene == 4:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_EXTJUMP_URL)
        elif scene == 5:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_GAZEBO_URL)
        elif scene == 6:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_BED_URL)
        # fail scenes, note: these are +100 from played scenes
        elif scene == 101:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_FAIL_LIBINT_URL)
        elif scene == 102:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_FAIL_LIBEXT_URL)
        elif scene == 103:
            SCENE_BACKGROUND = simplegui.load_image(
                BACKGROUND_FAIL_EXTWALL_URL)
        elif scene == 104:
            SCENE_BACKGROUND = simplegui.load_image(
                BACKGROUND_FAIL_EXTWALLJUMP_URL)
        elif scene == 105:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_FAIL_GAZEBO_URL)
        elif scene == 106:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_FAIL_BED_URL)
        # complete scenes
        elif scene == 110:
            SCENE_BACKGROUND = simplegui.load_image(BACKGROUND_PASS_URL)
        # clear scenes, note: these are +120 from played scenes
        elif scene == 122:
            SCENE_BACKGROUND = simplegui.load_image(
                BACKGROUND_CLEAR_LIBEXT_URL)
        elif scene == 124:
            SCENE_BACKGROUND = simplegui.load_image(
                BACKGROUND_CLEAR_EXTWALL_URL)

        canvas.draw_image(SCENE_BACKGROUND, BACKGROUND_IMG_CENTRE, BACKGROUND_IMG_DIMS,
                          (x1, y1), BACKGROUND_img_dest_dim, BACKGROUND_img_rot)


class Treat:
    def __init__(self, position, type, scene):
        # for the treat sprite
        self.pos = position
        self.move_up = True
        self.timer = 0
        x, y = self.pos.get_p()
        self.scene = scene
        self.type = type

        # hitbox
        self.left_border = x-40
        self.right_border = x+40
        self.top_border = y-30
        self.bottom_border = y+30
        self.hit = False

        # loading different treat images
        if self.type == 'blue':
            self.img = simplegui.load_image(BLUE_TREAT_URL)
        elif self.type == 'gold':
            self.img = simplegui.load_image(GOLD_TREAT_URL)

        # for sparkle sprite
        self.sparkle_img = simplegui.load_image(SPARKLE_URL)
        self.sprk_width = SPARKLE_WIDTH
        self.sprk_height = SPARKLE_HEIGHT
        self.sprk_columns = 4
        self.sprk_rows = 4
        # how many draw()s it should stay before it changes to the next frame
        self.sprk_frame_duration = 1
        self.num_frames = 16  # how many frames are used in the sheet

        self.dest_centre = self.pos.get_p()
        self.frame_width = SPARKLE_WIDTH / self.sprk_columns
        self.frame_height = SPARKLE_HEIGHT / self.sprk_rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frames_used = 0  # counter for how many frames have passed so far

    def draw(self, canvas):
        # calculating image values for treat
        dest_size = (52, 52)
        source_centre = (TREAT_WIDTH/2, TREAT_HEIGHT/2)
        source_size = (TREAT_WIDTH, TREAT_HEIGHT)

        # display treat while it has not been hit
        if self.hit == False:
            if scene == self.scene:
                canvas.draw_image(self.img, source_centre,
                                  source_size, self.pos.get_p(), dest_size)
        # once hit display sparkle animation
        else:
            if scene == self.scene:
                if self.timer % self.sprk_frame_duration == 0:
                    if self.frames_used != self.num_frames:  # stops when all frames are used
                        self.next_frame()
                        source_centre = (  # centre position of current frame
                            self.frame_width * \
                            self.frame_index[0] + self.frame_centre_x,
                            self.frame_height * \
                            self.frame_index[1] + self.frame_centre_y
                        )

                        source_size = (self.frame_width, self.frame_height)
                        dest_size = (80, 80)
                        canvas.draw_image(self.sparkle_img,
                                          source_centre,
                                          source_size,
                                          self.dest_centre,
                                          dest_size)

    def update(self):
        # moving treat's position up and down every 60 frames
        if self.timer % 60 == 0:
            self.move_up = not self.move_up
        if self.move_up == True:
            self.pos.add(Vector(0, 0.1))
        else:
            self.pos.add(Vector(0, -0.1))

        # updating hitbox with the new position
        self.x, self.y = self.pos.get_p()

        # frame timer
        self.timer += 1

    # collision with the cat
    def got_hit(self, position):  # takes the cat's position
        global btreat_count, gtreat_count
        x, y = position

        # if the cat is within the hitbox set hit to true and up the treat count
        if x > self.left_border and x < self.right_border and y > self.top_border and y < self.bottom_border:
            self.hit = True
            if self.type == 'blue':
                btreat_count += 1
            if self.type == 'gold':
                gtreat_count += 1

    # changes position of frame index to the next frame for the sparkle animation
    def next_frame(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.sprk_columns
        # if it does go back to zero it then increases the row number so we go down to the next row
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.sprk_rows
        self.frames_used += 1

    # when the game resets
    def reset(self):
        self.hit = False
        self.frames_used = 0


class Enemy:  # Class responsible for positioning and functionaility of enemy objects
    def __init__(self, position, type, scene, movement):
        self.pos = position
        self.move_up = True
        self.move_left = True
        self.move_right = True
        self.move_down = True
        self.move_middle = True
        self.timer = 0
        x, y = self.pos.get_p()
        self.scene = scene
        self.movement = movement

        # Hitbox Settings
        self.left_border = x - 20
        self.right_border = x + 20
        self.top_border = y - 30
        self.bottom_border = y + 35
        self.hit = False

        if type == 'cucumber':
            self.img = simplegui.load_image(ENEMY_URL)

        # Smoke Sprite Formatting:
        self.smke_width = SMOKE_WIDTH
        self.smke_height = SMOKE_HEIGHT
        self.smke_columns = 7
        self.smke_rows = 1
        self.smke_frame_duration = 4  # Number of draw()s to be called until it changes frame
        self.num_frames = 7  # Number of frames used in spritesheet

        self.dest_centre = self.pos.get_p()
        # Calculates the size of each frame
        self.frame_width = SMOKE_WIDTH / self.smke_columns
        self.frame_height = SMOKE_HEIGHT / self.smke_rows

        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]
        self.frames_used = 0  # Counts how many frames have been used so far

    def draw(self, canvas):
        global scene, CAT_STATUS
        dest_size = (36, 36)
        source_centre = (ENEMY_WIDTH/2, ENEMY_HEIGHT/2)
        source_size = (ENEMY_WIDTH, ENEMY_HEIGHT)
        smoke_img = simplegui.load_image(ENEMY_SMOKE_URL)

        # Checks if the object has been hit or not
        if self.hit == False:
            # If the object is in same scene as the player, it will draw the object's image on the canvas
            if scene == self.scene:
                canvas.draw_image(self.img, source_centre,
                                  source_size, self.pos.get_p(), dest_size)

        else:
            # Checks if the object is in the same scene as the player
            if scene == self.scene:
                # Checks if the timer is a multiple of the smoke frame duration
                if self.timer % self.smke_frame_duration == 0:
                    # If not all the frames of the smoke animation have been used, it'll go to next frame
                    if self.frames_used != self.num_frames:
                        self.next_frame()
                        # Determination of the centre of current frame
                        source_centre = (
                            self.frame_width *
                            self.frame_index[0] + self.frame_centre_x,
                            self.frame_height *
                            self.frame_index[1] + self.frame_centre_y
                        )

                        CAT_STATUS = "yuck"

                        source_size = (self.frame_width, self.frame_height)
                        dest_size = (80, 80)

                        canvas.draw_image(
                            smoke_img,
                            source_centre,
                            source_size,
                            self.dest_centre,
                            dest_size
                        )

    def update(self):
        # Checks if the time is on 60 seconds
        if self.timer % 60 == 0:
            # If it is, flips the value of the 'move_up' attribute
            self.move_up = not self.move_up
            self.move_right = not self.move_right
            self.move_down = not self.move_down

        if self.timer % 100 == 0:
            self.move_middle = not self.move_middle

        if self.movement == "down":
            # Depending on the value of 'move_up', adjusts the 'pos' attribute using a Vector object
            if self.move_down == True:
                self.pos.add(Vector(0, 1.3))
                x, y = self.pos.get_p()
                self.top_border = y - 20
                self.bottom_border = y + 20
                self.dest_centre = self.pos.get_p()

            else:
                x, y = self.pos.get_p()
                self.pos.add(Vector(0, -1.3))
                self.top_border = y - 20
                self.bottom_border = y + 20
                self.dest_centre = self.pos.get_p()

        if self.movement == "right":
            if self.move_right == True:
                self.pos.add(Vector(1, 0))
                x, y = self.pos.get_p()
                self.left_border = x - 20
                self.right_border = x + 20
                self.dest_centre = self.pos.get_p()
            else:
                self.pos.add(Vector(-1, 0))
                x, y = self.pos.get_p()
                self.left_border = x - 20
                self.right_border = x + 20
                self.dest_centre = self.pos.get_p()
        if self.movement == "middle":
            if self.move_middle == True:
                self.pos.add(Vector(2, 0))
                x, y = self.pos.get_p()
                self.left_border = x - 20
                self.right_border = x + 20
                self.dest_centre = self.pos.get_p()
            else:
                self.pos.add(Vector(-2, 0))
                x, y = self.pos.get_p()
                self.left_border = x - 20
                self.right_border = x + 20
                self.dest_centre = self.pos.get_p()

        # Increments the 'timer' attribute by 1 on every iteration
        self.timer += 1

    def got_hit(self, position):
        # States '' as global to modify the variable

        # Unpacks the position tuple into 'x' and 'y' variables
        x, y = self.pos.get_p()
        # Checks if 'x' and 'y' coordinates are within the boundaries of the current object
        if x > self.left_border and x < self.right_border and y > self.top_border and y < self.bottom_border:
            # Sets the 'hit' attribute of the objects to be True if it's been hit
            self.hit = True

    def got_hit_cucumber(self, position):
        # Unpacks the position tuple into 'x' and 'y' variables
        x, y = position
        # Checks if 'x' and 'y' coordinates are within the boundaries of the current object
        if (x > self.left_border and x < self.right_border and y > self.top_border and y < self.bottom_border):
            # Sets the 'hit' attribute of the objects to be True if it's been hit
            self.hit = True
            cat.lose_life()

    # The next_frame function does the following:
    # Changes position of the frame index to the next frame
    # Each time frame_index[0] (column counter) gets added to but when it reaches
    # the end it returns to the start because the modulus function is 0
    def next_frame(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.smke_columns
        # If it does go back to zero, it goes to the next row
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.smke_rows
        self.frames_used += 1

    def reset(self):
        self.hit = False
        self.frames_used = 0


class Mouse:
    def __init__(self):
        self.pos = Vector(0, 0)

    def click_handler(self, position):
        x, y = position
        pos = Vector(x, y)
        self.pos = pos

    def click_pos(self):
        return self.pos

    def within(self, pt1, pt2, pt3, pt4):
        # is click within square button?
        xc, yc = mouse.click_pos().get_p()
        x1, y1 = pt1
        x2, y2 = pt2
        x3, y3 = pt3
        x4, y4 = pt4
        return ((x1 < xc < x2) and (y1 < yc < y4))

    def reset(self):
        self.pos = Vector(0, 0)


class Clock:
    def __init__(self):
        self.frame_time = 0  # frame counter
        self.seconds = 0
        self.minutes = 0
        self.timer_start = False  # for stopping and starting the game timer
        self.img = simplegui.load_image(CLOCK_URL)  # clock image
        self.source_centre = (CLOCK_WIDTH/2, CLOCK_HEIGHT/2)

    def tick(self):
        # frame counter
        self.frame_time += 1

        # seconds increase every 60 frames
        if self.frame_time % 60 == 0:
            self.seconds += 1

        # minutes increase every 60 seconds and then resets the seconds
        if self.seconds % 60 == 0 and self.seconds != 0:
            self.seconds = 0
            self.minutes += 1

    # timer only goes up during the game scenes
    def update(self):
        if (1 <= scene <= 6):
            self.tick()
            self.timer_start == True
        else:
            self.timer_start == False

    # when the game is reset
    def reset(self):
        self.seconds = 0
        self.minutes = 0

    # drawn on game screens, level complete screens and game over screens
    def draw(self, canvas):
        # game screens
        if (1 <= scene <= 6):
            canvas.draw_image(self.img,
                              self.source_centre,
                              (CLOCK_WIDTH, CLOCK_HEIGHT),
                              (54, 30),
                              (120, 120))
            canvas.draw_text(
                (str(self.minutes) + ":" + str(self.seconds)), (52, 34), 17, 'black', "monospace")

        # level complete screens
        if (scene == 122 or scene == 124):
            canvas.draw_image(self.img,
                              self.source_centre,
                              (CLOCK_WIDTH, CLOCK_HEIGHT),
                              (480, 275),
                              (132, 130))
            canvas.draw_text((str(self.minutes) + ":" + str(self.seconds)), (475, 281),
                             18, 'black', "monospace")


class Number:  # To display specific number
    def __init__(self, number):
        self.number = number

        # numbers 0-9 sprite sheet
        self.img = simplegui.load_image(NUMBERS_URL)
        self.width = NUMBERS_WIDTH
        self.height = NUMBERS_HEIGHT
        self.columns = 10
        self.rows = 1

        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

        self.frame_index = [0, 0]

    def update(self, number):  # for if the number is changing live
        self.number = number

    def draw(self, canvas, pos, size):
        # setting frame index to correct frame to display chosen number
        self.frame_index = [0, 0]
        self.frame_index[0] = self.frame_index[0] + self.number

        source_centre = (  # centre position of current number on the sprite sheet
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        # size of number frame on sprite sheet
        source_size = (self.frame_width, self.frame_height)

        # draw number with given position and size
        canvas.draw_image(self.img,
                          source_centre,
                          source_size,
                          pos,
                          size)


class Score:
    def __init__(self):
        # for base of end scoreboard
        self.endScore_board_img = simplegui.load_image(ENDSCORE_DISPLAY_URL)
        self.endScoreboard_source_centre = (
            ENDSCORE_DISPLAY_WIDTH/2, ENDSCORE_DISPLAY_HEIGHT/2)
        self.endScoreboard_source_size = (
            ENDSCORE_DISPLAY_WIDTH, ENDSCORE_DISPLAY_HEIGHT)

        # for base of level complete scoreboard
        self.levelScore_board_img = simplegui.load_image(
            LEVELSCORE_DISPLAY_URL)
        self.levelScoreboard_source_centre = (
            LEVELSCORE_DISPLAY_WIDTH/2, LEVELSCORE_DISPLAY_HEIGHT/2)
        self.levelScoreboard_source_size = (
            LEVELSCORE_DISPLAY_WIDTH, LEVELSCORE_DISPLAY_HEIGHT)

        # for treat count display on scoreboards
        self.btreat_count = Number(btreat_count)
        self.gtreat_count = Number(gtreat_count)

        # bottom bar for live score
        self.bottom_bar_img = simplegui.load_image(BOTTOM_BAR_URL)
        self.bottombar_source_centre = (
            BOTTOM_BAR_WIDTH/2, BOTTOM_BAR_HEIGHT/2)
        self.bottombar_source_size = (BOTTOM_BAR_WIDTH, BOTTOM_BAR_HEIGHT)

        # treat counts for live score display
        self.live_btreat_count = Number(btreat_count)
        self.live_gtreat_count = Number(gtreat_count)

        # final scores
        # lists because the numbers will be split up to display as seperate Number()s
        self.time_bonus = []
        self.final_score = []
        self.total_treat_score = []

    def draw_end_scoreboard(self, canvas):

        # turning timebonus list into a list of corresponding Number()s
        timeBonus_numbers = []
        for number in self.time_bonus:
            timeBonus_numbers.append(Number(number))

        # turning finalscore list into a list of corresponding Number()s
        finalScore_numbers = []
        for number in self.final_score:
            finalScore_numbers.append(Number(int(number)))

        # where the numbers will be placed
        timebonus_positions = [(547, 197), (578, 197), (609, 197)]
        finalscore_positions = [(549, 270), (584, 270), (619, 270), (654, 270)]

        # when game complete screen appears or game over screens appear
        if (110 <= scene <= 112 or 101 <= scene <= 106):
            # drawing base scoreboard
            canvas.draw_image(self.endScore_board_img, self.endScoreboard_source_centre, (ENDSCORE_DISPLAY_WIDTH, ENDSCORE_DISPLAY_HEIGHT),
                              (350, 210),  # dest pos
                              (550, 315))  # dest size

            # drawing blue treat count
            self.btreat_count.update(btreat_count)
            self.btreat_count.draw(canvas, (640, 91), (30, 35))

            # drawing gold treat count
            self.gtreat_count.update(gtreat_count)
            self.gtreat_count.draw(canvas, (640, 140), (30, 35))

            # calculate the scores and draw them
            self.calculate_scores()
            # looping through each number and position
            for i in range(len(timeBonus_numbers)):
                timeBonus_numbers[i].draw(
                    canvas, timebonus_positions[i], (35, 40))

            for i in range(len(finalScore_numbers)):
                finalScore_numbers[i].draw(
                    canvas, finalscore_positions[i], (40, 45))

    def draw_level_scoreboard(self, canvas):

        # when level complete screens appear
        if (scene == 122 or scene == 124):
            # drawing base scoreboard
            canvas.draw_image(self.levelScore_board_img, self.levelScoreboard_source_centre, (LEVELSCORE_DISPLAY_WIDTH, LEVELSCORE_DISPLAY_HEIGHT),
                              (300, 190),  # dest pos
                              (479, 270))  # dest size

            # drawing blue treat count
            self.btreat_count.update(btreat_count)
            self.btreat_count.draw(canvas, (175, 199), (30, 35))

            # drawing gold treat count
            self.gtreat_count.update(gtreat_count)
            self.gtreat_count.draw(canvas, (175, 234), (30, 35))

            # time elapsed is drawn in clock class

    def draw_livescore(self, canvas):

        # turning treat score list into a list of corresponding Number()s
        score_numbers = []
        for number in self.total_treat_score:
            score_numbers.append(Number(int(number)))

        # 4 positions next to eachother for the numbers to be displayed
        scoreNumber_positions = [
            (387, 388), (405, 388), (424, 388), (443, 388)]

        if (0.5 < scene < 7):  # during the game scenes
            canvas.draw_image(self.bottom_bar_img, self.bottombar_source_centre, (BOTTOM_BAR_WIDTH, BOTTOM_BAR_HEIGHT),
                              (400, 386),  # dest pos
                              (800, 28))  # dest size
            # blue treat count
            self.btreat_count.update(btreat_count)
            self.btreat_count.draw(canvas, (80, 388), (20, 25))

            # drawing gold treat countS
            self.gtreat_count.update(gtreat_count)
            self.gtreat_count.draw(canvas, (192, 388), (20, 25))

            # calculate scores then display treat score ojn bottom bar
            self.calculate_scores()
            for i in range(len(score_numbers)):
                score_numbers[i].draw(
                    canvas, scoreNumber_positions[i], (20, 25))

    # reset all scores when game resets
    def reset(self):
        global gtreat_count, btreat_count
        gtreat_count = 0
        btreat_count = 0

    def calculate_scores(self):
        # calculates the time taken using the minutes and seconds from clock
        time_taken = (clock.minutes * 60) + clock.seconds

        # time bonuses depending on the time taken. over 55 seconds taken means no time bonus
        # if time bonus is being displayed on a game over screen it should be 0
        if time_taken <= 25:
            timebonus = 500
            self.time_bonus = [5, 0, 0]
        elif 25 < time_taken <= 35:
            timebonus = 400
            self.time_bonus = [4, 0, 0]
        elif 35 < time_taken < 45:
            timebonus = 300
            self.time_bonus = [3, 0, 0]
        elif 45 < time_taken < 55:
            timebonus = 200
            self.time_bonus = [2, 0, 0]
        else:
            timebonus = 0
            self.time_bonus = [0]

        # if we are on a game over screen the timebonus should show as zero
        if 101 <= scene <= 106:
            self.time_bonus = [0]

        # calculating final score with treats and time bonus.
        # Blue treats are worth 100 points and gold treats are worth 300 points
        blue_treats_score = btreat_count * 100
        gold_treats_score = gtreat_count * 300
        total_treat_score = str(blue_treats_score + gold_treats_score)
        score = str(blue_treats_score + gold_treats_score + timebonus)

        # splitting the numbers up to display with the number class
        self.final_score = [char for char in score]
        self.total_treat_score = [char for char in total_treat_score]


class Interaction:
    def __init__(self, cat, keyboard, background, treats, mouse, clock, enemies):
        self.cat = cat
        self.keyboard = keyboard
        self.background = background
        self.treats = treats
        self.mouse = mouse
        self.clock = clock
        self.enemies = enemies

    def update(self):
        global game_complete, CAT_STATUS, scene, game_start, CAT_SELECT

        x1, y1 = self.cat.pos.get_p()
        if (0.5 < scene < 7) and (game_complete != True):
            if self.keyboard.right:
                self.cat.vel.add(Vector(1, 0))
            if self.keyboard.left:
                self.cat.vel.add(Vector(-1, 0))
            # space and down key only work if sprite is on ground
            if self.cat.on_ground() == True:
                if self.keyboard.down:
                    self.cat.vel.add(Vector(0, 0))
                if (self.keyboard.up and not terrain_block):
                    # single jump only, set size
                    self.cat.vel.add(Vector(0, -30))

        # Terrain clash/position modifiers
        # SCENE 1
        if scene == 1 and terrain_block and x1 < 350:
            self.cat.pos = Vector(353, 275)  # reset to bottom of sofa
        # SCENE 2
        if scene == 2 and terrain_block:
            # reset to top of ledge if fell in hole
            self.cat.pos = Vector(140, 249)
            cat.lives -= 1
            CAT_STATUS = "sit"
        # SCENE 3
        if scene == 3 and terrain_block and 280 < x1 < 380:
            self.cat.pos = Vector(277, 275)  # reset to bottom of first step
        elif scene == 3 and terrain_block and 381 < x1 < 630:
            self.cat.pos = Vector(378, 239)  # reset to bottom of second step
        elif scene == 3 and terrain_block and 630 < x1 < 800:
            self.cat.pos = Vector(628, 209)  # reset to bottom of third step
        # SCENE 4
        if scene == 4 and terrain_block:
            # reset to top of ledge if fell in hole
            self.cat.pos = Vector(150, 155)
            cat.lives -= 1
            CAT_STATUS = "sit"
        # SCENE 5
        if scene == 5 and terrain_block and x1 < 125:
            self.cat.pos = Vector(128, 209)  # reset to lhs of second step
        elif scene == 5 and terrain_block and 125 < x1 < 180:
            self.cat.pos = Vector(183, 239)  # reset to lhs of third step
        elif scene == 5 and terrain_block and 180 < x1 < 230:
            self.cat.pos = Vector(233, 274)  # reset to lhs of ground
        # SCENE 6
        if scene == 6 and terrain_block and x1 < 270:
            # reset to top of ledge if fell in hole
            self.cat.pos = Vector(100, 274)
            CAT_STATUS = "sit"
            cat.lives -= 1
        if scene == 6 and terrain_block and 290 < x1 < 650:
            # reset to top of ledge if underground
            self.cat.pos = Vector(100, 274)
            CAT_STATUS = "sit"
        if scene == 6 and terrain_block and x1 > 660:
            self.cat.pos = Vector(655, 275)  # reset to bottom of sofa

        # GAME COMPLETE? (cat in bed)
        if scene == 6 and x1 > 700 and y1 > 220:
            self.cat.pos = Vector(735, 225)  # cat automatic to bed
            CAT_STATUS = "sleep"
            game_complete = True

        for entity in (treats):
            if scene == entity.scene and not entity.hit:
                entity.got_hit(self.cat.pos.get_p())

        for entity in (enemies):
            if scene == entity.scene and not entity.hit:
                entity.got_hit_cucumber(self.cat.pos.get_p())

        # Button click
        # S0 start button
        if mouse.within(BUTTON_S0START_P1, BUTTON_S0START_P2, BUTTON_S0START_P3, BUTTON_S0START_P4):
            if scene == 0:
                scene = 0.2
                mouse.reset()

        # close game s0
        elif mouse.within(BUTTON_S0EXIT_P1, BUTTON_S0EXIT_P2, BUTTON_S0EXIT_P3, BUTTON_S0EXIT_P4):
            if scene == 0:
                exit()
        # S0 ? help button
        if mouse.within(BUTTON_S0Q_P1, BUTTON_S0Q_P2, BUTTON_S0Q_P3, BUTTON_S0Q_P4):
            if scene == 0:
                scene = 0.2
                mouse.reset()

        # S0.2 start button
        if mouse.within(BUTTON_S02PLAY_P1, BUTTON_S02PLAY_P2, BUTTON_S02PLAY_P3, BUTTON_S02PLAY_P4):
            if scene == 0.2:
                scene = 0.5
                CAT_STATUS = "sit"
                mouse.reset()

        # S0.2 back button
        if mouse.within(BUTTON_S02BACK_P1, BUTTON_S02BACK_P2, BUTTON_S02BACK_P3, BUTTON_S02BACK_P4):
            if scene == 0.2:
                scene = 0
                mouse.reset()

        # quit playing game
        if mouse.within(BUTTON_PLAYEXIT_P1, BUTTON_PLAYEXIT_P2, BUTTON_PLAYEXIT_P3, BUTTON_PLAYEXIT_P4):
            if (scene == 0.5):
                scene = 0
            elif (0.5 < scene < 7):  # if exit during level or before full game end, then fail
                game_start = False  # end the timer
                CAT_STATUS = "sit"
                scene += 100
            mouse.reset()

        # Replay
        if mouse.within(BUTTON_REPLAY_P1, BUTTON_REPLAY_P2, BUTTON_REPLAY_P3, BUTTON_REPLAY_P4):
            if (100 < scene < 120):
                scene = 0.5
                game_complete = False
                CAT_STATUS = "sit"
                cat.lives = 3
                for treat in treats:
                    treat.reset()
                for enemy in enemies:
                    enemy.reset()
                score.reset()
                mouse.reset()
                clock.reset()

        # Next button/continue game
        if mouse.within(BUTTON_REPLAY_P1, BUTTON_REPLAY_P2, BUTTON_REPLAY_P3, BUTTON_REPLAY_P4):
            if (scene == 122):
                scene = 3
                CAT_STATUS = "sit"
                mouse.reset()
            if (scene == 124):
                scene = 5
                CAT_STATUS = "sit"
                mouse.reset()

        # menu exit game
        if mouse.within(BUTTON_MENUEXIT_P1, BUTTON_MENUEXIT_P2, BUTTON_MENUEXIT_P3, BUTTON_MENUEXIT_P4):
            if (100 < scene < 120):
                exit()
                mouse.reset()
            if (scene == 122):  # if exit before full game end, then fail
                game_start = False  # end the timer
                CAT_STATUS = "sit"
                scene = 102
                mouse.reset()
            if (scene == 124):  # if exit before full game end, then fail
                game_start = False  # end the timer
                CAT_STATUS = "sit"
                scene = 104
                mouse.reset()

        # select white cat
        if mouse.within(BUTTON_WCAT_P1, BUTTON_WCAT_P2, BUTTON_WCAT_P3, BUTTON_WCAT_P4):
            if scene == 0.5:
                CAT_STATUS = "sit"
                CAT_SELECT = "white"
                game_complete = False
                scene = 1
                self.cat.pos = Vector(55, 235)  # ensure cat at start location
                game_start = True
                mouse.reset()

        # select calico cat
        elif mouse.within(BUTTON_CCAT_P1, BUTTON_CCAT_P2, BUTTON_CCAT_P3, BUTTON_CCAT_P4):
            if scene == 0.5:
                CAT_STATUS = "sit"
                CAT_SELECT = "calico"
                game_complete = False
                scene = 1
                self.cat.pos = Vector(55, 235)
                game_start = True
                mouse.reset()

        # select grey cat
        elif mouse.within(BUTTON_GCAT_P1, BUTTON_GCAT_P2, BUTTON_GCAT_P3, BUTTON_GCAT_P4):
            if scene == 0.5:
                CAT_STATUS = "sit"
                CAT_SELECT = "grey"
                game_complete = False
                scene = 1
                self.cat.pos = Vector(55, 235)
                game_start = True
                mouse.reset()

        # complete screen
        if (cat.lives == 0 and scene == 1):
            scene = 101
        if (cat.lives == 0 and scene == 2):
            scene = 102
        if (cat.lives == 0 and scene == 3):
            scene = 103
        if (cat.lives == 0 and scene == 4):
            scene = 104
        if (cat.lives == 0 and scene == 5):
            scene = 105
        if (cat.lives == 0 and scene == 6):
            scene = 106

        if (scene == 6 and game_complete == True):
            scene = 110
            self.cat.pos = Vector(735, 225)


bg = Background(Vector(CANVAS_WIDTH/2, CANVAS_HEIGHT/2))
kbd = Keyboard()
mouse = Mouse()
clock = Clock()
score = Score()
# last param is where cat spawns initially
cat = Player(CAT_WALK_URL, CAT_WALK_WIDTH, CAT_WALK_HEIGHT,
             CAT_WALK_COLUMNS, CAT_WALK_ROWS, 10, Vector(55, 235), 3)

treats = [Treat(Vector(248, 130), 'blue', 1),
          Treat(Vector(480, 190), 'blue', 1),
          Treat(Vector(434, 240), 'blue', 2),
          Treat(Vector(719, 60), 'blue', 3),
          Treat(Vector(345, 225), 'blue', 3),
          Treat(Vector(409, 238), 'gold', 4),
          Treat(Vector(300, 180), 'blue', 4),
          Treat(Vector(545, 238), 'gold', 5),
          Treat(Vector(275, 150), 'blue', 5),
          Treat(Vector(132, 149), 'blue', 6),
          Treat(Vector(355, 156), 'blue', 6)]

enemies = [Enemy(Vector(527, 192), 'cucumber', 1,  "right"),
           Enemy(Vector(228, 348), 'cucumber', 2, "static"),
           Enemy(Vector(725, 150), 'cucumber', 2, "static"),
           Enemy(Vector(610, 212), 'cucumber', 3, "middle"),
           Enemy(Vector(205, 275), 'cucumber', 3,   "down"),
           Enemy(Vector(487, 232), 'cucumber', 5, "static"),
           Enemy(Vector(487, 202), 'cucumber', 5, "static"),
           Enemy(Vector(487, 172), 'cucumber', 5, "static"),
           Enemy(Vector(487, 142), 'cucumber', 5, "static")]

interaction = Interaction(cat, kbd, bg, treats, mouse, clock, enemies)


def draw(canvas):
    interaction.update()
    bg.draw(canvas)
    cat.update()
    cat.draw(canvas)
    clock.update()
    clock.draw(canvas)
    score.draw_end_scoreboard(canvas)
    score.draw_level_scoreboard(canvas)
    score.draw_livescore(canvas)

    forGeneration = treats + enemies
    for object in forGeneration:
        object.update()
        object.draw(canvas)


frame = simplegui.create_frame("Campus Cat", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_canvas_background("Grey")

frame.set_mouseclick_handler(mouse.click_handler)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
# game_timer.start()
frame.start()
