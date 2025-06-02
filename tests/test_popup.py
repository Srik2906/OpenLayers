import pytest
import random
from pages.map_page import MapPage


@pytest.mark.usefixtures("setup")
class TestPopUp:

    @pytest.fixture(autouse=True)
    def classSetup(self,setup):
        self.map_page = MapPage(self.page)


    def test_popup_coordinates(self):
        # Click near center of the map (adjust x,y as needed)
        self.map_page.click_map_offset(offset_x_ratio=random.random(), offset_y_ratio=random.random())
        # Assert popup text matches coordinate pattern
        assert self.map_page.popup_text_matches_coordinates(), "Popup text does not match coordinate pattern"
        self.map_page.close_popup()
