{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>视频排行榜</title>
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

    function switchTabs(tabId, labelId){
      var tab = $('.ranking')[tabId]
      var labelTabs = tab.children[0].children

      for(var i = 1; i <= 3; i++)
        tab.children[i].style.display = "none"
      tab.children[labelId+1].style.display = "block";
    
      for(var i = 0; i < 3; i++)
        labelTabs[i].style.borderBottom = "none";
      labelTabs[labelId].style.borderBottom = "solid 2px #FF6633";
    } 
  </script>
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}

  <div class="container container-my">
    <div class="row">
      <div class="col-md-6">
        <h3 style="color:white;margin:2px 20px;">电影排行榜</h3>
        <div class="row ranking">
          <div id="option">
            <label style="border-bottom:solid 2px #FF6633" onmousemove="switchTabs(0,0);">日排行</label>
            <label onmousemove="switchTabs(0,1);">周排行</label>
            <label onmousemove="switchTabs(0,2);">月排行</label>
          </div>
          <ul class="ranktab" style="display:block">
            {% for popular_video in leaderboard.m.rday %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/movie/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.m.rweek %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/movie/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rweek }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.m.rmonth %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/movie/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rmonth }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
        </div>
      </div>
      <div class="col-md-6">
        <h3 style="color:white;margin:2px 20px;">电视剧排行榜</h3>
        <div class="row ranking">
          <div id="option">
            <label style="border-bottom:solid 2px #FF6633" onmousemove="switchTabs(1,0);">日排行</label>
            <label onmousemove="switchTabs(1,1);">周排行</label>
            <label onmousemove="switchTabs(1,2);">月排行</label>
          </div>
          <ul class="ranktab" style="display:block">
            {% for popular_video in leaderboard.t.rday %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/tvseries/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.t.rweek %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/tvseries/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rweek }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.t.rmonth %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/tvseries/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rmonth }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="container container-my">
    <div class="row">
      
      <!-- 综艺排行榜 -->
      <div class="col-md-6">
        <h3 style="color:white;margin:2px 20px;">综艺排行榜</h3>
        <div class="row ranking">
          <div id="option">
            <label style="border-bottom:solid 2px #FF6633" onmousemove="switchTabs(2,0);">日排行</label>
            <label onmousemove="switchTabs(2,1);">周排行</label>
            <label onmousemove="switchTabs(2,2);">月排行</label>
          </div>
          <ul class="ranktab" style="display:block">
            {% for popular_video in leaderboard.v.rday %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/variety/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.v.rweek %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/variety/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rweek }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.v.rmonth %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/variety/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rmonth }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
        </div>
      </div>

      <!-- 动漫排行榜 -->
      <div class="col-md-6">
        <h3 style="color:white;margin:2px 20px;">动漫排行榜</h3>
        <div class="row ranking">
          <div id="option">
            <label style="border-bottom:solid 2px #FF6633" onmousemove="switchTabs(3,0);">日排行</label>
            <label onmousemove="switchTabs(3,1);">周排行</label>
            <label onmousemove="switchTabs(3,2);">月排行</label>
          </div>
          <ul class="ranktab" style="display:block">
            {% for popular_video in leaderboard.a.rday %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/anime/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rday }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.a.rweek %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/anime/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rweek }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
          <ul class="ranktab">
            {% for popular_video in leaderboard.a.rmonth %}
            <div class="row">
              <div class="col-md-8 col-xs-7">
                <span class="item-symbol">{{forloop.counter}}</span>
                <a href="/play/anime/{{ popular_video.id }}">《{{ popular_video.name }}》</a></div>
              <div class="col-md-4 col-xs-5">
                <span class="playnums">播放量(<em>{{ popular_video.rmonth }}</em>)</span>
              </div>
            </div>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>
  </div>

  {% include 'component/friendlink.tpl' %}
  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}  

</body>
</html>

