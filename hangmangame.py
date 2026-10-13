
import random

words = [
    "Manichitrathazhu", "Ustad Hotel", "Drishyam",
    "Bangalore Days", "Premam", "Charlie", "Lucifer",
    "Maheshinte Prathikaaram", "Thanneer Mathan Dinangal",
    "Kumbalangi Nights", "Kunjiramayanam",
    "Ayyappanum Koshiyum", "Godha", "Minnal Murali",
    "Jacobinte Swargarajyam", "Hridayam",
    "Ohm Shanthi Oshaana", "Aadujeevitham", "Premalu",
    "Pulimurugan", "Manjummel Boys", "Neram", "Aavesham",
    "Om Shanti Oshana", "Varshangalkku Shesham",
    "Thoovanathumbikal", "Kishkindha Kaandam",
    "Devasuram", "Bramayugam", "Spadikam", "Kireedam",
    "Home", "Chithram", "Android Kunjappan", "Kilukkam",
    "Virus", "Nadodikkattu", "Helen", "Sandesham", "Uyare",
    "In Harihar Nagar", "Ishq", "Ramji Rao Speaking",
    "Nayattu", "Godfather", "Jana Gana Mana",
    "Thenmavin Kombath", "Driving Licence", "Bharatham",
    "Anjaam Pathiraa", "His Highness Abdullah", "Forensic",
    "Vietnam Colony", "Memories", "Manathe Kottaram",
    "Mumbai Police", "Summer in Bethlehem", "Traffic",
    "Niram", "Ustad", "Friends", "Big B",
    "Chronic Bachelor", "Rajamanikyam", "Classmates",
    "Pokkiri Raja", "Twenty:20", "Christian Brothers",
    "Narasimham", "Ravanaprabhu", "Runway",
    "Rajavinte Makan", "New Delhi", "Irupatham Noottandu",
    "Oru Vadakkan Veeragatha", "Aaram Thampuran",
    "Perumthachan", "Nandanam", "Kaliyattam",
    "Meesa Madhavan", "Ee Parakkum Thalika",
    "Punjabi House", "CID Moosa", "Chotta Mumbai",
    "Vettam", "Hallo", "Bodyguard", "Pattanathil Bhootham",
    "My Boss", "Salt N' Pepper", "Two Countries",
    "Diamond Necklace", "Amar Akbar Anthony",
    "Annayum Rasoolum", "Adi Kapyare Kootamani",
    "North 24 Kaatham", "Aadu"
]

word = random.choice(words).lower()
guessed = set()
chances = 6

print("Welcome to Malayalam Movie Hangman!")
print("Guess the movie name one letter at a time.")
print("You have", chances, "chances.")

while chances > 0:
    display = ""

    for letter in word:
        if letter == " ":
            display += "  "
        elif letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nMovie:", display)

    if all(letter == " " or letter in guessed for letter in word):
        print("Congratulations You won!")
        print("Movie name:", word.title())
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter one English letter!")
        continue

    if guess in guessed:
        print("You already guessed that letter")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct guess")
    else:
        chances -= 1
        print("Wrong guess!")
        print("Chances left:", chances)

else:
    print("\nGame over You lost.")
    print("The movie name was:", word.title())
