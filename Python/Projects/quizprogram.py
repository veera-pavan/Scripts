# Using Dictionary to store question and answers
# Using a variable to store score value
# Loop through question and answers
# Print each question and take user input for answer, and compare this key : value pair with the dictionary key : value pairs
# Print score based on the correct/wrong answer
# Finally print the total score and its percentage

quiz_questions = {
    
            "question1": {
                        "question": "what is the capital of Andhra Pradesh?",
                        "answer": "Amaravathi"
                    },
            "question2": {
                "question": "what is the capital of Telangana?",
                "answer": "Hyderabad"
            },
            "question3": {
                "question": "what is the capital of Maharashtra?",
                "answer": "Mumbai"
            },
            "question4": {
                "question": "what is the capital of Karnataka?",
                "answer": "Bengaluru"
            },
            "question5": {
                "question": "what is the capital of Tamil Nadu?",
                "answer": "Chennai"
            },
            "question6": {
                "question": "what is the capital of UP?",
                "answer": "Lucknow"
            },
            "question7": {
                "question": "what is the capital of Kerala?",
                "answer": "Thiruvananthapuram"
            }
    
}

score = 0

for key, value in quiz_questions.items():
    print(value['question'])
    answer = input("Answer ?: ")
    if value['answer'].lower() == answer.lower():
        print("Correct Answer")
        score = score + 1
        print("score:" + str(score))
    else:
        print("Wrong Answer")
        score = score
        print("score:" + str(score))


print("Total score:" + str(score) + "     Percentage:" + str(int(score/7*100)))
