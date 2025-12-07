\# TREE\_DESIGN.md



\## Tree Selection

I chose the \*\*Trie (Prefix Tree)\*\* because it fits perfectly with building an autocomplete application. It is simple to understand and performs very fast lookups.



\## Use Cases

A Trie is commonly used for:

\- Autocomplete

\- Spell checking

\- Prefix searching

\- Word games

\- Predictive text



\## Properties

\- Each node represents a prefix.

\- Lookup time depends on \*\*word length\*\*, not number of words.

\- Worst-case space is O(total characters).



\## Interface Design



\### insert(word)

Time: O(m)  

Space: O(m)



\### search(word)

Time: O(m)



\### starts\_with(prefix)

Time: O(p)



\### get\_words\_with\_prefix(prefix, limit)

Time: O(p + k)



\### delete(word)

Time: O(m)



\### size()

Time: O(1)



\### load\_from\_file(path)

Time: O(n\*m)



\## Implementation Notes

The Trie uses:

\- TrieNode objects (children dictionary + is\_word flag)

\- A root node

\- Size counter



\## Evolution of the Interface

While building the CLI app, several helper methods were added:

\- `\_\_contains\_\_`

\- `\_\_len\_\_`

\- `load\_from\_file`



These changes were necessary for convenience and functionality.



