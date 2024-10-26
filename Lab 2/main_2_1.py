salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0


for i in range(1, months+1):
    money_capital += abs(salary-spend)
    percent = spend/100
    spend += percent*(increase*100)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
