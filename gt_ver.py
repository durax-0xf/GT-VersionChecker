#Growtopia version
#new = current version
def vers(age = 'new'):
    if(age == 'new'): #working on a previous version checker. Will update if i ever find out how.
        from google_play_scraper import app
        res = app(
        'com.rtsoft.growtopia',
        lang='en',
        country='us'
        )
        out = res.get('version')
        return float(out)
