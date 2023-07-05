'''
You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer , the number of lines in the HTML code snippet.
The next  lines contain HTML code.

Constraints


Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

Format your answers as explained in the problem statement.

Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
# must you Regex to parse
import re
n = int(input())
for _ in range(n):
    line = input()
    # ignore the comment tags <!--, it can be multiline
    # line = re.sub(r'<!--.*?-->', '', line)
    # ingnore mutiline commeng tags
    line = re.sub(r'<\s*!--.*?--\s*>', '', line) # still failed some test cases
    tags = re.findall(r'<\s*(\w+)', line)
    for tag in tags:
        print(tag)
    attrs = re.findall(r'(\w+)="([^"]*)"', line)
    for attr in attrs:
        print('->', attr[0], '>', attr[1])


# Use HTML Parser
# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         for attr in attrs:
#             print('->', attr[0], '>', attr[1])
# parser = MyHTMLParser()
# for _ in range(int(input())):
#     parser.feed(input())



