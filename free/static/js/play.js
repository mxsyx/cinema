window.onload = function () {
    addWatchHistory();
};

/**
 * 新增历史记录
 * 历史记录通过cookie实现
 * whp 记录着播放过的视频路径
 * whn 记录着播放过的视频名称
 */
function addWatchHistory() {
    let historyPath =   // 历史记录路径字符串
        $.cookie('whp') ? $.cookie('whp') : "";
    let historyName =   // 历史记录名称字符串
        $.cookie('whn') ? $.cookie('whn') : "";
    let paths = historyPath.split('$$');  // 历史记录路径数组
    let names = historyName.split('$$');  // 历史记录名称数组

    // 当前页面的地址与视频名字
    let path = '/play/' + window.location.href.split('/play/')[1];
    let name = $('.breadcrumb a')[3].innerText

    /**
     * 判断当前页面是否记录在历史记录中
     * 若当前页面没有记录在历史记录中，则新增历史记录
     */
    for (var i = 0; i < paths.length && path != paths[i]; i++);

    if (i == paths.length) { // 历史记录中无当前页面地址
        // 历史记录最多写入十条
        // 超过十条时删除尾部记录
        if (paths.length == 10) {
            paths.shift();
            names.shift();
        }
        // 新增历史记录
        paths.push(path)
        names.push(name)
        let historyPathNew = paths.join('$$')
        let historyNameNew = names.join('$$')
        // 更新历史记录
        $.cookie('whp', historyPathNew, { expires: 7, path: '/' });
        $.cookie('whn', historyNameNew, { expires: 7, path: '/' });
    }
}

function submitFeedbackInfo() {
    if ($('#feedback-form')[0].feedbackinfo.value == "") {
        alert("反馈信息不能为空");
        return;
    }
    $.ajax(
        {
            type: "POST",
            dataType: "html",
            url: "/feedback/",
            data: $('#feedback-form').serialize(),
            success:
                function (result) {
                    $("#infocon").html("<font color='green'><b>反馈成功！请留意您的邮箱！</b></font>")
                    $('#myModal').modal();
                },
            error:
                function (data) {
                    $("#infocon").html("<font color='green'><b>Sorry，反馈失败，管理员即将修复BUG</b></font>")
                    $('#myModal').modal();
                }
        });
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie(csrftoken));
        }
    });
}

