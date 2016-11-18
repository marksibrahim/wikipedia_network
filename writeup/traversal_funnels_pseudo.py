"""
Pseudo Code for Traversal Funnels

Reviewer Comments
Reviewer #1: I am not fully satisfied with the updates that the authors have provided. After taking into account the comments by Reviewer 2, many of which are valid concerns, I would like to see another revision addressing the following two points.

(a) Present in an algorithm form,  the steps that the authors used to compute the "Traversal-Funnel" based influence measure instead of a descriptive discussion. Comment on the running time complexity of the same.
(b) Please double check the eigenvector centrality values. Normally the eigenvector corresponding to the top eigenvalue is selected and the entires are all non-negative. There are some negative entries present in the values shown.

Reviewer #2: I am satisfied with the modifications made and the author response.  I would suggest adding something to the introduction pointing out that you are introducing the new notion of traversal funnels, and make it a bit more prominent that this is a novel measure you have created.
"""


class Article():
    funnels = 0
    in_cycle = False

    title = ""
    first_link = article

    def discover_cycle(self):
        """determines whether the current article is in a cycle"""
        article = self.first_link
        while article.title != self.title and article.first_link:
            article = article.first_link
        if article.title == self.title:
            return True
        return False

# 1. Determine Cycles
for article in Graph:
    # O(n)
    article.discover_cycle()
    # worst case: O(n)

# 2. Compute Traversal Funnels
for article in Graph:
    # O(n)
    while not article.in_cycle:
        # worst case: O(n)
        article.funnels += 1
        article = article.first_link

# Complexity: O(2n^2) = O(n^2)
#  and no auxilary memory
    # For a graph with small cycles (fixed number of cycles, independent of n)
        # O(n) (for a graph with a maximum number of cycles, say 5)

# Paper Version
    # Include Article class in appendix 
    # Describe Graph as an iterable data structure containing articles
# 1. Determine Cycles (detailed)        
for article in Graph:
    next_article = article.first_link
    # advance to next article until potential cycle
    if next_article.title != article.title and next_article:
        next_article = next_article.first_link
    # mark cycle
    if article.title == next_article.title:
        article.in_cycle = True

# 2. Compute Traversal Funnels
for article in Graph:
    # O(n)
    while not article.in_cycle:
        # worst case: O(n)
        article.funnels += 1
        article = article.first_link

