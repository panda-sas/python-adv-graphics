# import colorgram
import turtle as turtle_module
import random
turtle_module.colormode(255)
#
# colors = colorgram.extract('hirst-spots.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(197, 13, 32), (249, 237, 21), (39, 77, 188),  (238, 227, 5), (39, 216, 68), (228, 160, 47),
              (243, 247, 253), (28, 40, 155), (214, 75, 14),  (16, 153, 17), (199, 15, 11), (242, 34, 164),
              (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208),  (11, 97, 62), (220, 160, 10),
              (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217),  (73, 212, 168),
              (81, 234, 202), (61, 233, 241), (5, 67, 42)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()



