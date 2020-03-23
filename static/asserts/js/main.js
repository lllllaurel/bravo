$(function() {

   $(".input input").focus(function() {

      $(this).parent(".input").each(function() {
         $("label", this).css({
            "line-height": "18px",
            "font-size": "18px",
            "font-weight": "100",
            "top": "0px"
         })
         $(".spin", this).css({
            "width": "100%"
         })
      });
   }).blur(function() {
      $(".spin").css({
         "width": "0px"
      })
      if ($(this).val() == "") {
         $(this).parent(".input").each(function() {
            $("label", this).css({
               "line-height": "60px",
               "font-size": "24px",
               "font-weight": "300",
               "top": "10px"
            })
         });

      }
   });

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
              $("#register-result").removeClass().addClass("badge badge-warning").text("Appid已存在!");
          }else if(e=='500'){
              $("#register-result").removeClass().addClass("badge badge-danger").text("数据库异常!");
          }else{
              let response = "注册成功! appid:"+e['appid']+" phone:"+e['phone']+" username:"+e['uname']+" password:"+e['password'];
              $("#register-result").removeClass().addClass("badge badge-success").text(response);
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