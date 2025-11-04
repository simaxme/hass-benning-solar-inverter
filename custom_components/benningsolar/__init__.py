"""The HASS Benning Solar Inverter Integration integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant


# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
# _PLATFORMS: list[Platform] = [Platform.]

# TODO Create ConfigEntry type alias with API object
# TODO Rename type alias and update all entry annotations
# type New_NameConfigEntry = ConfigEntry[MyApi]  # noqa: F821


# TODO Update entry annotation
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up HASS Benning Solar Inverter Integration from a config entry."""


    # TODO 1. Create API instance
    # TODO 2. Validate the API connection (and authentication)
    # TODO 3. Store an API object for your platforms to access
    # entry.runtime_data = MyAPI(...)

    # hass.config_entries.entry

        # await hass.config_entries.async_add_entities(entry, _PLATFORMS)

    # hass.states.async_set("testentity.world", "Hallo")

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR])


    return True

# TODO Update entry annotation
async def async_unload_entry(hass: HomeAssistant, entry: New_NameConfigEntry) -> bool:
    """Unload a config entry."""
    return True
