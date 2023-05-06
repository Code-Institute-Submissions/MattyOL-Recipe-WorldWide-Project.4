# Recipe-WorldWide-Project.4
<img width="1290" alt="Screen Shot 2023-05-06 at 12 13 08" src="https://user-images.githubusercontent.com/111317260/236620760-f9e61e04-9cf7-4203-a732-78b66bc46c63.png">



Recipe WorldWide is a Blog post website where Users get to share Recipes frm around the world, The admin can Add posts, Add Images, Create content for the blog posts , Manage User requestes on adding blog post Via Email, This user can send a email when they sign up to the site. 
The aim of this site was to Bring all Recipes and people together to share there way of cooking.

Link url{https://project-4-fsf.herokuapp.com/}

# UX
I wanted to keep the colour scheme quite simpley so its easy for the user to navigate and not get distracted while on the website The colour i used is 

### Colour Scheme 

<img width="56" alt="Screen Shot 2023-05-04 at 13 29 29" src="https://user-images.githubusercontent.com/111317260/236205297-4a7eaf21-4fcd-4265-a6ea-ae74d2b8d751.png"> rgb(67, 97, 67)
<img width="52" alt="Screen Shot 2023-05-04 at 13 29 21" src="https://user-images.githubusercontent.com/111317260/236205393-d3c108cf-dd44-46b5-a9fd-e868e202fde1.png"> white 
<img width="46" alt="Screen Shot 2023-05-04 at 13 29 14" src="https://user-images.githubusercontent.com/111317260/236205480-bd0f07f5-e2be-404d-9a0f-b38ea4601b39.png"> rgb(175, 174, 174)
<img width="37" alt="Screen Shot 2023-05-04 at 13 29 08" src="https://user-images.githubusercontent.com/111317260/236205500-4725147f-fe68-435b-8f91-c3a74f8a88b5.png"> #2ecc71

### Typography
Lato, sans-serif was used for the website name , navbar , easy to read for any user. 

Fantasy was used for the for the text across the body of the site including the blog posts.




# User Storie's









# Wireframe's
I used Justinmind.com to create the wireframes for my website to give me a guide to how id like to create the website so i have a more clearer plan of developing the site.

## Home-Page 

<img width="852" alt="Screen Shot 2023-05-04 at 13 52 41" src="https://user-images.githubusercontent.com/111317260/236211223-ef284002-d437-4305-a068-ec1826a85926.png">

## Home-Next-Page 

<img width="852" alt="Screen Shot 2023-05-04 at 13 53 31" src="https://user-images.githubusercontent.com/111317260/236211275-c9d49a76-6041-44ac-92ab-edf9809147a3.png">

## About-Page

<img width="851" alt="Screen Shot 2023-05-04 at 13 54 05" src="https://user-images.githubusercontent.com/111317260/236211299-2b6d3049-3ee6-4415-82ea-9396a91186fe.png">

## Sign-Up-Page

<img width="848" alt="Screen Shot 2023-05-04 at 13 54 18" src="https://user-images.githubusercontent.com/111317260/236211382-2db2cc48-567d-4f0e-8784-ceb2d22013e8.png">

## login-Page

<img width="846" alt="Screen Shot 2023-05-04 at 13 54 28" src="https://user-images.githubusercontent.com/111317260/236211410-2cc8fdf4-d478-4148-848a-e4ba58a01e04.png">

 ## Contact-Page

<img width="845" alt="Screen Shot 2023-05-04 at 13 54 45" src="https://user-images.githubusercontent.com/111317260/236211454-ad2c81bc-560b-46c5-a54b-d4d8a776d636.png">

## Add-Recipe-Page

<img width="840" alt="Screen Shot 2023-05-04 at 13 54 34" src="https://user-images.githubusercontent.com/111317260/236211466-b0963ff8-7d48-4c52-8ee1-6d1cffd82f09.png">

## 404-Error-Page 

<img width="847" alt="Screen Shot 2023-05-04 at 13 54 51" src="https://user-images.githubusercontent.com/111317260/236211485-8d0c7f84-a750-4fdd-a6aa-8b3d91eb28e7.png">


# Feature's







# Tools & Teshnologie's


# local Deployment 
This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the requirements.txt file.

* pip3 install -r requirements.txt.
You will need to create a new file called env.py at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

Sample env.py file:




Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

Start the Django app: python3 manage.py runserver
Stop the app once it's loaded: CTRL+C or ⌘+C (Mac)
Make any necessary migrations: python3 manage.py makemigrations
Migrate the data to the database: python3 manage.py migrate
Create a superuser: python3 manage.py createsuperuser
Load fixtures (if applicable): python3 manage.py loaddata file-name.json (repeat for each file)
Everything should be ready now, so run the Django app again: python3 manage.py runserver
Cloning
You can clone the repository by following these steps:

Go to the GitHub repository
Locate the Code button above the list of files and click it
Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
Open Git Bash or Terminal
Change the current working directory to the one where you want the cloned directory
In your IDE Terminal, type the following command to clone my repository:
git clone 
Press Enter to create your local clone.
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

Open in Gitpod

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed. A tutorial on how to do that can be found here.

Forking
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

Log in to GitHub and locate the GitHub Repository
At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
Once clicked, you should now have a copy of the original repository in your own GitHub account!
# credits 
 * I used code institutes project 4 blog post tutorial to get me up and running with a template so i can then add new features to Create a fully functionaly web applcation. 
 * I wanna Thank Ben Kanvanagh for the guidance in this project , Helping me to test my boundiers. 
 * All photos used on throughout the site are used from www.pexels.com and www.upslash.com .
 * I used Django: The web framework for perfectionists with deadlines https://www.djangoproject.com. 
 *  I used flexbox to make the website more easier and to make it mote responsive i used a guide from csstrick.com to be able to implement this to suit my site. to create the about and donation page - flexbox tricks 
 *  I wanna Thank slack communtiy were i could easily search a problem that a previous student might have had Meaning i could fix this.
 *  I want to thank any tutor that had helped me along the way ith getting past errors in the terminal. 
  







