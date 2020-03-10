{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>求片留言</title>
  {% include 'component/link.tpl' %}
  <style>
    #begfilm-form textarea{
      width: 100%;
    }
    #begfilm-form input{
      width:100px;
      margin:10px;
      margin-bottom:100px;
    }
  </style>
  <script>
    function submitBeginfo(){
        if(document.forms[0].beginfo.value == ""){
          alert("留言信息不能为空");
          return ;
        }
        $.ajax(
          {
            type: "POST",
            dataType: "html",
            url: "/begfilm/",
            data: $('#begfilm-form').serialize(),
            success: 
            function (result) {
              $("#infocon").html("<font color='green'><b>留言成功！请留意您的邮箱！</b></font>")
		    		  $('#myModal').modal();
            },
            error: 
            function(data) {
              $("#infocon").html("<font color='green'><b>Sorry，留言失败，管理员即将修复BUG</b></font>")
		    		  $('#myModal').modal();
            }
        });
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie(csrftoken));
          }
        });
		}
  </script>
</head>

<body>
  {% include 'component/header.tpl' %}
  {% include 'component/navbar.tpl' %}

  <div class="container">
    <h3 style="color:white">{{ tips }}</h3>
  </div>

  <div class="container">
    <form id="begfilm-form">
      {% csrf_token %}
      <textarea name="beginfo" rows="6"></textarea>
      <input class="btn btn-primary" value="留言" type="button" onclick="submitBeginfo()">
    </form>
  </div>

  {% include 'component/friendlink.tpl' %}
  {% include 'component/aside.tpl' %}
  {% include 'component/copyright.tpl' %}
  {% include 'component/tips.tpl' %}
  {% include 'component/message.tpl' %}
  {% include 'component/share.tpl' %}  

</body>
</html>

