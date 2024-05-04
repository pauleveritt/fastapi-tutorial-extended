from datetime import datetime


# Create initial data for questions
questions_data = [
    {"question_text": "Which planet is known as the Red Planet?", "pub_date": datetime.now()},
    {"question_text": "Who wrote the famous play 'Romeo and Juliet'?", "pub_date": datetime.now()},
    {"question_text": "What is the capital city of Australia?", "pub_date": datetime.now()},
    {"question_text": "Who painted the Mona Lisa?", "pub_date": datetime.now()},
    {"question_text": "What is the tallest mountain in the world?", "pub_date": datetime.now()},
    {"question_text": "What is the largest mammal in the world?", "pub_date": datetime.now()},
    {"question_text": "In which year did the Titanic sink?", "pub_date": datetime.now()},
    {"question_text": "Who discovered penicillin?", "pub_date": datetime.now()},
    {"question_text": "What is the currency of Japan?", "pub_date": datetime.now()},
    {"question_text": "Which country is known as the Land of the Rising Sun?", "pub_date": datetime.now()},
]

# Create initial data for choices
# Create initial data for choices
choices_data = [
    {"choice_text": "Mars", "question_id": 1},
    {"choice_text": "Jupiter", "question_id": 1},
    {"choice_text": "Venus", "question_id": 1},
    {"choice_text": "Mercury", "question_id": 1},
    {"choice_text": "William Shakespeare", "question_id": 2},
    {"choice_text": "Jane Austen", "question_id": 2},
    {"choice_text": "Charles Dickens", "question_id": 2},
    {"choice_text": "Mark Twain", "question_id": 2},
    {"choice_text": "Sydney", "question_id": 3},
    {"choice_text": "Melbourne", "question_id": 3},
    {"choice_text": "Canberra", "question_id": 3},
    {"choice_text": "Brisbane", "question_id": 3},
    {"choice_text": "Leonardo da Vinci", "question_id": 4},
    {"choice_text": "Pablo Picasso", "question_id": 4},
    {"choice_text": "Vincent van Gogh", "question_id": 4},
    {"choice_text": "Michelangelo", "question_id": 4},
    {"choice_text": "Mount Everest", "question_id": 5},
    {"choice_text": "K2", "question_id": 5},
    {"choice_text": "Kangchenjunga", "question_id": 5},
    {"choice_text": "Lhotse", "question_id": 5},
    {"choice_text": "Elephant", "question_id": 6},
    {"choice_text": "Blue whale", "question_id": 6},
    {"choice_text": "Giraffe", "question_id": 6},
    {"choice_text": "Hippopotamus", "question_id": 6},
    {"choice_text": "1912", "question_id": 7},
    {"choice_text": "1915", "question_id": 7},
    {"choice_text": "1917", "question_id": 7},
    {"choice_text": "1919", "question_id": 7},
    {"choice_text": "Alexander Fleming", "question_id": 8},
    {"choice_text": "Albert Einstein", "question_id": 8},
    {"choice_text": "Marie Curie", "question_id": 8},
    {"choice_text": "Isaac Newton", "question_id": 8},
    {"choice_text": "Yen", "question_id": 9},
    {"choice_text": "Dollar", "question_id": 9},
    {"choice_text": "Euro", "question_id": 9},
    {"choice_text": "Pound", "question_id": 9},
    {"choice_text": "Japan", "question_id": 10},
    {"choice_text": "China", "question_id": 10},
    {"choice_text": "South Korea", "question_id": 10},
    {"choice_text": "India", "question_id": 10},
]

INITIAL_DATA = {
    'question': questions_data,
    'choice': choices_data,
}


def initialize_table(target, connection, **kw):
    table_name = target.description
    if table_name in INITIAL_DATA and len(INITIAL_DATA[table_name]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[table_name])