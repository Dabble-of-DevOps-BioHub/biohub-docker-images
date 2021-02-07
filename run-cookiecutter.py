#!/usr/bin/env python

from cookiecutter.main import cookiecutter
import os
import json
import shutil

TEMPLATE = os.path.dirname(os.path.realpath(__file__))
TEMPLATE = os.path.join(TEMPLATE, 'templates')

with open('templates/cookiecutter.json', 'r') as reader:
    data = json.load(reader)

for pangeo_version in data['pangeo_versions']:

    data['pangeo_notebook_version'] = pangeo_version

    cookiecutter(
        TEMPLATE,  # path/url to cookiecutter template
        overwrite_if_exists=False,
        extra_context=data,
        output_dir='biohub-docker-images',
        no_input=True
    )
