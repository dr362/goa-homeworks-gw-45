# დავალება 10წთ (8:33):
# ```
# 1)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელი და დააბრუნებს ამ სახელს, ოღონდ ლუწ ინდექსზე მდგომი ასოები უნდა იყოს გადიდებული, კენტ ინდექსზე მდგომი ელემენტები უნდა იყოს დაპატარავებული.

# 2)შექმენით ფუნქცია manual_join() რომელიც გააკეთებს იგივე დავალებას რასაც აკეთებს მეთოდი .join() (ანუ შექმენით join-ის კლონი).

# 3)შექმენით ორი ცვლადი, პირველში შეინახეთ ემაილი, მეორეში შეინახეთ პაროლი, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და ემაილი სანამ არ დაემთხვევა სწორ პაროლ და ემაილს.```
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
    
