# coding: utf-8
import markdown
import clipboard


input_file = clipboard.get()

s = input_file


md = markdown.Markdown()
html = md.convert(s)

print(html)

clipboard.set(html)
