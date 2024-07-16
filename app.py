import pandas as pd
from shiny.express import input, render, ui
from queries.get import get_all
from shinywidgets import render_widget
import json
import requests
import os
from ipyleaflet import Map, AwesomeIcon, Marker
# from modules import map

BASE_URL = 'http://localhost:8001'
ui.panel_title("Irish Heads of Mission")


@render_widget
def diplomatic_map():
    dfa = (53.33658, -6.25953)
    center = (15.14, 18.81203)
    world = Map(center=center, zoom=2)
    star = AwesomeIcon(name="star", marker_color="green")
    pointer = Marker(icon=star,
                     location=dfa,
                     dragable=False,
                     title="Department of Foreign Affairs",
                     alt="Dublin, Ireland",
                     opacity=1)
    # world.add(geo_json)
    world.add(pointer)
    return world


ui.input_text("text", "Search Diplomat", "first, last, or mission...")


@render.data_frame
async def heads_of_mission():
    url = f'{BASE_URL}/diplomats'
    dip_list = get_all(url)
    df = pd.DataFrame(dip_list)
    df["mission"] = df["mission"].str.title()

    return df[["first_name", "last_name", "mission", "mission_type"]]



