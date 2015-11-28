import urllib

def read_text():
    file_name = "movie_quotes.txt"
    filehandler = open(file_name)
    text = filehandler.read()
    filehandler.close()
    check_profanity(text)

def check_profanity(text):
    url = "http://www.wdyl.com/profanity?q="
    check_url = url+text
    connection = urllib.urlopen(check_url)
    result = connection.read()
    print result
    connection.close()
