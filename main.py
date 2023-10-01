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

if __name__ == '__main__':
    myvalue = KiloNum(34500101112)
    print(myvalue)
    print()
    print(myvalue.giga)
