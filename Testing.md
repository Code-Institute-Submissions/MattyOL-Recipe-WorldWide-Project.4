### Return to README.md

[README.md](https://github.com/MattyOL/Recipe-WorldWide-Project.4/edit/main/Testing.md#:~:text=Procfile-,README,-.md)
## Code Validation
I have used the recommended HTML W3C Validator to validate all of my HTML files.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

* Navigate to the deployed pages which require authentication
* Right-click anywhere on the page, and select View Page Source (usually CTRL+U or ⌘+U on Mac).
* This will display the entire "compiled" code, without any Jinja syntax.
* Copy everything, and use the validate by input method.
* Repeat this process for every page that requires a user to be logged-in/authenticated

### Home-page 
* no issues 
<img width="1389" alt="Screen Shot 2023-05-15 at 19 03 02" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/f141ec09-797a-41db-a947-bca35b86427d">


### Sign-up
* no issues 
<img width="1382" alt="Screen Shot 2023-05-15 at 17 51 47" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/49d2cb66-c179-491a-b1bc-db1f8e2a394d">


### Login 
* no issues 
<img width="1382" alt="Screen Shot 2023-05-15 at 17 51 47" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/332ca842-5ed7-466c-8c11-675c2455e21a">


### Contact form 
* no issues 
<img width="1399" alt="Screen Shot 2023-05-15 at 17 54 17" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/934006b4-afac-483d-9e46-a918d46f7c7b">



### Add recipe 
* no issues 
<img width="1383" alt="Screen Shot 2023-05-15 at 17 55 44" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/15b1ea56-7700-4d6a-ab67-fc34e475bd98">


### 404 error page
* no issues 
<img width="1407" alt="Screen Shot 2023-05-15 at 17 58 11" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/a54283b6-4bcf-40cb-8c72-85029063ba8b">

## Css Testing 
* I have used the recommended CSS Jigsaw Validator to validate my CSS file. 
* No issues 
<img width="1335" alt="Screen Shot 2023-05-15 at 18 03 29" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/3778965e-73d3-4dff-ae1c-7eb0d958c4bb">
## Python 
I have used the recommended CI Python Linter to validate all of my Python files.

## tests.py 
I done sone some test in the test.py file using the terminal to get results using the 
* python3 manage.py test / command 
* 
![Screen Shot 2023-05-16 at 14 49 10](https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/390dbebd-8b21-4294-9cf0-3e735ac21bc4)

![Screen Shot 2023-05-16 at 14 49 22](https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/484f2494-dbfc-454f-90cb-1c86816e66a0)


### Results 
<img width="595" alt="Screen Shot 2023-05-16 at 14 49 56" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/90d5edc6-eb49-4434-b371-0de3b639d8e3">


## Manual Testing 
1. * Test: click on Login button

   * Expected result: taken to login screen.

   * Result: pass

2. * Test:click on Sign up form.

   * Expected: taken too signup form Create an account.

   * Result: pass.

3. * Test: Home button navbar.

   * Expected: taken to home page.

   * Results: pass.

4. * Test:Click Contact form.

   * Expected:to be brought to page, form filled out, submit.

   * Result: pass.

5. * Test: Click Add Recipe.

   * Expected: To be brought to page.

   * Result: pass.

6. * Test:Search bar searches recipe.

   * Expected: To be displayed with recipes.

   * Result: pass

7. * Test: Search invalid entry to display 404 error.

   * Expected: To be brought to 404error feedback.

   * Result: pass.

8. * Test: Go back button on 404page.

   * Expected: to return to home.

   * Result: pass.

9. * Test: Logout.

   * Expected: user to logout.

   * Result: pass

10. * Test: When user clicks a blog post.

    * Expected: To be brought into the posts info.

    * Results: pass.

11. * Test: User deletes post they created.

    * Expected: post can only be deleted by the user/admin.

    * Results: pass.

12. * Test: User can edit the post they created.

    * Expected: User can only edit the post they have created.

    * Result: pass.

13. * Test: Next page button

    * Expected: to be brought onto next page of blof post's

    * Result: pass

13. * Test: likes/comments on posts

    * Expected: The admin has to verify like/comments on post when submitted

    * Results: pass

14.  * Test: websites name is clickable

     * Expected: to refresh to home-page

     * Results: pass


## Lighthouse Test's

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

### Home page

* Desktop devices
<img width="684" alt="Screen Shot 2023-05-15 at 17 01 24" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/1252b977-1d0e-40f0-957b-61abcb0284c7">

* Mobile devices
<img width="674" alt="Screen Shot 2023-05-15 at 17 00 56" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/51ce996f-a96f-41d5-a1dd-5473cdf44c46">


### About page

* Desktop devices
<img width="639" alt="Screen Shot 2023-05-15 at 17 03 16" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/a25cfd91-28c7-4211-8b40-912a383fb0b5">

* Mobile devices
<img width="623" alt="Screen Shot 2023-05-15 at 17 02 51" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/b71ce52b-c516-4c08-a7e3-1733de3bc05d">


### Sign up page

* Desktop devices
<img width="579" alt="Screen Shot 2023-05-15 at 17 04 16" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/9480eea6-e34e-4496-86b5-9e39cb0b02cb">

* Mobile devices
<img width="626" alt="Screen Shot 2023-05-15 at 17 05 05" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/16856f40-8454-4271-a300-27d563b76694">

### Login page

* Desktop devices
<img width="559" alt="Screen Shot 2023-05-15 at 17 06 07" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/e1c1d4e4-d98e-4fff-92f4-27731c58c792">

* Mobile devices
<img width="626" alt="Screen Shot 2023-05-15 at 17 05 05" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/600153c7-fd33-4a30-a340-23f87d8680f8">

### Contact Form

* Desktop devices
<img width="608" alt="Screen Shot 2023-05-15 at 17 07 22" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/04275ab1-6e1f-405c-9a7d-b6c8623aec47">

* Mobile devices
<img width="607" alt="Screen Shot 2023-05-15 at 17 07 42" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/eb694c37-1810-418a-baf7-658082d52a58">

### Add recipe page

* Desktop devices
<img width="587" alt="Screen Shot 2023-05-15 at 17 08 22" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/107b7d48-9670-440b-8910-c24a114e47a0">

* Mobile devices
<img width="603" alt="Screen Shot 2023-05-15 at 17 08 43" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/903c1957-9343-4692-84d4-b993648addb2">

### 404 error page

* Desktop devices
<img width="620" alt="Screen Shot 2023-05-15 at 17 09 45" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/9e15fe25-c880-44de-9721-d2b8a840e36f">

* Mobile devics
<img width="633" alt="Screen Shot 2023-05-15 at 17 10 07" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/986de55d-0f81-48e9-9d2d-574082023231">

### Log out page

* Desktop devices
<img width="628" alt="Screen Shot 2023-05-15 at 17 10 44" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/7c39d0f5-fce0-4135-a6b8-81db24870a96">

* Mobile devices
<img width="641" alt="Screen Shot 2023-05-15 at 17 11 26" src="https://github.com/MattyOL/Recipe-WorldWide-Project.4/assets/111317260/420cc4c1-bd20-41d0-b8ea-058fcbfcb736">



