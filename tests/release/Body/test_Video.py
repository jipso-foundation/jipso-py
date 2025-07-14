import pytest
from jipso.Body.Video import Video
import logging


logger = logging.getLogger(__name__)

class Test_Video:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
