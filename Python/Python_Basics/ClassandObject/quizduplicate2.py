#now lets create question paper in a array

Question_paper = [
    "1. How many planets in our solar system \n\n (a)9 (b)6 (c)8 \n\n",
    "2. Largest planet in our solar system \n\n (a)Jupiter (b)Mercury (c)Mars \n\n",
    "3. Fourth country to step on the moon ? \n\n (a)US (b)Russia (c)India \n\n"
]

#now let create question class

class question:
    def __init__(self, prompt, answer):
       self.prompt = prompt
       self.answer = answer 

#now lets create an array using above create question class

Questions = [
    question(Question_paper[0], "c"),
    question(Question_paper[1], "a"),
    question(Question_paper[2], "c")
]

# now lets create a definition to run this test
def questionpapertestrun(Questions): 
        score = 0
        for question in Questions:        
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("you got " + str(score) + "/" + str(len(Questions)) + " are correct")

questionpapertestrun(Questions)
