
# from .production import *

try:
    from .local import *
except:
    pass

# try:
#     from .vercel_settings import *  # PG ADMIN 4
# except:
#     pass
