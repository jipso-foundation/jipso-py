import pytest
from jipso.Output import Output
import logging


logger = logging.getLogger(__name__)

class Test_Output:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
