# Task 3:

### Assumptions:

The map shows all the listings in the current page. The factor(s) that brings a particular listing to the first page is not in the context of testing.
The map does not show all the listings grouped to a particular location. 
Even if I change the location of a listing in the current page to another country, the map should zoom out and cover that country as well.
Geolocation testing is not needed because the map shows the location of each listing.

--- 

## General test cases for Environments and Platforms:

#### Execute all the below testcases in 
1. Windows, Macos, Linux machines
	1. For each machines, execute the tests in all the major browsers Chrome, Safari, Firefox
2. Android and IOS mobiles
	1. For each mobile platform, execute the tests in all the major browsers Chrome, Safari, Firefox, default browser
#### Check the API calls for each of the below testcases

---

#### Verify if "show map" toggle is present in the search page or landing page

###### Steps
1. Navigate to https://paulcamper.com/rent.camper/
2. Look for the "show map" toggle

###### Expected Results
1. .
2. "show map" toggle should be available in the search page or landing Page


#### Verify the number of listings in the first page before and after the map is toggled on

###### Steps
1. Note down the number of listings before toggling on the map.
2. Note down the number of listings after toggling on the map.

###### Expected Results
The listings the number of listings should not be altered. The number of listings should be 24 (based on a screen of 15 inch laptop)


#### Verify if the filters applied on the page are retained after toggling on and toggling off the map feature.

###### Steps
1. Apply filters to the page before toggling on the map feature
2. Toggle on the map feature
3. Check if the filters are still applied
4. Toggle off the map feature

###### Expected Results
1. .
2. .
3. The filters should be applied on the page before and after toggling on the map feature
4. .

#### Verify if the map feature’s zoom option works

###### Steps
1. enable map feature
2. click on the zoom in icon
3. Click on the zoom out icon

###### Expected Results
1. .
2. The map should Zoom In and display the area in a more detailed view
3. The map should Zoom out and display the area in a macro level

#### Verify if the map is draggable

###### Steps
1. Click inside the map and drag the map from default position to a farther location

###### Expected Results
1. That farther location should also be shown in the map

#### Verify if the “Search when I move the map”  option works

###### Steps
1. enable map feature
2. move the map to a different location
3. check the listings  in the grid
4. Move the map to a different country

###### Expected Results
1. By default, “Search when I move the map” option  should be enabled
2. .
3. The listings should be filtered and only the listings located in the current latest map location should be shown in the page
4. A default page mentioning "no search results are found" should be displayed.

#### Verify if the “Search when I move the map” option can be unchecked

###### Steps
1. enable map feature
2. uncheck the “Search when I move the map” option
3. move the map to a different location
4. check the listings in the grid

###### Expected Results
1. .
2. .
3. .
4. The listings should be not filtered out based on the current dragged map location and all the listings should be shown in the page

#### Verify if  the map updates to show the current page listings

###### Steps
1. enable the map feature on the first page
2. check the listing present on the map
3. navigate to the second page
4. check the listing present on the map

###### Expected Results
1. .
2. The listings on the first page should be shown on the map now
3. map feature should still be shown after navigating to the second page
4. The listings on the second page should be shown on the map now

#### Verify if the rent amount of each listing on the current page is shown on the map 

###### Steps
1. enable the map feature on the first page
2. check the listing present on the map

###### Expected Results
1. .
2. The rent amount of each listings on the current page should be shown on the map now


#### Verify that always the latest rent amount of each listing on the current page is shown on the map 

###### Steps
1. enable the map feature on the first page
2. check a particular listing present on the map and its rent amount
3. Update the rent amount of a listing
4. check the rent amount of that listing on the map

###### Expected Results
The updated rent amount of of the listing on the current page should be shown on the map


#### Verify if the location of a listing shown on the current page is updated, then the map should show that latest location of that listing.

###### Steps
1. Enable the map feature
2. select a particular listing in the current page
3. update the location of that listing to a farther location or another country
4. Check if that listing is shown in the map in the latest location and the remaining listings should also be shown

###### Expected Results
1. .
2. .
3. .
4. That listing should be shown in the map in the latest location and the remaining listings should also be shown

#### Verify that the rent amount displayed in the map are clickable elements and shows a thumbnail when clicked

###### Steps
1. Enable the map feature
2. Click on a rent amount inside the map
3. Click on the thumbnail displayed

###### Expected Results
1. .
2. The corresponding listing’s thumbnail should be shown
3. The application should redirect to a new page to show the detailed.view of that listing

#### Verify that on hovering over a listing in the grid, the corresponding rent amount is highlighted in the map

###### Steps
1. Enable the map feature
2. Hover over a listing in the grid
3. check the map

###### Expected Results
1. .
2. .
3. the corresponding rent amount is highlighted in the map
