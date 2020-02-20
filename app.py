from flask import Flask, render_template, request, jsonify
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    url = request.json['url']
    parsed_uri = urlparse(url)

    contents = urllib.request.urlopen(url).read()

    author = ''
    soup = BeautifulSoup(contents)
    authors = soup.findAll("meta", {"name" : "author"})
    if authors.__len__() >= 1:
        author = authors[0]["content"]

    title = soup.find('title').text
    shortName = parsed_uri.netloc
    now = datetime.datetime.now()

    bibtex = 'website:' + shortName + ',\n'
    if author: bibtex += '   author = {' + author + '},\n'
    bibtex += '   title = {' + title + '},\n'
    bibtex += '   year = {' + str(now.year) + '},\n'
    bibtex += '   howpublished  = {\\url{' + url + '}},\n'
    bibtex += '   note  = {Online; accessed ' + str(now.day) + '-' + now.strftime("%B") + '-' + str(now.year) + '}\n'

    bibitem = '\\bibitem{website:'+ shortName + '} ' + author + '. ' + title +'. (' + str(now.year) + '), \\url{' + url + '}, Online; accessed ' + str(now.day) + '-' + now.strftime("%B") + '-' + str(now.year)

    sample = author + '. <em>' + title + '</em>. <tt><a href="' + url + '">' + url +'</a></tt>, ' + str(now.year) + '. [Online; accessed ' + str(now.day) + '-' + now.strftime("%B") + '-' + str(now.year) + ']'

    return jsonify(['@misc{{{0}}}'.format(bibtex), bibitem, sample])

if __name__ == '__main__':
    app.run()