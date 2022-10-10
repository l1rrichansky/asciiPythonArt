from PIL import Image, ImageEnhance
import os


def get_b(p):
    r, g, b = p
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


k = int(input('width: '))
name = input('name: ')
attempts = int(input('attempts: '))
x = int(input('x: '))
characters = """¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,'.` """


with Image.open('image.jpg') as image:

    if os.path.exists(f"arts/{name}"):
        pass
    else:
        os.mkdir(f"arts/{name}")
        os.mkdir(f"arts/{name}/images")
        os.mkdir(f"arts/{name}/results")

    image.save(f'arts/{name}/images/orig {name}.png')
    enhancer = ImageEnhance.Contrast(image)

    for h in range(attempts):
        enh_image = enhancer.enhance(h+1)
        resized_image = enh_image.resize((k, image.height//(image.width//k)))
        px = resized_image.load()

        with open(f"arts/{name}/results/c{h+1} w{k} {name} x{x}.txt", "w", encoding="utf-8") as t:
            for i in range(resized_image.height):
                for j in range(resized_image.width):
                    y = get_b(px[j, i])
                    t.write(characters[int(y//(255/len(characters)))]*x)
                t.write("\n")
        enh_image.save(f'arts/{name}/images/c{h+1} w{k} {name}.png')

    print('\nDone')
    print(f'\nResults saved in arts/{name}')
