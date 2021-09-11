import requests
from string import ascii_letters
from random import choice


def add_one(number):
    return number + 1

def Encrypt_Refresh(token):
    front = ''
    back = ''
    for i in range(450):
        front += choice(ascii_letters)
    for j in range(640):
        back += choice(ascii_letters)
    refresh = front + token + back 
    return refresh

def Extractor(token):
    return token[450:][:-640]

def API_call(token):
    print('Using cached tokens')
    url1 = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
              "Accept": "application/json",
              "Authorization": "Basic QUI1NjJrYUdVSE1UN2praVF2UFppcnRJQVNyajlmTFl5VXlab2ZmcXUwaXJkRE5PNDE6bTVxVHNSbDZxVlF0S2JIM25kRjhBU1RlYkNZUEdZeGFFWVRYb2RWNQ=="}
    
    payload = {"grant_type": "refresh_token","refresh_token":token}
    response = requests.post(url1, headers = headers,data=payload)
    api_token = response.json()['refresh_token']
    api_access = response.json()['access_token']
    return api_token, api_access
          
#Generate Refresh Tokens
def Get_Refresh():
    try:
        #Check cache for existing tokens
        with open(r'./__pycache__/repo1.txt','r') as file1:
            refresh = file1.read()
        with open(r'./__pycache__/repo2.txt','r') as file2:
            access = file2.read()
        gen_token = Extractor(refresh)
        gen_access = Extractor(access)
    except:
        print("Tokens from cache FAILED")
        #Manually input tokens if not cached
        try:
            gen_token = input("Input new REFRESH token from Intuit Dev site")
            #gen_access = input("Input new ACCESS token from Intuit Dev site")            
        except:
            print("Tokens not valid.  Try again from Intuit Dev site")
    try:
        #Use gen_token and gen_access to make api call
        api_token, api_access = API_call(gen_token)[0], API_call(gen_token)[1]
    except:
        #If cached tokens are invalid manually enter and retry the call
        print("Error, problem with refresh token. Enter Tokens from Intuit Dev site")
        gen_token = input("Input new REFRESH token from Intuit Dev site")
        #gen_access = input("Input new ACCESS token from Intuit Dev site")
        api_token, api_access = API_call(gen_token)[0], API_call(gen_token)[1]
    
    #compare cached or input tokens, with returned tokens from api call
    if gen_token == api_token and gen_access == api_access:
        pass
    else:
        print('Tokens exchanged')
        crypt_refresh = Encrypt_Refresh(api_token)
        crypt_access = Encrypt_Refresh(api_access)
        with open(r'./__pycache__/repo1.txt','w') as file:
            file.write(crypt_refresh)
            file.close()
        with open(r'./__pycache__/repo2.txt','w') as file2:
            file2.write(crypt_access) 
            file2.close()
        print('Tokens saved')


    return api_token, api_access
if __name__ == "__main__":
    print('Excuted as main file')
    
else:
    print ("Executed when imported")