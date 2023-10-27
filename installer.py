import os

def ask_api_key(api_name):
    print("Enter " + api_name + " API Key (leave blank to skip): ")
    api_key = input()
    return api_key

def main():
    os.system("git clone https://github.com/lanmaster53/recon-ng.git")
    os.system("cd recon-ng")
    os.system("pip install -r REQUIREMENTS")

    print("Recon-ng installed!\n")

    bing_api = ask_api_key("Bing API Key")
    builtwith_api = ask_api_key("BuiltWith API Key")
    censysio_id = ask_api_key("Censys API Key")
    censysio_secret = ask_api_key("Censys API Secret")
    flickr_api = ask_api_key("Flickr API Key")
    google_api = ask_api_key("Google API Key (has YouTube Data API, Custom Search API andMaps JavaScript API enabled)")
    google_cse = ask_api_key("Google Custom Search Engine (CSE) ID")
    github_api = ask_api_key("Github API Key (you don't need to give the token any permissions)")
    hashes_api = ask_api_key("Hashes.org API Key")
    ipinfodb_api = ask_api_key("IPInfoDB API Key")
    jigsaw_api = ask_api_key("Jigsaw API Key")
    pwnedlist_api = ask_api_key("PwnedList API Key")
    pwnedlist_iv = ask_api_key("PwnedList Initialization Vector")
    pwnedlist_secret = ask_api_key("PwnedList Secret")
    shodan_api = ask_api_key("Shodan API Key")
    twitter_api = ask_api_key("Twitter Consumer Key")
    twitter_secret = ask_api_key("Twitter Consumer Secret")
    virustotal_api  = ask_api_key("Virus Total API Key")

    print("Applying API Keys\n")
    os.system("./recon-ng")
    
    os.system("keys add bing_api " + bing_api)
    os.system("keys add builtwith_api " + builtwith_api)
    os.system("keys add censysio_id " + censysio_id)
    os.system("keys add censysio_secret " + censysio_secret)
    os.system("keys add flickr_api " + flickr_api)
    os.system("keys add google_api " + google_api)
    os.system("keys add google_cse " + google_cse)
    os.system("keys add github_api " + github_api)
    os.system("keys add hashes_api " + hashes_api)
    os.system("keys add ipinfodb_api " + ipinfodb_api)
    os.system("keys add jigsaw_api " + jigsaw_api)
    os.system("keys add pwnedlist_api " + pwnedlist_api)
    os.system("keys add pwnedlist_iv " + pwnedlist_iv)
    os.system("keys add pwnedlist_secret " + pwnedlist_secret)
    os.system("keys add shodan_api " + shodan_api)
    os.system("keys add twitter_api " + twitter_api)
    os.system("keys add twitter_secret " + twitter_secret)
    os.system("keys add virustotal_api " + virustotal_api)

    print("API Keys applied!\n")

    print("Add recon-ng to /usr/bin? (Y/n)\n")
    add_to_bin = input()
    if add_to_bin.lower() == "y":
        os.system("cp ./recon-ng /usr/bin/recon-ng")
        print("Recon-ng added to /usr/bin!\n")

if __name__ == "__main__":
    main()