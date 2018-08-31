# -*- coding: utf-8 -*-
import os

if os.getenv('FLASK_CONFIG', 'prod') != 'prod':
    from .dev_settings import DevelopmentConfig as Config  # noqa: F401
else:
    from .prod_settings import ProductionConfig as Config  # noqa: F401
