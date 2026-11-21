"""Structural smoke checks; no browser/layout/contrast claims. Stdlib only."""
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.captions = []
        self.in_caption = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == 'figcaption':
            self.in_caption = True
            self.captions.append('')
    def handle_endtag(self, tag):
        if tag == 'figcaption': self.in_caption = False
    def handle_data(self, data):
        if self.in_caption: self.captions[-1] += data

def check():
    for name, count in [('hero-readability', 1), ('ordered-photo-captions', 7)]:
        directory = ROOT / 'skills' / name
        skill = (directory / 'SKILL.md').read_text()
        assert skill.startswith('---\nname: ' + name + '\n'), name
        assert '\ndescription: ' in skill
        text = (directory / 'assets' / 'example.html').read_text()
        doc = Document(text)
        assert any(t == 'html' and a.get('lang') == 'en' for t, a in doc.elements)
        assert any(t == 'meta' and a.get('name') == 'viewport' for t, a in doc.elements)
        images = [a for t, a in doc.elements if t == 'img']
        assert len(images) == count
        for image in images:
            assert image['src'].startswith('data:image/svg+xml,')
            svg = ET.fromstring(unquote(image['src'].split(',', 1)[1]))
            assert int(svg.attrib['width']) == int(image['width'])
            assert int(svg.attrib['height']) == int(image['height'])
            assert image.get('alt') == ''  # deliberately decorative synthetic swatches
        assert not any(t in ('script', 'iframe') for t, a in doc.elements)
        ids = [a['id'] for t, a in doc.elements if 'id' in a]
        assert len(ids) == len(set(ids))
        for tag, attrs in doc.elements:
            if tag == 'a' and attrs.get('href', '').startswith('#'):
                assert attrs['href'][1:] in ids
            if 'aria-labelledby' in attrs:
                assert all(i in ids for i in attrs['aria-labelledby'].split())
        if name == 'hero-readability':
            assert not doc.captions
            assert images[0].get('loading') == 'eager'
            assert 'pointer-events:none' in text and 'z-index:2' in text
        else:
            assert len(doc.captions) == 7
            assert [c.split('.')[0] for c in doc.captions] == ['1','2','3','1','2','3','4']
            assert ':last-child:nth-child(odd)' in text
            assert 'margin:0' in text and 'overflow-wrap:anywhere' in text
            assert re.search(r'grid-template-columns:repeat\(2,minmax\(0,1fr\)\)', text)
        print(f'PASS {name}: structural checks ({count} inline SVG images)')

if __name__ == '__main__': check()
