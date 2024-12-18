import json

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    for q in questions:
        print(q['prompt'])
        for option in q['options']:
            print(option)
        while True:
            answer = input('Please enter your answer (A, B, C or D): ').upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C or D.")
        if answer == q['answer']:
            print('YAAAAY!! It is correct answer!\n')
            score += 1
        else:
            print('Sorry, the correct answer is ', q['answer'], '\n')
            print(q['explanation'],'\n')
            score -= 1

    print(f'You got {score} out of {total_questions}.')

filename = 'questions.json'
with open(filename, 'r') as json_file:
    questions = json.load(json_file)  # Load the questions from the JSON file

run_quiz(questions)