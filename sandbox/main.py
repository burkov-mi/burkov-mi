# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class py_solution:
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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
