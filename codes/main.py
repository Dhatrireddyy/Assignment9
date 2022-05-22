# CBSE Probability Grade 12
# Example 33

# Name: Velma Dhatri Reddy
# Roll number: AI21BTECH11030

""" Problem Statement
Coloured balls are distributed in four boxes as shown in the following table. A box is selected at
random and then a ball is randomly drawn from the selected box. The colour of the ball is black,
what is the probability that ball drawn is from the box III?
"""


def main():
    P_1 = 3/18 
    P_2 = 1/4 
    P_3 = 1/7  
    P_4 = 4/13
    P = 1/4 

    #Output
    print(f"The probability that ball drawn is from the box III is {Prob(P_1,P_2,P_3,P_4,P)}")

         
def Prob(P_1,P_2,P_3,P_4,P) -> float:
        """ Returns the probability that student is a hostler if he gets an A grade """
        return P*P_3/ P*P_1 + P*P_2 + P*P_3 + P*P_4

if __name__ == '__main__':
       main()
