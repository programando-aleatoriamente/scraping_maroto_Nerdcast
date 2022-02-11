import re, requests, glob, json

def reqtext(url):

	req = requests.get(url)
	data = req.text
	req.close()
	return data

def downloadmp3(url, name):

	req = requests.get(url)
	with open(name,'wb') as file:
		file.write(req.content)
	req.close()

def config(file):

	with open(file) as file:
		return json.loads(file.read())

def main():

	configuration = config('config.json')
	listaurls = re.findall('<link>http.*/nerdcast/.*</link>', reqtext(configuration["feed-url"]))
	listapages =[]
	listaepisodios = []

	for ind in listaurls:

		listapages.append(re.sub('<link>|</link>','',ind))

	for ind in listapages:

		objsearch = re.findall('http.*\.mp3',reqtext(ind))
		listaepisodios.append(objsearch[0])
		print(f'baixando episodio: {objsearch[0]}')
		downloadmp3(objsearch[0], f"{configuration['pasta']}{re.sub('http.*/','', objsearch[0])}")
		print(f'terminou o download do episodio: {objsearch[0]}')

if __name__ == '__main__':
	main()