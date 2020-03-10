{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>{{ info.name }} - 详情</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/infovideo.css">
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}

  {% block breadcrumb %}
  {% endblock%}

  <!-- 影视信息容器 -->
  <div class="container container-info">
    <div class="col-md-3 col-xs-5 container_l">
      <img src="{{ info.url_img }}" alt="图片加载失败">
    </div>
    <div class="col-md-9 col-xs-7 container_r">
      <h2 class="hidden-xs">{{ info.name }}</h2>
      <p class="hidden-xs">
        {% for star in score|custom_star_light %}
        <span class="star">★</span>
        {% endfor %}
        {% for star in score|custom_star_slake %}
        <span class="star">☆</span>
        {% endfor %}
        <span id="score">{{ info.score }}</span>
      </p>
      <p>导演：<a href="/search/keyword/{{ info.director }}/page/0">{{ info.director }}</a></p>
      <p>主演：{% for actor in actor|custom_split_actors %}<a href="/search/keyword/{{ actor }}/page/0"
          class="relation">{{ actor }}</a>
        {% endfor %}
      </p>
      <p>类型：<a>{{ info.flag_type }}</a></p>
      <p>年代：<a>{{ info.flag_time }}</a></p>
      <p>地区：<a>{{ info.flag_area }}</a></p>
      <p>更新时间：<a>{{ info.update_time }}</a></p>
    </div>
  </div><!-- ./container-info -->

  <!-- 剧情简介容器 -->
  <div class="container container-intro">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" href="#collapse-1">
            剧情简介（点我展开）
          </a>
        </h4>
      </div>
      <div id="collapse-1" class="collapse">
        <div class="panel-body">
          {{ info.introduction }}
        </div>
      </div>
    </div>
  </div><!-- ./container-intro -->

  {% block playurl %}
  {% endblock %}

  <!-- 视频推荐容器 -->
  <div class="container container-show">
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title">
          <a><span>当前热播</span></a>
        </div>
      </div>
      {% block recommendation %}
      {% endblock %}
    </div>
  </div><!-- ./container-show -->

  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}  

</body>
</html>