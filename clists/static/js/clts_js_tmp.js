$(function(){
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = cookies[i].trim();
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) === (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
});
$(function(){
	// console.log('am I here..?');
	$('.title_ip').focus();
	// $('#customSwitch1').bootstrapSwitch();
});

$(function(){

	$('.mn_sec').on('click','.adder', function(){
		this_c = $(this);
		// console.log(this);
		var ip_val = $(this).parents('.iform-cls').find('input[type="text"]');
		// console.log(ip_val.setCustomValidity('Please fill out this field'));
		// console.log('heheh');
		// console.log($(this).parents('.iform-cls').find('.item-ip').val() == '');
		if($(ip_val).val() == ''){
			// console.log(ip_val[0].validationMessage);
			$(ip_val)[0].setCustomValidity('Please fill out this field');
			$(ip_val)[0].reportValidity();
		}else{
			var form = $('.iform-cls');
			// console.log(form.serialize())
			$.ajax({
				context:this,
				url:'clists/items/',
				type: 'post',
				data:form.serialize(),
				success:function(data){
					// Displaying the saved items 
					if(data.status==true){
						$(this).parents('.form_container').prepend('<div id="Squarecheck"></div>');
						$(this).parents('.form_container').find('#Squarecheck').load('static/html/temp.html #Squarecheck');
					}
					$(this).parents('.form_container').find('.itm_ip_dv').empty().append('<span class="item-ip">'+data.items+'<span>');
					$(this).parents('.form_container').attr('id',data.id);

					// Empty items fields generator
					$(this).parents('.itms-secdv').append('<div class="lintothis"></div>');
					$(this).parents('.itms-secdv').find('.lintothis').load('static/html/temp.html #itm-cont', function(){
						$(this).attr('class','lintothis_old');
					})
					// console.log(this);
					if($(this).parents('.mn_sec').find('.lintothis').length == 1){
						$(this_c).hide()
					}else{
						$(this_c).remove();
					}		
				},
			});	
		}
	});

	$('.mn_sec').on('click','.remoer', function(){
		if($('.lintothis_old').length == 1){
			// console.log('here');
			$('.form_container').find('.adder:hidden').show();
			// append('<span type="submit" class="adder align-text-top">+</span>');
		}
		$(this).parents('.lintothis_old').remove();
	});


	$('.mn_sec').on('change','.custom-control-input', function(){
		var id = $(this).parents('.form_container').attr('id');
		var status = $(this).prop('checked');
		var items = $(this).parents('.form_container').find('.item-ip').text();
		// console.log(this);
		// console.log(items);
		var ip = $(this).parents('.form_container').find('.item-ip');
		if($(ip).val() != ''){
			$(this).parents('.form_container').prepend('<div class="p-2" id="compl"></div>');
			
			$(this).parents('.form_container').find('#compl').load('static/html/temp.html #Squarecheck', function(){
				console.log('Completed');
			})
		}else if(ip){
			// console.log($(this).prop());
			$(this).prop('checked', false);
			$(ip)[0].setCustomValidity('Please fill out this field');
			$(ip)[0].reportValidity();
		}
		if($(this).prop('checked') && items){
			console.log(this);
			ieAjFun();
			
		}
		else if(items){
			// console.log(this);
			ieAjFun();
			$(this).parents('.form_container').find('#compl').remove();
		}
		function ieAjFun(){
			$.ajax({
				context:this,
				url:'clists/items_edit/'+id+'/',
				type:'post',
				data:{'status':status, 'items':items},
				success:function(data){
					console.log('success');
				},

			})
		}
	});

});