

class SearchResult(object):

    def __init__(self, results, total_results):
        self.total_results = total_results
        self._results = results

    def total(self):
        return self.total_results

    def results(self):
        return self._results

    def set(self, results, total_results):
        self.total_results = total_results
        self._results = results
