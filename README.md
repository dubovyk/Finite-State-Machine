## Brief Information
This is a library that implements a determinated finite state machine with one cell stack.
## Installation
You don`t need to use any package manager or etc to use this library. You should just import
the fsm.py to your project.
## Using the Library
To use this lib you need create a new instance of class FSM.
As arguments you should give:
1) Initial state of FSM.
2) A dictionary of states and transitions for each state.
E.g. : 
state_l = {}
 \nstate_l['Going'] = [('Go', None, 'Going'), ('Stop', None, 'Staying'), ('Jump', None, 'Jumping')]  \n
state_l['Staying'] = [('Go', None, 'Going'), ('Stop', None, 'Staying'), ('Jump', None, 'Jumping')] \n
state_l['Jumping'] = [('Go', None, 'Going'), ('Jump', 'Jumping', 'Staying'), ('Jump', 'Going', 'Jumping')] \n

 \nfinite_state_machine = FSM('Staying', state_l) \n

This will create a new finite state machine with a table of transactions given in a dictionary.
Each tuple contains three values:
1) Message got by state machine
2) Previous state(before current). If None - this transaction doesn`t depend on previous state, just on current.
3) New state. After setting a new state to current, the state that was current is set to previous state.

To get current state of FSM you can use function fsm.get_state(), and to get previous state you can use
fsm.get_prev_state().

## License
This library can be used under the MIT License.