money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.06  # Ежемесячный рост цен


balance = money_capital
i = 0

# while True:
#     balance += salary - spend
#     spend *= 1 + increase
#     if balance > 0:
#         i += 1
#         print(balance)
#         print(i)
#         continue
#     break

# while balance > 0:
#     balance += salary - spend
#     spend *= 1 + increase
#     if balance > 0:
#         i += 1
#         print(balance)
#         print(i)
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while balance + salary - spend > 0:
    i += 1
    balance += salary - spend
    spend *= 1 + increase
    print(balance)
    print(i)




print("Количество месяцев, которое можно протянуть без долгов:", i)
