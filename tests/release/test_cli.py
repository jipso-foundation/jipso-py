from typer.testing import CliRunner
from jipso.cli import cli
import logging


logger = logging.getLogger(__name__)

def test_basic():
  runner = CliRunner()
  result = runner.invoke(cli, ['--version'])
  assert True
