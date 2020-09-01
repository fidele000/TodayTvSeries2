from flask import Flask,render_template,jsonify
from bs4 import BeautifulSoup
from urllib.request import urlopen
app=Flask(__name__,static_url_path='')


@app.route('/')
def index():
    return render_template('index.html',**locals())

@app.route('/ajax/<where>/<num>',methods=['GET'])
def ajaxLoad(where,num):
    if where == 'home':
        num=int(num)
        html=urlopen('http://www.todaytvseries2.com/tv-series').read()
        bs=BeautifulSoup(html,features='html5lib')
        articles=bs.findAll(class_='uk-article tm-tag-10')
        #posts=list()

        return jsonify({
                    'image':articles[num].findAll('img')[0]['src'],
                    'link':articles[num].findAll('a')[0]['href'],
                    'title':articles[num].find(class_='uk-article-title1').get_text(),
                    'body':articles[num].find(class_='teasershort').get_text(),
                })
        '''
        for article in articles:
            
            posts.append({
                'image':article.findAll('img')[0]['src'],
                'link':article.findAll('a')[0]['href'],
                'title':article.find(class_='uk-article-title1').get_text(),
                'body':article.find(class_='teasershort').get_text(),
            })
            '''

@app.route('/<where>/<cont>')
def view(where,cont):
    link='http://www.todaytvseries2.com/'+where+'/'+cont
    html=urlopen(link).read()
    bs=BeautifulSoup(html,features='html5lib')
    image=bs.find(class_='uk-width-1-1 imageseries1').findAll('img')[0]['src']
    title=bs.find(class_='uk-article-title uk-badge1').get_text()

    i=0
    for well in bs.find(class_='uk-accordion uk-text-left').findAll('a'):
        print(well[i]['href'])
        i=i+1

    return render_template('view.html',**locals())
            
        
if __name__=='__main__':
    app.run()

