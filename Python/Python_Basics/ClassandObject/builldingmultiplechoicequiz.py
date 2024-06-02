#creating a question array

#from multiprocessing.connection import answer_challenge


questions_prompt = [
    "1. who is the hero in the Bahubali \n\n (a)Rana (b)Prabhas (c)Yash \n\n",
    "2. who is the president for India \n\n (a)Droupadi Murmu (b) Ramnath kovind (c) Narendra Modi \n\n",
    "3. who is the Chief Minister of Telangana State \n\n (a)K ChandraSekar Rao (b)A Revanth Reddy (c)Bhatti Vikramarka \n\n"
]


#from questionclass import question
# here defining question class(datatype)
class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
#now creating one more array
questions = [
    question(questions_prompt[0], "b"),
    question(questions_prompt[1], "a"),
    question(questions_prompt[2], "b")
]
    
#defining a funtion to run the test
def test_run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("you got " + str(score) + "/" + str(len(questions)) + " are correct")

test_run(questions)
        