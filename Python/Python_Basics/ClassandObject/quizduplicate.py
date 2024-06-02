#creating an questions array

questions_prompt = [
    "1. who is the father of our nation India \n\n (a)Mahatma Gandhi (b)Subhash Chandrabose \n\n",
    "2. India's first citizen \n\n (a)Prime Minister of India (b)President of India \n\n"
]

#lets create question class

class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#now lets create an another array to access question and answer using "question" class defined above
        
questions = [
    question(questions_prompt[0],"a"),
    question(questions_prompt[1],"b")
]

# now let define a funtion to run our questionpaper

def test_run(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("you got " + str(score) + "/" + str(len(questions)) + " are correct")
          
test_run(questions)