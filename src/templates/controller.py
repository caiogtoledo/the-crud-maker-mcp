CONTROLLER_EXAMPLE = """
from src.modules.create_alert.app.create_alert_usecase import CreateAlertUsecase
from src.modules.create_alert.app.create_alert_viewmodel import AlertViewmodel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created


class CreateAlertController:

    def __init__(self, usecase: CreateAlertUsecase):
        self.CreateAlertUsecase = usecase
        
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('type') is None:
                raise MissingParameters('type')
            if request.data.get('message') is None:
                raise MissingParameters('message')

            measure = self.CreateAlertUsecase(
                alert_id=request.data.get('alert_id'),
                type=request.data.get('type'),
                message=request.data.get('message'),
                is_resolved=request.data.get('is_resolved'),
                timestamp_created_at=request.data.get('timestamp_created_at'),
            )
            viewmodel = AlertViewmodel(measure)
            return Created(viewmodel.to_dict())
        except NoItemsFound as err:
            return NotFound(body=err.message)
        except MissingParameters as err:
            return BadRequest(body=err.message)
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        except EntityError as err:
            return BadRequest(body=err.message)
        except Exception as err:
            return InternalServerError(body=err.args[0])
"""

CONTROLLER_TEST_EXAMPLE = """
import datetime

from src.modules.create_alert.app.create_alert_controller import CreateAlertController
from src.modules.create_alert.app.create_alert_usecase import CreateAlertUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock


class Test_CreateAlertController:

    def test_create_alert_controller(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo=repo)
        controller = CreateAlertController(usecase=usecase)

        request = HttpRequest(body={
            'alert_id': '1',
            'type': "severity",
            'message': 'temperature is too high',
            'is_resolved': False,
            'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['alert_id'] == repo.alerts[-1].alert_id
        assert isinstance(response.body['type'], str)
        assert isinstance(response.body['message'], str)
        assert isinstance(response.body['is_resolved'], bool)
        assert response.body['timestamp_created_at'] == repo.alerts[-1].timestamp_created_at
        assert isinstance(response.body['timestamp_created_at'], int)
        assert response.body['timestamp_created_at'] == int(
            datetime.datetime.now().timestamp())*1000

    def test_create_alert_controller_missing_measurement_id(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo=repo)
        controller = CreateAlertController(usecase=usecase)

        request = HttpRequest(body={
            # 'alert_id': '1',
            'type': "severity",
            'message': 'temperature is too high',
            'is_resolved': False,
            'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['alert_id'] == repo.alerts[-1].alert_id
        assert isinstance(response.body['type'], str)
        assert isinstance(response.body['message'], str)
        assert isinstance(response.body['is_resolved'], bool)
        assert response.body['timestamp_created_at'] == repo.alerts[-1].timestamp_created_at
        assert isinstance(response.body['timestamp_created_at'], int)
        assert response.body['timestamp_created_at'] == int(
            datetime.datetime.now().timestamp())*1000

    def test_create_sensor_measure_controller_missing_message(self):
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo=repo)
        controller = CreateAlertController(usecase=usecase)

        request = HttpRequest(body={
            'alert_id': '1',
            'type': "severity",
            # 'message': 'temperature is too high',
            'is_resolved': False,
            'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field message is missing"

    def test_create_sensor_measure_controller_missing_timestamp(self):
        # Mesmo faltando timestamp, o caso de uso gerará um timestamp
        repo = AlertsRepositoryMock()
        usecase = CreateAlertUsecase(repo=repo)
        controller = CreateAlertController(usecase=usecase)

        request = HttpRequest(body={
            'alert_id': '1',
            'type': "severity",
            'message': 'temperature is too high',
            'is_resolved': False,
            # 'timestamp_created_at': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['alert_id'] == repo.alerts[-1].alert_id
        assert isinstance(response.body['type'], str)
        assert isinstance(response.body['message'], str)
        assert isinstance(response.body['is_resolved'], bool)
        assert response.body['timestamp_created_at'] == repo.alerts[-1].timestamp_created_at
        assert isinstance(response.body['timestamp_created_at'], int)
        assert response.body['timestamp_created_at'] == int(
            datetime.datetime.now().timestamp())*1000
"""