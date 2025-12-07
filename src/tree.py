from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_word: bool = False

class Trie:
    def __init__(self):
        self._root = TrieNode()
        self._size = 0

    def insert(self, word: str) -> None:
        word = word.strip().lower()
        node = self._root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        if not node.is_word:
            node.is_word = True
            self._size += 1

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str, limit: Optional[int] = None) -> List[str]:
        prefix = prefix.lower().strip()
        node = self._find_node(prefix)
        if node is None:
            return []

        results = []
        self._collect(node, prefix, results, limit)
        return results

    def delete(self, word: str) -> bool:
        word = word.lower().strip()
        deleted = False

        def _delete(node: TrieNode, index: int) -> bool:
            nonlocal deleted
            if index == len(word):
                if not node.is_word:
                    return False
                node.is_word = False
                deleted = True
                return len(node.children) == 0

            ch = word[index]
            child = node.children.get(ch)
            if not child:
                return False

            should_delete = _delete(child, index + 1)

            if should_delete:
                del node.children[ch]
                return not node.is_word and len(node.children) == 0

            return False

        _delete(self._root, 0)

        if deleted:
            self._size -= 1

        return deleted

    def size(self) -> int:
        return self._size

    def __len__(self):
        return self._size

    def load_from_file(self, path: str) -> int:
        added = 0
        with open(path, "r") as f:
            for line in f:
                before = self._size
                self.insert(line.strip())
                if self._size > before:
                    added += 1
        return added

    def _find_node(self, text: str) -> Optional[TrieNode]:
        node = self._root
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def _collect(self, node: TrieNode, prefix: str, out: List[str], limit: Optional[int]):
        if limit is not None and len(out) >= limit:
            return

        if node.is_word:
            out.append(prefix)

        for ch, child in node.children.items():
            if limit is not None and len(out) >= limit:
                return
            self._collect(child, prefix + ch, out, limit)
