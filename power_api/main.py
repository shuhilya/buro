import logging
from logging import config

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from power_api.api.v1 import power_system
from power_api.core.logger import LOGGING
from power_api.drivers import power_drivers
from power_api.drivers.power_drivers import PowerMeasure, PowerOutput, PowerSource


config.dictConfig(LOGGING)

app = FastAPI(
    title="UGC API",
    description="API to save and work with UGC data",
    version="1.0.0",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup() -> None:
    """Connect to power drivers."""
    power_drivers.ps = PowerSource()
    power_drivers.po = PowerOutput()
    power_drivers.pm = PowerMeasure()


app.include_router(power_system.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8325,
        log_config=LOGGING,
        log_level=logging.DEBUG,
        reload=True,
    )
