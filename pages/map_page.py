import re
from playwright.sync_api import Page
from utils import custom_logger as cl

class MapPage:
    COORDINATE_PATTERN = re.compile(
        r"\d+°\s\d+′\s\d+″\s[NS]\s\d+°(?:\s\d+′\s\d+″)?\s[EW]"
    )

    def __init__(self, page: Page):
        self.page = page
        self.popup_selector = "div.ol-popup"          # Popup container
        self.coordinate_selector = "#popup-content code"  # Popup text container
        self.map_selector = "div.ol-viewport"         # Map container for clicking
        self.pop_close = "#popup-closer"
        self.logger = cl.customLogger()

    def click_map_offset(self, offset_x_ratio, offset_y_ratio):
        try:
            map_element = self.page.locator(self.map_selector)
            box = map_element.bounding_box()
            if box is None:
                self.logger.error("Map element not visible")
                raise Exception("Map element not visible")

            # Calculate click coordinates
            click_x = box["x"] + box["width"] * offset_x_ratio
            click_y = box["y"] + box["height"] * offset_y_ratio

            self.logger.info(f"Clicking at offset ratios x: {offset_x_ratio}, y: {offset_y_ratio}")
            self.page.mouse.click(click_x, click_y)
        except Exception as e:
            self.logger.exception(f"Error clicking on map at offsets x: {offset_x_ratio}, y: {offset_y_ratio}")
            raise

    def get_popup_text(self):
        try:
            self.page.wait_for_selector(self.popup_selector, timeout=3000)
            text = self.page.locator(self.coordinate_selector).inner_text()
            self.logger.debug(f"Popup text retrieved: {text}")
            return text
        except Exception as e:
            self.logger.exception("Failed to retrieve popup text")
            raise

    def popup_text_matches_coordinates(self):
        try:
            text = self.get_popup_text()
            match = bool(self.COORDINATE_PATTERN.search(text))
            if match:
                self.logger.info("Popup text matches coordinate pattern")
            else:
                self.logger.warning("Popup text does not match coordinate pattern")
            return match
        except Exception as e:
            self.logger.exception("Error matching popup text to coordinate pattern")
            return False

    def close_popup(self):
        try:
            self.page.locator(self.pop_close).click()
            self.logger.info("Popup closed successfully")
        except Exception as e:
            self.logger.warning("Failed to close popup")