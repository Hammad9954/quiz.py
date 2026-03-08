import random

print("Welcome to Hammad's Quiz!")

playing = input("Do you want to play? (yes): ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "Who invented the telephone?": "alexander graham bell",
    "How many continents are there on Earth?": "7",
    "Which ocean is the largest?": "pacific",
    "What gas do plants absorb from the atmosphere?": "carbon dioxide",
    "What is the largest mammal in the world?": "blue whale",
    "Who wrote the play Romeo and Juliet?": "william shakespeare",
    "What is the fastest land animal?": "cheetah",
    "Which country invented pizza?": "italy",
    "What is the capital of Japan?": "tokyo",
    "Which metal is liquid at room temperature?": "mercury",
    "How many sides does a triangle have?": "3",
    "What is the hardest natural substance on Earth?": "diamond",
    "Which planet is the largest in our solar system?": "jupiter",
    "What is the boiling point of water in Celsius?": "100",
    "Which animal is known as the king of the jungle?": "lion",
    "Which continent is the Sahara Desert located in?": "africa",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the national sport of Japan?": "sumo"
}

score = 0
num_questions = 5

random_questions = random.sample(list(questions.items()), num_questions)

for question, answer in random_questions:
    user_answer = input(question + " ")

    if user_answer.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is:", answer)

print("\nYou got", score, "out of", num_questions, "questions correct.")
print("Your score is:", (score / num_questions) * 100, "%")