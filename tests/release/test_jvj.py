import pytest
from jipso.jvj import jvj
import logging


logger = logging.getLogger(__name__)

class Test_jvj:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
