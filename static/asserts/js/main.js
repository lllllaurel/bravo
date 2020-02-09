$(document).ready(function(e){
    $("#main-tablelist a").click(function(e){
        var tablename = $(this).attr("attr");
        $(location).attr('href', '/data?table='+tablename);
    });

    $("#main-condition-button").click(function(){
        let param = $("#main-condition-val").val();
        let tablename = $("table").attr("attr")
        //判断是否为limit(limit格式：1-2， keyword格式：Name:Jack)
        if(param.indexOf('-')!=-1){
            var limit1 = param.split('-')[0]
            var limit2 = param.split('-')[1]
            if (isNumber(limit1)&&isNumber(limit2)&&Number(limit1)<=Number(limit2)){
                $(location).attr('href', '/data?table='+tablename+'&limit='+param);
            }else{
                alert("error")
            }
        }else if(param.indexOf(':')!=-1){
            $(location).attr('href', '/data?table='+tablename+'&keyword='+param);
        }else{
            alert("参数不合法!")
        }
    });

    $("#register-newapp").click(function(e){
        let uname = $("#register-uname").val()
        let appid = $("#register-appid").val()
        let phone = $("#register-phone").val()
        $.get('/register/appid', data={appid:appid,phone:phone,uname:uname}, function(e){
            if(e=='300'){
                alert("数据库异常")
            }
        })
    })
})

function isNumber(val) {
    var regPos = /^\d+(\.\d+)?$/; //非负浮点数
    var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/; //负浮点数
    if(regPos.test(val) || regNeg.test(val)) {
        return true;
    } else {
        return false;
    }
}