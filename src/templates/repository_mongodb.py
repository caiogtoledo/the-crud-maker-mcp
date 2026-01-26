REPOSITORY_MONGODB_EXAMPLE = """
from pymongo import MongoClient
from typing import List

from src.shared.domain.entities.alert import Alert
from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository


class AlertsRepositoryMongoDB(IAlertsRepository):
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["alerts_db"]
        self.collection = self.db["alerts"]

    def create_alert(self, alert: Alert) -> Alert:
        self.collection.insert_one(alert.to_dict())
        return alert

    def get_all_alerts(self) -> List[Alert]:
        alerts = []
        for doc in self.collection.find():
            alerts.append(Alert.from_dict(doc))
        return alerts

    def update_alert(self, alert: Alert) -> Alert:
        self.collection.update_one({"alert_id": alert.alert_id}, {"$set": alert.to_dict()})
        return alert
"""

REPOSITORY_MONGODB_TEST_EXAMPLE = """
import pytest
from .alert_repository_mongodb import AlertsRepositoryMongoDB
from src.shared.domain.entities.alert import Alert

class TestAlertsRepositoryMongoDB:
    def test_create_alert(self):
        repo = AlertsRepositoryMongoDB()
        repo.collection.delete_many({})  # Clean collection
        alert = Alert(alert_id="4", type="test", message="Test Alert", is_resolved=False, timestamp_created_at=123)
        created_alert = repo.create_alert(alert)
        assert created_alert.alert_id == "4"

    def test_get_all_alerts(self):
        repo = AlertsRepositoryMongoDB()
        repo.collection.delete_many({})  # Clean collection
        repo.create_alert(Alert(alert_id="5", type="test", message="Test Alert 1", is_resolved=False, timestamp_created_at=123))
        repo.create_alert(Alert(alert_id="6", type="test", message="Test Alert 2", is_resolved=False, timestamp_created_at=124))
        alerts = repo.get_all_alerts()
        assert len(alerts) == 2
"""