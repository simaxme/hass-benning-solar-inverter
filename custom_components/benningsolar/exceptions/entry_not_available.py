
from homeassistant.exceptions import HomeAssistantError

class EntryNotAvailable(HomeAssistantError):
    """Error to indicate that a specified entry from the inverter is not available."""
