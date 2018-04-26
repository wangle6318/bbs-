$(function(){
	checkLegal();
	
	
})


function checkLegal(){
	showUserNameWarnInfo();
	showPasswordWarnInfo();
	showCheckPwdSame();
	
	
	var _promptInfo = '<p class="warn-info"></p>';
	
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
		var pwd = $("#pwd1");
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
				return false;
			} else {
				$(this).siblings(".warn-info").remove();
				return true;
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
	
	
	function showCheckPwdSame(){
		var cpwd = $("#pwd2");
		cpwd.on("focus",function(){
			var _Strinfo = '请再次输入密码';
			if ($(this).siblings().hasClass("warn-info")) {
				$(this).siblings(".warn-info").text(_Strinfo).css("color","#333");
			} else{
				$(this).parent().append(_promptInfo);
				$(this).siblings(".warn-info").text(_Strinfo);
			}
		})
		cpwd.on("blur",function(){
			var _Strinfo = ''
			if (cpwd.val() == $("#pwd1").val()) {
				$(this).siblings(".warn-info").remove();
				return true;
			} else{
				_Strinfo = '两次输入的密码不一致，请重新输入';
				$(this).siblings(".warn-info").text(_Strinfo).css("color","red");
				return false;
			}
		})
	}

	return showPasswordWarnInfo() && showCheckPwdSame();
	
}
