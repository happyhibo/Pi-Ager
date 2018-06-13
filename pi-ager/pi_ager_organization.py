#!/usr/bin/python3
"""
    basic functions
    
    
"""
import RPi.GPIO as gpio
import pi_ager_logging
import pi_ager_names
import pi_ager_gpio_config

global logger
logger = pi_ager_logging.create_logger(__name__)
logger.debug('logging initialised')

# Function goodbye
def goodbye():
    """
    last function for clean up system
    """
    global logger
    cleanup()
    logstring = _('goodbye') + '!'
    logger.info(logstring)

# Function cleanup
def cleanup():
    """
    clean up gpio
    """
    global logger
    
    pi_ager_logging.check_website_logfile()
    if pi_ager_gpio_config.gpios_are_in_use:
        logstring = _('running cleanup script') + '...'
        logger.info(logstring)
        gpio.cleanup() # gpio zuruecksetzen
        logstring = _('cleanup complete') + '.'
    else:
        logstring = _('nothing to cleanup') + '!'
    logger.info(logstring)
    logger.info(pi_ager_names.logspacer)