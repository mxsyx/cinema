{% load tplfilter %}

<!-- 页面头部 -->
<header>
  <div class="container">
    <div class="row">
      <div class="col-md-10">
        <a id="logo" href="/">自在仙</a>
        <small>浮云轻入鹤撩雾，青山深处自在仙</small>
      </div>
      <div class="history-box col-md-2 visible-md visible-lg">
        <span onmouseover="showHistoryBox()">☂观看历史</span>
        <ul onmouseleave="closeHistoryBox()">
          {% for i in paths|custom_create_iterator %}
          <li><a href="{{ i|custom_at:paths }}">{{ i|custom_at:names }}</a>
          {% endfor %}
          <li onclick="clearWatchHistory()">清空历史记录</li>
        </ul>
      </div>
    </div><!-- /.row -->  
  </div><!-- /.container -->  
</header>