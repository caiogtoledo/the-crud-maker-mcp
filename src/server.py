from mcp.server.fastmcp import FastMCP
from src.templates.entity import ENTITY_EXAMPLE, ENTITY_TEST_EXAMPLE
from src.tools.entity import create_entity_tool, create_entity_test_tool
from src.tools.repository_interface import create_repository_interface_tool
from src.tools.usecase import create_usecase_tool, create_usecase_test_tool
from src.templates.controller import CONTROLLER_EXAMPLE, CONTROLLER_TEST_EXAMPLE
from src.tools.controller import create_controller_tool, create_controller_test_tool
from src.templates.viewmodel import VIEWMODEL_EXAMPLE, VIEWMODEL_TEST_EXAMPLE
from src.tools.viewmodel import create_viewmodel_tool, create_viewmodel_test_tool
from src.templates.repository_mongodb import REPOSITORY_MONGODB_EXAMPLE, REPOSITORY_MONGODB_TEST_EXAMPLE
from src.tools.repository_mongodb import create_repository_mongodb_tool, create_repository_mongodb_test_tool
from src.templates.presenter import PRESENTER_EXAMPLE 
from src.tools.presenter import create_presenter_tool
from src.tools.create_route import create_route_tool


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

@mcp.resource("mcp://examples/viewmodel")
def get_viewmodel_example() -> str:
    return VIEWMODEL_EXAMPLE

@mcp.resource("mcp://examples/tests/viewmodel")
def get_viewmodel_test_example() -> str:
    return VIEWMODEL_TEST_EXAMPLE

@mcp.tool(name="create_viewmodel")
async def create_viewmodel(module_name: str, viewmodel_name: str) -> str:
    """Generates a viewmodel file content following the viewmodel example."""
    return create_viewmodel_tool(module_name, viewmodel_name)

@mcp.tool(name="create_viewmodel_test")
async def create_viewmodel_test(module_name: str, viewmodel_name: str) -> str:
    """Generates a viewmodel test file content following the viewmodel test example."""
    return create_viewmodel_test_tool(module_name, viewmodel_name)

@mcp.resource("mcp://examples/repository_mongodb")
def get_repository_mongodb_example() -> str:
    return REPOSITORY_MONGODB_EXAMPLE

@mcp.resource("mcp://examples/tests/repository_mongodb")
def get_repository_mongodb_test_example() -> str:
    return REPOSITORY_MONGODB_TEST_EXAMPLE

@mcp.tool(name="create_repository_mongodb")
async def create_repository_mongodb(module_name: str, repository_name: str, entity_name: str) -> str:
    """Generates a mongodb repository file content following the repository example."""
    return create_repository_mongodb_tool(module_name, repository_name, entity_name)

@mcp.tool(name="create_repository_mongodb_test")
async def create_repository_mongodb_test(repository_name: str) -> str:
    """Generates a mongodb repository test file content following the repository test example."""
    return create_repository_mongodb_test_tool(repository_name)

@mcp.resource("mcp://examples/presenter")
def get_presenter_example() -> str:
    return PRESENTER_EXAMPLE

@mcp.tool(name="create_presenter")
async def create_presenter(module_name: str, presenter_name: str) -> str:
    """Generates a presenter file content following the presenter example."""
    return create_presenter_tool(module_name, presenter_name)

@mcp.tool(name="create_route")
async def create_route(route_name: str, url_prefix: str) -> str:
    """Generates a new route and declare in server.py."""
    return await create_route_tool(route_name, url_prefix)

@mcp.prompt("CRIAR CRUD")
def prompt(description: str):
    """
    Prompt MCP que cria um CRUD utilizando tools específicas
    """
    
    return [
        {
            "role": "assistant",
            "content": f"""
            Crie um CRUD que tenha o seguinte objetivo: {description}, utilize as ferramentas para cada rota:
            Caso não exista as entidades necessárias: `create_entity`
            Caso não exista a interface do repositorio necessário: `create_repository_interface`
            O caso de uso para cada rota, use: `create_usecase`
            Para cada rota, crie um viewmodel com: `create_viewmodel`
            Para cada rota, crie um controller com: `create_controller`
            Para cada rota, crie um presenter com: `create_presenter`
            Por fim, use a ferramenta `create_route` para declarar as rotas que forem criadas
            """
        }
    ]

def main():
    mcp.run()

if __name__ == "__main__":
    main()
