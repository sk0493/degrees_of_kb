'''local program for kevin bacon'''
import sys
import degrees_of_kb  # pylint: disable=import-error,wrong-import-position
# sys.path.insert(0, "..")


def main(wiki_page_id):
    '''
    Receives a wiki page id, in the format: /wiki/YOUR_WIKI_PAGE_NAME and navigates
    links inside wikipedia up to 6 degrees away from that page recording the URL it
    has gone through. Note that you can get wiki_page_ids by cutting out the specific 
    portion of the wikipedia page URL, example:
     - for the page: https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon
     - the wiki_page_id variable should be: /wiki/Six_Degrees_of_Kevin_Bacon
    '''

    k_b = degrees_of_kb.KevinBacon6Degrees(wiki_page_id)
    k_b.generate_6_degrees()
    k_b.get_summary_as_list()
    result = k_b.get_summary_as_json()

    return(result)


if __name__ == "__main__":
    wiki_page_id = "/wiki/Six_Degrees_of_Kevin_Bacon"
    main(wiki_page_id)
