import os.path
import config

abs_path_data = config.path_data if os.path.isabs(config.path_data) else config.path+config.path_data

print 'path_data', abs_path_data
