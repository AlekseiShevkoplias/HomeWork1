import argparse
import json
from LaGame import LaStory

parser = argparse.ArgumentParser(prog='game',
                                 description='Домашнее задание 2')
parser.add_argument('--game',
                    help='new : новая игра, load : загрузить игру')

args = parser.parse_args()

if args.game == 'new':
    print('НАЧАТЬ НОВУЮ ИГРУ')
    gamename = input('Назовите свою игру:')
    inp = '1'
    game = LaStory(gamename)

if args.game == 'load':
    print('ЗАГРУЗИТЬ ИГРУ')
    with open('save.json') as json_file:
        data = json.load(json_file)
    print(f"Название игры: {data['Название']}")
    gamename = data['Название']
    game = LaStory(gamename)
    game.state = data['Текущий этап']
    inp = game.state
    game.progress = data['Прохождение']
    print('Вы были в данных состояниях:')
    print(game.progress)

while not inp == "ВЫЙТИ":
    try:
        state = game.state
        print('\n________________________________________')
        print('Чтобы сохранить игру, напишите СОХРАНИТЬ')
        print('Чтобы закончить игру, напишите ВЫЙТИ')
        print('Чтобы вернуться в первое состояние, напишите СБРОС')
        print('________________________________________\n')
        print(f'Текущее состояние: {state}')
        print(f'Доступные состояния: {game.transdict[int(state)]}')
        inp = input().upper()
        if inp == 'СОХРАНИТЬ':
            save = {'Название': game.name,
                    'Прохождение': game.progress,
                    'Текущий этап': game.state}
            with open('save.json', 'w') as saving:
                json.dump(save, saving, ensure_ascii=False)
            print(f'Игра {game.name} сохранена')

        if inp == 'СБРОС':
            game.restart()

        if inp in game.states:
            f = getattr(game, f"{state}_to_{inp}")
            f()

    except:
        print('Что-то пошло не так!')