from PIL import ImageGrab, ImageOps, ImageTk
from numpy import array
from time import sleep, time
from pyautogui import keyDown, keyUp, click
import tkinter as tk
import keyboard


replay_button = [298, 197]
dinosaur = [74, 205]
hitbox_area = [10, 26, 50, 40]
hitbox_distance_x = 29
hitbox_distance_y = 76

def jump(elapsed_time):
    if elapsed_time >= 45:
        sleep_time_1 = 0.2
        sleep_time_2 = 0.035
        sleep_time_3 = 0.03
    elif elapsed_time >= 90:
        sleep_time_1 = 0.15
        sleep_time_2 = 0.03
        sleep_time_3 = 0.02
    else:
        sleep_time_1 = 0.27
        sleep_time_2 = 0.05
        sleep_time_3 = 0.04
    sleep(0.01)
    keyboard.release('down')
    keyboard.press('space')
    sleep(sleep_time_1)
    keyboard.release('space')
    sleep(sleep_time_2)
    keyboard.press('down')
    sleep(sleep_time_3)

    
    
    

def hitbox(elapsed_time):
    if elapsed_time >= 45:
        hitbox_distance_x = 43
    elif elapsed_time >= 90:
        hitbox_distance_x = 50
    else:
        hitbox_distance_x = 29
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
    #print(image_colors.sum())
    return image_colors.sum()

def end():
    end = (199, 151, 413, 229)
    image = ImageGrab.grab(end)

    image.save("output.jpg")
    grayscale_image = ImageOps.grayscale(image)
    # Get each pixel color and put it in an array.
    image_colors = array(grayscale_image.getcolors())
    # Return the sum of the array.
    
    return image_colors.sum()

def main():
    click(replay_button)
    start = time()
    while True:
        """
        If the sum of the hitbox array changes, it means one of the pixels
        has changed its color (greyscale in our case), therefore something
        has entered the hitbox.
        """
        print(time() - start)
        if(hitbox(elapsed_time = time() - start) != 807):
            jump(elapsed_time = time() - start) 
            
            
        """
        Same technique is applied to stop the loop. When the game is over,
        a text appears at the top of the game, but that area is empty when
        the game is running. So as soon as the text appears, the loop breaks.
        """
        #end()

main()     