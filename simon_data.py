# Simon Data:
import requests
import json

# Implementation
# Store response of 10 shops
def get_response(each_shop,api_token):
    # for each_shop in list_shops:
    url = "https://openapi.etsy.com/v2/shops/"+ each_shop +"/listings/active?api_key="+ api_token
    response = requests.get(url).json()['results']
    return response

# Retrieve each shop's listing title and description and store in dictionary, 
# example {"shopname":{"listing_id":{"title":"","description":""}}}}
def get_title_description(response):
    listing = {}
    for i in response:
        listing[i['listing_id']] = {'title': i['title'], 'description': i['description']}
    return listing

# Count the freq of words in title and decription and extract words with count > 1
def get_frequency(shop_listing):
    title_counts = {}
    description_counts = {}
    
    for k, v in shop_listing.items():
        for each_k, each_v in v.items():
            if each_k == 'title':
                split_title = each_v.split(" ")
                for word in split_title:
                    title_counts[word] = title_counts.get(word, 0) + 1
            if each_k == 'description':
                split_description = each_v.split(" ")
                for word1 in split_description:
                    description_counts[word1] = description_counts.get(word1, 0) + 1
        title_result = get_words(title_counts)
        description_result = get_words(description_counts)
    return title_result,description_result

def get_words(counts):
    return [word for word in counts if counts[word] > 1 and len(word)>4 and word.isalpha()]

# Find common words from title and description
def common(lst1, lst2): 
    return list(set(lst1) & set(lst2))

def main():
    list_shops = ["Beads2string", "TeresasCeramics", "gallery28", 
    "CreaseStudio", 
    "sugarplumcottage",
    "ChristiCreations", 
    "YanaDee", 
    "creativerags",
    "PipsyShop", 
    "tycaalak", ]
    try:
        val = input("Enter your api token: ")
        if not val:
            val = '4kpf96rrgoruwjvo4ok3w5c0'
        api_token = str(val)
        final_result = {}
        for i in list_shops:
            print ("please wait while program gets results")
            response = get_response(i, api_token)
            shop_listing = get_title_description(response)    
            freq_title, freq_description = get_frequency(shop_listing)
            common_words=common(freq_title,freq_description)
            final_result[i] = common_words[:5]
        print (json.dumps(final_result))
    except ValueError:
        print ("invalid token")
if __name__ == "__main__":
    main()


 