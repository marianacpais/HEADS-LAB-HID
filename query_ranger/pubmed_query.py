from pymed import PubMed
import pandas as pd
import itertools
from datetime import datetime

from .abstract_query import AbstractQuery

class PubmedQuery(AbstractQuery):
  DEFAULT_QUERY=""
  DEFAULT_TOOL="EurekaQuery"
  DEFAULT_EMAIL=""

  def __init__(self, query=None, results=None, max_results=None, params=None):
    super().__init__(query, results, params)
    # TODO @mariana.pais add logic for when max_results is not integer
    self.max_results = None if max_results is None else max_results
    self.pubmed = PubMed(tool=self.DEFAULT_TOOL, email=self.DEFAULT_EMAIL)
    self.tabular_data = []

  def get_results(self):
    """
    """
    try:
      self.query_data['results'] = list(self.pubmed.query(
        self.query_data['query'],
        self.max_results,
      ))
    except:
      self.sys_message.append(
        f"[{datetime.now()}] Retreiving data from PubMed was unsuccessful"
      )

  def tabulate_results(self):
    if not self.query_data.get('results'):
      self.sys_message.append(
        f"[{datetime.now()}] No results were found to tabulate"
      )
      return None

    results = list(self.query_data['results'])

    for article in results:

      article_data = {
        "Title": article.title,
        "Abstract": article.abstract,
        "Authors": ", ".join([str(author) for author in article.authors]) if article.authors else None,
        "DOI": article.doi,
        "Journal": article.journal,
        "Publication Date": article.publication_date,
        "Keywords": ", ".join([str(keyword) for keyword in article.keywords]) if article.keywords else None,
        "Methods": article.methods,
        "Results": article.results,
        "Conclusions": article.conclusions,
        "Pubmed ID": article.pubmed_id,
        "Copyrights": article.copyrights,
      }
      self.tabular_data.append(article_data)

    self.tabular_data = pd.DataFrame(self.tabular_data)
    return self.tabular_data

  def print_results(self):
    results_object = self.query_data['results']
    results = list(results_object)

    for article in results:
      data_attributes = [attr for attr in dir(article) if not callable(getattr(article, attr)) and not attr.startswith('_')]
      print(data_attributes)
      print("======================================")
      print(">>>>> Abstract: ", article.abstract)
      print(">>>>> Authors:", article.authors)
      print(">>>>> Conclusions:", article.conclusions)
      print(">>>>> Copyrights:", article.copyrights)
      print(">>>>> DOI:", article.doi)
      print(">>>>> Journal:", article.journal)
      print(">>>>> Keywords:", article.keywords)
      print(">>>>> Methods:", article.methods)
      print(">>>>> Publication Date:", article.publication_date)
      print(">>>>> Pubmed ID:", article.pubmed_id)
      print(">>>>> Results:", article.results)
      print(">>>>> Title:", article.title)
      print(">>>>> XML:", dir(article.xml))