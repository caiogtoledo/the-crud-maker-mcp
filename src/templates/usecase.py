USECASE_EXAMPLE = """
from typing import Optional
import datetime
from src.shared.domain.entities.battery import Battery
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.helpers.errors.usecase_errors import CreationError


class MeasureBatteryUsecase:
    def __init__(self, repo: IBatteryRepository):
        self.repo = repo

    def __call__(self, battery_id: float, soc: float, voltage: float, current: float, temperature: float, timestamp: Optional[int]) -> Battery:

        if timestamp is None:
            timestamp = int(datetime.datetime.now().timestamp())*1000

        measure = Battery(
            battery_id=battery_id,
            soc=soc,
            voltage=voltage,
            current=current,
            temperature=temperature,
            timestamp=timestamp
        )

        try:
            self.repo.create_measure(measure)
        except Exception as e:
            raise CreationError("Error creating battery measure: {e}")

        return measure
"""

USECASE_TEST_EXAMPLE = """
import pytest

from src.modules.measure_battery.app.measure_battery_usecase import MeasureBatteryUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
import datetime


class Test_MeasureBatteryUsecase:

    def test_create_battery_measurement(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo)

        battery_measurement = usecase(
            battery_id="2",
            soc=0.50,
            voltage=0.5,
            current=0.5,
            temperature=30.0,
            timestamp=int(datetime.datetime.now().timestamp())*1000
        )

        assert repo.battery_measurements[-1] == battery_measurement

    def test_create_battery_measurement_without_timestamp(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo)

        battery_measurement = usecase(
            battery_id="2",
            soc=0.50,
            voltage=0.5,
            current=0.5,
            temperature=30.0,
            timestamp=None
        )

        assert repo.battery_measurements[-1] == battery_measurement
        assert repo.battery_measurements[-1].timestamp is not None
        assert repo.battery_measurements[-1].timestamp == int(
            datetime.datetime.now().timestamp())*1000

    def test_create_user_invalid_name(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo)

        with pytest.raises(EntityError):
            battery_measurement = usecase(
                battery_id=2,
                soc=0.50,
                voltage=0.5,
                current=0.5,
                temperature=30.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000
            )
"""
