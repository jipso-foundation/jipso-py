import pytest
from jipso.ovo import ovo
import logging


logger = logging.getLogger(__name__)

class Test_ovo:
  def test_basic(self):
    assert True


if __name__ == '__main__':
  pytest.main([__file__, '-v'])
