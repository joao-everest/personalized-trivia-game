import numpy as np
import random
import json
import sys

sys.path.append('/Users/joaocosta/Desktop/data_science_joao_projects/quiz_project/data')

JSON_PATH = '/Users/joaocosta/Desktop/data_science_joao_projects/quiz_project/data/all_quiz_questions.json'

question_area = {
    1: "History",
    2: "Geography",
    3: "Science & Nature",
    4: "Pop Culture & Entertainment",
    5: "Sports",
    6: "Arts & Literature",
}


test_json = [
  {
    "question_id": '1_1',
    "difficulty": 1,
    "question": "What is the capital of France?",
    "options": {
      "A": "Berlin",
      "B": "Madrid",
      "C": "Paris",
      "D": "Rome"
    },
    "correct_answer": "C"
  },
  {
    "question_id": '2_1',
    "difficulty": 2,
    "question": "Who wrote 'Hamlet'?",
    "options": {
      "A": "Charles Dickens",
      "B": "William Shakespeare",
      "C": "Leo Tolstoy",
      "D": "Mark Twain"
    },
    "correct_answer": "B"
  }
]

history_json = [
  {
    "question_id": "1_1",
    "difficulty": 1,
    "question": "Who was the first President of the United States?",
    "options": {
      "A": "Thomas Jefferson",
      "B": "Abraham Lincoln",
      "C": "George Washington",
      "D": "John Adams"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "1_2",
    "difficulty": 1,
    "question": "In which year did World War II end?",
    "options": {
      "A": "1945",
      "B": "1918",
      "C": "1939",
      "D": "1955"
    },
    "correct_answer": "A"
  },
  {
    "question_id": "2_1",
    "difficulty": 2,
    "question": "The ancient pyramids of Giza are located in which country?",
    "options": {
      "A": "Sudan",
      "B": "Egypt",
      "C": "Mexico",
      "D": "Peru"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "2_2",
    "difficulty": 2,
    "question": "Which famous explorer is often credited with 'discovering' America in 1492?",
    "options": {
      "A": "Ferdinand Magellan",
      "B": "Marco Polo",
      "C": "Vasco da Gama",
      "D": "Christopher Columbus"
    },
    "correct_answer": "D"
  },
  {
    "question_id": "3_1",
    "difficulty": 3,
    "question": "The Renaissance, a period of 'rebirth' in art and learning, began in which European country?",
    "options": {
      "A": "France",
      "B": "Spain",
      "C": "Italy",
      "D": "England"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "3_2",
    "difficulty": 3,
    "question": "The Roman Empire was centered around which sea?",
    "options": {
      "A": "Black Sea",
      "B": "Mediterranean Sea",
      "C": "Red Sea",
      "D": "Caspian Sea"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "4_1",
    "difficulty": 4,
    "question": "The Magna Carta, a foundational document for modern democracy, was signed in which country in 1215?",
    "options": {
      "A": "France",
      "B": "Germany",
      "C": "Spain",
      "D": "England"
    },
    "correct_answer": "D"
  },
  {
    "question_id": "4_2",
    "difficulty": 4,
    "question": "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
    "options": {
      "A": "Joseph Stalin",
      "B": "Vladimir Lenin",
      "C": "Nikita Khrushchev",
      "D": "Mikhail Gorbachev"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "5_1",
    "difficulty": 5,
    "question": "Which empire was ruled by the famous leader Julius Caesar?",
    "options": {
      "A": "The Persian Empire",
      "B": "The Greek Empire",
      "C": "The Roman Republic/Empire",
      "D": "The Mongol Empire"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "5_2",
    "difficulty": 5,
    "question": "The Treaty of Tordesillas (1494) divided the newly discovered lands outside Europe between which two countries?",
    "options": {
      "A": "England and France",
      "B": "Spain and Portugal",
      "C": "Netherlands and England",
      "D": "France and Spain"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "6_1",
    "difficulty": 6,
    "question": "What was the name of the last imperial dynasty of China, which ended in 1912? ",
    "options": {
      "A": "Ming Dynasty",
      "B": "Han Dynasty",
      "C": "Tang Dynasty",
      "D": "Qing Dynasty"
    },
    "correct_answer": "D"
  },
  {
    "question_id": "6_2",
    "difficulty": 6,
    "question": "The Battle of Austerlitz in 1805 is considered a tactical masterpiece by which military commander? ",
    "options": {
      "A": "Duke of Wellington",
      "B": "Napoleon Bonaparte",
      "C": "General Kutuzov",
      "D": "Archduke Charles"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "7_1",
    "difficulty": 7,
    "question": "The 'Great Game' was a 19th-century political and diplomatic confrontation between which two empires over influence in Central Asia? [6, 12, 32]",
    "options": {
      "A": "The Ottoman and Persian Empires",
      "B": "The French and British Empires",
      "C": "The British and Russian Empires",
      "D": "The Austro-Hungarian and Russian Empires"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "7_2",
    "difficulty": 7,
    "question": "Who was the founder of the Mali Empire in the 13th century? [3, 27, 28]",
    "options": {
      "A": "Mansa Musa",
      "B": "Sundiata Keita",
      "C": "Askia the Great",
      "D": "Sunni Ali Ber"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "8_1",
    "difficulty": 8,
    "question": "The Thirty Years' War (1618-1648) began primarily as a conflict between which two religious groups?",
    "options": {
      "A": "Christians and Muslims",
      "B": "Pagans and Christians",
      "C": "Catholics and Protestants",
      "D": "Sunni and Shia Muslims"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "8_2",
    "difficulty": 8,
    "question": "What was the name of the series of wars fought between Rome and Carthage for control of the Mediterranean?",
    "options": {
      "A": "The Peloponnesian Wars",
      "B": "The Punic Wars",
      "C": "The Gallic Wars",
      "D": "The Samnite Wars"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "9_1",
    "difficulty": 9,
    "question": "What was the 'Code of Hammurabi'?",
    "options": {
      "A": "A collection of epic poems",
      "B": "A treaty ending the first Egyptian dynasty",
      "C": "A manual for pyramid construction",
      "D": "A Babylonian legal text"
    },
    "correct_answer": "D"
  },
  {
    "question_id": "9_2",
    "difficulty": 9,
    "question": "The political entity established by the Treaty of Rome in 1957, a precursor to the European Union, was known as what?",
    "options": {
      "A": "The European Coal and Steel Community",
      "B": "The European Free Trade Association",
      "C": "The European Economic Community",
      "D": "The Council of Europe"
    },
    "correct_answer": "C"
  },
  {
    "question_id": "10_1",
    "difficulty": 10,
    "question": "The 'War of the Triple Alliance' (1864-1870), one of the deadliest conflicts in South American history, saw Paraguay fight against which three allied countries?",
    "options": {
      "A": "Chile, Peru, and Bolivia",
      "B": "Argentina, Brazil, and Uruguay",
      "C": "Colombia, Venezuela, and Ecuador",
      "D": "Argentina, Chile, and Peru"
    },
    "correct_answer": "B"
  },
  {
    "question_id": "10_2",
    "difficulty": 10,
    "question": "Who was the last emperor of the Byzantine Empire, who died during the Fall of Constantinople in 1453?",
    "options": {
      "A": "Justinian I",
      "B": "Alexios I Komnenos",
      "C": "Constantine XI Palaiologos",
      "D": "Heraclius"
    },
    "correct_answer": "C"
  }
]


def get_questions_by_difficulty(json_file, difficulty_level, category):
    """
    Aux function that returns questions from a json file based on their difficulty level
    """
    return [q for q in json_file if q['difficulty'] == difficulty_level and q['category']==category]

class Question:
    def __init__(self, question_json):
        self.question_text = question_json['question']
        self.options = question_json['options']
        self.correct_answer = question_json['correct_answer']
        self.difficulty = question_json['correct_answer']
        self.category = question_json['category']

    def display_question(self):
        
        """Display the question with formatted options"""
        print(f"\nQuestion:")
        print(self.question_text)
        print()  # Empty line for better readability
        
        for option_key, option_value in self.options.items():
            print(f"{option_key}. {option_value}")
        
        print()  # Empty line before input
        self.user_answer = input("Your answer (A, B, C, or D): ").upper()
    
    def check_answer(self):
        if self.user_answer == self.correct_answer:
            print('Perfect! Correct Answer')
            print('Lets move to the next question!')
            return True

        else:
            print('Oh no! Wrong answer...')
            print(f"The correct answer was {self.options[self.correct_answer]}")
            return False
 


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 1

    def update_score(self, move):
        if move == 'up':
            self.score += 1
        elif move == 'down':
            self.score -= 1
        else:
            self.score = self.score
# This uses composition (Game "has a" Player) rather than inheritance (Player "is a" Game),
#  which makes more logical sense.


class Game:

    def __init__(self):
        self.player = None
        self.level = 1

        print('Loading game ....')
        # Open and read the JSON file
        with open(JSON_PATH, 'r') as file:
            json_data = json.load(file)


        self.db = json_data
        print('Loading Complete!')


        self.category_dict =  {
                                1: "History",
                                2: "Geography",
                                3: "Science & Nature",
                                4: "Pop Culture & Entertainment",
                                5: "Sports",
                                6: "Arts & Literature",
                              }

    def start_game(self):

        if self.player is None:
            print('Welcome to Who Wants do be a Millionaire?')
            player_name = input('Please enter your name: ')
            self.player = Player(player_name)
            print(f"Hello {self.player.name}! Let's start the game!")
        else:
            print(f"Welcome back, {self.player.name}! Let's continue the game!")

    def update_level(self, move):
        if move == 'up':
            self.level = min(10, self.level + 1)
            if self.level == 10:
                print('Congratulations - You are a Millionaire!')
        elif move == 'down':
            self.level = max(1, self.level - 1)

    


    def ask_question(self):

        area_code = np.random.randint(1,7)

        area_text = self.category_dict[area_code]

        print(f'Choosen topic: {area_text}')


        question_by_level =  get_questions_by_difficulty(self.db,self.level, area_text)

        question_index = random.randrange(len(question_by_level))

        question_json = question_by_level[question_index]

        question = Question(question_json)

        question.display_question()

        if question.check_answer() == True:
            self.update_level('up')
            print('You moved on level up')
        else:
            self.update_level('down')

    def ask_level(self):

        print(f'You are in level {self.level}')





    