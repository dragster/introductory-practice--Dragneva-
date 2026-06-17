# =====================================================================
# 1. РАСЧЁТ НДС (Параметры по умолчанию)
# =====================================================================
def calculate_vat(price: float, vat_rate: float = 20.0) -> float:
    """Принимает цену и ставку НДС в процентах (по умолчанию 20%).
    Возвращает сумму налога.
    """
    return price * (vat_rate / 100)


print("--- 1. Функция calculate_vat() ---")
item_price = 10000.0

# Вызов со стандартной ставкой (20%)
vat_default = calculate_vat(item_price)
print(f"Цена: {item_price} руб. НДС (стандартный 20%): {vat_default:.2f} руб.")

# Вызов с явной ставкой (например, льготная ставка 10%)
vat_custom = calculate_vat(item_price, vat_rate=10.0)
print(f"Цена: {item_price} руб. НДС (явный 10%): {vat_custom:.2f} руб.")
print()


# =====================================================================
# 2. СЛОЖНЫЙ ПРОЦЕНТ (Расчет на разный срок)
# =====================================================================
def compound_interest(capital: float, interest_rate: float, years: int) -> float:
    """Принимает начальный капитал, годовую ставку (%) и срок в годах.
    Возвращает итоговую сумму на счете.
    """
    interest_coefficient = interest_rate / 100
    return capital * ((1 + interest_coefficient) ** years)


print("--- 2. Функция compound_interest() ---")
start_capital = 100000.0
annual_rate = 12.0  # 12% годовых

# Выводим результаты для 3, 5 и 10 лет с помощью цикла
for period in [3, 5, 10]:
    final_amount = compound_interest(start_capital, annual_rate, period)
    print(f"Срок {period:2d} лет | Итоговая сумма: {final_amount:,.2f} руб.")
print()


# =====================================================================
# 3. КОНВЕРТЕР ВАЛЮТ (Условная логика внутри функции)
# =====================================================================
def currency_convert(amount: float, exchange_rate: float, direction: str) -> float:
    """Конвертирует сумму по курсу в зависимости от направления ('to_usd' или 'to_rub')."""
    if direction == "to_usd":
        return amount / exchange_rate
    elif direction == "to_rub":
        return amount * exchange_rate
    else:
        print("Ошибка: Неверное направление конвертации!")
        return 0.0


print("--- 3. Функция currency_convert() ---")
current_rate = 92.5
money_amount = 50000.0

# Перевод рублей в доллары
usd_result = currency_convert(money_amount, current_rate, direction="to_usd")
print(f"{money_amount:,.2f} руб. по курсу {current_rate} -> {usd_result:,.2f} USD")

# Перевод долларов обратно в рубли
usd_to_exchange = 500.0
rub_result = currency_convert(usd_to_exchange, current_rate, direction="to_rub")
print(f"{usd_to_exchange:,.2f} USD по курсу {current_rate} -> {rub_result:,.2f} руб.")
print()


# =====================================================================
# 4. СРОК ОКУПАЕМОСТИ (Обработка исключительных ситуаций)
# =====================================================================
def payback_period(investment: float, annual_profit: float):
    """Принимает объем инвестиций и годовую прибыль.
    Возвращает срок окупаемости (float) или None, если проект не окупается.
    """
    if annual_profit <= 0:
        return None
    return investment / annual_profit


print("--- 4. Функция payback_period() ---")
initial_investment = 500000.0

# Случай 1: Проект приносит прибыль
profit_positive = 125000.0
period_1 = payback_period(initial_investment, profit_positive)
if period_1 is not None:
    print(f"Инвестиции: {initial_investment} руб., Прибыль: {profit_positive} руб./год.")
    print(f"Срок окупаемости: {period_1:.1f} лет.")
else:
    print("Проект не окупается (прибыль отсутствует или отрицательная).")

# Случай 2: Проект работает в убыток или ноль
profit_negative = -10000.0
period_2 = payback_period(initial_investment, profit_negative)
if period_2 is not None:
    print(f"Срок окупаемости: {period_2:.1f} лет.")
else:
    print(f"Инвестиции: {initial_investment} руб., Прибыль: {profit_negative} руб./год.")
    print("Результат: Проект никогда не окупится!")
print()


# =====================================================================
# 5. ВЗАИМОДЕЙСТВИЕ ФУНКЦИЙ (Сбор данных + анализ списка)
# =====================================================================
def get_revenues(count: int) -> list:
    """Запрашивает у пользователя `count` значений выручки и возвращает их списком."""
    revenue_list = []
    print(f"Введите выручку за {count} периодов:")
    for i in range(1, count + 1):
        value = float(input(f"Период {i}: "))
        revenue_list.append(value)
    return revenue_list


def analyze(data: list) -> tuple:
    """Принимает список чисел. Возвращает кортеж: (минимум, максимум, среднее)."""
    if not data:  # Проверка на пустой список
        return 0.0, 0.0, 0.0

    minimum_value = min(data)
    maximum_value = max(data)
    average_value = sum(data) / len(data)
    return minimum_value, maximum_value, average_value


print("--- 5. Взаимодействие get_revenues() и analyze() ---")
# Шаг 1: Собираем данные (запросим данные за 3 месяца)
months_count = 3
collected_revenues = get_revenues(months_count)

# Шаг 2: Анализируем собранный список
min_rev, max_rev, avg_rev = analyze(collected_revenues)

# Шаг 3: Выводим результаты анализа
print("\n--- Результаты анализа выручки ---")
print(f"Введенный список: {collected_revenues}")
print(f"Минимум : {min_rev:,.2f} руб.")
print(f"Максимум: {max_rev:,.2f} руб.")
print(f"Среднее : {avg_rev:,.2f} руб.")
