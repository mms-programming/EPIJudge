from test_framework import generic_test


def h_index(citations):
    max_citations = get_max(citations)
    for i in range(0, max_citations+1):
        count = calculate_articles_with_citations(citations, i)
        if count < i:
            return i - 1

    return i


def get_max(citations):
    max_citation = 0
    for citation in citations:
        if citation > max_citation:
            max_citation = citation
    return max_citation


def calculate_articles_with_citations(citations, threshold):
    count = 0
    for citation in citations:
        if citation >= threshold:
            count += 1

    return count

if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
