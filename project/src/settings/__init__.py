import os
from .base import *

if os.environ['DJANGO_ENV'] == 'production':
   from .prod import *
else:
   from .dev import *