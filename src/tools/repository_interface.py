from typing import Dict
from src.templates.repository_interface import REPOSITORY_INTERFACE_EXAMPLE

def create_repository_interface_tool(repository_name: str, methods: Dict[str, str]) -> str:
    """Generates an repository interface file content following the repository interface example."""
    return f"""Create a repository interface file in the folder /src/shared/domain/repositories/{repository_name} (with the pattern _interface.py in the final) 
    that have this methods: {methods}.
    Follow this example of repository interface: {REPOSITORY_INTERFACE_EXAMPLE}
    """
