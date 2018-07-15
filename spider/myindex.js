var ivsurl="http://192.23.0.45:7001/";

function getProUrl() {
	var location = (window.location + '').split('/');
	var basePath = "";
	if(location[3] == "hljweb"){
		basePath = location[0] + '//' + location[2] + '/' + location[3];
	} else{
		basePath = location[0] + '//' + location[2];
	}
	/*if (location[3] == undefined || location[3] == "") {
		basePath = location[0] + '//' + location[2];
	} else if (location[3] == "pub") {
		basePath = location[0] + '//' + location[2] ;
	} else {
		basePath = location[0] + '//' + location[2] + '/' + location[3];
	}*/
	return basePath;
}
var webPath = getProUrl();


$(document).ready(function(){
	// 内部核查地址
	$("#dtSpan").html('');
	$("#dtSpan").append(GetCurrentDateTime(1,0,0));
	$("#dtSpan").append(' 农历');
	$("#dtSpan").append(GetCNDate());
	$("#dtSpan").append(GetCurrentDateTime(0,0,1));
	// 公示信息
    // show=1表示当前页面为首页,show=2表示当前不为首页;传递number值表示当前页面最多能够展示10条数据

	settopHi();
});
/** 退出 */
function logout_(){
	$.ajax(webPath+"/regController.do?logout",{
		data:{},
		dataType:'json',// 服务器返回json格式数据
		type:'post',// HTTP请求类型
		success:function(data){
			// alert(data.flag);
			if(data.flag==true || data.flag=="true"){ 
				/*$.cookie("websitlogin", "");
				$.cookie("websitusername", "");*/
				window.location.href=webPath;
			}
		}
});

};

// 修改验证码
function changeRand(){
	var location = (window.location+'').split('/'); 
	var basePath = "";
	if(location[3]==undefined || location[3]==""){
		basePath = location[0]+'//'+location[2];
	}else if(location[3]=="index.html"){
		basePath = location[0]+'//'+location[2];
	}else{
		basePath = location[0]+'//'+location[2]+'/'+location[3];
	}
	document.getElementById('randImg').src=basePath+'/imageServlet?dt='+new Date();
}

function enterlogin(event){
		var code=(navigator.userAgent.indexOf("MSIE")>0)?event.keyCode:event.which;
		if(parseInt(code)==13){
			$("#subA").focus();
			subForm();
		}
	}

// 提交查询
function subForm(){
	var uniscid = $('input[name=uniscid]').val();
	var qymcGs = $('input[name=qymcGs]').val();
	if(uniscid =='' && qymcGs==''){
		alert('请输入查询条件');
		$('input[name=uniscid]').focus();
		return ;
	}
	var randCode = $('#randCode').val();
	if(randCode==''){
		// setTip('请输入验证码');
		alert('请输入验证码');
		$('#randCode').focus();
		return ;
	}
	
	jQuery.ajax({
		type : "get",
		url : webPath+"/WebCreditQueryService.do?doCheckCode&randCode="+randCode, 
		async : false,
		cache : false,
		dataType:'text',
		success : function(result) {
			result = $.trim(result);
			if(result=='1'){
				document.WebCreditQueryServiceFrameName.submit();
				changeRand();
				$('#randCode').val('');
			}else if(result=='0'){
// setTip('验证码错误');
				alert('验证码错误');
				changeRand();
				$('#randCode').val('');
				$('#randCode').focus();
			}else if(result=='-1'){
			// setTip('验证码已过期');
				alert('验证码已过期');
				changeRand();
				$('#randCode').val('');
				$('#randCode').focus();
			}else if(result=='-2'){
// setTip('请输入验证码');
				alert('请输入验证码');
				$('#randCode').focus();
			}
		}
	});
	
}
// 设置错误信息
function setTip(_html){
	$('#errorTip').html(_html);
}
	
// 当前时间
	function CurentTime(){ 
        var now = new Date();
       
        var year = now.getFullYear();       // 年
        var month = now.getMonth() + 1;     // 月
        var day = now.getDate();            // 日
       
        var hh = now.getHours();            // 时
        var mm = now.getMinutes();          // 分
       
        var clock ='今日是 ' +year + "-";
       
        if(month < 10)
            clock += "0";
       
        clock += month + "-";
       
        if(day < 10)
            clock += "0";
           
        clock += day + " ";
       
       // if(hh < 10)
       // clock += "0";
           
      // clock += hh + ":";
       // if (mm < 10)
      // clock += '0';
      // clock += mm;
        
        clock +='  农历';
        clock +='  星期';
        
        return (clock); 
	} 
	// 给顶部的欢迎词赋值
	function settopHi() {
		
			$.ajax(webPath+"/regController.do?checkislogin",{
				data:{},
				dataType:'json',// 服务器返回json格式数据
				type:'post',// HTTP请求类型
				success:function(data){
					if(data.flag==true || data.flag=="true"){ 
						$("#welcome").html("您好：" + data.loginUser + "，欢迎访问信用黑龙江");
						$("#dtSpan").html('');
						$("#dtSpan").append(GetCurrentDateTime(1,0,0));
						$("#dtSpan").append(' 农历');
						$("#dtSpan").append(GetCNDate());
						$("#dtSpan").append(GetCurrentDateTime(0,0,1));
						$("#dtSpan").append(" <a href='javascript:void(0)' id='logout_hlj' onclick='logout_();' style='color:white;'>[退出]</a>");
					}else{
						$("#welcome").html("您好！欢迎访问信用黑龙江");
						$("#dtSpan").html('');
						$("#dtSpan").append(GetCurrentDateTime(1,0,0));
						$("#dtSpan").append(' 农历');
						$("#dtSpan").append(GetCNDate());
						$("#dtSpan").append(GetCurrentDateTime(0,0,1));
					}
				}
		});
			
		};	
// 友链等打开页面
 function opentargetwindow(targeturl){
	 if (targeturl!="" && targeturl !="#" && targeturl !="http://"){
		 window.open(targeturl);
	 }
 }	
	function _QueryByUrl(url){
	 	url =url;// + "&marprid="+parseInt(${tBCoreBdataPage_jc.id});
// $('#one1').panel('refresh', url);
	 	window.open(url, "_blank", "", false);
 	}

	// 将window.open 优化一下，改写成链接的方式
	function openwin(url) {
		// 1 这种方法会被 360急速、火狐拦截
	  /*
		 * var a = document.createElement("a"); a.setAttribute("href", url);
		 * a.setAttribute("target", "_blank"); a.setAttribute("id", "openwin");
		 * document.body.appendChild(a); a.click();
		 */
		/*
		 * $.ajax(url); //模拟新新窗口方式的表单提交以打开新开页 if (url !== "") { var $tempForm =
		 * $('<form method="post" target="_self" action="' + url + '"></form>');
		 * $("body").append($tempForm); $tempForm.submit(); $tempForm.remove(); }
		 */

	   // newTab.location.href=url;
	    // 3 这种方法会被 360，火狐拦截
		/*
		 * var tempwindow=window.open('_blank'); tempwindow.location=url;
		 */
	}	
	
	//流控
	function tongji(cmain) {
		$.ajax(webPath+"/flowCalculateController.do?index",{
			data:{"cmain":cmain,"flowname":"xyhlj"},
			dataType:'json',//服务器返回json格式数据
			type:'post',//HTTP请求类型
			success:function(data){
			}
		});
	}