

class SearchResult(object):

    def __init__(results, totalResults):
        self._totalResults = totalResults
        self._results = results

    def total(self):
        return self._totalResults

    def results(self):
        self._results

    def set(self, results, total_results):
        self._totalResults = totalResults
        self._results = results
