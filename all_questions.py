import pytest
from all_questions import *
import pickle
import math



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    prob_B_good = 0.9
    prob_F_empty = 0.2
    prob_G_empty_given_B_good_F_empty = 0.8
    prob_S_yes_given_B_good_F_empty = 0.2
    
    prob_part_a = prob_B_good * prob_F_empty * prob_G_empty_given_B_good_F_empty * prob_S_yes_given_B_good_F_empty
    
    answers['(a)'] = prob_part_a

    # type: float
    # Calculate the probability.
    prob_B_bad = 0.1
    prob_F_empty = 0.2
    prob_G_nonempty_given_B_bad_F_empty = 0.9
    prob_S_no_given_B_bad_F_empty = 1
    
    prob_part_b = prob_B_bad * prob_F_empty * prob_G_nonempty_given_B_bad_F_empty * prob_S_no_given_B_bad_F_empty
    
    answers['(b)'] = prob_part_b

    # type: float
    # Calculate the probability.
    # P(S=yes | B=bad) = P(S=yes, B=bad)/P(B=bad)
    prob_s_yes_b_bad = 0.0
    prob_b_bad = 0.1

    prob_part_c = prob_s_yes_b_bad / prob_b_bad

    answers['(c)'] = prob_part_c
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = False

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    alpha = .5 * math.log((1-.3)/.3)
    answers['(c) Weight update'] = alpha

    # type: float
    # the answer should be correct to 3 significant digits
    new_weight = 1 * math.e**alpha
    answers['(d) Weight influence'] = new_weight
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "no"

    # type: explain_string
    answers['Explain'] = "Coin flips are random and have no relationship with the stock markets actual behavior. He isn't learning from the data since there is no consideration of historical data, market trends, or relevant features."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = True

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = 900/1000

    # type: eval_float
    answers['(a) C2-FPR'] = 900/1000

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "yes"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "The line on the ROC curve for C2 starts higher whihc indicates a better classifier."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "TPR/FPR is better because it considers both positive and negative classes and provides a more balanced assessment then precison/recall since precision/recall do not consider the negative classes."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = None

    # type: explain_string
    answers['(i) Best classifier, explain'] = None

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = None

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = None

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = None

    # type: explain_string
    answers['(iii) best classifier, explain'] = None
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    # p = FPR
    p = 900/1000
    
    #precision = TP/(TP+FP)
    precision_C0 = .1 / (.1 + p*.9)
    answers['(a) precision for C0'] = precision_C0

    # type: eval_float
    # recall = TP / (TP+FN)
    recall_C0 = .1 / (.1+.8)
    answers['(a) recall for C0'] = recall_C0

    # type: eval_float
    f_measure_C0 = (2*precision_C0 * recall_C0)/(precision_C0 + recall_C0)
    answers['(b) F-measure of C0'] = f_measure_C0
    print(f_measure_C0)

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = None
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # recall = TP / TP+FN
    recall = 80 / (80+70)
    
    # precision = TP / TP+FP
    precision = 80 / (80+50)
    
    # F-measure = 2*TP / 2*TP+FN+FP
    f_measure = (2*80) / (2*80 + 70 + 50)
    
    # accuracy = TP+TN / TP+FN+FP+TN
    accuracy = 80 + 800 / (80+70+50+800)


    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    
    answers['(i) metrics'] = {
        'recall': recall,
        'precision': precision,
        'F-measure': f_measure,
        'accuracy': accuracy
        }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = None

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = None
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = None

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = None

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = None
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
