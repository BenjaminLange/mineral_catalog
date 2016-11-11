import os

from urllib import parse


def rename():
    images_dir = os.path.join(os.getcwd(), 'minerals/static/images')
    print(images_dir)
    for filename in os.listdir(images_dir):
        os.rename(os.path.join(images_dir, filename),
                  parse.unquote(os.path.join(images_dir, filename)))


if __name__ == '__main__':
    rename()
