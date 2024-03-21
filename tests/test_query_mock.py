import pytest
from unittest.mock import patch, MagicMock
from query_ranger.pubmed_query import PubmedQuery

@patch('query_ranger.pubmed_query.PubMed')
@pytest.mark.skip
def test_get_results_with_mock(mock_pubmed_class):
  expected_query = "occupational medicine"
  expected_max_results = 10
  expected_tool = 'EurekaQuery'
  expected_email = ''

  mock_pubmed_instance = MagicMock()
  mock_pubmed_class.return_value = mock_pubmed_instance
  mock_pubmed_instance.query.return_value = MagicMock()

  pico_query = PubmedQuery(query=expected_query, max_results=expected_max_results)

  pico_query.get_results()

  mock_pubmed_class.assert_called_with(tool=expected_tool, email=expected_email)

  mock_pubmed_instance.query.assert_called_with(expected_query, expected_max_results)
