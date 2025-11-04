from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from custom_components.hassbenningsolar.BenningEntity import BenningEntity
from custom_components.hassbenningsolar.benning_client import BenningClient


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    client = BenningClient(hass, "192.168.1.23", "", "")

    available_entries = await client.get_available_entries()
    print(available_entries)

    result_entities: list[BenningEntity] = []

    for bentry in available_entries:
        id = "_".join(str(bentry["label"]).split("."))
        entity = BenningEntity(hass, client, id, bentry["uitext"])
        result_entities.append(entity)

    await async_add_entities(result_entities)
    # async_add_entities([BenningEntity(hass, entry, client)])

