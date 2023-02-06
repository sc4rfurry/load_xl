import load_xl
import os

load_xl.load_envi_file('.envi')
print(os.environ['TEST'])
print(os.environ['TEST_ENV'])

# load_xl.read_config_file('.configx')
print(load_xl.read_config_file('.configx'))
print(os.environ['CONFIG_ENV'])