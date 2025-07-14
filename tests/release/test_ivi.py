import pytest
from jipso.ivi import ivi
import logging


logger = logging.getLogger(__name__)

class Test_ivi:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
