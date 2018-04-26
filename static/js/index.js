$(function(){
	//changeCurLeftNav();
	displaySetView();
	previewArticle();
	slideUpCommentInput();
	PDfshow();
	showReplyBlank();
})

function changeCurLeftNav(){
	var url = window.location.href
	var urlattr = url.split("/")
	if(urlattr[3]=='article_list'){
		var num = urlattr[4]
		console.log(num)
		var cur = $(".left-nav > ul >li");
		cur.eq(num).addClass("cur-left-nav").siblings().removeClass("cur-left-nav")
	}
}

function displaySetView(){
	var log = $(".logined > li >a");
	var view = $(".set-view");
	log.on("mouseenter",function(){
		view.css("display","block");
	})
	log.on("mouseleave",function(){
		view.css("display","none");
	})
	view.on("mouseenter",function(){
		view.css("display","block");
	})
	view.on("mouseleave",function(){
		view.css("display","none")
	})
}


function previewArticle(){
	var _strPre = '<div class="preview">'+
				  '<div class="close-preview">'+
				  '<img src="../../static/img/close.svg"/>'+
				  '</div>'+
				  '<div class="preview-ct">'+
				  '</div>'+
			      '</div>'
	var btn = $(".editor-article > span");
	var ct = $(".ncontent");
	
	btn.on("click",function(){
		ct.append(_strPre);
		ct.children(".preview").children(".preview-ct").html($("#text1").val())
	})

	ct.on("click",".close-preview img",function(){
		ct.children(".preview").remove();
	} )
}

function slideUpCommentInput(){
	$(".abs-com > .com-menu button").on("click",function(){
		$(".abs-com > .com-input").slideToggle();
	})
}


function PDfshow() {
	$(".prevpdf > a").on("click",function () {
		$("#pop").slideToggle();
    })
}

function showReplyBlank() {
	var btn = $(".btn-reply")
	btn.on("click",function () {
		$(this).siblings(".com-input").slideToggle()
    })
}

