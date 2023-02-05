from pages.landing_page import LandingPage

def test_select_all_option_check(browser):
    '''
    As a user, 
    I should be able to see the Select All checkbox under the filters Vehicle > Body Styles > Select All

    As a user, 
    When I check the Select All checkbox
    Then All other body styles should be selected.
    '''
    landing_page = LandingPage(browser)
    landing_page.load(landing_page.LANDING_PAGE_URL)

    assert landing_page.accept_and_close_cookie_window() == False

    landing_page.select_vehicle_dropdown_filter()
    landing_page.check_select_all_option()

    assert landing_page.checkboxes_status(selected=True) == True
    assert landing_page.descriptions_status(selected=True) == True


def test_select_all_option_uncheck(browser):
    '''
    As a user, 
    When I uncheck the Select All checkbox
    Then All other body styles should be unselected.
    '''
    landing_page = LandingPage(browser)
    landing_page.load(landing_page.LANDING_PAGE_URL)

    assert landing_page.accept_and_close_cookie_window() == False
    
    landing_page.select_vehicle_dropdown_filter()
    landing_page.check_select_all_option()
    landing_page.check_select_all_option()

    assert landing_page.checkboxes_status(selected=False) == True
    

def test_select_all_option_search_results_count_check(browser):
    '''
    As a user, 
    When I check the Select All checkbox
    Then Search Results count should be updated on the button "Search Results" inside the Vehicle Filter

    As a user, 
    When I check the Select All checkbox
    Then the page should filter the results on all the Body Styles 
    And the Search Results count should be updated on the top of the page.
    '''
    landing_page = LandingPage(browser)
    landing_page.load(landing_page.LANDING_PAGE_URL)

    assert landing_page.accept_and_close_cookie_window() == False
    
    default_search_count = landing_page.get_search_count(landing_page.TOTAL_SEARCH_RESULTS)
    print(f"{default_search_count=}")

    landing_page.select_vehicle_dropdown_filter()
    landing_page.check_select_all_option()

    assert landing_page.checkboxes_status(selected=True) == True

    estimated_search_count = landing_page.get_search_count(landing_page.SEARCH_RESULTS_BUTTON)
    print(f"{estimated_search_count=}")
    assert float(default_search_count) > float(estimated_search_count)

    landing_page.click_on_elem(landing_page.SEARCH_RESULTS_BUTTON)

    actual_search_count = landing_page.get_search_count(landing_page.TOTAL_SEARCH_RESULTS)
    print(f"{actual_search_count=}")
    assert estimated_search_count == actual_search_count

def test_select_all_option_search_results_count_uncheck(browser):
    '''
    As a user, 
    When I uncheck the Select All checkbox
    Then the page should display all of the results.
    '''
    landing_page = LandingPage(browser)
    landing_page.load(landing_page.LANDING_PAGE_URL)

    assert landing_page.accept_and_close_cookie_window() == False
    
    default_search_count = landing_page.get_search_count(landing_page.TOTAL_SEARCH_RESULTS)
    print(f"{default_search_count=}")

    landing_page.select_vehicle_dropdown_filter()
    landing_page.check_select_all_option()
    landing_page.check_select_all_option()

    assert landing_page.checkboxes_status(selected=False) == True

    estimated_search_count = landing_page.get_search_count(landing_page.SEARCH_RESULTS_BUTTON)
    print(f"{estimated_search_count=}")
    assert float(default_search_count) > float(estimated_search_count)

    landing_page.click_on_elem(landing_page.SEARCH_RESULTS_BUTTON)

    actual_search_count = landing_page.get_search_count(landing_page.TOTAL_SEARCH_RESULTS)
    print(f"{actual_search_count=}")
    assert estimated_search_count != actual_search_count
    assert default_search_count == actual_search_count