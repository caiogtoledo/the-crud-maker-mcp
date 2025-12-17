from mcp.server.fastmcp import FastMCP

mcp = FastMCP("the-crud-maker")

@mcp.resource("mcp://name")
def get_resource() -> str:
    return "Meu nome é Caio"

@mcp.tool()
def formula_caio(a: float, b: float):
    """Calcula a fórmula de Caio Toledo"""
    return float(a) + float(b)

@mcp.prompt("prompt_1")
def prompt(a: float, b: float):
    """
    Prompt MCP que:
    1. Obtém o nome do recurso mcp://name
    2. Solicita dois números do usuário para calcular a fórmula de Caio Toledo
    3. Chama a tool formula_caio(a, b)
    4. Retorna mensagem final com o resultado
    """
    my_name = get_resource()
    result = formula_caio(a, b)
        
    return [
            {
                "role": "assistant",
                "content": f"Olá! Meu nome é {my_name}. A o resultado da formula de Caio Toledo para a: {a} e b: {b} é {result}."
            }
        ]

def main():
    mcp.run()

if __name__ == "__main__":
    main()