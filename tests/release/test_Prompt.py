import pytest
from jipso.Prompt import Prompt
import logging


logger = logging.getLogger(__name__)

class Test_Prompt:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
