import pytest
import pandas as pd

from query_ranger.pubmed_query import PubmedQuery

def test_get_and_print_results():
  pico_query = PubmedQuery(
    query="occupational medicine",
    max_results=10
    )
  pico_query.get_results()
  pico_query.tabulate_results()

  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', 1000)
  pd.set_option('display.max_colwidth', None)

  pico_query.print_results()
  results = pico_query.query_data['results']

  for article in results:
    print(type(article))
    # data_attributes = [attr for attr in dir(article) if not callable(getattr(article, attr)) and not attr.startswith('_')]
    # print(data_attributes)
    # print("======================================")
    # print(">>>>> Abstract: ", article.abstract)
    # print(">>>>> Authors:", article.authors)
    # print(">>>>> Conclusions:", article.conclusions)
    # print(">>>>> Copyrights:", article.copyrights)
    # print(">>>>> DOI:", article.doi)
    # print(">>>>> Journal:", article.journal)
    # print(">>>>> Keywords:", article.keywords)
    # print(">>>>> Methods:", article.methods)
    # print(">>>>> Publication Date:", article.publication_date)
    # print(">>>>> Pubmed ID:", article.pubmed_id)
    # print(">>>>> Results:", article.results)
    # print(">>>>> Title:", article.title)
    # print(">>>>> XML:", dir(article.xml))

  raise
