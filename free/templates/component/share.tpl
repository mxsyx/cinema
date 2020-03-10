<!-- 模态框（Modal） -->
<div class="modal fade" id="modal-share" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          <h4 class="modal-title" id="myModalLabel">分享当前地址</h4>
        </div>
        <div class="modal-body">
          <div class="shared-item" onclick="share('qq')">
            <img width="40" height="40" src="/static/images/icon/qq.svg" onclick="share()">
            <p>QQ好友</p>
          </div>
          <div class="shared-item" onclick="share('qqzone')">
            <img width="40" height="40" src="/static/images/icon/qqzone.svg" onclick="share()">
            <p>QQ空间</p>
          </div>
          <div class="shared-item" onclick="share('weibo')">
            <img width="40" height="40" src="/static/images/icon/weibo.svg" onclick="share()">
            <p>新浪微博</p>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
        </div>
      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal -->