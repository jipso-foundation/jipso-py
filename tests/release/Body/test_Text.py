import pytest
from jipso.Body.Text import Text
import logging


logger = logging.getLogger(__name__)

class Test_Text:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
