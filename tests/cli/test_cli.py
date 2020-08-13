import toml
from click.testing import CliRunner
from pyprojroot import here

from aer.cli import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert result.output == "Hello, World!\n"


def test_version_option():
    pyproject = toml.load(here("pyproject.toml"))
    pyproject_version = pyproject["tool"]["poetry"]["version"]

    runner = CliRunner()
    result = runner.invoke(cli, "--version")

    assert result.exit_code == 0
    assert result.output == f"main, version {pyproject_version}\n"
