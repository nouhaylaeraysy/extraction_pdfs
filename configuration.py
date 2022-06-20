
from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()



    #Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")   

#Get the password


def getConfigBySection(section,keye):
    try:
        value = config_object.get(section, keye)
        return value
    except ConfigParser.NoOptionError:
        return 0

    





