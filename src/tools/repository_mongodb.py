from src.templates.repository_mongodb import REPOSITORY_MONGODB_EXAMPLE, REPOSITORY_MONGODB_TEST_EXAMPLE

def create_repository_mongodb_tool(module_name: str, repository_name: str, entity_name: str) -> str:
    """Generates a mongodb repository file content following the repository example."""
    return f"""Create a mongodb repository file in the folder /src/modules/{module_name}/infra/repositories/{repository_name}_mongodb.py for the entity {entity_name}.
    Follow this example of mongodb repository: {REPOSITORY_MONGODB_EXAMPLE}
    """

def create_repository_mongodb_test_tool(module_name: str, repository_name: str) -> str:
    """Generates a mongodb repository test file content following the repository test example."""
    return f"""Create a mongodb repository test file in the folder /tests/modules/{module_name}/infra/repositories/{repository_name}_mongodb_test.py.
    Follow this example of mongodb repository test: {REPOSITORY_MONGODB_TEST_EXAMPLE}
    """