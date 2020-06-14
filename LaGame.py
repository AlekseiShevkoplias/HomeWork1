import json
from transitions import Machine


class LaStory(object):

    transdict = {
        1: [2, 3, 4],
        2: [5, 6, 3],
        3: [6, 7],
        4: [8, 9],
        5: [7, 30],
        6: [10, 11],
        7: [12, 13, 14],
        8: [15, 12, 22, 5],
        9: [17, 16],
        10: [3, 29],
        11: [],
        12: [6, 8],
        13: [18, 2, 15],
        14: [25, 27, 28, 4],
        15: [],
        16: [18, 23],
        17: [22, 24, 27],
        18: [19, 22],
        19: [20, 21],
        20: [4, 5, 6, 7, 8],
        21: [],
        22: [],
        23: [8],
        24: [],
        25: [],
        26: [9, 25],
        27: [8, 17],
        28: [],
        29: [3],
        30: []
    }

    states = ['1', '2', '3', '4', '5',
              '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20',
              '21', '22', '23', '24', '25',
              '26', '27', '28', '29', '30']

    progress = []

    def __init__(self, name):
        self.start()
        self.name = name
        self.machine = Machine(model=self, states=LaStory.states,
                               initial='1')

        for state in self.states:
            self.machine.add_transition(
                trigger=f"restart",
                source=state,
                dest='1',
                before='bye'
            )
            for dest in self.transdict[int(state)]:
                self.machine.add_transition(
                    trigger=f"{state}_to_{dest}",
                    source=state,
                    dest=str(dest),
                    before='bye',
                    after='hello'
                )   

    def start(self):
        print('start')

    def bye(self):
        print(f'Выхожу из состояния {self.state}')

    def hello(self):
        self.progress.append(self.state)
        print(f'Вхожу в состояние {self.state}')
