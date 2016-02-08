import itertools


class FSM(object):
    """
    Finite states are stored in dictionary states_dict as:
    [key=current_state]:[(message, prev_state, end_state)]
    """

    def __init__(self, init_state, states_dict):
        super(FSM, self).__init__()
        self.state = init_state
        self.prev_state = ''

        message_list = list(set((itertools.chain(
            *[[message[0] for message in states_dict[state]] for state in states_dict.keys()]))))
        self.message_list = message_list
        self.states_dict = states_dict
        self.current_message = None

    def handle_message(self, message):
        if message in self.message_list:
            self.current_message = message
            print('\nGot message {} \n'.format(self.current_message))
            self.update()
            return 0
        else:
            raise ValueError('This message is not in allowed messages')

    def update(self):
        for i in range(len(self.states_dict[self.state])):
            # print(self.states_dict[self.state][i])
            case = self.states_dict[self.state][i]
            p_state = self.prev_state
            # print(case)
            if self.current_message == case[0] and (case[1] == p_state or case[1] == None):
                # print('New state {}, Current state: {}, Prev state: {}'.
                      # format(case[2], self.state, self.prev_state))
                #print('AAAAAAAA        ' + case[2])
                self.prev_state = self.state
                self.state = case[2]
                return 0

    def get_state(self):
        return self.state

    def get_prev_state(self):
        return self.prev_state


#############################################################
print('OVER \n \n \n \n')
state_l = {}
state_l['Going'] = [('Go', None, 'Going'), ('Stop', None,
                                            'Staying'), ('Jump', None, 'Jumping')]
state_l['Staying'] = [
    ('Go', None, 'Going'), ('Stop', None, 'Staying'), ('Jump', None, 'Jumping')]
state_l['Jumping'] = [
    ('Go', None, 'Going'), ('Jump', 'Jumping', 'Staying'), ('Jump', 'Going', 'Jumping')]

b = FSM('Staying', state_l)

b.handle_message('Go')
#print('Current state: ' + b.state)
#print('Prev state: ' + b.prev_state)
b.handle_message('Jump')
#print('Current state: ' + b.state)
#print('Prev state: ' + b.prev_state)
b.handle_message('Jump')
#print('Current state: ' + b.state)
#print('Prev state: ' + b.prev_state)
b.handle_message('Jump')
#print('Current state: ' + b.state)
#print('Prev state: ' + b.prev_state)
