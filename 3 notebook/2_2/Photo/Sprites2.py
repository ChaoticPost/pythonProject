from PIL import Image
import random
import matplotlib.pyplot as plt

SPRITE_SIZE = 5
SPRITE_SPACING = 1  # расстояние между спрайтами
MAP_SIZE = 50
SPRITES_PER_ROW = MAP_SIZE // (SPRITE_SIZE )

def generate_random_sprite():
    # Создаем новое черно-белое изображение
    img = Image.new('1', (SPRITE_SIZE, SPRITE_SIZE))

    # Заполняем каждый пиксель случайным значением
    for x in range(SPRITE_SIZE):
        for y in range(SPRITE_SIZE):
            img.putpixel((x, y), random.randint(0, 1))

    # Генерируем случайное число для определения направления оси (0 - горизонтальная, 1 - вертикальная)
    axis = random.randint(0, 1)

    # Копируем верхнюю половину изображения в нижнюю с помощью свойства симметрии
    if axis == 0:
        for x in range(SPRITE_SIZE):
            for y in range(SPRITE_SIZE // 2, SPRITE_SIZE):
                pixel_value = img.getpixel((x, y - SPRITE_SIZE // 2))
                img.putpixel((x, y), pixel_value)
    elif axis == 1:
        for x in range(SPRITE_SIZE // 2, SPRITE_SIZE):
            for y in range(SPRITE_SIZE):
                pixel_value = img.getpixel((x - SPRITE_SIZE // 2, y))
                img.putpixel((x, y), pixel_value)

    return img

def generate_sprite_map():
    # Вычисляем размеры карты спрайтов с учетом расстояния между спрайтами
    map_width = MAP_SIZE + SPRITES_PER_ROW * SPRITE_SPACING
    map_height = MAP_SIZE + SPRITES_PER_ROW * SPRITE_SPACING

    # Создаем новое черно-белое изображение для карты спрайтов
    map_img = Image.new('1', (map_width, map_height))

    # Генерируем случайные спрайты и добавляем их на карту спрайтов
    for i in range(SPRITES_PER_ROW * SPRITES_PER_ROW):
        sprite = generate_random_sprite()

        # Вычисляем координаты верхнего левого угла для текущего спрайта
        x = (i % SPRITES_PER_ROW) * (SPRITE_SIZE + SPRITE_SPACING) + SPRITE_SPACING
        y = (i // SPRITES_PER_ROW) * (SPRITE_SIZE + SPRITE_SPACING) + SPRITE_SPACING

        map_img.paste(sprite, (x, y))

        # Сохраняем спрайт в отдельный файл
        sprite.save(f'sprite_{i}.png')

    # Сохраняем карту спрайтов в файл
    #map_img.save('sprite_map.png')
    img = Image.open('sprite_map.png')
    plt.imshow(img, cmap='binary')
    plt.show()

generate_sprite_map()
