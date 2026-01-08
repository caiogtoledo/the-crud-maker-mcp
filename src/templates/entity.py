ENTITY_EXAMPLE = """
import abc
from typing import Optional
import uuid

from src.shared.helpers.errors.domain_errors import EntityError


class Alert(abc.ABC):
    alert_id: str
    type: float
    message: str  #
    is_resolved: bool
    timestamp_created_at: int
    timestamp_updated_at: Optional[int]

    def __init__(self,
                 alert_id: str,
                 type: str,
                 message: str,
                 timestamp_created_at: float,
                 timestamp_updated_at: float,
                 is_resolved: bool
                 ):
        if not self.validate_alert_id(alert_id):
            raise EntityError("alert_id")
        self.alert_id = alert_id

        if not self.validate_type(type):
            raise EntityError("type")
        self.type = type

        if not self.validate_message(message):
            raise EntityError("message")
        self.message = message

        if not self.validate_is_resolved(is_resolved):
            raise EntityError("is_resolved")
        self.is_resolved = is_resolved

        if not self.validate_timestamp(timestamp_created_at):
            raise EntityError("timestamp_created_at")
        self.timestamp_created_at = timestamp_created_at

        self.timestamp_updated_at = timestamp_updated_at

    @staticmethod
    def validate_alert_id(alert_id: str) -> bool:
        return isinstance(alert_id, str) and len(alert_id) > 0

    @staticmethod
    def validate_type(type: str) -> bool:
        return isinstance(type, str) and len(type) > 0

    @staticmethod
    def validate_message(message: str) -> bool:
        return isinstance(message, str) and len(message) > 0

    @staticmethod
    def validate_is_resolved(is_resolved: bool) -> bool:
        return isinstance(is_resolved, (bool))

    @staticmethod
    def validate_timestamp(timestamp: float) -> bool:
        return isinstance(timestamp, (int, float))

    @staticmethod
    def validate_uuid(value: float) -> bool:
        try:
            uuid_obj = uuid.UUID(value, version=4)
        except ValueError:
            return False
        return str(uuid_obj) == value

    def __repr__(self):
        return (f"Alert(alert_id={self.alert_id}, type={self.type}, "
                f"message={self.message}, is_resolved={self.is_resolved}, "
                f"timestamp_created_at={self.timestamp_created_at}, "
                f"timestamp_updated_at={self.timestamp_created_at}"
                )
"""

ENTITY_TEST_EXAMPLE = """
import pytest
from src.shared.domain.entities.battery import Battery
from src.shared.helpers.errors.domain_errors import EntityError
import datetime


class Test_Battery:
    def test_battery(self):
        measure = Battery(
            battery_id="1",
            soc=0.5,
            voltage=3.7,
            current=0.1,
            temperature=25.0,
            timestamp=int(datetime.datetime.now().timestamp())*1000,
        )

        assert type(measure) == Battery
        assert measure.battery_id == "1"
        assert measure.soc == 0.5
        assert measure.voltage == 3.7
        assert measure.current == 0.1
        assert measure.temperature == 25.0
        assert measure.timestamp == int(
            datetime.datetime.now().timestamp())*1000

    def test_battery_id_is_none(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=None,
                soc=0.5,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_id_is_not_str(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.5,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_soc_is_none(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=None,
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_soc_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc="TESTE",
                voltage=3.7,
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_voltage_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage="TESTE",
                current=0.1,
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_current_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage=2,
                current="TESTE",
                temperature=25.0,
                timestamp=int(datetime.datetime.now().timestamp())*1000,
            )

    def test_battery_temperature_is_not_valid(self):
        with pytest.raises(EntityError):
            measure = Battery(
                battery_id=2,
                soc=0.1,
                voltage=2,
                current=0.1,
                temperature="TESTE",
                timestamp=int(datetime.datetime.now().timestamp())*1000
            )
"""
