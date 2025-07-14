import pytest
from jipso.pvp import pvp
import logging


logger = logging.getLogger(__name__)

class Test_pvp:
  def test_basic(self):
    assert True


if __name__ == '__main__':
  pytest.main([__file__, '-v'])
