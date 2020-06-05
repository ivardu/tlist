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
	$('.mn_sec').on('submit','.iform-cls, .tform-cls', function(event){
		event.preventDefault();
	})
	// $('#customSwitch1').bootstrapSwitch();
});


$(function(){
	// Title addition
	$('#id_title').on('blur', function(event){
		event.preventDefault();
		if($('#id_title').val() !== ''){
			var form = $('.tform-cls');
			$.ajax({
				context:this,
				url:'/clists/title/',
				type:'post',
				data:form.serialize(),
				success: function(data){
					$(this).parents('.tform-cls').replaceWith('<span class="sp-title-cls" id="val">'+data.title+'</span>');
					$('.sp-title-cls').attr('id',data.id);
					// console.log($('.sp-title-cls'));

				},
			})
		}
	})
	// Adder event execution
	$('.mn_sec').on('click','.adder', function(event){
		event.preventDefault();
		this_c = $(this);
		var ip_val = $(this).parents('.iform-cls').find('input[type="text"]');
		var item = $(this).parents('.iform-cls').find('.item-ip').text();
		// Validating the input text value when clicked on adder
		if($('#id_title').val() == ''){
				$('#id_title')[0].setCustomValidity('Enter the title');
				$('#id_title')[0].reportValidity();
		}else if($(ip_val).val() == ''){
			$(ip_val)[0].setCustomValidity('Please fill out this field');
			$(ip_val)[0].reportValidity();
		}else if(item){
			itemAdder.call(this);
		}else{
			var form = $('.iform-cls');
			var id = $('.sp-title-cls').attr('id');
			var error = $(this).parents('.lintothis_old').find('.dt-exi');
			if(error.length==0){
			// start of if
			$.ajax({
				context:this,
				url:'/clists/items/'+id+'/',
				type: 'post',
				data:form.serialize(),
				success:function(data){
					if(data.items){
						$(this).parents('.form_container').find('.itm_ip_dv').empty().append('<span class="item-ip item-ip1 ml-2">'+data.items+'<span>');
						$(this).parents('.form_container').attr('id',data.id);
						$(this).parents('.form_container').find('.custom-control-input').attr('id','ip'+data.id);
						$(this).parents('.form_container').find('.custom-control-label').attr('for','ip'+data.id);
						itemAdder.call(this);
					}
				},
				error: function(data){
					// console.log(data);
					var ip = $(this).parents('.form_container').find('.item-ip');
					$(ip).css({'border':'2px solid red'});
					$(this).parents('.form_container').after("<span class='dt-exi'>Duplicate Entry<span>");
					$(ip).focus();
					$(ip).on('keydown', function(){
						$(ip).css({'border':'1px solid'});
						$(ip).parents('.lintothis_old').find('.dt-exi').remove();
					});
				}
			});
			// Endofif
			}	
		}
		// Empty items fields generator
		function itemAdder(){
			$(this).parents('.itms-secdv').append('<div class="lintothis"></div>');
			$(this).parents('.itms-secdv').find('.lintothis').load('https://ticklistt.s3.amazonaws.com/static/html/temp.html #itm-cont', function(){
				// console.log($(this).attr('class'));
				$(this).attr('class','lintothis_old');
				// console.log($(this).attr('class'));
			})
			// Hiding the + 
			if($(this).parents('.mn_sec').find('.lintothis').length == 1){
				// console.log($(this).parents('.mn_sec').find('.lintothis').length);
				$(this_c).hide()
			}else{
				$(this_c).remove();
			}	

		}
	});

	$('.mn_sec').on('click','.remoer', function(){
		if($('.lintothis_old').length == 1){
			// console.log('here');
			$('.form_container').find('.adder:hidden').show();
			// append('<span type="submit" class="adder align-text-top">+</span>');
		}else if($('.lintothis_old').length == 2)
		{
			$('.lintothis_old').find('.adder:hidden').show();
		}
		if($(this).parents('.lintothis_old').length == 0){
			// $(this).parents('.form_container').remove();
			if($(this).parents('.form_container').find("input[class*='item-ip']").length==1){
				$(this).parents('.form_container').remove();
			}else{
				itmRem.call(this);
			}
		}else{
			// $(this).parents('.lintothis_old').remove();
			if($(this).parents('.form_container').find("input[class*='item-ip']").length==1){
				$(this).parents('.lintothis_old').remove();
			}else{
				itmRem.call(this);
			}
		}

		function itmRem(){
			var id = $(this).parents('.form_container').attr('id');
			$.ajax({
				context:this,
				url:'/clists/items_del/'+id+'/',
				type:'DELETE',
				success:function(data){
					console.log(data.success);
					if($(this).parents('.lintothis_old').length == 0){
						$(this).parents('.form_container').remove();
					}else{
						$(this).parents('.lintothis_old').remove();
					}

				}
			})
		}
	});


	$('.mn_sec').on('change','.custom-control-input', function(event){
		event.preventDefault();
		var id = $(this).parents('.form_container').attr('id');
		var status = $(this).prop('checked');
		var items = $(this).parents('.form_container').find('.item-ip').text();
		var ip = $(this).parents('.form_container').find('input[class*="item-ip"]');

		// validating the switch with input text value
		if($(ip).val() != ''){
			if($(this).prop('checked')){
				remCompl.call(this);
			}
			else{
				$(this).parents('.form_container').find('#Squarecheck').remove();
			}
		}else if(ip.length==1){
			$(this).prop('checked', false);
			$(ip)[0].setCustomValidity('Please fill out this field');
			$(ip)[0].reportValidity();
		}

		// Validating the Switch with span text value
		if($(this).prop('checked') && items){
			if($(this).parents('.form_container').find('#Squarecheck').length == 0){
				remCompl.call(this);
			}
			ieAjFun.call(this);
		}
		else if(items){
			ieAjFun.call(this);
			$(this).parents('.form_container').find('#Squarecheck').remove();
		}
		// Adding the Squarecheck
		function remCompl(){
			$(this).parents('.form_container').find('.compl').load('https://ticklistt.s3.amazonaws.com/static/html/temp.html #Squarecheck', function(){
					console.log('Added Squarecheck');
				});
		}
		// Editing the existing data
		function ieAjFun(){
			$.ajax({
				context:this,
				url:'/clists/items_edit/'+id+'/',
				type:'post',
				data:{'status':status, 'items':items},
				success:function(data){
					console.log('success');
				},

			})
		}
	});

});

// Delete functoinality
$(function(){
	$('#staticBackdrop').modal('hide');
	$('.mn_sec').on('click', '.del', function(event){
		event.preventDefault();
		// $('#dialog-confirm').dialog({});
		var this_c = $(this)
		// console.log(this_c)
		$('#staticBackdrop').modal('show');
		$('#mod-del').on('click', function(){
			console.log('working');
			var lid = $(this_c).parents('li').attr('id');
			$.ajax({
				context:this,
				url:'/clists/clist_delete/'+lid+'/',
				type:'DELETE',
				success:function(data){
					// console.log(this_c);
					// console.log($(this_c));
					// console.log(this);
					console.log(data.count);
					$('#staticBackdrop').modal('hide');
					$('#hdr-br-tmpl').text(data.count);
					$(this_c).parents('li').remove();
				}
			});
			// console.log(this_c);
		});
		
	});

	$('#sBdrop').modal('hide');
	$('.lgn').on('click', function(event){
		event.preventDefault();
		// $('#dialog-confirm').dialog({});
		// var this_c = $(this)
		console.log('Am I here..?')
		$('#sBdrop').modal('show');
	});

});