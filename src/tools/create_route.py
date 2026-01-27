from src.templates.route import ROUTES_EXAMPLE

def create_route_tool(route_name: str, url_prefix: str) -> str:
    """
    Generates a new route definition to be added to server.py.
    """
    return f"""
    Create a route or modify the file in the folder /src/shared/infra/routes/{route_name}.py
    With the url prefix: {url_prefix}
    Follow this example of route configuration: {ROUTES_EXAMPLE}
    After create/modify the route configuration, remember to change de server.py file.
    """