#!/usr/bin/python3
import Adafruit_DHT
import time
import gettext
import pi_ager_database
import pi_ager_names
from pi_ager_logging import create_logger

global system_starttime
global circulation_air_start
global exhaust_air_start
global uv_starttime
global uv_stoptime
global light_starttime
global light_stoptime
global logger

logger = create_logger(__name__)
logger.debug('logging initialised')

# Function zum Setzen des Sensors
def set_sensortype():
    global sensor
    global sensorname
    global sensorvalue
    global logger

    logger.debug('set_sensortype()')

    if sensortype == 1: #DHT
        sensor = Adafruit_DHT.DHT11
        sensorname = 'DHT11'
        sensorvalue = 1
    elif sensortype == 2: #DHT22
        sensor = Adafruit_DHT.DHT22
        sensorname = 'DHT22'
        sensorvalue = 2
    elif sensortype == 3: #SHT
        #sensor = Adafruit_DHT.AM2302
        sensor = 'SHT'
        sensorname = 'SHT'
        sensorvalue = 3

def set_system_starttime():
    global system_starttime
    global circulation_air_start
    global exhaust_air_start
    global uv_starttime
    global uv_stoptime
    global light_starttime
    global light_stoptime
    global logger

    logger.debug('set_system_starttime()')
    
    system_starttime=int(time.time())
    circulation_air_start = system_starttime
    exhaust_air_start = system_starttime
    uv_starttime = system_starttime
    uv_stoptime = uv_starttime
    light_starttime = system_starttime
    light_stoptime = light_starttime

def set_language():
    global logger
    
    logger.debug('set_language()')
    
    ####   Set up message catalog access
    # translation = gettext.translation('pi_ager', '/var/www/locale', fallback=True)
    # _ = translation.ugettext
    
    if language == 1:
        translation = gettext.translation('pi_ager', '/var/www/locale', languages=['en'], fallback=True)
    elif language == 2:
        translation = gettext.translation('pi_ager', '/var/www/locale', languages=['de'], fallback=True)

    translation.install()

loopcounter = 0                      #  Zaehlt die Durchlaeufe des Mainloops
    
# Sensortyp
sensortype = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.sensortype_key)
# Sprache der Textausgabe
language = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.language_key)
# Einschalttemperatur
switch_on_cooling_compressor = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.switch_on_cooling_compressor_key)
# Ausschalttemperatur
switch_off_cooling_compressor = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.switch_off_cooling_compressor_key)
# Einschaltfeuchte
switch_on_humidifier = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.switch_on_humidifier_key)
# Ausschaltfeuchte
switch_off_humidifier = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.switch_off_humidifier_key)
# Luftbefeuchtungsverzoegerung
delay_humidify = pi_ager_database.get_table_value(pi_ager_names.config_settings_table, pi_ager_names.delay_humidify_key)


# Sprache
set_language()