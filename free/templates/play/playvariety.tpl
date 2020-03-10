{% extends "play/playbase.tpl" %}
{% load tplfilter %}

{% block breadcrumb %}
<!-- 站点导航 -->
<div class="container">
  <ul class="breadcrumb">
    <li><a href="/">首页</a></li>
    <li><a href="/classify/type/15/time/0/area/0/page/0">综艺</a></li>
    <li><a href="/classify/type/{{ info.flag_type|custom_type_to_num }}/time/0/area/0/page/0">{{ info.flag_type}}</a></li>
    <li class="active"><a href="/info/variety/{{ info.id }}">{{ info.name }}</a></li>
  </ul>
</div>
{% endblock %}

{% block play %}
<!-- 播放容器 -->
<div class="container" id="container_play">
  <iframe src="{{ url }}" width="100%" height="100%" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
  <a href="/play/variety/{{ info.id }}/{{ previous_episode }}" class="pn">【上一集】</a>
  <a href="/play/variety/{{ info.id }}/{{ next_episode }}" class="pn">【下一集】</a>
</div>
{% endblock %}

{% block playurl %}
<!-- 播放线路容器 -->
<div class="container" id="container_playurl">
  <h3>播放线路</h3>
  <ul class="itemlist">
    {% for num in nums %}
    <li><a href="/play/playvariety/{{ info.id }}/{{forloop.counter}}">第{{forloop.counter}}期</a></li>
    {% endfor %}
  </ul>
</div>
{% endblock %}

