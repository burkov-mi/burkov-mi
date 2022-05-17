# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def roman_to_int(self, string):
        dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        num = 0
        flag = False
        for s in range(0, len(string)):
            if flag:
                temp = string[s-1] + string[s]
                num += dict[temp]
                flag = False
            elif s == (len(string) - 1) or dict[string[s]] >= dict[string[s + 1]]:
                num += dict[string[s]]
            else:
                flag = True
        return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(py_solution().roman_to_int('MMCMCM'))
    print(py_solution().roman_to_int('MMCDCDII'))
    print(py_solution().int_to_Roman(1024))
    print(py_solution().int_to_Roman(4000))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
