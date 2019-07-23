# import
from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 1800, 900)
window.set_font_color('white')
window.set_font_name('comicsansms')
window.set_bg_color('black')
window.set_font_size(20)

# initialize variables
y_axis = 0
string_height = window.get_font_height()

# display remaining attempts
window.draw_string('1 ATTEMPT LEFT', 0, 0)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

# display password list (similar to above, copy/paste for each password)
window.draw_string('PASSWORDS AVAILABLE: ', 0, y_axis)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

window.draw_string('qXLoPz109', 0, y_axis)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

window.draw_string('TNQmAAiA', 0, y_axis)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

window.draw_string('soAOQLAl11', 0, y_axis)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

window.draw_string('461564', 0, y_axis)
window.update()
sleep(0.5)
y_axis = y_axis + string_height

# prompt user for password
guess = window.input_string('ENTER A PASSWORD > ', 0, y_axis)

# clear window
window.clear()

# create outcome
if guess == "soAOQLAl11":
    window.draw_string("<PASSWORD SUCCESSFULLY ENTERED>", 0, 0)
    window.update()
else:
    window.set_font_color("red")
    window.draw_string("<INCORRECT PASSWORD - - - SECURITY BREACH - - - THE FBI ARE ON THEIR WAY - - - RUN>", 0, 0)
    window.update()

sleep(2)

# clear window
window.clear()

# prompt for end
window.set_font_color("green")
window.input_string('< PRESS ENTER TO QUIT >', 0, 0)

# close window
window.close()