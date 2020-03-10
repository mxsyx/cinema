{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>自在仙</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/index.css">
  <script type="text/javascript" >
    function switchTab(labelId){
      var ranktabs = $('.ranktab');
    
      for(var i = 0; i < 4; i++)
        ranktabs[i].style.display = "none"
      ranktabs[labelId].style.display = "block";
    
      for(var i = 0; i < 4; i++)
        $('#option').find('label')[i].style.borderBottom = "none";
      $('#option').find('label')[labelId].style.borderBottom = "solid 2px #FF6633";
    }
  </script>
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}
  <div class="container container-my">
    <div class="row">
      <!-- 轮播框 -->
      <div class="col-md-7">
        <div class="carousel slide" data-ride="carousel" id="carousel-1">
          <!-- 指示符 -->
          <ol class="carousel-indicators">
            <li data-target="#carousel-1" data-slide-to="0" class="active"></li>
            <li data-target="#carousel-1" data-slide-to="1"></li>
            <li data-target="#carousel-1" data-slide-to="2"></li>
            <li data-target="#carousel-1" data-slide-to="3"></li>
            <li data-target="#carousel-1" data-slide-to="4"></li>
          </ol>
          <!-- 轮播内容 -->
          <div class="carousel-inner" role="listbox">
            <div class="item active">
              <img src="/static/images/lb/001.jpg" alt="...">
              <div class="carousel-caption">测试数据</div>
            </div>
            <div class="item">
              <img src="/static/images/lb/002.jpg" alt="...">
              <div class="carousel-caption">测试数据</div>
            </div>
            <div class="item">
              <img src="/static/images/lb/003.jpg" alt="...">
              <div class="carousel-caption">测试数据</div>
            </div>
            <div class="item">
              <img src="/static/images/lb/004.jpg" alt="...">
              <div class="carousel-caption">测试数据</div>
            </div>
            <div class="item">
              <img src="/static/images/lb/005.jpg" alt="...">
              <div class="carousel-caption">测试数据</div>
            </div>
          </div>
          <!-- 轮播控件 -->
          <a class="carousel-control left" href="#carousel-1" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
          </a>
          <a class="carousel-control right" href="#carousel-1" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
          </a>
        </div>
      </div>
      <!-- 排行榜 -->
      <div class="col-md-5">
        <!-- 切换栏 -->
        <div id="fealist" class="row" >
          <div class="col-md-3 col-xs-3">
            <a href="/ranking/"><img src="/static/images/icon/rank.svg"><span>排行榜</span></a>
          </div>
          <div class="col-md-3 col-xs-3">
            <a href="/begfilm/"><img src="/static/images/icon/message.svg"><span>求片留言</span></a>
          </div>
          <div class="col-md-3 col-xs-3">
            <a href=""><img src="/static/images/icon/wechat.svg"><span>公众号</span></a>
          </div>
          <div class="col-md-3 col-xs-3">
            <a href="/download/"><img src="/static/images/icon/app.svg"><span>下载APP<span></span></span></a>
          </div>
        </div><!-- /.fealist -->
        <div class="row ranking">
          <div id="option">
            <label style="border-bottom:solid 2px #FF6633" onmousemove="switchTab(0);">电影榜</label>
            <label onmousemove="switchTab(1);">电视榜</label>
            <label onmousemove="switchTab(2);">综艺榜</label>
            <label onmousemove="switchTab(3);">动漫榜</label>
          </div>
          <ul class="ranktab" style="display:block">
            {% for popular_video in popular_videos.m %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/movie/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul><!-- /.ranktab 电影 -->
          <ul class="ranktab">
            {% for popular_video in popular_videos.t %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/tvseries/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul><!-- /.ranktab 电视 -->
          <ul class="ranktab">
            {% for popular_video in popular_videos.v %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/variety/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul><!-- /.ranktab 综艺 -->
          <ul class="ranktab">
            {% for popular_video in popular_videos.a %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/anime/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul><!-- /.ranktab 动漫 -->
        </div>
      </div><!-- /.排行榜结束 -->
    </div>
  </div><!-- /.container-my -->

  <!-- 影视信息展示容器 -->
  <div class="container container_show">
    <!-- 电影展示 -->
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title">
          <img src="/static/images/icon/dy.svg"><span>&nbsp;热播电影</span>
          <a href="/classify/type/0/time/0/area/0/page/0" class="more pull-right">更多&nbsp;&gt;</a>
        </div>
      </div>
      <div class="panel-body row">
        {% for item in movie_items %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/movie/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/movie/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/movie/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div><!-- ./电影展示结束 -->
    <!-- 电视展示 -->
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title">
          <img src="/static/images/icon/dsj.svg"><span>&nbsp;热播电视</span>
          <a href="/classify/type/9/time/0/area/0/page/0" class="more pull-right">更多&nbsp;&gt;</a>
        </div>
      </div>
      <div class="panel-body row">
        {% for item in tvseries_items %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/tvseries/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/tvseries/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/tvseries/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div><!-- ./电视展示结束 -->
    <!-- 综艺展示 -->
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title">
          <img src="/static/images/icon/zy.svg"><span>&nbsp;热播综艺</span>
          <a href="/classify/type/14/time/0/area/0/page/0" class="more pull-right">更多&nbsp;&gt;</a>
        </div>
      </div>
      <div class="panel-body row">
        {% for item in variety_items %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/variety/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/variety/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/variety/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div><!-- ./综艺展示结束 -->
    <!-- 动漫展示 -->
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title">
          <img src="/static/images/icon/dm.svg"><span>&nbsp;热播动漫</span>
          <a href="/classify/type/15/time/0/area/0/page/0" class="more pull-right">更多&nbsp;&gt;</a>
        </div>
      </div>
      <div class="panel-body row">
        {% for item in anime_items %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/anime/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/anime/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/anime/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div><!-- ./动漫展示结束 -->
  </div><!-- ./container-show -->

  {% include 'component/friendlink.tpl' %}
  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}

  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}  

</body>
</html>