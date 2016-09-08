from lxml import html
import requests

f=open('C:/Users/Raj/Desktop/movies/movieapp/criticname.txt','r')
cname= f.read()
c=open('C:/Users/Raj/Desktop/movies/movieapp/criticlist.txt','w')
d=open('C:/Users/Raj/Desktop/movies/movieapp/criticimages.txt','w')
print (cname)



                
    
def rmasand():
    url='http://www.rajeevmasand.com/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    movnames = tree.xpath('//div[@class="featuredcopy"]/h3/a/text()')
    imnames=tree.xpath('//div[@class="featuredbox"]/img/@src')
    print(imnames)
    movnames=[str(i).strip() for i in movnames]
    print(movnames)
    c.write(str(movnames))
    d.write(str(imnames))


def nypost():
    url='http://nypost.com/tag/movie-reviews/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    anames=  tree.xpath('//header[@class="entry-header"]/h3/a/@href')
    imnames=tree.xpath('//div[@class="entry-thumbnail"]/a/picture/source/@srcset')[0:4]
    imnames=[i.split(",")[0] for i in imnames]      
    print(imnames)  
    anames=[str(i).strip() for i in anames]
    
    movie=[]
    for i in range(0,4):
        url=anames[i]
        page = requests.get(url)
        tree = html.fromstring(page.content)
        movie.append(tree.xpath('//div[@class="box half-tone module inline desktop"]/h6/text()')[0])
    
    c.write(str(movie))
    d.write(str(imnames))

def metacritic():
    url='http://www.metacritic.com/movie'
    page = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    anames=  tree.xpath('//h3[@class="product_title"]/a/text()')
    #imnames= tree.xpath('//img[@class="product_image small_image"]/@src')
    #print(imnames[0:4])
    #print(str(u.content))
    inames=[]
    anames=[str(i).strip() for i in anames]
    c.write(str(anames[0:4]))
    for i in anames[0:4]:
        u=requests.get("http://www.omdbapi.com/?t="+i)
        start=u.content.decode("utf-8").index('"Poster"')
        end=u.content.decode("utf-8").index('"Metascore"')-2
        inames.append(u.content.decode("utf-8")[start:end].split(':"')[1])
    print(inames)    
    d.write(str(inames[0:4]))



def washington():
    url='https://www.washingtonpost.com/goingoutguide/movies/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    anames=  tree.xpath('//h3/a/text()')
    anames=[str(i).strip() for i in anames]
    anames_new=[]
    print(anames)
    #ord() to get ascii
    for i in anames[0:4]:
        #print (i)
        k=i.index(chr(8216))
        j=i.index(chr(8217))
        anames_new.append((i[k+1:j]))
    #c.write(str(anames_new))
    inames=[]
    print (inames)
    anames_new=[]
    anames_new=['Me Before You','Teenage Mutant Ninja Turtles','X-Men: Apocalypse','Alice Through the Looking Glass']
    c.write(str(anames_new))
    print (anames_new)
    for i in anames_new[0:4]:
        u=requests.get("http://www.omdbapi.com/?t="+i)
        start=u.content.decode("utf-8").index('"Poster"')
        end=u.content.decode("utf-8").index('"Metascore"')-2
        inames.append(u.content.decode("utf-8")[start:end].split(':"')[1])
    print(inames)
    d.write(str(inames))

def guardian():
    url='http://www.theguardian.com/film+tone/reviews'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    anames=  tree.xpath('//div[@class="fc-item__container"]/a/text()')

    anames_new=[]
    for i in anames:
        text = i.index('review')
        anames_new.append((i[0:text]))
    print (anames_new)
    #anames_new.remove("The Nice  ")       
    c.write(str(anames_new[0:4]))
    inames=[]
    for i in anames_new[0:4]:
        u=requests.get("http://www.omdbapi.com/?t="+i)
        #print(u.content)
        start=u.content.decode("utf-8").index('"Poster"')
        end=u.content.decode("utf-8").index('"Metascore"')-2
        inames.append(u.content.decode("utf-8")[start:end].split(':"')[1])
    print(inames)
    d.write(str(inames))

    

if(cname=="rajeev masand"):
    rmasand()
elif(cname=="washington"):
    washington()
elif(cname=="newyork post"):
    nypost()
elif(cname=="guardian"):
    guardian()
else:
    metacritic()





