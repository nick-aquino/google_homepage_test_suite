# Additional Test Cases

Examples of additional test cases that could be run on the Google Homepage.

### Search Submission

1. **Use Enter Key**
    - Check that Enter key can be used for form submission 
    - Steps:
        - Select search box element
        - Type in some text (i.e. True Fit)
        - Press Enter Key
        - Page will navigate to Search Page for text
2. **Click predicted text item**
    - When connection is Fast the predicted text dropdown will become visible 
    - Steps:
        - Select search box element
        - Type in some text (i.e. True Fit)
        - Wait for predicted text dropdown to appear
        - Select option from drop down list to perform search
        - Page will navigate to Search Page for selected result
3. **Slow Network "Google Search" button test**
    - When connections is slow predicted text does not cause dropdown 
    allowing for static "Google Search" button to be pressed
    - Requires method of adjusting network speed
    - Steps:
        - Select search box element
        - type in some text (i.e. True)
        - Predicted text dropdown does not appear
        - click static "Google Search" button
        - verify Search is performed (after network delay)
4. **Slow Network "I'm Feeling Lucky" button test**
    - Same steps as above replacing "Google Search" button with "I'm Feeling Lucky"
5. **Fast Network "I'm Feeling Lucky" button test**
    - When connection is Fast the predicted text dropdown will become visible 
    along with a new "I'm Feeling Lucky" button that was hidden before.
    - Steps:
        - Select search box element
        - Type in some text (i.e. True Fit)
        - Wait for predicted text dropdown to appear
        - Click "I'm Feeling Lucky" button that has just become visible
        - Page URL will change when search is performed

### Predicted Search Text

1. **Check that predicted search terms are relevant**
    - The predicted search text should be relevant.
     This can be difficult as relevant predicted text is not always 
     apparent and can change regularly
    - Steps:
        - Select search box element
        - Type in some text (i.e. Fac)
        - Wait for predicted text dropdown to appear
        - Verify the text creates relevant results (i.e. Facebook)
        
2. **Check that previous search terms are stored and returned in predicted text**
    - The predicted search text should show previously searched terms.
    - Steps:
        - Select search box element
        - Type in some text (i.e. True Fit)
        - Submit search
        - Verify results returned
        - Return to homepage
        - Type in partial text from previous search (i.e. True)
        - Verify previously searched term is 
       
3. **Check that previous search terms are removed when "remove" option is selected**
    - The predicted search text should allow removing previously searched terms.
    - Steps:
        - Select search box element
        - Type in some text (i.e. True Fit)
        - Submit search
        - verify results returned
        - return to homepage
        - Type in partial text from previous search (i.e. True)
        - Verify previously searched text is predicted
        - Select "Remove" option for stored text
        - option should be removed
        - Refresh homepage
        - Type in partial text from previous search (i.e. True)
        - Verify previously searched text is not predicted        
        
### Special Results

The following are just a few examples of possible special results
that should be returned when enterd on the google homepage search. 
This set is becoming increasingly large since Google has begun integrating 
more from the android and home platforms into the google homepage

1. Verify Math problems are treated correctly
2. Verify weather results are treated correctly
3. Verify flight results are treated correctly

### Search Text Limitations

Text limitation tests are fairly simple and generally repeat 
the steps of the positive search test but with inputs meant to 
test the limits of the search boxes character support

1. **Long String**
    - Input string greater than maximum allowed string length
2. **White Space**
    - Input only white space and check for expected behavior
    - Currently it seems google will perform the search and return empty results
3. **Special Characters**
    - Check the use of special characters and characters with different encodings
4. **Numbers**
    - Rarely a problem, but check the results for using numbers alone and in mixed character company
5. **XSS Scripting**
    - Text input into the search box should be sanitized to prevent cross site scripting attacks

### Miscellaneous

There are many more possible tests in the interest of time 
I will be brief with some additional ideas

1. Testing additional links on page
    - About
    - Store
    - Gmail
    - Images
    - Advertising
    - Business
    - Privacy
    - Terms
    - Settings popup and included links
2. Google Account Tests
    - Applications dropdown and all included images and links
    - Account Sign in
    - Account Sign out
    - Additional Accounts
    - Account specific items
        - Notifications shown and updated when logged in
        - No notifications icon when logged out
        - User image loaded
        - Entire popup dialogue for updating user image
        
    
