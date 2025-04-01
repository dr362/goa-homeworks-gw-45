from turtle import *


#we want to paint a house

#step 1:   draw a square
speed()


width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing and coloring a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)   

end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()

#end of roof

#drawing 2 windows

color("blue")
begin_fill()
left(30)
forward(70)
left(90)
forward(60)
left(90)
forward(70)
left(90)
forward(60)

end_fill()

color("purple")
left(90)
left(90)
forward(140)
color("blue")
begin_fill()
forward(60)
right(90)
forward(70)
right(90)
forward(60)
right(90)
forward(70)

end_fill()

right(90)
color("purple")
forward(60)

#end












exitonclick()




surname = "gabidzashvili"

#  print(name)
#პრინტ ფუნქციას გადაცემა ეკრანზე გამოსატანი ობიექტი

name = "alexandre"  #ეს არის str (string)  ტიპის ცვლადი
age = (10) #ეს არის int (integer) მთელი რიცხვი
height = 141 #ეს არის float ტიპის ცვლადი (ათწილადი)
#booLean (booL) ტიპის ცვლადი

knows_programing = True  #True ან false
is_ugly = False   #snakecase (უბრალოდ წერისცსტილისტანდაეტულად)

isUgly = False #ჯავასკრიპტული cameLcase


#  print(name +" " + surname)

#  #სტრინგი არის ბრჭყალებშიმოქცეულისიმბოლოები
#  print(name + age)

#print (type(age))
#print (type(name))
#print (type(surname))
#print (type(height))
#print (type(knows_programing))

print(name + str(age))





