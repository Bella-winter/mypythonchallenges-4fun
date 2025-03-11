
# Personalized Greeting App with Hobbies

# Ask for user's name
name = input("What is your name? ")

# Ask for user's favorite color
color = input("What is your favorite color? ")

# Ask for user's favorite animal
animal = input("What is your favorite animal? ")

# Ask for user's hobbies
hobby = input("What is one of your favorite hobbies? ")

# Ask for users favorite food
food = input("What is your favorite food? ")

# Ask for users favorite movie
movie = input("What is your favorite movie? ")

# Ask for users favourite sport
sport = input("What is your favourite sport? ")
#Ask for users Height
height = input("What is your height? ")
# Ask for users weight
weight = input("What is your weight? ")
# Ask for users favorite music
music = input("What is your favorite music? ")
# Ask for users shoe size
shoe_size = input("What is your shoe size? ")   
# Ask for users birth year
birth_year = input("What year were you born? ") 
# Calculate the users age
age = 2025 - int(birth_year)
print(age)
# Convert the shoe size to an integer
# Use the shoe size to calculate the users height
height = int(shoe_size) + 10
# Ask for users instagram
instagram = input("What is your instagram? ")
# Ask for users snapchat
snapchat = input("What is your snapchat? ")
# Ask for users twitter
twitter = input("What is your twitter? ")
# Ask for users facebook
facebook = input("What is your facebook? ") 
# Ask for users linkedin
linkedin = input("What is your linkedin? ")
# Ask for users tiktok
tiktok = input("What is your tiktok? ")
# users favourite quote
quote = input("What is your favourite quote? ")



# Print a personalized greeting
print(f"Hello, {name}! Your favorite color, {color}, is awesome! {animal}s are amazing creatures! It's great that you enjoy {hobby}. Keep doing what you love! 😊.")
print(f"Also, I see that you like {food} and {movie}. I love those too! 😊.")
print(f"Lastly, I see that you like {sport}. I love that sport too! 😊.")
print(f"Your height is {height}cm and your weight is {weight}.")
print(f"You are {age} years old.")
print(f"Your favorite music is {music}.")
print(f"Your shoe size is {shoe_size}.")
print(f"Your instagram is {instagram}.")
print(f"Your snapchat is {snapchat}.")
print(f"Your twitter is {twitter}.")
print(f"Your facebook is {facebook}.")
print(f"Your linkedin is {linkedin}.")
print(f"Your tiktok is {tiktok}.")
print(f"Your favourite quote is {quote}.")

print(f"Thank you for sharing a bit about yourself! Have a great day! 😊.")