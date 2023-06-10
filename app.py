import requests
from bs4 import BeautifulSoup
# pip install requests 
# pip install beautifulsoup4 

# In this file:
# trying to extract film data from letterboxd.com
# result...
# letterboxd page content is generated dynamically
# on to other methods

# function to fetch and parse the web page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        print(f"Failed to fetch page: {url}")
        return None
    
# function to extract film data from a web page
def extract_film_data(page):
    film_data = []
    # film_elements = page.select(".film-poster-link")
    film_elements = page.find_all("div", class_="react-component")

    for element in film_elements:
        
        for element in film_elements:
            link_element = element.find("a", class_="frame-title")
            film_name = link_element.get_text(strip=True) if link_element else None
            if film_name:
                film_data.append(film_name)


        # try:
        #     film_name = element["data-film-name"]
        #     film_data.append(film_name)
        # except KeyError:
        #     pass
    
        # title = element.find("img")["alt"]        
        # director = element.select_one(".text-slug").text
        # poster_image = element.find("img")["src"]

        # film_data.append({
        #     "title": title,
        #     "director": director,
        #     "poster_image": poster_image
        # })
    return film_data

# main function
def main():
    base_url = "https://letterboxd.com/films/decade/"
    # decades = ["1920s/", "1930s/", "1940s/"]
    decades = ["1940s/"]

    for decade in decades:
        url = base_url + decade
        print(f"url: {url}")
        page = fetch_page(url)   
        # print(page.prettify())

        # Write HTML content to a text file
        # with open("output1.html", "w", encoding="utf-8") as file:
        #     file.write(page.prettify())
        # print("HTML content saved to 'output1.html' file.")

        if page:
            film_data = extract_film_data(page)
            # print(film_data)

            # for film in film_data:
                # print("Title:", film["title"])
                # print("Director:", film["director"])
                # print("Poster Image:", film["poster_image"])
                # print("---")
        for film_name in film_data:
            print("Film Name:", film_name)

        if len(film_data) == 0:
            print("nada")

# run the main function
if __name__ == "__main__":
    main()