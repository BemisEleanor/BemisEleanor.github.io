import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (229, 249, 148)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (126, 165, 165)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")



class SnowFlake():
#     '''
#     This class will be used to create the SnowFlake Objects.
#     It takes: 
#         size - an integer that tells us how big we want the snowflake
#         position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
#         wind - a boolean that lets us know if there is any wind or not.  
#     '''
        #constructor class
    def __init__(self, size, x_pos, y_pos):
        self.size = size
        self.x_pos = x_pos        
        self.y_pos = y_pos
    
    def fall(self, speed):   
        self.y_pos += speed
        # """
        # Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        # A positive integer will have the snowflake falling down the screen. 
        # A negative integer will have the snowflake falling up the screen. 
        
        # If wind = True
        #     - the x direction of the snowflake changes
        # """
        
    def draw(self):
       pygame.draw.circle(screen, WHITE, (self.x_pos, self.y_pos), self.size, 0)
    

        # """
        # Uses pygame and the global screen variable to draw the snowflake on the screen
        # """
#snows = SnowFlake(5,(250,0), False)
# snowflakes = []
# xpos = [200, 300, 400]
# for i in range(10):
#         snows.append(SnowFlake(xpos[i]))


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 3

#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []

# -------- Main Program Loop -----------




while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREY, (700, 0), 125, 0)
    pygame.draw.circle(screen, GREEN, (0,500), 150, 0)
    pygame.draw.circle(screen, GREEN, (200,500), 150, 0)
    pygame.draw.circle(screen, GREEN, (400,500), 150, 0)
    pygame.draw.circle(screen, GREEN, (600,500), 150, 0)


    # --- Drawing code should go here
    # Begin Snow
    x = random.randint(0, 700)
    y = 0

    snow_list.append(SnowFlake(5, x, y))

    for snowflake in snow_list:
        snowflake.draw()
        snowflake.fall(speed)

    # y += speed




    



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
