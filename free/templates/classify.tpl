{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>视频分类</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/index.css">
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}

  <!-- 分类导航 -->
  <div class="container container-show">
    <div class="panel">
        <div class="panel-body">
          <dl class="classify-box">
            <dt>按类型：</dt>
            {% for type_id in 16|custom_range %}
              {% ifequal type_id video_type %}
                <dd class="classify-box-active">
                  <a href="/classify/type/{{ type_id }}/time/{{ video_time }}/area/{{ video_area }}/page/0">
                    {{ type_id | custom_type_list}}
                  </a>
                </dd>
              {% else %}
                <dd>
                  <a href="/classify/type/{{ type_id }}/time/{{ video_time }}/area/{{ video_area }}/page/0">
                    {{ type_id | custom_type_list}}
                  </a>
                </dd>
              {% endifequal %}
            {% endfor %}
          </dl>
          <dl class="classify-box">
            <dt>按年代：</dt>
            {% for time_id in 11|custom_range %}
              {% ifequal time_id video_time %}
                <dd class="classify-box-active">
                  <a href="/classify/type/{{ video_type }}/time/{{ time_id }}/area/{{ video_area }}/page/0">
                    {{ time_id | custom_time_list}}
                  </a>
                </dd>
              {% else %}
                <dd>
                  <a href="/classify/type/{{ video_type }}/time/{{ time_id }}/area/{{ video_area }}/page/0">
                    {{ time_id | custom_time_list}}
                  </a>
                </dd>
              {% endifequal %}
            {% endfor %}
          </dl>
          <dl class="classify-box">
            <dt>按地区：</dt>
            {% for area_id in 16|custom_range %}
              {% ifequal area_id video_area %}
                <dd class="classify-box-active">
                  <a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ area_id }}/page/0">
                    {{ area_id | custom_area_list}}
                  </a>
                </dd>
              {% else %}
                <dd>
                  <a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ area_id }}/page/0">
                    {{ area_id | custom_area_list}}
                  </a>
                </dd>
              {% endifequal %}
            {% endfor %}
          </dl>
        </div>
    </div>
  </div><!-- ./分类导航结束 -->

  <!-- 影视信息展示容器 -->
  <div class="container container_show" style="margin-top:0px">
    <div class="panel">
      <div class="panel-heading">
        <div class="panel-title"><span style="color:white">分类查询结果：</span></div>
      </div>
      <div class="panel-body row">
        {% for item in result %}
        <div class="col-md-2 col-xs-4 videocon">
          <a href="/info/{{ mtva }}/{{ item.id }}" class="videoimg" style="background-image: url({{ item.url_img }});"></a>
          <a href="/info/{{ mtva }}/{{ item.id }}" class="action hidden-xs"><img src="/static/images/icon/action.svg"></a>
          <a href="/info/{{ mtva }}/{{ item.id }}" class="videoname">{{ item.name }}</a>
          <div class="performer">{{ item.actor }}</div>
          <div class="labelcontent">{{ item.score }}</div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div><!-- ./影视信息展示容器结束 -->

  <!-- 分页 -->
  <div class="container">
    <ul class="pagination">
      <li><a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/0">首页</a></li>
      <li><a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/{{ previous_page }}">&laquo;</a></li>
      {% for page in pages %}
        {% ifequal page current_page %}
        <li class="active" id="p{{ page|add:-1 }}">
          <a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/{{ page|add:-1 }}">
            {{ page }}
          </a>
        </li>
        {% else %}
        <li id="p{{ page|add:-1 }}">
          <a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/{{ page|add:-1 }}">
            {{ page }}
          </a>
        </li>
        {% endifequal %}
      {% endfor %}
      <li><a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/{{ next_page }}">&raquo;</a></li>
      <li><a href="/classify/type/{{ video_type }}/time/{{ video_time }}/area/{{ video_area }}/page/{{ sum_pages }}">尾页</a></li>
    </ul>
  </div><!-- ./分页结束 -->

  {% include 'component/friendlink.tpl' %}
  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}

</body>
</html>

