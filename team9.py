####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'DillyDilly' # Only 10 chars displayed.
strategy_name = 'Savagery'
strategy_description = 'How does this strategy decide?'
    




    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: 
            return 'c'
    else: 
        if 'b' in their_history[-1:]:
            return 'b'
        else:
            if 'b' in their_history[-3:]: 
                if random.random()<0.75:
                    return 'b'   
                else:
                    return 'c' 
            else:    
                    return 'c'         
            
                    
             