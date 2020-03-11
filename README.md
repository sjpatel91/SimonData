# SimonData

#### Web UI
  - Please wait for 2-3 sec
[http://patelsj35.pythonanywhere.com/]
#### CLI 
python simon_data.py
#### Code involves few sections:
  - You can enter your api-token(handles invalid input) or default is set 
  - List of shops(10) are declared
  - Implementation
      - For each shop, 
        - Stored title and description for each listing_id
        - Extracted words with following conditions for each listing's title and description
            - Conditions: 
                - count of frequency > 1, 
                - word consists of only alphabets, 
                - lenghth of word > 4(removing is, are, to types of words)  
        - Find common words from title and description
        - Return only first 5 of the result

#### Improve
- Would work more on reducing time and space complexity,
- finding more meaningful words