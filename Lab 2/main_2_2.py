money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
spend1 = spend

while money_capital>spend1:
    money_capital += salary - spend
    percent = spend/100
    spend += percent*(increase*100)
    months += 1
    
print("Количество месяцев, которое можно протянуть без долгов:", months)