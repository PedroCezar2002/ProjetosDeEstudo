url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)
acha_interrogacao = url.find('?')
url_base = url[:acha_interrogacao]
print(url_base)

url_parametros = url[acha_interrogacao+1:]
print(url_parametros)