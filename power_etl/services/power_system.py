from power_etl.drivers.power_drivers import PowerMeasure

__all__ = ["PowerSystem"]


class PowerSystem:
    def __init__(self, power_measure: PowerMeasure):
        self._power_measure = power_measure

    async def current_channels_condition(self, channels: list[int]):
        return await self._power_measure.chanel_condition(chanel_numbers=channels)
