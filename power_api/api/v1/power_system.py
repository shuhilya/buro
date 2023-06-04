import logging
from typing import List

from fastapi import APIRouter, Depends

from power_api.services.power_system import get_power_system
from power_api.drivers.power_drivers import Measures

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    path="/switch_chanel_on",
    summary="Switch on the current chanel",
    description="Switch on the current chanel with settings of current and tension",
    tags=["SwitchOn"],
)
async def switch_chanel_on(
    current: float,
    tension: float,
    chanel_number: int,
    power_system=Depends(get_power_system)
):
    logger.info(f"Switch on the chanel {chanel_number}")

    await power_system.switch_on_power_chanel(
        chanel_number=chanel_number,
        current=current,
        tension=tension
    )


@router.post(
    path="/switch_chanel_off",
    summary="Switch off the current chanel",
    description="Switch off the current chanel",
    tags=["SwitchOff"],
)
async def switch_chanel_off(
        chanel_number: int,
        power_system=Depends(get_power_system)
):
    logger.info(f"Switch off the chanel {chanel_number}")

    await power_system.switch_off_power_chanel(
        chanel_number=chanel_number
    )


@router.post(
    path="/measures",
    summary="Get measures from all channels",
    description="Get measures from all channels by theirs ids",
    response_description="Set of time, current and tension",
    response_model=Measures,
    tags=["Measures"],
)
async def get_power_mesures(
    channels_ids: List[int],
    power_system=Depends(get_power_system)
) -> Measures:

    logger.info(f"Get measures from all channels: {channels_ids}")

    return await power_system.current_channels_condition(channels=channels_ids)
