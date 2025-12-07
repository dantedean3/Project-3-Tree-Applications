import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from tree import Trie

def test_insert_search():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("apples")

def test_prefix():
    trie = Trie()
    trie.insert("apple")
    trie.insert("application")

    words = trie.get_words_with_prefix("app")
    assert "apple" in words
    assert "application" in words

def test_delete():
    trie = Trie()
    trie.insert("apple")
    trie.delete("apple")
    assert not trie.search("apple")
