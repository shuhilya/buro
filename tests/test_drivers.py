from unittest.mock import MagicMock


async def test_power_source_driver():
    from power_api.drivers.power_drivers import PowerSource, PowerMeasure, PowerOutput
    from power_api.services.power_system import PowerSystem

    power_source = PowerSource()

    power_system = PowerSystem(
        power_source=power_source,
        power_measure=PowerMeasure(),
        power_output=PowerOutput()
    )

    await power_system.switch_on_power_chanel(
        chanel_number=2,
        tension=3.2,
        current=0.8
    )

    assert power_source._scpi_current_message == "current:0.8\n"
    assert power_source._scpi_tension_message == "tension:3.2\n"
