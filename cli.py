# -*- coding: utf-8 -*-
import click
from loguru import logger

from src.program import run


@click.command()
@click.argument("arg")
def main(arg):
    run(arg)


if __name__ == "__main__":
    logger.info("Starting app in cli.")
    SystemExit(main())
