import logging
from logging import config
from time import sleep

import backoff

from power_etl.core.logger import LOGGING
from power_etl.drivers.power_drivers import PowerMeasure
from power_etl.services.power_system import PowerSystem

config.dictConfig(LOGGING)
logger = logging.getLogger()


def raise_exception(details):
    raise Exception("Error in power system connection!!")


@backoff.on_exception(
    wait_gen=backoff.expo,
    exception=ConnectionError,
    max_time=100,
    on_giveup=raise_exception
)
async def test_connection(power_system: PowerSystem, channels: list[int]):
    await power_system.current_channels_condition(channels=channels)


if __name__ == '__main__':
    measure = PowerMeasure()
    system = PowerSystem(power_measure=measure)

    channels = [1, 5]

    while True:
        try:
            info = await system.current_channels_condition(channels=channels)
            logger.info(f"{info.measure_time} {info.currents} {info.tensions}")
            sleep(2)
        except Exception:
            await test_connection(power_system=system, channels=channels)



