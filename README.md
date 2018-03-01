Just a prototype about online doc management cost me a week or so to code, help me learning Django.
The purpose of the product is to help users writing essays online. I believe when writing essay, one should focus on topics and discourses rather than academic English and format. However, non native speaker(myself include) always find it struggle on academic English and format.
This verson I only finish the basic feature. Include: login/logout,sign in,add new article, edit article and delete oneself's article.
The database only have 2 objects by now: Article(FK=user),Part(FK=Article). Both are 1 to many relations. Also I'm really not spend any time on front end. So it looks really simple.
Below is some feature showing:
When a user logged in. He should get all his article at the index page with a cover
<img width="1614" alt="screen shot 2018-03-01 at 8 26 21 pm" src="https://user-images.githubusercontent.com/25581405/36838082-4837938a-1d92-11e8-83d3-d2a5123eab4b.png">
After click on title/cover, one should be in the detail page. Here shows each part of his article and he can edit/delete/create new part. Also, he can edit the info about his article.
<img width="1599" alt="screen shot 2018-03-01 at 8 26 50 pm" src="https://user-images.githubusercontent.com/25581405/36838295-ea32fc92-1d92-11e8-97fd-af8d1239b99d.png">
Also, one can add new article and update the cover of this article.
<img width="1612" alt="screen shot 2018-03-01 at 8 27 31 pm" src="https://user-images.githubusercontent.com/25581405/36838383-254101b2-1d93-11e8-83a6-89f332942e62.png">
If logout/people without an account visit the webpage. Then a tutorial will show at the main page. See the right top, currenttly the user is not login
<img width="1612" alt="screen shot 2018-03-01 at 8 27 44 pm" src="https://user-images.githubusercontent.com/25581405/36838525-85a0f030-1d93-11e8-9156-2af6421331f1.png">
