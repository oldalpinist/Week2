def discounted(price, discount, max_discount=30, phone_name=""):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError or TypeError:
        print("Неправельное значение - выбери целое число")
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif "iphone" in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)

new_price = discounted(input(), 10, phone_name='iPhone 12')
print(new_price)


# Домашнее задание №1
# Исключения: приведение типов
# * Перепишите функцию discounted(price, discount, max_discount=20)
# из урока про функции так, чтобы она перехватывала исключения,
# когда переданы некорректные аргументы.
# * Первые два нужно приводить к вещественному числу при помощи float(),
# а третий - к целому при помощи int() и перехватывать исключения
# ValueError и TypeError, если приведение типов не сработало.

# """
