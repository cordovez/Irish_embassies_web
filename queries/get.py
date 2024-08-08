import requests
import pandas as pd

BASE_URL = 'http://localhost:8001'


def corresponding_df(selection: str):
    match selection:
        case "go to representations":
            return representations_df()
        case "go to bilateral":
            return bilateral_df()
        case "go to diplomats":
            return diplomats_df()
        case _:
            return embassies_df()


def diplomats_df():
    url = f'{BASE_URL}/public/diplomats'
    df = _make_df(url)
    selected = df[["last_name", "first_name", "mission_title"]]
    return selected


def representations_df():
    url = f'{BASE_URL}/public/representations'
    df = _make_df(url)
    selected = df[["rep_name", "head_of_mission"]]
    renamed = selected.rename(columns={"rep_name": "Representation",
                                       "head_of_mission": "Ambassador"})
    return renamed


def embassies_df():
    url = f'{BASE_URL}/public/embassies'
    df = _make_df(url)
    selected_cols = df[["country", "head_of_mission"]]
    renamed = selected_cols.rename(columns={"country": "Country",
                                            "head_of_mission": "Ambassador"})
    return renamed


def bilateral_df():
    url = f'{BASE_URL}/public/countries'
    df = _make_df(url)
    bi_df = df.loc[df["accredited_to_ireland"] &
                   df["hosts_irish_mission"]]
    selected_cols = bi_df[["country_name", "with_mission_in"]]
    renamed = selected_cols.rename(columns={"country_name": "Country",
                                         "with_mission_in": "Embassy location"})
    renamed["Embassy location"] = renamed["Embassy location"].str.title()
    return renamed


def _make_df(url):
    data = requests.get(url).json()
    return pd.DataFrame(data)
