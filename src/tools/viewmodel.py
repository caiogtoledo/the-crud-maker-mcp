from src.templates.viewmodel import VIEWMODEL_EXAMPLE, VIEWMODEL_TEST_EXAMPLE

def create_viewmodel_tool(module_name: str, viewmodel_name: str) -> str:
    """Generates a viewmodel file content following the viewmodel example."""
    return f"""Create a viewmodel file in the folder /src/modules/{module_name}/app/{viewmodel_name}_viewmodel.py.
    Follow this example of viewmodel: {VIEWMODEL_EXAMPLE}
    """

def create_viewmodel_test_tool(module_name: str, viewmodel_name: str) -> str:
    """Generates a viewmodel test file content following the viewmodel test example."""
    return f"""Create a viewmodel test file in the folder /tests/modules/{module_name}/app/{viewmodel_name}_viewmodel_test.py.
    Follow this example of viewmodel test: {VIEWMODEL_TEST_EXAMPLE}
    """

