## Brief Information
This is a library that implements a determinated finite state machine with one cell stack.
## Using the Library
To use this lib you need to import the file "fsm.py" and than create a new instance of class FSM.
As arguments you should give:
1) Initial state of FSM.
2) A dictionary of states and transitions for each state.
E.g. : 
state_l = {}
state_l['Going'] = [('Go', None, 'Going'), ('Stop', None,
                                            'Staying'), ('Jump', None, 'Jumping')]
state_l['Staying'] = [
    ('Go', None, 'Going'), ('Stop', None, 'Staying'), ('Jump', None, 'Jumping')]
state_l['Jumping'] = [
    ('Go', None, 'Going'), ('Jump', 'Jumping', 'Staying'), ('Jump', 'Going', 'Jumping')]

b = FSM('Staying', state_l)