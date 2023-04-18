start_speed = float(input("Введите начальную скорость в км/ч: "))
end_speed = float(input("Введите конечную скорость в км/ч: "))
time = float(input("Введите время в секундах: "))

acceleration = (end_speed - start_speed) / time

print(f"Ускорение: {acceleration:.2f} км/ч^2")
