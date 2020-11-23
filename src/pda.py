# created by isaboll1

class PDA:
    # states (Set): a set of all the states that are to be used in the PDA.
    # input_alphabet (Set): a set that contains the inputs that are to be accepted by the input alphabet.
    # stack_alphabet (Set): a set that contains the stack symbols used by the PDA.
    # transitions (Dict){Key: Tuple(state: str, input_char: str, stack_popped: str), Value: Tuple(state: str, stack_pushed: str)}: a dictionary with tuples representing the transition table of the PDA, by the format specified.
    # initial_state (str): a string that represents the state that is the initial state of the PDA.
    # initial_stack_symbol (str): a string that represents the initial alphabet symbol within the stack.
    # final_states (Set): a set that contains all of the final states that are accepted by the PDA.
    def __init__(self,  states: set,
                        input_alphabet: set,
                        stack_alphabet: set,
                        transitions: dict,
                        initial_state: str,
                        initial_stack_symbol: str,
                        final_states: set):
        self.states = states
        self.input_alphabet = input_alphabet
        self.input_alphabet.add(' ')
        self.stack_alphabet = stack_alphabet
        self.transition_relation = transitions
        self.start_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states

    # transitions states based on what is defined by the "transition_relation" dictionary
    def transition_states(self, input_string: str, current_state: str, stack: list, transition_list: list = []):
        next_state = current_state
        if (len(input_string)):
            input_char = input_string[0]
            stack_symbol = stack[-1]
            if (current_state in self.states) and (input_char in self.input_alphabet):
                transition_key = (current_state, input_char, stack_symbol)
                if self.transition_relation.get(transition_key, None) != None:
                    stack.pop()
                    state_and_stack_char = self.transition_relation[transition_key]
                    next_state = state_and_stack_char[0]
                    for symbol in state_and_stack_char[1][::-1]:
                        if symbol in self.stack_alphabet and symbol != ' ':
                            stack.append(symbol)
                    transition_string = "("+current_state+','+input_char+','+stack_symbol+")"+":"+"("+state_and_stack_char[0]+','+state_and_stack_char[1]+")"
                    transition_list.append((transition_string, next_state +'|'+ ''.join(stack[::-1])))
                else:
                    transition_list.append(('', current_state))
                    return (current_state, transition_list)
                return self.transition_states(input_string[1:], next_state, stack, transition_list)
        return self.transition_states(" ", next_state, stack, transition_list)

    # returns (str):  reads the input and returns the final state that the PDA finished on.
    def read_input(self, input_string: str):
        stack = []
        transition_list = []
        stack.append(self.initial_stack_symbol)
        transition_list.append((input_string, stack))
        state = self.start_state
        finished_state = self.transition_states(input_string, state, stack, transition_list)[0]
        return finished_state

    
    # returns (lst)[tuple]:  reads the input and returns a list of the transitions taken stepwise.
    def read_input_stepwise(self, input_string: str):
        stack = []
        transition_list = []
        stack.append(self.initial_stack_symbol)
        transition_list.append((input_string, stack))
        state = self.start_state
        transitions_taken = self.transition_states(input_string, state, stack, transition_list)[1]
        return transitions_taken

    # returns (boolean): checks to see if input is accepted by the PDA.
    def accepts_input(self, input_string: str):
        ended_state = self.read_input(input_string)
        if ended_state in self.final_states:
            return True
        return False
    
     






