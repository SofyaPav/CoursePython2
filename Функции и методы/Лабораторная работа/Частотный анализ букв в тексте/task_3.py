# TODO  Напишите функцию count_letters
def count_letters(str_name):
    str_name = str_name.lower()
    for i in str_name:
        if not i.isalpha():
            str_name = str_name.replace(i, '')
    set_ = set(str_name)
    dict_ = {}
    for i in set_:
        x = str_name.count(i)
        dict_.update({i: x})
    return dict_

# TODO Напишите функцию calculate_frequency


def calculate_frequency(dict_name):
    len_ = 0
    dict_ = {}
    for i in dict_name.values():
        len_ = len_ + i
    for key_, value_ in dict_name.items():
        frequency = value_/len_
        dict_.update({key_: frequency})
    return dict_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
res_1 = count_letters(main_str)
res_2 = calculate_frequency(res_1)
for key, value in res_2.items():
    print(key, ':', round(value, 2))
