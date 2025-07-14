import pytest
from jipso.Body.Image import Image
import logging


logger = logging.getLogger(__name__)

class Test_Image:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
