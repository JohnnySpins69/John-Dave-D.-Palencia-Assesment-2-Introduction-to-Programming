#imports for functions:
import datetime #using for the time/day function.
import pyttsx3 #python text-to-speech.

#text-to-speech setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


#greeting based on time:
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        print("\nGood morning fam!")
        print("\nWelcome to my vending machine Chief!")
        speak("\nWelcome to my vending machine Chief!")
        print("What can bossman get you?")
        speak("What can bossman get you?")
        speak("Good morning fam.")
    elif hour < 18:
        print("\nGood afternoon cuz!")
        print("\nWelcome to my vending machine Chief!")
        speak("\nWelcome to my vending machine Chief!")
        print("What can bossman get you?")
        speak("What can bossman get you?")
        speak("Good afternoon cuz.")
    else:
        print("\nNice evening we got fam!")
        print("\nWelcome to my vending machine Chief!")
        speak("\nWelcome to my vending machine Chief!")
        print("What can bossman get you?")
        speak("What can bossman get you?")
        speak("Nice evening we got fam.")
    speak("What can i get you chief?")


#product menu:
products = {
    "A1": {"item": "Beef Burger", "price": 5.00, "stock": 5},
    "A2": {"item": "Sandwich(Salami)", "price": 3.50, "stock": 5},
    "A3": {"item": "Sandwich(Egg)", "price": 4.00, "stock": 5},
    
    "B1": {"item": "Chocolate", "price": 5.00, "stock": 10},
    "B2": {"item": "Cookies", "price": 3.00, "stock": 10},
    "B3": {"item": "Marshmallows", "price": 3.50, "stock": 5},
    
    "C1": {"item": "Juice", "price": 6.00, "stock": 8},
    "C2": {"item": "Coffee", "price": 2.50, "stock": 8},
    "C3": {"item": "Water", "price": 1.50, "stock": 8}
    }
#for pairings:
foods = ["A1","A2","A3"]
sweets = ["B1","B2","B3"]
drinks = ["C1","C2","C3"]


#display menu to user
def show_menu():
    print(
    "\n================= VENDING MACHINE MENU ================="
    "\nCode   | Item                 | Price   | Stock"
    "\n--------------------------------------------------------"  #this looks fire sheeeesh
    )
    for code, details in products.items():
        print(f"{code:<6}| {details['item']:<20} | {details['price']:<7} AED | Stock: {details['stock']}")
    print("========================================================")


#suggest the user for extra products (extra money extracted):
def func_suggest_pairing(code):
    if code in foods:
        print("\nWould you like a drink with that bruv?")
        print("\nI personally recommend: C1 (Juice), C2(Coffee), and C3 (Water)")
        recommended = ["C1","C2","C3"]
    elif code in drinks:
        print("\nSweets would go bonkers with your drink fam.")
        print("\nI personally recommend: B1 (Chocolate), B2 (Cookies), and (marshmallows)")
        recommended = ["B1","B2","B3"]
    elif code in sweets:
        print("\nA drink goes well with sweets as usual (Don't be shy now fam).")
        print("\nI personally recommend: C1 (Juice), C2(Coffee), and C3 (Water)")
        recommended = ["C1", "C2", "C3"]

    else:
        return None #returns None if user didnt choose.
    
    want_pair = input("\nWant to add some of my recommendations cuz? (Y/N): ").upper()
    if want_pair != "Y":
        return None
    
    #let user choose a recommended stuff.
    while True:
        choice = input("Enter that code of the recommended item chief. (or Q to cancel): ").upper()
        if choice == "Q": #quit if user changes mind.
            print("\n purchasing first item only (Touche)...")
            return None
    
        if choice in recommended:
            print(f"\nGood choice fam, Adding {choice} to your purchase.")
            return choice
    else:
        print("\nNot in the our choices im afraid chief. please choose again.")


#get user input for product selection:
def get_choice():
    user_choice = input("\nEnter a product code here chief (or type Q to quit): ").upper() #added quit function.
   
    #exit option if "q" is typed:
    if user_choice == "Q":
        print("Thank you, please come again.")
        speak("Thank you, please come again.")
        exit()

    if user_choice in products: #if choice is in the products "Dont forget!".
        
        #almost forgot this crap:
        if products[user_choice]["stock"] <= 0: #if no more stock part.
            print("We dont have the stock for that, sorry chief.")
            return None
    
        item = products[user_choice]
        print(f"\nYou have selected {item['item']}, for the low price of = {item['price']} AED.")
        speak(f"You have selected {item['item']}. for the low price of {item['price']} dirhams.")
        
        extra = func_suggest_pairing(user_choice) #suggest user with pairings [food,snacks,drinks]
        
        if extra:
            return [user_choice, extra]
        else:
            return [user_choice]
              
    else:
        print("\nInvalid selection boss. Try again, yeah?")
        speak("Invalid selection boss. Try again, yeah?")
        return None


#ask user for currency:
def get_money():
    while True:
        user_input = (input("\nPlease enter currency (AED) or type Q to cancel: ")).upper()
        
        if user_input == "Q":
            print("\nPurchase cancelled.")
            return None
        try:
            amount = float(user_input)
            return amount
        except:
            print("\nInvalid amount. Please try again.")


#receipt:
def make_receipt(codes,total,money,change):
    print("\n========== RECEIPT ==========")
    for stuff in codes:
        print(f"{stuff} - {products[stuff]['item']} : {products[stuff]['price']} AED")
    print(f"\nTotal: {total} AED")
    print(f"Paid: {money} AED")
    print(f"Change: {change} AED")
    print("Thank you for your purchase!")
    print("=============================")


#main loop test-67 lmao:
def main_loop():
    greet_user()

    while True:
        show_menu()
        codes = get_choice()
    
        #purchasing process part (lowkey janky but it iz wut it iz):
        if codes:
            print("\nCalculating total...") #dramatic pause...
            
            total_sum = 0 #i always forget this XD.
            
            for stuff in codes:
                print("adding:",  products[stuff]["item"])
                total_sum += products[stuff]["price"]
                
            print(f"\nTotal amount: {total_sum} AED")
            money = get_money()
                
            if money is None:
            
                continue #user cancelled the payment :(
            
            elif money < total_sum:
                print("\nNot enough dosh bruv (Money).")
                speak("Not enough dosh bruv.")
                continue #so stock doesnt get lost/prevents receipt
            else:
                change = money - total_sum
                print("Payment accepted. Nice!")
                print(f"\nYour change is {change} AED.")
                speak("Payment accepted.")

            #respectfully vanquish 1 stock:
            for stuff in codes:
                products[stuff]["stock"] -= 1
                    
            make_receipt(codes, total_sum, money, change)

            #ask again:
            again = input("\nWould you like to purchase again? (Y/N): ").upper()
            if again != "Y":
                print("See you next time cuz!")
                speak("thanks for stopping by fam!")
                
                print(
                "\n========================================="
                        "\nTHANKS FOR STOPPING BY FAM!"
                        "\nCOME BACK SOON, YEAH?"
                "\n========================================="
                )
                
                speak("come back soon, yeah?")
                
                break
            
#AND FOR THE GRAND FINALE!!!:
print(
"\n========================================="
    "\nWELCOME TO MY VENDING MACHINE TWIN"      #gotta love that introduction mane.
"\n========================================="
)

main_loop()
