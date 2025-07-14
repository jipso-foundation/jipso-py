from jipso.Mind.Model import Model
import pytest
import logging


logger = logging.getLogger(__name__)

class Test_Model:
  def test_basic(self):
    assert True

if __name__ == '__main__':
  pytest.main([__file__, '-v'])
