VIEWMODEL_EXAMPLE = """
from typing import Optional
from src.shared.domain.entities.alert import Alert


class AlertViewmodel:
    alert_id: str
    type: str
    message: str
    is_resolved: bool
    timestamp_created_at: int
    timestamp_updated_at: Optional[int]

    def __init__(self, alert: Alert):
        self.alert_id = alert.alert_id
        self.type = alert.type
        self.message = alert.message
        self.is_resolved = alert.is_resolved
        self.timestamp_created_at = alert.timestamp_created_at
        self.timestamp_updated_at = alert.timestamp_updated_at

    def to_dict(self):
        return {
            'alert_id': self.alert_id,
            'type': self.type,
            'message': self.message,
            'is_resolved': self.is_resolved,
            'timestamp_created_at': self.timestamp_created_at,
            'timestamp_updated_at': self.timestamp_updated_at,
        }
"""

VIEWMODEL_TEST_EXAMPLE = """

import datetime

from src.modules.create_alert.app.create_alert_viewmodel import AlertViewmodel
from src.shared.domain.entities.alert import Alert


class Test_AlertViewModel:

    def test_create_alert_viewmodel(self):
        alert = Alert(
            alert_id="1",
            type="baixa_carga_bateria",
            message="A carga da bateria está abaixo de 20%",
            is_resolved=False,
            timestamp_created_at=int(datetime.datetime.now().timestamp())*1000,
            timestamp_updated_at=None
        )
        viewmodel = AlertViewmodel(
            alert=alert).to_dict()

        expected = {
            'alert_id': "1",
            'type': "baixa_carga_bateria",
            'message': "A carga da bateria está abaixo de 20%",
            'is_resolved': False,
            'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
            'timestamp_updated_at': None,
        }

        assert expected == viewmodel
"""