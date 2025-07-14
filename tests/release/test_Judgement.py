import pytest
from jipso.Judgement import Judgement
import logging


logger = logging.getLogger(__name__)

class Test_Judgement:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
