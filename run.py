from bs4 import BeautifulSoup
from flask import Flask,render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results/page=1')
def results():
    term = 'Hotel'
    location = 'UK'
    url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=' \
          + term + \
          '&location=' + \
          location + \
          '&scrambleSeed=509559697&pageNum='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    hitung = 0
    datas = []
    for page in range(1, 2):
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        product = soup.findAll('div', 'row businessCapsule--mainRow')
        for x in product:
            name = x.find('span', 'businessCapsule--name').text.strip()
            street = x.find('span', {'itemprop': 'streetAddress'})
            local = x.find('span', {'itemprop': 'addressLocality'})
            post = x.find('span', {'itemprop': 'postalCode'})
            telp = x.find('span', 'business--telephoneNumber')
            web = x.find('a', {'rel': 'nofollow noopener'})
            if web == None:
                continue
            if street == None:
                continue
            if local == None:
                continue
            if post == None:
                continue
            if telp == None:
                continue
            street = street.text.strip()
            local = local.text.strip()
            post = post.text.strip()
            telp = telp.text.strip()
            address = street+' '+local
            web = web['href'].split('?')[0].replace('https://', '').replace('http://', '').replace('http:',
                                                                                                   '').replace(
                '/', '').replace('www.', '').strip()
            hitung += 1
            datas.append([hitung, name, address, post, telp, web])
    return render_template('results.html', datas=datas, term=term, location=location)
@app.route('/results/page=2')
def results2():
    term = 'Hotel'
    location = 'UK'
    url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=' \
          + term + \
          '&location=' + \
          location + \
          '&scrambleSeed=509559697&pageNum='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    hitung = 0
    datas = []
    for page in range(2, 3):
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        product = soup.findAll('div', 'row businessCapsule--mainRow')
        for x in product:
            name = x.find('span', 'businessCapsule--name').text.strip()
            street = x.find('span', {'itemprop': 'streetAddress'})
            local = x.find('span', {'itemprop': 'addressLocality'})
            post = x.find('span', {'itemprop': 'postalCode'})
            telp = x.find('span', 'business--telephoneNumber')
            web = x.find('a', {'rel': 'nofollow noopener'})
            if web == None:
                continue
            if street == None:
                continue
            if local == None:
                continue
            if post == None:
                continue
            if telp == None:
                continue
            street = street.text.strip()
            local = local.text.strip()
            post = post.text.strip()
            telp = telp.text.strip()
            address = street+' '+local
            web = web['href'].split('?')[0].replace('https://', '').replace('http://', '').replace('http:',
                                                                                                   '').replace(
                '/', '').replace('www.', '').strip()
            hitung += 1
            datas.append([hitung, name, address, post, telp, web])
    return render_template('results2.html', datas=datas, term=term, location=location)
@app.route('/results/page=3')
def results3():
    term = 'Hotel'
    location = 'UK'
    url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=' \
          + term + \
          '&location=' + \
          location + \
          '&scrambleSeed=509559697&pageNum='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    hitung = 0
    datas = []
    for page in range(3, 4):
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        product = soup.findAll('div', 'row businessCapsule--mainRow')
        for x in product:
            name = x.find('span', 'businessCapsule--name').text.strip()
            street = x.find('span', {'itemprop': 'streetAddress'})
            local = x.find('span', {'itemprop': 'addressLocality'})
            post = x.find('span', {'itemprop': 'postalCode'})
            telp = x.find('span', 'business--telephoneNumber')
            web = x.find('a', {'rel': 'nofollow noopener'})
            if web == None:
                continue
            if street == None:
                continue
            if local == None:
                continue
            if post == None:
                continue
            if telp == None:
                continue
            street = street.text.strip()
            local = local.text.strip()
            post = post.text.strip()
            telp = telp.text.strip()
            address = street+' '+local
            web = web['href'].split('?')[0].replace('https://', '').replace('http://', '').replace('http:',
                                                                                                   '').replace(
                '/', '').replace('www.', '').strip()
            hitung += 1
            datas.append([hitung, name, address, post, telp, web])
    return render_template('results3.html', datas=datas, term=term, location=location)
@app.route('/results/page=4')
def results4():
    term = 'Hotel'
    location = 'UK'
    url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=' \
          + term + \
          '&location=' + \
          location + \
          '&scrambleSeed=509559697&pageNum='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    hitung = 0
    datas = []
    for page in range(4, 5):
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        product = soup.findAll('div', 'row businessCapsule--mainRow')
        for x in product:
            name = x.find('span', 'businessCapsule--name').text.strip()
            street = x.find('span', {'itemprop': 'streetAddress'})
            local = x.find('span', {'itemprop': 'addressLocality'})
            post = x.find('span', {'itemprop': 'postalCode'})
            telp = x.find('span', 'business--telephoneNumber')
            web = x.find('a', {'rel': 'nofollow noopener'})
            if web == None:
                continue
            if street == None:
                continue
            if local == None:
                continue
            if post == None:
                continue
            if telp == None:
                continue
            street = street.text.strip()
            local = local.text.strip()
            post = post.text.strip()
            telp = telp.text.strip()
            address = street+' '+local
            web = web['href'].split('?')[0].replace('https://', '').replace('http://', '').replace('http:',
                                                                                                   '').replace(
                '/', '').replace('www.', '').strip()
            hitung += 1
            datas.append([hitung, name, address, post, telp, web])
    return render_template('results4.html', datas=datas, term=term, location=location)

@app.route('/results/page=5')
def results5():
    term = 'Hotel'
    location = 'UK'
    url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords=' \
          + term + \
          '&location=' + \
          location + \
          '&scrambleSeed=509559697&pageNum='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    hitung = 0
    datas = []
    for page in range(5, 6):
        req = requests.get(url + str(page), headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        product = soup.findAll('div', 'row businessCapsule--mainRow')
        for x in product:
            name = x.find('span', 'businessCapsule--name').text.strip()
            street = x.find('span', {'itemprop': 'streetAddress'})
            local = x.find('span', {'itemprop': 'addressLocality'})
            post = x.find('span', {'itemprop': 'postalCode'})
            telp = x.find('span', 'business--telephoneNumber')
            web = x.find('a', {'rel': 'nofollow noopener'})
            if web == None:
                continue
            if street == None:
                continue
            if local == None:
                continue
            if post == None:
                continue
            if telp == None:
                continue
            street = street.text.strip()
            local = local.text.strip()
            post = post.text.strip()
            telp = telp.text.strip()
            address = street+' '+local
            web = web['href'].split('?')[0].replace('https://', '').replace('http://', '').replace('http:',
                                                                                                   '').replace(
                '/', '').replace('www.', '').strip()
            hitung += 1
            datas.append([hitung, name, address, post, telp, web])
    return render_template('results5.html', datas=datas, term=term, location=location)
@app.route('/how-to-use')
def how():
    return render_template('how.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)