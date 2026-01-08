from mcp.server.fastmcp import FastMCP
from src.templates.entity import ENTITY_EXAMPLE, ENTITY_TEST_EXAMPLE
from src.tools.entity import create_entity_tool, create_entity_test_tool

mcp = FastMCP("the-crud-maker")

@mcp.resource("mcp://examples/entity")
def get_entity_example() -> str:
    return ENTITY_EXAMPLE

@mcp.resource("mcp://examples/tests/entity")
def get_entity_test_example() -> str:
    return ENTITY_TEST_EXAMPLE

@mcp.tool(name="create_entity")
def create_entity(entity_name: str, fields: dict[str, str]) -> str:
    """Generates an entity file content following the entity example."""
    return create_entity_tool(entity_name, fields)

@mcp.tool(name="create_entity_test")
async def create_entity_test(entity_name: str, fields: dict[str, str]) -> str:
    """Generates an entity test file content following the entity test example."""
    return await create_entity_test_tool(entity_name, fields)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
