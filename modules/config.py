#!/usr/bin/env python3
"""Module for configuration variables."""

# Standard
import os
# External
import yaml


# Read YAML config file
with open('config.yml', encoding='utf-8') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

# Assign variables
SITE_NAME = cfg.get('site_name', 'site_name')
CSS_PATH = cfg.get('css_path', 'inc/style.css')
PUBLISH_DIR = cfg.get('publish_dir', 'public/')
TEMPLATES_DIR = cfg.get('templates_dir', 'templates/')

MENU = cfg.get('menu', '')

# Make directories if they don't exist
for path in [PUBLISH_DIR, TEMPLATES_DIR]:
    if not os.path.isdir(path):
        os.makedirs(path)
