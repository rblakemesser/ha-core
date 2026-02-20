"""Constants for rainbird."""

DOMAIN = "rainbird"
MANUFACTURER = "Rain Bird"
DEFAULT_TRIGGER_TIME_MINUTES = 6

CONF_SERIAL_NUMBER = "serial_number"
CONF_IMPORTED_NAMES = "imported_names"

ATTR_DURATION = "duration"

TIMEOUT_SECONDS = 20

# Schedule fetching requires many sequential device RPCs and can take longer than
# simple status polling, especially on first load.
SCHEDULE_TIMEOUT_SECONDS = 60
