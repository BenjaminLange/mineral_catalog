import json
import os
import sys
from urllib import parse

from minerals.models import Mineral


def seed(json_filename):
    if not os.path.isfile(json_filename):
        print('{} not found! Please check your file path.'
              .format(json_filename))
    attributes = [
        'name',
        'image filename',
        'image caption',
        'category',
        'formula',
        'strunz classification',
        'crystal system',
        'unit cell',
        'color',
        'crystal symmetry',
        'cleavage',
        'mohs scale hardness',
        'luster',
        'streak',
        'diaphaneity',
        'optical properties',
        'refractive index',
        'crystal habit',
        'specific gravity',
    ]
    with open(json_filename) as json_file:
        mineral_data = json.load(json_file)
        for mineral in mineral_data:
            new_mineral = {}
            for item in attributes:
                if item in mineral.keys():
                    model_item = item.replace(' ', '_')
                    if model_item == 'image_filename':
                        mineral[item] = parse.unquote(mineral[item])
                    new_mineral[model_item] = mineral[item]
            Mineral.objects.create(**new_mineral)


if __name__ == '__main__':
    seed(sys.argv[1])
