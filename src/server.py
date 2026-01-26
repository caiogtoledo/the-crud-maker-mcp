from mcp.server.fastmcp import FastMCP
from src.templates.entity import ENTITY_EXAMPLE, ENTITY_TEST_EXAMPLE
from src.tools.entity import create_entity_tool, create_entity_test_tool
from src.tools.repository_interface import create_repository_interface_tool
from src.tools.usecase import create_usecase_tool, create_usecase_test_tool
from src.templates.controller import CONTROLLER_EXAMPLE, CONTROLLER_TEST_EXAMPLE
from src.tools.controller import create_controller_tool, create_controller_test_tool

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

@mcp.tool(name="create_repository_interface")
async def create_repository_interface(repository_name: str, methods: dict[str, str]) -> str:
    """Generates an repository interface file content following the repository interface example."""
    return await create_repository_interface_tool(repository_name, methods)

@mcp.tool(name="create_usecase")
async def create_usecase(module_name: str, usecase_name: str, business_rules: str) -> str:
    """Generates an usecase file content following the usecase example."""
    return await create_usecase_tool(module_name, usecase_name, business_rules)

@mcp.tool(name="create_usecase_test")
async def create_usecase_test(module_name: str, usecase_name: str) -> str:
    """Generates an usecase test file content following the usecase test example."""
    return await create_usecase_test_tool(module_name, usecase_name)

@mcp.resource("mcp://examples/controller")
def get_controller_example() -> str:
    return CONTROLLER_EXAMPLE

@mcp.resource("mcp://examples/tests/controller")
def get_controller_test_example() -> str:
    return CONTROLLER_TEST_EXAMPLE

@mcp.tool(name="create_controller")
async def create_controller(module_name: str, entity_name: str, usecase_name: str) -> str:
    """Generates a controller file content following the controller example."""
    return create_controller_tool(module_name, entity_name, usecase_name)

@mcp.tool(name="create_controller_test")
async def create_controller_test(module_name: str, entity_name: str) -> str:
    """Generates a controller test file content following the controller test example."""
    return create_controller_test_tool(module_name, entity_name)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
