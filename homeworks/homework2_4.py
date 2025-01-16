from ursina import *

# Инициализация приложения
app = Ursina()

# Создание куба
cube = Entity(model='cube', color=color.azure, scale=(1, 1, 1))

# Функция обновления, вызываемая каждый кадр
def update():
    # Управление движением куба
    if held_keys['w']:  # Движение вперед
        cube.position += (0, 0.1, 0)
    if held_keys['s']:  # Движение назад
        cube.position += (0, -0.1, 0.1)
    if held_keys['a']:  # Движение влево
        cube.position += (-0.1, 0, 0)
    if held_keys['d']:  # Движение вправо
        cube.position += (0.1, 0, 0)

    if held_keys['q']:  # Вращение влево
        cube.rotation_y += 2  # Увеличение угла
    if held_keys['e']:  # Вращение вправо
        cube.rotation_y -= 2  # Уменьшение угла

    # Вращение на других осях
    if held_keys['z']:  # Вращение вокруг оси Z
        cube.rotation_z += 2
    if held_keys['x']:  # Вращение вокруг оси X
        cube.rotation_x += 2

# Запуск приложения
app.run()
