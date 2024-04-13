money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
balance = money_capital
i = 0
while balance + salary - spend > 0:
    i += 1
    balance += salary - spend
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", i)
