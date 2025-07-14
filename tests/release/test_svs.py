import pytest
from jipso.svs import svs
import logging


logger = logging.getLogger(__name__)

class Test_svs:
  def test_basic(self):
    assert True


if __name__ == '__main__':
  pytest.main([__file__, '-v'])
