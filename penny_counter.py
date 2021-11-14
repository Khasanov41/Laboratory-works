"""
penny_counter.py

Переводит количество копеек в рубли и выводит строки вида:
    <кол-во рублей> РУБЛЕЙ(-ЛЯ, ЛЬ)
    <кол-во копеек> КОПЕЕК(-КА, -КИ).

(c)Хасанов Ислам, КЭ-101
"""


def ruble_word(rubles):
    word = str(rubles)
    if word[-1] == '1':
        return 'РУБЛЬ'
    elif word[-1] == '2':
        return 'РУБЛЯ'
    else:
        return 'РУБЛЕЙ'


def penny_word(penny):
    word = str(penny)
    if word[-1] == '1':
        return 'КОПЕЙКА'
    elif word[-1] == '2':
        return 'КОПЕЙКИ'
    else:
        return 'КОПЕЕК'


def convert_penny_to_rubles(penny):
    """
    Convert pennies to rubles.
    Input:  penny - penny number (int)
    Output: rubles - rubles number (int)
            penny - penny number (int)
    """
    rubles = penny // 100
    penny_reminder = penny % 100

    return rubles, penny_reminder


def get_result(rubles, penny):
    penny_ruble_phrase = ""
    if rubles:
        penny_ruble_phrase += f"{rubles} {ruble_word(rubles)}\n"
    if penny:
        penny_ruble_phrase += f"{penny} {penny_word(penny)}"
    return penny_ruble_phrase


if __name__ == "__main__":

    # Uncomment to get the tests
    # tests = (13413, 100000, 0, 2, 1, 99999, 100)
    # for test in tests:
    #     rub, pen = convert_penny_to_rubles(test)
    #     print(get_result(rub, pen))

    rubles_input, penny_input = convert_penny_to_rubles(int(input("Enter penny number: ")))
    print(get_result(rubles_input, penny_input))
