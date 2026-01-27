from src.templates.usecase import USECASE_EXAMPLE, USECASE_TEST_EXAMPLE

def create_usecase_tool(module_name: str, usecase_name: str, business_rules: str) -> str:
    """Generates an usecase file content following the usecase example."""
    return f"""Create a usecase file in the folder /src/modules/{module_name}/app/{usecase_name} that have this business rules: {business_rules}.
    Follow this example of usecase: {USECASE_EXAMPLE}
    If the use case requires access to or modification of a repository, create it using the `create_repository_interface` tool or use an existing one.
    After create the usecase, call the `create_usecase_test` tool
    """

def create_usecase_test_tool(module_name: str, usecase_name: str) -> str:
    """Generates an usecase test file content following the usecase test example."""
    return f"""Create a usecase test file in the folder /tests/modules/{module_name}/app/{usecase_name} to covarage this file: /src/modules/{module_name}/app/{usecase_name}.
    Follow this example of usecase test: {USECASE_TEST_EXAMPLE}
    """
