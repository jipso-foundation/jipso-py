import pytest
from jipso.Standard import Standard
import logging


logger = logging.getLogger(__name__)

class Test_Standard:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
