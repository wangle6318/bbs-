$(function(){
	changeLoginNav();
	showPromptInfo();
	alertErrMsg();

})

function changeLoginNav(){
	var nav = $(".login-nav li");
	var logFor = $(".form-wraper");
	nav.on("click",function(){
		if ($(this).hasClass("cur-nav")) {
			return false;
		} else{
			$(this).addClass("cur-nav").siblings().removeClass("cur-nav");
			logFor.eq($(this).index()).css({
				"display":"block"
			}).siblings().css({
				"display":"none"
			})
		}
	})
}

function showPromptInfo(){
	showUserNameWarnInfo();
	showPasswordWarnInfo();
	showEmailWarnInfo();
	showCodeWarnInfo();
	
	var _promptInfo = '<li class="warn-info"></li>';
	
	function showUserNameWarnInfo(){
		var username = $("#userName");
		username.on("focus",function(){
			var _Strinfo = '长度不超过8个中文，注册成功后不可修改'
			if ($(this).siblings().hasClass("warn-info")) {
				$(this).siblings(".warn-info").text(_Strinfo).css("color","#333");
			} else{
				$(this).parent().append(_promptInfo);
				
				$(this).siblings(".warn-info").text(_Strinfo);
			}
		})
		username.on("blur",function(){
			var _Strinfo = ''
			if(username.val().length > 8){
				_Strinfo = '您输入的用户名长度大于8个中文，请重新输入';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else if (username.val().length == 0){
				_Strinfo = '请输入用户名';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else {
				$(this).siblings(".warn-info").remove();
			}
		})
	}
	
	function showPasswordWarnInfo(){
		var pwd = $("#password");
		pwd.on("focus",function(){
			var _Strinfo = '密码由6-20个字母、数字或下划线组成。'
			if ($(this).siblings().hasClass("warn-info")) {
				$(this).siblings(".warn-info").text(_Strinfo).css("color","#333");
			} else{
				$(this).parent().append(_promptInfo);
				$(this).siblings(".warn-info").text(_Strinfo);
			}
		})
		
		pwd.on("blur",function(){
			var _Strinfo = '';
			if(!passwordIslegal()){
				_Strinfo = '您输入的密码不合法，请重新输入';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else {
				$(this).siblings(".warn-info").remove();
			}
		})
		
		function passwordIslegal(){
			var patrn=/^(\w){6,20}$/;  
			if (!patrn.exec(pwd.val())){
				return false;
			} else {
				return true;
			}
		}
		
	}

	function showEmailWarnInfo(){
		var email = $("#email");
		email.on("focus",function(){
			var _Strinfo = '请输入您的邮箱'
			if ($(this).siblings().hasClass("warn-info")) {
				$(this).siblings(".warn-info").text(_Strinfo).css("color","#333");
			} else{
				$(this).parent().append(_promptInfo);
				
				$(this).siblings(".warn-info").text(_Strinfo);
			}
		})
		email.on("blur",function(){
			var _Strinfo = ''
			if(email.val().length == 0){
				_Strinfo = '请输入邮箱';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else if (!emailIsLegal()){
				_Strinfo = '您输入的邮箱格式有误，请重新输入';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else {
				$(this).siblings(".warn-info").remove();
			}
		})
		
		function emailIsLegal(){
			myReg=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;
			if (myReg.test(email.val())) {
				return true;
			} else{
				return false;
			}
		}
	}
	
	function showCodeWarnInfo(){
		var code = $("#code");
		code.on("focus",function(){
			var _Strinfo = '请输入验证码，区分大小写';
			if ($(this).siblings().hasClass("warn-info")) {
				$(this).siblings(".warn-info").text(_Strinfo).css("color","#333");
			} else{
				$(this).parent().append(_promptInfo);
				
				$(this).siblings(".warn-info").text(_Strinfo);
			}
		})
		code.on("blur",function(){
			var _Strinfo = ''
			if(code.val().length == 0){
				_Strinfo = '请输入验证码';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else if (code.val().length != 6) {
				_Strinfo = '请输入的验证码不合法';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
			} else{
				$(this).siblings(".warn-info").remove()
			}
		})
	}
}

function alertErrMsg(){
	var warnNum = $(".errct").text();
	if (warnNum.length != 0 ) {
		if (warnNum == '1') {
			$(".login-nav > ul >li").eq(1).addClass("cur-nav").siblings().removeClass("cur-nav");
			$("#signup").css({
				"display":"block"
			}).siblings().css({
				"display":"none"
			})
			$(".errmsg > p > span").text("账号密码有误");
			$(".errmsg").show().delay(500).fadeOut(2000);
		} else if(warnNum == '2'){
			$(".errmsg > p > span").text("验证码错误");
			$(".errmsg").show().delay(500).fadeOut(2000);
		} else if(warnNum == '3'){
			$(".login-nav > ul >li").eq(1).addClass("cur-nav").siblings().removeClass("cur-nav");
			$("#signup").css({
				"display":"block"
			}).siblings().css({
				"display":"none"
			})
			$(".errmsg > p > span").text("注册成功，请登陆");
			$(".errmsg").show().delay(500).fadeOut(2000);
		}else if(warnNum == '4'){
			$(".errmsg > p > span").text("注册失败");
			$(".errmsg").show().delay(500).fadeOut(2000);
		}else if(warnNum == '5'){
			$(".login-nav > ul >li").eq(1).addClass("cur-nav").siblings().removeClass("cur-nav");
			$("#signup").css({
				"display":"block"
			}).siblings().css({
				"display":"none"
			})
		}
	} else{
		return false;
	}
}

