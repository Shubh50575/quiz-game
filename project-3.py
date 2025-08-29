import random
import time

def display_welcome():
    print("\n"+ "="* 50)
    print("🎮 WELCOME TO THE ULTIMATE QUIZ CHALLENGE! 🎮".center(50))
    print("="* 50)
    print("\n 📔 Instruction:")
    print("- Choose a quiz category")
    print("- Answer multiple-choice question")
    print("- Each correct final score at the end")
    print("- Have fun and learn something new!")
def display_categories():
    print("\n QUIZ CATEGORIES")
    print("1. General Knowledge")
    print("2. Sports and Culture")
    print("3. Science and Nature")
    print("4. Movies and TV")
    print("5. Random Mix (Questions from all Categories)")
    


def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect a category(1-5): "))
            if 1<= choice <=5:
                return choice
            else:
                print(f"Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")
def load_questions():
    general_knowledge = [
    {
        "question": "What is the capital of USA?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Washington"],
        "answer": "D"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Mars"],
        "answer": "C"
    },
    {
        "question": "Who is the father of the Indian Constitution?",
        "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. B.R Ambedkar", "D. Sardar Patel"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "Who wrote the national song of India?",
        "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Subhash Chandra Bose", "D. Lala Lajpat Rai"],
        "answer": "B"
    }
]
    sports_culture = [
        {

            "question":"Which sports is conisdered the most popular in the world?",
            "options": ["A. Football", "B. Chess", "C. Cricket", "D. Hockey"],
            "answer": "A"
         },
         {

            "question":"In what year were the first modern Summer Olympic games held?",
            "options": ["A. 1896", "B. 1904", "C. 1948", "D. 1971"],
            "answer": "A"
         },
         {

            "question":"What game is called th'sports of kings'?",
            "options": ["A. Cricket", "B. Volleyball", "C. Ludo", "D. Chess"],
            "answer": "D"
         },
         {

            "question":"In what kind of sport are the 'Golden Stanley Cup medals won'?",
            "options": ["A. Football", "B. Hockey", "C. Golf", "D. Tennis"],
            "answer": "B"
         },
         {

            "question":"In which year the India won the first ICC World Cup?",
            "options": ["A. 1883", "B. 1999", "C. 2011", "D. 1948"],
            "answer": "A"
         },

        
    ]
    science_nature = [
        {

            "question":"What is the unit of Electric Power?",
            "options": ["A. Watt", "B. Joule", "C. Pascal", "D. Newton"],
            "answer": "A"
         },
         {

            "question":"Who built Taj Mahal?",
            "options": ["A. Shah Jahan", "B. Akbar", "C. Humanu", "D. Babur"],
            "answer": "A"
         },
         {

            "question":"Which river is known as the Ganga of the South?",
            "options": ["A. Kavari", "B. Godavari", "C. Krishna", "D. Brahmaputra"],
            "answer": "B"
         },
         {

            "question":"How many states are there in India?",
            "options": ["A. 29", "B. 27", "C. 28", "D. 25"],
            "answer": "C"
         },
         {

            "question":"Who was the first Prime Minister of India?",
            "options": ["A. Jawaharlal Nehru", "B. Sardar Patel", "C. Mahatama Gandhi", "D. Bhagat Singh"],
            "answer": "A"
         },

        
    ]
    movies_tv = [
        {

            "question":"Who played Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Chris Evans", "B. Robert Downey", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "B"
         },
         {

            "question":"Which TV Show features a high school chemistry teacher who become a drug dealer?",
            "options": ["A. Breaking Bad", "B. The Walking Dead", "C. Games of Thrones", "D. Stranger Things"],
            "answer": "A"
         },
         {

            "question":"What was the first film in the Star Wars original trilogy?",
            "options": ["A. The Empire Strikes Back", "B. Return of the Jedi", "C. A New Hope", "D. The Phantom Menace"],
            "answer": "C"
         },
         {

            "question":"Which actress played Katniss in The Hunger Games?",
            "options": ["A. Emma Watson", "B. Jennifer Lawrence", "C. Scarlett Johansson", "D. Emma Stone"],
            "answer": "B"
         },
         {

            "question":"Which animated movies features a snowman named Olaf?",
            "options": ["A. Toy Story", "B. Shrek", "C. Frozen", "D. Finding Nemo"],
            "answer": "C"
         },

        
    ]
    return{
        1:{"name":"General Knowlege","questions":general_knowledge},
        2:{"name":"Movies and TV Shows","questions":sports_culture},
        3:{"name":"Science and Nature","questions":science_nature},
        4:{"name":"Movies and TV","questions":movies_tv},
        5:{"name":"Random Mix","questions":general_knowledge + sports_culture + science_nature + movies_tv},
    }
def run_quiz(category_data):
    category_name = category_data["name"]
    questions = category_data["questions"]

    random.shuffle(questions)
    print(f"\nStarting the {category_name} quiz")
    print("Answer each question by typing the letter of your choice (A, B, C, or D).\n")

    score = 0
    correct_answers = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}/{len(questions)}")
        print(q["question"])
        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("\nYour answer (A,B,C,D): ").upper()
            if user_answer not in ['A', 'B', 'C', 'D']:
                print("Please enter A, B, C, or D.")
            else:
                break

        correct = user_answer == q["answer"]
        if correct:
            score += 10
            correct_answers += 1
            print("Correct☑️! +10 points")
        else:
            print(f"Wrong❎! The correct answer is {q['answer']}")

        if i < len(questions) - 1:
            print("Next question coming up...")
            time.sleep(1.5)

    print("\n" + "="*50)
    print("QUIZ RESULTS".center(50))
    print("="*50)
    print(f"Score: {score}")
    print(f"Category: {category_name}")
    print(f"Correct Answers: {correct_answers}/{len(questions)}")
    print(f"Total Score: {score} points")

    percentage = (score / (len(questions) * 10)) * 100
    if percentage == 100:
        print("\nPERFECT SCORE! You're a quiz master!")
    elif percentage >= 80:
        print("\nGOOD JOB! You really know your stuff!")
    elif percentage >= 40:
        print("\nNOT BAD! There's room for improvement.")
    else:
        print("\nKEEP LEARNING! Practice makes perfect!")

    return score

def main():
    display_welcome()

    total_score = 0
    play_again = True

    while play_again:
        display_categories()
        categories_choice = get_user_choice()
        all_categories = load_questions()
        score = run_quiz(all_categories[categories_choice])
        total_score += score
        again = input("\nPlay another round?(Yes/No): ").lower()
        while not {again.startswith("y") or again.startswith("n")}:
            print("Please type Yes or No.")
            again = input("Play another round?(Yes/No): ").lower()
        play_again = again.startswith("y")
    print(f"\n👍 Thanks for playing! your score from all rounds: {total_score} points")

main()