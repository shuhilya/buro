from typing import List

from pydantic import BaseModel

__all__ = ["Measures", "PowerMeasure"]


class Measures(BaseModel):
    measure_time: List[float]
    currents: List[float]
    tensions: List[float]


class PowerMeasure:
    async def chanel_condition(self, chanel_numbers: list[int]) -> Measures:
        res = Measures(
            power=[2, 6],
            currents=[12, 5.2],
            tensions=[2.5, 0.3]
        )

        return res
