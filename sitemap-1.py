import time
 
date=time.strftime('%Y-%m-%d',time.localtime())
 
list=[url.strip() for url in open('url.txt').readlines()]
 
 
class sitemaps:
    def __init__(self):
        self.n=1
 
    def name(self,c):
        opxml=open('sitemap%s.xml'%c,'a')
        opxml.write('''<?xml version="1.0" encoding="utf-8"?>
<sitemapindex >\n''')
        return opxml
 
 
    def make(self,urllist):
        xmldata=self.name(self.n)
         
    #     print '''<?xml version="1.0" encoding="utf-8"?>
    # <sitemapindex>'''
        m=0
        for i in urllist:
            i=i.strip()
            m+=1
            sitemaps='''    <sitemap>
        <loc>'''+str(i)+'''/sitemap_1.xml</loc>
        <lastmod>'''+date+'''</lastmod>
    </sitemap>\n'''
            xmldata.write(sitemaps)
 
            # print sitemaps
            if m==50000:
                self.n+=1
                xmldata.write('</sitemapindex>\n')
                xmldata=self.name(self.n)
                m=0
                 
            else:
                pass
        xmldata.write('</sitemapindex>\n')
        # print '</sitemapindex>'
 
 
if __name__ == '__main__':
    p=sitemaps()
    p.make(list)