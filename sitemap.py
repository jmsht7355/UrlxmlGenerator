import time
 
date=time.strftime('%Y-%m-%d',time.localtime())
 
list=[url.strip() for url in open('url.txt').readlines()]
 
 
class sitemaps:
    def __init__(self):
        self.n=1
 
    def name(self,c):
        opxml=open('sitemap%s.xml'%c,'a')
        opxml.write('''<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n''')
        return opxml
 
 
    def make(self,urllist):
        xmldata=self.name(self.n)
         
    #     print '''<?xml version="1.0" encoding="utf-8"?>
    # <urlset>'''
        m=0
        for i in urllist:
            i=i.strip()
            m+=1
            sitemaps='''    <url>
        <loc>'''+str(i)+'''</loc>
        <lastmod>'''+date+'''</lastmod>
        <priority>0.8</priority>
        <changefreq>hourly</changefreq>
    </url>\n'''
            xmldata.write(sitemaps)
 
            # print sitemaps
            if m==50000:
                self.n+=1
                xmldata.write('</urlset>\n')
                xmldata=self.name(self.n)
                m=0
                 
            else:
                pass
        xmldata.write('</urlset>\n')
        # print '</urlset>'
 
 
if __name__ == '__main__':
    p=sitemaps()
    p.make(list)