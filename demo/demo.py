'''demo program for kevin bacon'''
import sys
import degrees_of_kb  # pylint: disable=import-error,wrong-import-position
sys.path.insert(0, "..")


def main():
    '''main function for the program to scrape'''

    k_b = degrees_of_kb.KevinBacon6Degrees("/wiki/Six_Degrees_of_Kevin_Bacon")
    k_b.generate_6_degrees()
    k_b.get_summary_as_list()
    k_b.get_summary_as_json()


if __name__ == "__main__":
    main()
