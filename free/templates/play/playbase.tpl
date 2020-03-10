{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>{{ info.name }} - 在线播放</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/playvideo.css">
  <script src="/static/js/play.js"></script>
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}

  {% block breadcrumb %}
  {% endblock %}

  {% block play %}
  {% endblock %}

  {% block playurl %}
  {% endblock %}

  <!-- 反馈容器 -->
  <div class="container container-feedback">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h4 class="panel-title">
          <a data-toggle="collapse" href="#collapse-1">影片报错（点我展开）</a>
        </h4>
      </div>
      <div id="collapse-1" class="collapse">
        <form class="panel-body" id="feedback-form">
          {% csrf_token %}
          <p><label>当前视频地址： </label><input name="url" readonly value="{{ request.path }}"></p>
          <p><label>请输入详细的报错信息（必须）</label><input name="feedbackinfo" type="text"></p>
          <p><label>请输入您的邮件地址方便与您联系（可选）</label><input name="email" type="email" value=""></p>
          <button type="button" onclick="submitFeedbackInfo()">点击报错</button>
        </form>
      </div>
    </div>
  </div><!-- ./container-feedback -->

  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/tips.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}




</body>

</html>