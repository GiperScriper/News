<h2>Агрегатор новостей (ver. 0.1)</h2>

<h3>Используемые технологии:</h3>
<ul>
	<li>Python</li>
	<li>Django</li>
	<li>Django Rest Framework</li>
	<li>SQLite3</li>
	<li>HTML, CSS (Twitter Bootstrap)</li>
	<li>JS (JQuery)</li>
</ul>

<h3>Функционал:</h3>
<ul>
	<li>Авторизация</li>
	<li>Добавление новостей</li>
	<li>Admin interface with Django Suit</li>
	<li>Лайк новостей</li>
	<li>RESTful API</li>
</ul>

<h4>Главная страница:</h4>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/promo.jpg)
<h4>Страница добавления новости через Django Admin</h4>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/add_from_admin.jpg)
<h4>RESTful API:</h4>
<h5>GET /api/v1/stories/</h5>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/api_get.jpg)
<h5>GET /api/v1/stories/6</h5>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/api_get_single.jpg)
<h5>POST /api/v1/stories/{ content }</h5>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/api_post.jpg)
<h5>PUT /api/v1/stories/{ content }</h5>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/api_pust.jpg)
<h5>DELETE /api/v1/stories/24</h5>
![ScreenShot](https://raw.githubusercontent.com/GiperScriper/News/master/static/img/api_delete.jpg)