# 1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია


# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ


# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is
#1)
list = [1,2,100,3,4]
list.pop(2)
list.insert(0,0)
print(list)
#2)
def xarisxshi_gadayvana(num1,num2):
    num1 = num1**num2
    print(num1)
xarisxshi_gadayvana(3,2)
#3)
def checking_length():
    list = [2,4,6,8,10]
    if list % 2 == 0:
        print("list length is even")
    else:
        print("list length is odd")