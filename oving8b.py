# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:38:47 2021

@author: BinuShaakir
"""

class Quiz:
    def __init__(self, question, alternative, correct_answer):
        self.question = question 
        self.alternative = alternative
        self.correct_answer = correct_answer
        
    def __str__(self):
        resultat=self.question+ "\n Answers\n"
        for tall, svaralternativ in enumerate(self.alternative):
            resultat+= f"{tall} {svaralternativ} \n"
        return resultat
        
    def check_answer(self, user_answer):
        if user_answer == self.correct_answer:
            return True
        else:
            return False
       # def check_answer(self, correct_answer):
       #     for element in correct_answer == correct_answer[1]
       #     if correct_answer == question:
       #         print(correct_anwser: )
     
    



if __name__ == "__main__":
    sp1=Quiz("Which country is best", ["Norway","South Africa","Japan"], 0)
    print(sp1)
    user_answer = int(input("Your answer:"))
    if sp1.check_answer(user_answer)==True:
        print(' correct answer ')
    else:
        print('not correct answer ')
        
    sp2=Quiz("Which country  is most peaceful ", ["Norway","South Africa","Japan"], 1)
    print(sp2)
    user_answer =int(input("your answer:"))
    if sp2.check_answer(user_answer)==True:
        print('correct answer')
    else:
        print(' not correct answer')
    
    

    
    