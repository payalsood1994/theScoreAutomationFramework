import time
from utils import util
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver.common.touch_action import TouchAction
from utils.locators.android_locators import *


class TeamsPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.team_page_locator = TeamPageLocators

    def verify_team_page(self):
        """
        This method will verify the elements of team screen and also matches them with expected values
        :return:
        """
        time.sleep(10)
        assertion_failures = []
        util.is_element_present(self.driver, self.team_page_locator.TEAM_IMAGE_ICON, 10)
        team_name = util.get_text_from_element(self.driver, self.team_page_locator.TEAM_TEXT_NAME)
        if not team_name == TestData.TEAM:
            assertion_failures.append(
                "Team Name %s in Players screen doesn't match searched team %s"
                % (team_name, TestData.TEAM)
            )
        util.is_element_present(self.driver, self.team_page_locator.TEAM_NEWS_SUBNAV, 10)
        util.is_element_present(self.driver, self.team_page_locator.TEAM_CHAT_SUBNAV, 10)
        util.is_element_present(self.driver, self.team_page_locator.TEAM_SCHEDULE_SUBNAV, 10)
        util.is_element_present(self.driver, self.team_page_locator.TEAM_ROSTER_SUBNAV, 10)
        util.is_element_present(self.driver, self.team_page_locator.TEAM_INFO_SUBNAV, 10)

    def click_on_info_sub_navigation(self):
        """
        Click on Info sub Navigation on Teams Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.team_page_locator.TEAM_INFO_SUBNAV, 10)

    def click_on_chat_sub_navigation(self):
        """
        Click on Chat sub Navigation on Teams Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.team_page_locator.TEAM_CHAT_SUBNAV, 10)

    def click_on_schedule_sub_navigation(self):
        """
        Click on schedule sub Navigation on Teams Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.team_page_locator.TEAM_SCHEDULE_SUBNAV, 10)

    def click_on_roster_sub_navigation(self):
        """
        Click on roster sub Navigation on Teams Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.team_page_locator.TEAM_ROSTER_SUBNAV, 10)

    def click_on_news_sub_navigation(self):
        """
        Click on news sub Navigation on Teams Screen
        :return:
        """
        util.wait_for_element_and_click(self.driver,self.team_page_locator.TEAM_NEWS_SUBNAV, 10)
