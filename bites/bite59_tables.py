#!/usr/bin/env python3
# https://codechalleng.es/bites/59/


class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.calc_list = [0]
        for x in range(1, length + 1):
            self.calc_list.append([])
        for x in range(1, length + 1):
            for y in range(1, length + 1):
                self.calc_list[x].append(x*y)
        return

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        length = len(self.calc_list) - 1
        return length * length

    def __str__(self):
        """Returns a string representation of the table"""
        table_str = ""
        for x in range(1, len(self.calc_list)):
            table_str =  table_str +  ' | '.join(map(str, self.calc_list[x])) + '\n'
        return table_str

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        return self.calc_list[x][y - 1]

if __name__ == '__main__':
    multi = MultiplicationTable(3)
    print(len(multi))
    print(str(multi))
    print(multi.calc_cell(1, 1))
    print(multi.calc_cell(2, 2))
    print(multi.calc_cell(2, 3))
