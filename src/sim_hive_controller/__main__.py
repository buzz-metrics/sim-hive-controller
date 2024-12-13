"""Interface for ``python -m hive_controller_ioc`` using Typer."""

import typer
import uvicorn

from ._version import __version__
from .sim import app

cli = typer.Typer(no_args_is_help=True)


@cli.command()
def run(
    port: str = typer.Argument(..., help="The port to run the simulation on."),
):
    """
    Start the simulation.

    ARGS:
        Port: The port to run the simulation on.
    """
    typer.echo("Starting the simulation...")
    uvicorn.run(app, host="0.0.0.0", port=int(port), reload=False, log_level="debug")


def version_callback(value: bool):
    if value:
        typer.echo(f"{__version__}")
        raise typer.Exit()


@cli.callback()
def main(version: bool = typer.Option(None, "--version", callback=version_callback)):
    """
    Simulation entry point
    """


if __name__ == "__main__":
    cli()
