#  Level 40(CODEWARS):
# ```დავალება:```
# ```
# 1)დაასრულეთ აუცილებლად საკლასო დავალება ვისაც არ დაგისრულებიათ:
#     1.1)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი და დააბრუნებს ამ სახელს, ოღონდ ლუწ ინდექსზე მდგომი ასოები უნდა იყოს გადიდებული, კენტ ინდექსზე მდგომი ელემენტები უნდა იყოს პატარა.
#     1.2)შექმენით ფუნქცია manual_join() რომელიც გააკეთებს იგივე დავალებას რასაც აკეთებს მეთოდი .join() (ანუ შექმენით join-ის კლონი).
#     1.3)შექმენით ორი ცვლადი, პირველში შეინახეთ ემაილი, მეორეში შეინახეთ პაროლი, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და ემაილი სანამ არ დაემთხვევა სწორ პაროლ და ემაილს.

# 2)ასევე შეასრულეთ შემდეგი Codewars ები:
# https://www.codewars.com/kata/53af2b8861023f1d88000832
# https://www.codewars.com/kata/57eae65a4321032ce000002d
# https://www.codewars.com/kata/5772da22b89313a4d50012f7
# https://www.codewars.com/kata/58649884a1659ed6cb000072

# 3)გაიმეორეთ ნასწავლი სტრინგისა და სიის მეთოდები პითონში და ივარჯიშეთ მათზე```
def name_change(name):
    result = ""
    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i].upper()
        else:
            result += name[i].lower()
    print(result)
name_change("alexandre ")

def manual_join(arr, symbol):
    result = ""

    for i in arr:
        result += i + symbol
    return result[0:-1]


print(manual_join(["gio", "alexandre", "taso", "akaki", "luka"], "$"))

email = "sandrogabidzashvili92@gmail.com"
password = "me"

user_email = ""
user_password = ""

while user_password != password or user_email != email:
    user_email = input("ENTER YOUR EMAIL NOW:")
    user_password = input ("ENTER YOUR PASSWORD NOW:")
print("no hw cus hw is in codewars")