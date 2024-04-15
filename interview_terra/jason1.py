import json
books ='''{
  "books1": [
    {
      "title": "Eloquent JavaScript, Third Edition",
      "subtitle": "A Modern Introduction to Programming",
      "author": "Marijn Haverbeke",
      "published": "2018-12-04T00:00:00.000Z",
      "publisher": "No Starch Press"
      
    }
  ],
  "books2": [
    {
      "title": "Practical Modern JavaScript",
      "subtitle": "Dive into ES6 and the Future of JavaScript",
      "author": "Nicolás Bevacqua",
      "published": "2017-07-16T00:00:00.000Z",
      "publisher": "O'Reilly Media"
      
    }
  ],
  "books3": [
    {
      "title": "Understanding ECMAScript 6",
      "subtitle": "The Definitive Guide for JavaScript Developers",
      "author": "Nicholas C. Zakas",
      "published": "2016-09-03T00:00:00.000Z",
      "publisher": "No Starch Press"
      
    }
  ]
}
'''
data = json.loads(books)
print(data)
d1={}
for i,j in data.items() :
    d1[i]=j[0]
print(d1)
import yaml
yaml_out=yaml.dump(d1)
print(yaml_out)
