import typer


def greet(name: str):
    typer.echo(f'Hello, {name}!')


if __name__ == '__main__':
    typer.run(greet)
