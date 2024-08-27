import turtle


screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coordinate(x, y):
    print(x, y)


# This method takes as argument a function whose input or argument are two int values.
# This function is called when the screen is clicked and uses the x and y coordinate of the
# clicked point as int values which will be passed into the get_mouse_click_coordinate function
turtle.onscreenclick(get_mouse_click_coordinate)
turtle.mainloop()
