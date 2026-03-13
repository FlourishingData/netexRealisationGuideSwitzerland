# Experimental Stuff

## Pandoc

We can use Pandoc for: 
- Initial conversion of the Word document
- Conversion of Markdown to other formats for publishing

### Pandoc Installation
Install [pandoc](https://pandoc.org/installing.html).

### Word to Markdown

`pandoc NeTEx.docx -t gfm -o rg2.md --extract-media=media`

Options:
- `-t gfm`: github type. See [Markdown Github Flavour Spec](https://github.github.com/gfm/).
- `-o rg2.md` the Markdown output file
- `extract-media=media`: extract media files to directory `media`



#### Experimental Pandoc Examples

| File                                   | Type | Description                                                                                                              | 
|----------------------------------------|------|--------------------------------------------------------------------------------------------------------------------------|
| StopPlace-pandoc-gfm.md                | `gfm` | Extract from markdown created with `pandoc NeTEx.docx -t gfm -o rg2.md --extract-media=media` |
| StopPlace-pandoc-gfm-corrected.md      | `gfm` | Edited gfm example.<br/><ul><li>Tables in Markdown<li>Links to anchors                                                   |
| StopPlace-pandoc-markdown-corrected.md | `markdown` | Extract from markdown created with `pandoc NeTEx.docx -t markdown -o rg2.md --extract-media=media`                       |

 