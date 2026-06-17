# Функция для расчёта динамики выручки по сравнению с прошлым месяцем
def calculate_trend(current: float, previous: float) -> str:
    change = current - previous
    if change > 0:
        return f"+{change:,.2f} руб. 📈"
    elif change < 0:
        return f"{change:,.2f} руб. 📉"
    return "Без изменений ➡️"


# 1. Сбор данных: запрашиваем выручку за 6 месяцев у пользователя
monthly_revenues = []  # Тип: list (список)
print("--- Ввод данных по выручке за полугодие ---")
for month_num in range(1, 7):
    user_input = float(input(f"Введите выручку за {month_num}-й месяц (руб.): "))
    monthly_revenues.append(user_input)

# 2. Расчёт основных финансовых показателей
total_revenue = sum(monthly_revenues)  # Тип: float
average_revenue = total_revenue / len(monthly_revenues)  # Тип: float
max_revenue = max(monthly_revenues)
min_revenue = min(monthly_revenues)

# 3. Вывод итоговой аналитики на экран
print("\n=== АНАЛИЗ ПРОДАЖ ЗА ПОЛУГОДИЕ ===")
print(f"Общая выручка: {total_revenue:,.2f} руб.")
print(f"Средняя выручка: {average_revenue:,.2f} руб.")
print(f"Лучший месяц: {monthly_revenues.index(max_revenue) + 1}-й ({max_revenue:,.2f} руб.)")
print(f"Худший месяц: {monthly_revenues.index(min_revenue) + 1}-й ({min_revenue:,.2f} руб.)")

# 4. Анализ помесячной динамики в цикле
print("\n--- Динамика к предыдущему периоду ---")
for index in range(1, len(monthly_revenues)):
    trend_result = calculate_trend(monthly_revenues[index], monthly_revenues[index - 1])  # Тип: str
    print(f"Месяц {index + 1} к месяцу {index}: {trend_result}")

 