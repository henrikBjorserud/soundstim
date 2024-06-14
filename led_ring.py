import board
import neopixel
import time
num_pixels = 12
pixels = neopixel.NeoPixel(board.D12, num_pixels, brightness=0.2)


def full_circle():

    for i in range(3):
        for i in range(num_pixels):
            
            pixels[i] = (200, 0, 0)
            if i <=10:
                pixels[i+1] = (0, 100, 0)
            time.sleep(0.05)
            pixels[i] = (0, 0, 0)
            if i <=10:
                pixels[i+1] = (0, 0, 0)


def start_light():

    for i in range(num_pixels):
        pixels[i] = (0, 180, 180)
        time.sleep(0.5)

    for i in reversed(range(180)):
        pixels.fill((0,i,i))


def blink(times):
    for i in range(times):
        pixels.fill((100, 100, 100))
        time.sleep(0.1)
        pixels.fill((0, 0, 0))
        time.sleep(0.1)


def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 -pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbow(cycles):
    for j in range(cycles):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
            if i <= 10:
                pixels[i+1] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)
        for k in range(num_pixels):
            pixels[k] = (0,0,0)
            pixels.show()
            time.sleep(0.01)

def parts_true(states):
    trues = []
    rainbow(1)
    for key in states:
        if states[key] == True:
            trues.append(key)
            
    if 0 in trues:
        pixels[0] = (50, 0, 50)
        pixels[1] = (0, 50, 0)
    if 3 in trues:
        pixels[2] = (50, 0, 50)
        pixels[3] = (0, 50, 0)
    if 1 in trues:
        pixels[4] = (50, 0, 50)
        pixels[5] = (0, 50, 0)
    if 2 in trues:
        pixels[6] = (50, 0, 50)
        pixels[7] = (0, 50, 0)
    if 4 in trues:
        pixels[8] = (50, 0, 50)
        pixels[9] = (0, 50, 0)
    if 5 in trues:
        pixels[10] = (50, 0, 50)
        pixels[11] = (0, 50, 0)





"""
if __name__=="__main__":
    states = {0:False, 1:True, 2:False, 3:False, 4:True, 5:False}
    parts_true(states)
    blink(5)
    parts_true(states)
"""
