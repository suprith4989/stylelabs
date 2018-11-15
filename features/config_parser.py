""" Parser for settings.yml """
  
import os
import sys

import yaml

try:
    environment = 'development'
    # Read yaml file
    file_path = os.path.join(os.getcwd(), 'config', 'settings.yml')

    with open(file_path) as file_obj:
        file_data = yaml.safe_load(file_obj)
        data = file_data[environment]
        data['development'] = file_data['development']
# TODO write a method to navigate to parents by swim lane
# TODO we might as well can flatten the setting.yml with no parennts required

except IOError as e:
        raise e

except Exception as msg:
    print("ERROR: ", msg)
    sys.exit(1)

