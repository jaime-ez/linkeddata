# -*- coding: utf-8 -*-

import igraph
import mechanize
from bs4 import BeautifulSoup
from igraph import Graph
import subprocess

def prettify(br, response, encoding):
    soup = BeautifulSoup(response.get_data())
    data = soup.prettify().encode(encoding)
    response.set_data(data)
    br.set_response(response)

def content(br, response):
    html=""
    soup = BeautifulSoup(response.get_data())

    tag = soup.find_all('div', {"id":"mw-content-text"})
    for t in tag:
        html=html+str(t)
    response.set_data(html)
    br.set_response(response)

class Robot:

    def __init__(self):
        self.br = mechanize.Browser(factory=mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008\
071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.graph = Graph(0, directed=True)
        self.urls = {}
        self.path = []

    def draw(self, file_name):
        self.graph.write_dot(file_name)

    def add_node(self):
        if self.br.viewing_html():
            url = self.br.response().geturl()
            title=self.br.title()
            salida=open('salida3.txt','a')
            if url not in self.urls:
                node_label = len(self.graph.vs)
                output=str(node_label)+"; "+str(title)+"; "+str(url)
                print output
                salida.write(output+'\n')
                self.urls[url] = node_label
                self.graph.add_vertices(1)
            else:
                node_label = self.urls[url]
            self.path.append(node_label)
            if len(self.path) > 2:
                self.graph.add_edges([(self.path[-2], self.path[-1])])
                print self.path[-2], '->', self.path[-1]
                salida.write(str(self.path[-2])+', ->'+str(self.path[-1])+' \n')
            salida.close()

    def browse(self, url, n):
        self.br.open(url)
        self.add_node()
        self.visit_node(n)

    def visit_node(self, n):

        prettify(self.br, self.br.response(), 'UTF-8')
        self.add_node()
        content(self.br, self.br.response())
        if n > 1:
            for link in self.br.links():
                if link.url not in self.urls:
                    #print str(link.url)
                    #print "ojo"
                    if "wiki" in str(link.url) and not "#cite_" in str(link.url) and not "action=edit" in str(link.url):
                        #print link.url
                        #print "pes"
                        if self.br.viewing_html():
                            try:
                                self.br.follow_link(link)
                                self.visit_node(n-1)
                            except:
                                pass
        if self.path:
            self.path.pop()
        if len(self.br._history._history[:]) > 0:
            self.br.back()

robot = Robot()
robot.browse('http://es.wikipedia.org/wiki/Web', 3)

robot.draw("g.dot")
subprocess.call(["dot", "g.dot", "-Tpdf", "-og.pdf"])
