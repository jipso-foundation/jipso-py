import pytest
from jipso.Input import Input
import logging


logger = logging.getLogger(__name__)

class Test_Input:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
