
import tkinter as tk  
import random

subjects = [
    # Indian comedy sentences
    "Auto driver invents flying rickshaw",
    "Aunty opens world's first samosa ATM",
    "Cricket fans demand extra Sunday for matches",
    "Mumbai traffic jam declared new tourist spot",
    "Chaiwala launches tea-flavored toothpaste",
    "Bollywood stars spotted at pani puri competition",
    "Cow becomes Instagram influencer",
    "Rickshaw meter finally tells the truth",
    "Dosa breaks record for longest selfie",
    "Monkeys start yoga classes in park",
    # Senseable sentences
    "Teacher wins award for innovative teaching",
    "Scientist discovers new species of butterfly",
    "Local library hosts book reading event",
    "Student builds robot for science fair",
    "Doctor opens free health camp",
]

action = [
    "after eating too much biryani",
    "while dodging potholes",
    "during chai break",
    "as aunty gives life advice",
    "while bargaining at the market",
    "after missing the last metro",
    "while dancing to Bollywood tunes",
    "as uncle cracks another joke",
    "while waiting for monsoon rains",
    "after winning a spicy food challenge",
    # Senseable actions
    "after months of hard work",
    "with the help of volunteers",
    "during the annual festival",
    "after receiving community support",
    "while inspiring young minds",
]

places = [
    "at the local chai stall",
    "in Chandni Chowk",
    "at Marine Drive",
    "in a Mumbai local train",
    "at the neighborhood pani puri stand",
    "in a crowded Delhi metro",
    "at the cricket ground",
    "in front of India Gate",
    "at a wedding baraat",
    "in a busy IT office",
    "at the roadside dhaba",
    "in a Bengaluru traffic jam",
    "at the golgappa eating contest",
    "in a noisy vegetable market",
    "at the annual mela",
    "on a packed bus to Goa",
    "at the famous tea shop in Kolkata",
    "in a monsoon downpour",
    "at the local temple festival",
    "on the steps of a ghat in Varanasi",
    # Senseable places
    "in the city library",
    "at the science exhibition",
    "in the community hall",
    "at the local hospital",
    "in the school auditorium",
]
# Lists of subjects, actions, and places for headline generation
def generate_headline():
    subject = random.choice(subjects)
    action_phrase = random.choice(action)
    place = random.choice(places)
    headline = f"{subject} {action_phrase} {place}."
    headline_label.config(text=headline)

root = tk.Tk()
root.title("Random Funny Headline Generator")
root.geometry("700x500")
root.configure(bg="beige")

title_label = tk.Label(root, text="Welcome to the Random Funny Headline Generator!", font=("roboto", 16, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

headline_label = tk.Label(root, text="", wraplength=550, font=("roboto", 12, "bold"), fg="black", bg="beige")
headline_label.pack(pady=20)

generate_button = tk.Button(root, text="Generate Headline", command=generate_headline, font=("roboto", 12), bg="lightgreen")
generate_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("roboto", 10), bg="lightcoral")
exit_button.pack(pady=5)

root.mainloop()