import sys
from pathlib import Path


class KiloNum:
    def __init__(self, value, round_val=None):
        if any([isinstance(value, float), isinstance(value, int)]):
            if round_val is None:
                round_val = 3
            self.round_val = round_val
            self.value = value
            self.kilo = self.make_value(3)
            self.mega = self.make_value(6)
            self.giga = self.make_value(9)

    def make_value(self, key):
        numbers = {3: 'K',
                   6: 'M',
                   9: 'G'}
        return ''.join([str(round(self.value / 10 ** key, self.round_val)), numbers[key]])

    def __repr__(self):
        return f'{myvalue.kilo},\n{myvalue.mega},\n{myvalue.giga}'


myvalue = KiloNum(34500101112)
print(myvalue)
print(myvalue.giga)
my_root = Path(sys.argv[0]).parent
print(my_root)
