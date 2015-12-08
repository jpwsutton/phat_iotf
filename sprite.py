import scrollphat
import time

face_normal_happy  = ['00001001000',
                      '00001001000',
                      '00000000000',
                      '00010000100',
                      '00001111000']

face_normal_tongue = ['00001001000',
                      '00001001000',
                      '00000000000',
                      '00001111000',
                      '00000011000']

face_normal_wink   = ['00000001000',
                      '00001001000',
                      '00000000000',
                      '00010000100',
                      '00001111000']

face_normal_sad    = ['00001001000',
                      '00001001000',
                      '00000000000',
                      '00001111000',
                      '00010000100']

face_normal_meh    = ['00001001000',
                      '00001001000',
                      '00000000000',
                      '00001111000',
                      '00000000000']

face_normal_shock  = ['00001001000',
                      '00001001000',
                      '00000000000',
                      '00000110000',
                      '00000110000']

face_chibbi_happy  = ['00100001000',
                      '01010010100',
                      '00000000000',
                      '00100001000',
                      '00011110000']

face_chibbi_sad    = ['00100001000',
                      '01010010100',
                      '00000000000',
                      '00011110000',
                      '00100001000']

face_chibbi_shock  = ['01000000100',
                      '00100001000',
                      '01000000100',
                      '00001100000',
                      '00001100000']

face_chibbi_meh    = ['01000000100',
                      '00100001000',
                      '01000000100',
                      '00000000000',
                      '00011110000']

face_chibbi_dead   = ['10100001010',
                      '01000000100',
                      '10100001010',
                      '00000000000',
                      '00011110000']

face_chibbi_ugh    = ['01010010100',
                      '01010010100',
                      '00100001000',
                      '00000000000',
                      '00011110000']

def setCell(row, col, cell):
    if cell == '0':
        scrollphat.set_pixel(col, row, 0)
    else:
        scrollphat.set_pixel(col, row, 1)

# Displays a sprite defined in an array of 5
def displaySprite(sprite):
    for rowNum, row in enumerate(sprite):
        for colNum, cell in enumerate(row):
            setCell(rowNum, colNum, cell)
    scrollphat.update()

faces = [face_chibbi_happy, face_chibbi_sad, face_chibbi_shock, face_chibbi_meh, face_chibbi_dead, face_chibbi_ugh]
scrollphat.clear()
for face in faces:
    displaySprite(face)
    time.sleep(2)

scrollphat.clear()
