from functools import lru_cache

from fastapi import Depends

from power_api.drivers.power_drivers import (PowerMeasure,
                                             PowerOutput,
                                             PowerSource,
                                             get_power_measure,
                                             get_power_output,
                                             get_power_source)

__all__ = ["get_power_system", "PowerSystem"]


class PowerSystem:
    def __init__(
            self,
            power_source: PowerSource,
            power_output: PowerOutput,
            power_measure: PowerMeasure
    ):
        self._power_source = power_source
        self._power_output = power_output
        self._power_measure = power_measure

    async def switch_on_power_chanel(self, chanel_number: int, tension: float, current: float):
        await self._power_source.set_current(current=current)
        await self._power_source.set_tension(tension=tension)
        await self._power_output.switch_on(chanel_number=chanel_number)

    async def switch_off_power_chanel(self, chanel_number: int):
        await self._power_output.switch_off(chanel_number=chanel_number)

    async def current_channels_condition(self, channels: list[int]):
        return await self._power_measure.chanel_condition(chanel_numbers=channels)


@lru_cache()
def get_power_system(
        ps: PowerSource = Depends(get_power_source),
        po: PowerOutput = Depends(get_power_output),
        pm: PowerMeasure = Depends(get_power_measure)
):
    return PowerSystem(
        power_source=ps,
        power_output=po,
        power_measure=pm
    )
