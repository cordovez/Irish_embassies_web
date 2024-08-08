from shiny.express import render, ui, input
from queries import get

# ------------------------------------------------------------------------
# Define user interface
# ------------------------------------------------------------------------


with ui.sidebar(bg="#006845", id="main_sidebar"):
    ui.input_selectize(id="sidebar_nav", label="Select an option",
                       choices={"go to embassies": "Embassies",
                                "go to representations": "Representations",
                                "go to bilateral": "Bilateral Diplomacy ",
                                "go to diplomats": "Diplomats",
     })

with ui.layout_columns():
    @render.data_frame
    def data():
        selection = input.sidebar_nav()
        df = get.corresponding_df(selection)
        if selection != "go to representations":
            return render.DataGrid(df, filters=True, selection_mode="rows")
        return render.DataGrid(df, selection_mode="rows")
