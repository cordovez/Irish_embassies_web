import pandas as pd
from shiny import render, ui
from shinywidgets import render_widget
from ipyleaflet import Map, Marker
from shiny.express import render
from queries import diplomats


BASE_URL = 'http://localhost:8001'
ui.panel_title("Irish Heads of Mission")


@render_widget
def diplomatic_map():
    dfa = (53.33658, -6.25953)
    center = (15.14, 18.81203)
    world = Map(center=center, zoom=2)
    pointer = Marker(location=dfa,
                     dragable=False,
                     title="Department of Foreign Affairs",
                     alt="Dublin, Ireland",
                     opacity=.3)
    return world.add(pointer)


ui.input_text("text", "Search Diplomat", "first, last, or mission...")


@render.data_frame
async def heads_of_mission():
    url = f'{BASE_URL}/diplomats'
    dip_list = diplomats.get_all(url)
    df = pd.DataFrame(dip_list)
    df["mission"] = df["mission"].str.title()

    return df[["first_name", "last_name", "mission", "mission_type"]]

# ui.panel_title("Missions")
# @render.data_frame
# async def txt():
#     url = f'{BASE_URL}/missions'
#     dip_list = diplomats.get_all(url)
#     df = pd.DataFrame(dip_list)
#     return df
