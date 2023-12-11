from PIL import ImageGrab, ImageOps, ImageTk
from numpy import array
from time import sleep
from pyautogui import keyDown, keyUp, click
import tkinter as tk
import keyboard


replay_button = [298, 197]
dinosaur = [74, 205]
hitbox_area = [10, 17, 50, 40]
hitbox_distance_x = 27
hitbox_distance_y = 76

def jump():
    keyboard.release('down')
    keyboard.press('space')
    sleep(0.25)
    keyboard.release('space')
    sleep(0.025)
    keyboard.press('down')
    sleep(0.04)
    
    
    
    

def hitbox():
    area = (dinosaur[0] + hitbox_distance_x + hitbox_area[0],
            dinosaur[1] + hitbox_distance_y + hitbox_area[1],
            dinosaur[0] + hitbox_distance_x + hitbox_area[2],
            dinosaur[1] + hitbox_distance_y + hitbox_area[3])

    image = ImageGrab.grab(area)

    #root = tk.Tk()
    #tk_image = ImageTk.PhotoImage(image)
    #label = tk.Label(root, image=tk_image)
    #label.pack()
    #root.mainloop()
    #image.save("output.jpg")
    # Grayscale the image.
    grayscale_image = image.convert("L")
    image_colors = array(grayscale_image.getcolors())
    print(image_colors.sum())
    return image_colors.sum()

def end():
    end = (380, 130, 580, 160)
    image = ImageGrab.grab(end)

    image.save("output.jpg")
    grayscale_image = ImageOps.grayscale(image)
    # Get each pixel color and put it in an array.
    image_colors = array(grayscale_image.getcolors())
    # Return the sum of the array.
    
    return image_colors.sum()

def main():
    click(replay_button)
    while True:
        """
        If the sum of the hitbox array changes, it means one of the pixels
        has changed its color (greyscale in our case), therefore something
        has entered the hitbox.
        """
        
        if(hitbox() != 1167):
            jump() 
            
            
        """
        Same technique is applied to stop the loop. When the game is over,
        a text appears at the top of the game, but that area is empty when
        the game is running. So as soon as the text appears, the loop breaks.
        """
        #if(end() != 6247):
            #break

main()     