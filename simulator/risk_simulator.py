import random
from typing import Tuple


class Dice:

    def __init__(self):
        pass

    @classmethod
    def roll(cls):
        return random.randint(1, 6)


class Battle:

    def __init__(self, attack_armies, defender_armies, debug=False):
        self._attack_armies = attack_armies
        self._defender_armies = defender_armies
        self._debug = debug

    @staticmethod
    def battle_outcome(attacker_num: int, defender_num: int, debug=False) -> Tuple:
        attacker_dices = []
        defender_dices = []
        att_wins = 0
        def_wins = 0

        for at in range(min(3, attacker_num - 1)):
            attacker_dices.append(Dice.roll())

        for de in range(min(2, defender_num)):
            defender_dices.append(Dice.roll())

        attacker_dices.sort(reverse=True)
        defender_dices.sort(reverse=True)
        if debug:
            print(f"attacker: {attacker_dices}, defender: {defender_dices}")
        for i in range(0, min(len(defender_dices), len(attacker_dices))):
            if attacker_dices[i] > defender_dices[i]:
                att_wins += 1
            else:
                def_wins += 1
        return att_wins, def_wins

    def recalculate_armies(self, attacker_wins, defender_wins):
        self._attack_armies -= defender_wins
        self._defender_armies -= attacker_wins

    def simulate(self):
        result = False
        while self._defender_armies > 0 and self._attack_armies > 1:
            print(self._attack_armies, self._defender_armies) if self._debug else None
            att_wins, def_wins = Battle.battle_outcome(self._attack_armies, self._defender_armies, self._debug)
            print(att_wins, def_wins) if self._debug else None
            self.recalculate_armies(att_wins, def_wins)
            print("---") if self._debug else None
        if self._attack_armies > self._defender_armies:
            result = True
            msg = "Attacker wins!"
        else:
            result = False
            msg = "Defender wins!"
        if self._debug:
            print(f"attacker armies: {self._attack_armies}, defender armies: {self._defender_armies}, {msg}")
        return result


class BattleSimulator:

    def __init__(self):
        pass

    @staticmethod
    def simulate(num_battles, attacker_armies, defender_armies, debug=False):
        attacker_wins = 0
        defender_wins = 0
        for index in range(num_battles):
            print(f"Attacker: {attacker_armies}, Defender: {defender_armies}") if debug else None
            battle = Battle(attacker_armies, defender_armies, debug)
            if battle.simulate():
                attacker_wins += 1
            else:
                defender_wins += 1
        return attacker_wins, defender_wins

    @staticmethod
    def required_attack_army(defender_army, win_probability, num_battles=10000):
        attacker_temp = 2
        percentage = 0.0
        while percentage < win_probability:
            attack, defend = BattleSimulator.simulate(num_battles, attacker_temp, defender_army)
            percentage = attack / num_battles
            attacker_temp += 1
        return attacker_temp - 1

    @staticmethod
    def required_defense_army(attacker_army, win_probability, num_battles=10000):
        defender_temp = 1
        percentage = 0.0
        while percentage < win_probability:
            attack, defend = BattleSimulator.simulate(num_battles, attacker_army, defender_temp)
            percentage = defend / num_battles
            defender_temp += 1
        return defender_temp - 1

    @staticmethod
    def all_battle_combinations(attacker_army_range, defender_army_range, by_attacker=True, win_probability=0.0,
                                num_battles=10000):
        if type(attacker_army_range) == int:
            attacker_range = (attacker_army_range, attacker_army_range+1)
        else:
            attacker_range = (max(2, attacker_army_range[0]), attacker_army_range[1]+1)
            print(attacker_range)
        if type(defender_army_range) == int:
            defender_range = (defender_army_range, defender_army_range+1)
        else:
            defender_range = (max(1, defender_army_range[0]), defender_army_range[1]+1)
            print(defender_range)

            print('Attack Defense Probability')

        for i in range(*attacker_range):
            for j in range(*defender_range):
                attack, defend = BattleSimulator.simulate(num_battles, i, j)
                if by_attacker:
                    percentage = attack / num_battles
                else:
                    percentage = defend / num_battles
                if percentage >= win_probability:
                    print(i, j, percentage)


def main():
    BattleSimulator.all_battle_combinations((2, 20), (1, 20), False)


if __name__ == "__main__":
    main()
