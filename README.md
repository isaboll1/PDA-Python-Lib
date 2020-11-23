# Pushdown Automata Python Library

This is a library which implements pushdown automata within python 3.

usage would be implemented like this:

```python
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

To read inputs, you can use the method "accepts_inputs": here's an example:

```python
strings = ['b', '',  "aaaab", 'abbbb', 'aaaaabbbbb', 'aaabbbbb']
for string in strings:
    if pda.accepts_input(string):
        print(string+':', 'accepted')
    else:
        print(string+':', 'rejected')
```

You can read inputs in a stepwise manner to see how the stack changes on each step from transtitons through the PDA, as well as the state that you end up on from the transition.

To do this, use the "read_input_stepwise" method in the library. For example, using the PDA from the last example, if we were to call
```python
strings = ['aabbb']
for string in strings:
    stepwise = pda.read_input_stepwise(string)
    for steps in stepwise:
        print(steps)
    print('\n')
```
The result would be this
```python
"""
('aabbb', ['Z'])
('(Q0,a,Z):(Q1,aZ)', 'Q1|aZ')
('(Q1,a,a):(Q2,aa)', 'Q2|aaZ')
('(Q2,b,a):(Q2, )', 'Q2|aZ')
('(Q2,b,a):(Q2, )', 'Q2|Z')
('(Q2,b,Z):(Q3,Z)', 'Q3|Z')
('', 'Q3')
"""
```

looking at the second result from the list, what the syntax means is that from the transtion (Q0, a, Z):(Q1, aZ), the state that transition returns is "Q1", and the stack from the result of the transition is "aZ" (or ['a', 'Z']).


The "λ" symbol typically utilized for PDA is represented by an open space " ". 

Further documentation is provided through comments in the library.