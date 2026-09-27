import requests

base_url="https://api.chucknorris.io/jokes/"
cat_url="https://api.chucknorris.io/jokes/random?category="
l_cat = "https://api.chucknorris.io/jokes/categories"
topics = requests.get(l_cat).json()


print()
print("Welcome to chuck norris joke application!...")
print("About what would you like to read a joke?")
for i in range(len(topics)):
    print(i+1,". ",topics[i])
print("99 .  Exit")
while True:
    try:
        print()
        ch=int(input("Enter the topic number:"))
        print()
        joke = requests.get(cat_url+topics[ch-1]).json()

        print(joke['value'])

    except IndexError:
        print("Exiting...")

    
