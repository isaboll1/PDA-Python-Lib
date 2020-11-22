# Pushdown Automata Python Library

This is a library which implements pushdown automata within python 3.

usage would be implemented like this:

```
from pda import PDA

pda = PDA(
    states = {'Q0', 'Q1', 'Q2', 'Q3'},
    input_alphabet = {'a', 'b'},
    stack_alphabet = {'a', 'Z'},
    transitions = {
        ('Q0', 'a', 'Z'):('Q1', 'aZ'),
        ('Q0', ' ', 'Z'):('Q3', 'Z'),
        ('Q1', 'b', 'a'):('Q2', ' '),
        ('Q1', 'a', 'a'):('Q2', 'aa'),
        ('Q2', 'b', 'Z'):('Q3', 'Z'),
        ('Q2', 'b', 'a'):('Q2', ' '),
        ('Q2', ' ', 'Z'):('Q3', 'Z'),
        ('Q3', 'b', 'Z'):('Q3', 'Z'),
    },
    initial_state='Q0',
    initial_stack_symbol='Z',
    final_states={'Q3'},
)
```

The transitions dictionary uses two tuples, with the first one as the key being utilized in the format of the state that's expected, the input being checked, and what is popped from the stack. the result gives you the state to transition, and the inputs that are being pushed to the stack instead.

To read inputs, you can use the method "accepts_inputs": here's and example:

```
strings = ['b', '',  "aaaab", 'abbbb', 'aaaaabbbbb', 'aaabbbbb']
for string in strings:
    if pda.accepts_input(string):
        print(string+':', 'accepted')
    else:
        print(string+':', 'rejected')
```

Further documentation is provided throught the library directly.