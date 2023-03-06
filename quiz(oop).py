#question
class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, answer):
        return self.answer == answer
#quiz
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input("Answer: " )
        self.quess(answer)
        self.loadQuestion()

    def quess(self, answer):
        question = self.getQuestion()
        if question.check_answer(answer):
             self.score += 1
        self.questionIndex += 1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
         print(f"Score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz is over")
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(80,'*'))

q1 = Question('Which one is the best programming language ?', ['C#','Python','Java','Javascript'],'Python')
q2 = Question('which one is the most popular programming language ?', ['C#','Python','Java','Javascript'],'Python')
q3 = Question('Which one is the easiest programming language ?', ['C#','Python','Java','Javascript'],'Python')
q4 = Question('Which one is the most useful programming language ?', ['C#','Python','Java','Javascript'],'Python')

questions = [q1, q2, q3, q4]

quiz = Quiz(questions)

quiz.loadQuestion()