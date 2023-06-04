from typing import List

from pydantic import BaseModel

__all__ = ["Measures", "PowerMeasure", "PowerSource", "PowerOutput"]


class Measures(BaseModel):
    measure_time: float
    currents: List[float]
    tensions: List[float]


class PowerSource:
    async def set_current(self, current: float):
        ...

    async def set_tension(self, tension: float):
        ...


class PowerOutput:
    async def switch_on(self, chanel_number: int):
        ...

    async def switch_off(self, chanel_number: int):
        ...


class PowerMeasure:
    async def chanel_condition(self, chanel_numbers: list[int]) -> Measures:
        res = Measures(
            measure_time=12.4,
            currents=[12, 5.2],
            tensions=[2.5, 0.3]
        )

        return res


ps: PowerSource | None = None
po: PowerOutput | None = None
pm: PowerMeasure | None = None


async def get_power_source():
    return ps


async def get_power_output():
    return po


async def get_power_measure():
    return pm
