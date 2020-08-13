from click.testing import CliRunner

from aer.cli import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
    assert result.output == "Hello, World!\n"
