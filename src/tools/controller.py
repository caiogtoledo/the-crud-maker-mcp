from src.templates.controller import CONTROLLER_EXAMPLE, CONTROLLER_TEST_EXAMPLE

def create_controller_tool(module_name: str, entity_name: str, usecase_name: str) -> str:
    """Generates a controller file content following the controller example."""
    return f"""Create a controller file in the folder /src/modules/{module_name}/app/{entity_name}_controller.py for the usecase {usecase_name}.
    Follow this example of controller: {CONTROLLER_EXAMPLE}
    The controller should handle the creation of {entity_name}.
    """

def create_controller_test_tool(module_name: str, entity_name: str) -> str:
    """Generates a controller test file content following the controller test example."""
    return f"""Create a controller test file in the folder /tests/modules/{module_name}/app/{entity_name}_controller_test.py.
    Follow this example of controller test: {CONTROLLER_TEST_EXAMPLE}
    The test should cover the creation of {entity_name}.
    """
