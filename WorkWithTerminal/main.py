import typer

def greet(name: str) -> None:
    """
    This function prints a personalized greeting message to the console.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    None: The function does not return any value. It only prints the greeting message.
    """
    typer.echo(f'Hello, {name}!')


if __name__ == '__main__':
    typer.run(greet)