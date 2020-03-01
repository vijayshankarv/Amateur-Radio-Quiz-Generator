import pandas as pd 
from random import sample

 

class ham_mcq(object):
    """docstring for ham"""
    def __init__(self):
        
        self.num_questions = 10
        return None

    def _read_questions(self):
        """
        Load the questions from the file
        """

        self.ham_df = pd.read_csv('amat_basic_quest_delim.txt',delimiter=';',encoding='latin1')
        
        return None

    def _generate_scores_df(self):
        """
        Create and initialize a dataframe for keeping track of questions and scores per topic
        """
        self.scores_df = self.ham_df['question_id']
        return None


    def build_questions_df(self):
        """
        Ask how many questions in session
        """
        print("How many questions in session?")
        num_questions = int(input())

        self.questions_df = self.ham_df.sample(n=num_questions)
        return None

    def ask_questions(self):
        """
        From a dataframe, generates a shuffled dataframe
        From that 
            
        """
        
        shuffled_df = self.questions_df.sample(n=len(self.questions_df))
        correct = 0
        count = 0
        for index, row in shuffled_df.iterrows():
           print(row['question_id'], row['question_english'])
        
           count += 1
            
           choice_1 = row['correct_answer_english']
           choice_2 = row['incorrect_answer_1_english']
           choice_3 = row['incorrect_answer_2_english']
           choice_4 = row['incorrect_answer_3_english']
            
           choice_list = list(zip([1, 0, 0, 0], [choice_1, choice_2, choice_3, choice_4]))
         
           choices_shuffle = sample(choice_list, len(choice_list))
            
         
           for index, (num, choice) in enumerate(choices_shuffle):
               print("{}. {}".format(index + 1, choice))
         
           
           print("Enter your choice: one of 1, 2, 3, or 4. Enter 5 for exit")
           a = int(input())
         

           if a == 5:
               break
           elif choices_shuffle[a-1][0] == 1:
               correct += 1
               print("Correct answer! ")
               print()
           else: 
               print("Incorrect answer :-( ")
               correct_answer = list(filter(lambda x: x[0] == 1, choices_shuffle))[0][1]   
               print("The correct answer is {}".format(correct_answer))
               print()
    
        print("Quiz done for now")
        print("Got {} question(s) correct from a total of {} question(s)".format(correct, count))
        return None


def main():
    ham_quiz = ham_mcq()

    ham_quiz._read_questions()
    ham_quiz.build_questions_df()
    ham_quiz.ask_questions()
    return None

if __name__ == '__main__':
    main()
