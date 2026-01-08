from typing import Dict
from src.templates.entity import ENTITY_EXAMPLE, ENTITY_TEST_EXAMPLE

def create_entity_tool(entity_name: str, fields: Dict[str, str]) -> str:
    """Generates an entity file content following the entity example."""
    return f"""Create a entity file in the folder /src/shared/domain/entities/{entity_name} that have this fields: {fields}.
    Follow this example of entity: {ENTITY_EXAMPLE}
    After create the entity, call the `create_entity_test` tool
    """

async def create_entity_test_tool(entity_name: str, fields: Dict[str, str]) -> str:
    """Generates an entity test file content following the entity test example."""
    return f"""Create a entity test file in the folder /tests/shared/domain/entities/{entity_name} that have this fields: {fields}.
    Follow this example of entity test: {ENTITY_TEST_EXAMPLE}
    """
