from src.templates.presenter import PRESENTER_EXAMPLE, PRESENTER_TEST_EXAMPLE

def create_presenter_tool(module_name: str, presenter_name: str) -> str:
    """Generates a presenter file content following the presenter example."""
    return f"""Create a presenter file in the folder /src/modules/{module_name}/app/presenters/{presenter_name}_presenter.py.
    Follow this example of presenter: {PRESENTER_EXAMPLE}
    """
