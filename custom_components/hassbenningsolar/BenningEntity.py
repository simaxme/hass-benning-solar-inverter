from functools import cached_property
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

from .benning_client import BenningClient

class BenningEntity(Entity):
    hass: HomeAssistant
    benning_client: BenningClient
    _unique_id: str
    _name: str

    def __init__(self, hass: HomeAssistant, benning_client: BenningClient, id: str, name: str):
        super().__init__()

        self.hass = hass
        self.benning_client = benning_client
        self._unique_id = id
        self._name = name

    @cached_property
    def name(self):
        return self._name

    @cached_property
    def unique_id(self):
        return self._unique_id

