import RPi.GPIO as GPIO
import time

import argparse 
import random #grabs random pictures
import os #operating system

import pyglet #interval scheduling


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR


try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            time.sleep(.1)
            #input ON STATUS CODE
            #SLIDE SHOW CODE GOES BELOW THIS LINE VVVVVVVVVV
            
        def update_pan_zoom_speeds():
            global _pan_speed_x 
            global _pan_speed_y 
            #global _zoom_speed
            _pan_speed_x = 8 #random.randint(-8, 8)
            _pan_speed_y = 8 #random.randint(-8, 8)
            #_zoom_speed = random.uniform(-0.05, 0.05)
            return _pan_speed_x, _pan_speed_y #, _zoom_speed


#def update_pan(dt):
    #sprite.x += dt * _pan_speed_x
    #sprite.y += dt * _pan_speed_y


#def update_zoom(dt):
    #sprite.scale += dt * _zoom_speed


        def update_image(dt):
            img = pyglet.image.load(random.choice(image_paths))
            sprite.image = img
            sprite.scale = get_scale(window, img)
            sprite.x = 0
            sprite.y = 0
            #update_pan_zoom_speeds()
            window.clear()


        def get_image_paths(input_dir='.'):
            paths = []
            for root, dirs, files in os.walk(input_dir, topdown=True):
                for file in sorted(files):
                    if file.endswith(('jpg', 'png', 'gif')):
                        path = os.path.abspath(os.path.join(root, file))
                        paths.append(path)
            return paths


        def get_scale(window, image):
            if image.width > image.height:
                scale = float(window.width) / image.width
            else:
                scale = float(window.height) / image.height
            return scale


        window = pyglet.window.Window(fullscreen=False)


        @window.event
        def on_draw():
            sprite.draw()


        if __name__ == '__main__':
            #_pan_speed_x , _pan_speed_y #,_zoom_speed = update_pan_zoom_speeds()

            parser = argparse.ArgumentParser()
            parser.add_argument('dir', help='directory of images',
                                nargs='?', default=os.getcwd())
            args = parser.parse_args()

            image_paths = get_image_paths(args.dir)
            img = pyglet.image.load(random.choice(image_paths))
            sprite = pyglet.sprite.Sprite(img)
            sprite.scale = get_scale(window, img)

            pyglet.clock.schedule_interval(update_image, 5.0)
            #pyglet.clock.schedule_interval(update_pan, 1/60.0)
            #pyglet.clock.schedule_interval(update_zoom, 1/60.0)

            pyglet.app.run()


            
	   #SLIDE SHOW CODE GOES ABOVE THIS LINE ^^^^^^^^^^^^^^

        
        
        	# this print is for testing purposes
        print("Motion Detected...")
        time.sleep(1) #how long you want the slide show to last
           
		#cousins code goes below this lineVVVVVV
    while False:

        print("no motion")
        time.sleep(2)

		#cousins code goes above this line ^^^^^^^^^^^
            
        
        
    #time.sleep(10) #this delay is for the motion sensor it will try to detect this many seconds

except:
    GPIO.cleanup()
