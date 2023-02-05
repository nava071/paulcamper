## Task 1
1. Clone this repo `git clone https://github.com/nava071/paulcamper.git`
2. cd into the repo folder `cd paulcamper`
3. Create a virtual environment `pipenv install`
4. Switch to the virtual env `pipenv shell` 
5. Install the packages needed `pip install -r requirements.txt`
6. Run the tests from the root folder of the repo
`python -m pytest -s -v tests`



#### Scenarios for the "Select All" checkbox

As a user, 
I should be able to see the Select All checkbox under the filters Vehicle > Body Styles > Select All

As a user, 
When I check the Select All checkbox
Then All other body styles should be selected.

As a user, 
When I uncheck the Select All checkbox
Then All other body styles should be unselected.

As a user, 
When I check the Select All checkbox
Then Search Results count should be updated on the button "Search Results" inside the Vehicle Filter

As a user, 
When I uncheck the Select All checkbox
Then Search Results count should be updated on the button "Search Results" inside the Vehicle Filter to zero as none of the filter is selected

As a user, 
When I check the Select All checkbox
Then the page should filter the results on all the Body Styles 
And the Search Results count should be updated on the top of the page.

As a user, 
When I uncheck the Select All checkbox
Then the page should display all of the results.