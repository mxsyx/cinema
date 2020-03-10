{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>搜索视频</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/index.css">
  <script>
    window.onload = function(){
      var address = window.location.href;
      var strList = address.split('/')
      var page = parseInt(strList[7]);
      $('#p' + page)[0].classList.add('active');

      $('input')[0].onkeydown = function(event){       
         if(event && event.keyCode==13){
            searchByKeyword()
        }
      }; 
      $('input')[1].onclick = searchByKeyword;
    }
  </script>
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}
  
  <!-- 影视信息展示容器 -->
  <div class="container container_show" style="margin-top:0px">
    <div class="panel">
      <div class="panel-body row">
        {% for item in results %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/{{ item.flag_type|custom_type_to_mtva }}/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/{{ item.flag_type|custom_type_to_mtva }}/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/{{ item.flag_type|custom_type_to_mtva }}/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>

  <!-- 分页 -->
  <div class="container">
    <ul class="pagination">
      <li><a href="/search/keyword/{{ keyword }}/page/0">首页</a></li>
      <li><a href="/search/keyword/{{ keyword }}/page/{{ previous_page }}">&laquo;</a></li>
      {% for page in pages %}
        <li id="p{{ page|add:-1 }}"><a href="/search/keyword/{{ keyword }}/page/{{ page|add:-1 }}">{{ page }}</a></li>
      {% endfor %}
      <li><a href="/search/keyword/{{ keyword }}/page/{{ next_page }}">&raquo;</a></li>
      <li><a href="/search/keyword/{{ keyword }}/page/{{ sum_pages }}">尾页</a></li>
    </ul>
  </div>

  {% include 'component/friendlink.tpl' %}
  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}  

</body>
</html>

