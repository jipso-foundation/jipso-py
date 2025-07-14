import pytest
from jipso.Body.Audio import Audio
import logging


logger = logging.getLogger(__name__)

class Test_Audio:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
