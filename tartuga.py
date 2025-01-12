from turtle import Turtle, Screen

floyd = Turtle()

floyd.shape('triangle')
floyd.color('black')

tela = Screen()
print(tela.canvheight)


floyd.forward(100)
floyd.right(90)
floyd.forward(200)
floyd.right(90)
floyd.forward(100)
tela.exitonclick()

