import markdown

md_text = """
# Überschrift 1

Dies ist ein **fetter** Text und dies ist ein *kursiver* Text.

- Liste
- Mit
- Punkten

[Link zu Google](https://www.google.com)
"""

html = markdown.markdown(md_text)
print(html)
