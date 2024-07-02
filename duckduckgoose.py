import requests
import duckdb
import json
from tld import get_tld

def get_ducks():
    print("----------------------------------------------")
    print("|                                             |")
    print("|                                             |")
    print("|                                             |")
    print("|              DUCK, DUCK, GOOSE!             |")
    print("|                                             |")
    print("|        Simple asset discovery tool using    |")
    print("|               crt.sh and duckdb             |")
    print("|                  created by                 |")
    print("|                 CHALKINGCODE                |")
    print("|                                             |")
    print("|                                             |")
    print("----------------------------------------------")

    # Asking for domain to search against
    domain = input("What is your domain, please enter value: ")
    print("\nThanks for using duckduckgoose we are now looking for your ducks\n")
    res = get_tld(f"https://{domain}", as_object=True)
    base_domain = res.fld
    # Grabbing Results and returning in json format
    get_data = requests.get(f"https://crt.sh/?q={base_domain}&output=json")
    json_response = get_data.json()

    # Serializing json
    json_object = json.dumps(json_response, indent=4)

    file = f"{base_domain}_duck.json"
    # Writing to our json file
    with open(file, "w") as outfile:
        outfile.write(json_object)
    get_geese(file)
    more_results = input("\nWould you like to select other fields type (yes or no)? ")
    while more_results == "yes":
        test = input("\nare you sure you want to continue to select more fields (yes or no)? ")
        if test == "no":
            break
        else:
            get_geese(file)

def get_geese(file):
    # asking what exact fields you want to select
    print("Name of all the fields that data is returned for\n")
    print("""\n──────────────┬──────────────────────┬──────────────────────┬─────────────────────────────────┬─────────────┬─────────────────────────┬─────────────────────┬─────────────────────┬──────────────────────────────────────────┬──────────────┐
│ issuer_ca_id │     issuer_name      │     common_name      │           name_value            │     id      │     entry_timestamp     │     not_before      │      not_after      │              serial_number               │ result_count │
│    int64     │       varchar        │       varchar        │             varchar             │    int64    │         varchar         │       varchar       │       varchar       │                 varchar                  │    int64     │
    \n""")
    what_results = input("\nWhat fields are you looking to select in paticular type * to see  all or  example common_name, if multiple comma seperate, if you would like to see all fields type *. ")

    # Using duckdb to extract/filter data from json file instead of writing a for loop out. Duckdb is awesome and you can learn more about it here https://duckdb.org/"
    results = duckdb.sql(f"SELECT {what_results} FROM {file}")
    the_result = print(results)
    return(the_result)

get_ducks()
