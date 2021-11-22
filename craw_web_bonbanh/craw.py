import requests
from bs4 import BeautifulSoup
import urllib.request

link_base = 'https://bonbanh.com/oto/page,'
links = []
for i in range(1,2079):
    item = link_base+str(i)
    links.append(item)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page_count = 0
image_count = 0
# try:
if True:
    for i in range(len(links)):
        link = links[i]
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        id_content = soup.find("div", class_="g-box-content")
        ul = id_content.find_all('ul')
        
        if True:
            for li in ul[1].find_all('li'):
#                 if True:
                try:                  
                    img_color = li.find("div", class_="cb6_02")
                    for a in img_color:
                        color = str(a).split(',')[1]
                        break

                    name = li.find('h3').string
                    im = li.find('img')
                    image_url = im['src']                
                    
                    for a in li.find_all('a', href=True):
                        count_img_same = 0
                        link_img = 'https://bonbanh.com/'+a['href']
                        # print(link_img)
                        r_img = requests.get(link_img, headers=headers)
                        soup_img = BeautifulSoup(r_img.text, 'html.parser')
#                         print(soup_img.prettify())
                        #thoat
                        so_cho = soup_img.find("div",{"id":"sgg"})
                        b_row = so_cho.findAll("div", {"class": "row_last"})
                        c_row = b_row[0].find('span').text.strip()
#                         print(c_row)
                        
                
                        medimum_img = soup_img.find("div",{ "id" : "medium_img" })
                        for img_img in medimum_img.find_all('img'):
                            # print(img_img['src'])
                            #id_idsame_color_name
                            try:
#                             if True:
                                urllib.request.urlretrieve(img_img['src'], 'image/'+str(image_count)+'_'+str(count_img_same)+'_'+c_row+'_'+color+'_'+name+'.jpg')
                                image_count+=1
                            except Exception as e:
                                print("An exception occurred: ", e)
                            count_img_same += 1
                            if count_img_same == 3:
                                break
                    urllib.request.urlretrieve(image_url, 'image/'+str(image_count)+'_'+str(count_img_same)+'_'+c_row+'_'+color+'_'+name+'.jpg')
                    image_count+=1
#                     break
                except Exception as e:
                    print("An exception occurred: ", e)
        page_count+=1
        print('so luong anh la :'+ str(image_count)+ " page count "+ str(page_count))