function searchByKeyword(){
    var keyword = $('input')[0].value;
    window.location.href = "/search/keyword/" + keyword + "/page/0"
}

function showHistoryBox(){
    $('.history-box ul')[0].style.display = 'block'
}

function closeHistoryBox(){
    $('.history-box ul')[0].style.display = 'none'
}

function clearWatchHistory(){
    $.cookie('whp', '', {expires: -1, path: '/'});
    $.cookie('whn', '', {expires: -1, path: '/'});
    $('.history-box ul')[0].innerHTML = '<li>无历史记录</li>'
}


window.onload = function (){
    $('input')[0].onkeydown = function(event){       
         if(event && event.keyCode==13){
            searchByKeyword()
        }
    }; 
    $('input')[1].onclick = searchByKeyword;
};



function share(sharedTo){
    var url = window.location.href;
    var title = "自在仙影视网"
    var desc =  "我正在自在仙影视网上观看影片，你也来看看吧！"
    var summary = "浮云轻入鹤撩雾，青山深处自在仙。"
    var source = "www.zizaixian.top"
    var pics = "http://47.112.4.204/static/images/icon/favicon.png"

    if(url.split('/')[3] == 'info'){
        title = $('h2')[0].innerText
        desc = "我正在自在仙影视网上观看《" + title + "》，一部超级好看的影片，你也来看看吧！ ";
        summary = $('.container-intro .panel-body')[0].innerText.slice(0,80)
        pics = $('img')[0].src;
    }
    if(url.split('/')[3] == 'play'){
        title = $('.breadcrumb a')[3].innerText
        desc = "我正在自在仙影视网上观看《" + title + "》，一部超级好看的影片，你也来看看吧！ ";
    }

    var qqzoneLink = "http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=" + url + "&title=" + title + 
    "&desc=" + desc + "&summary=" + summary + "&site=" + source +"&pics=" + pics;
    
    var qqLink = "http://connect.qq.com/widget/shareqq/index.html?url=" + url + "&title=" + title + 
    "&source=" + source + "&desc="  + desc + "&pics=" + pics + "&summary=" + summary

    var weiboLink = "http://service.weibo.com/share/share.php?url=" + url + "&title=" + desc + "&pic=" + pics;

    switch(sharedTo){
        case 'qq': window.open(qqLink); break;
        case 'qqzone': window.open(qqzoneLink); break;
        case 'weibo': window.open(weiboLink); break;
    }
}