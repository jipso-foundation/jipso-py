import pytest
from jipso.tvt import tvt
import logging


logger = logging.getLogger(__name__)

class Test_tvt:
  def test_basic(self):
    assert True


if __name__ == '__main__':
  pytest.main([__file__, '-v', '--asyncio-mode=auto'])
