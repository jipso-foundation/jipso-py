import pytest
from jipso.Compute import Compute
import logging


logger = logging.getLogger(__name__)

class Test_Compute:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
