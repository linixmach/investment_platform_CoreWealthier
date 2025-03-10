jQuery(document).ready(function()
{      jQuery("a[role='tab']").click(function()
        {      		 
		     jQuery("input[type='radio'][name='h_id']").removeAttr('checked');		 
			 jQuery(this).parents("label").find("input[type='radio'][name='h_id']").attr('checked', 'checked').prop('checked', true);		 
			 console.log('radio checked');        
       });
});

$(document).ready(function(){
	wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100,
        callback:     function(box) {
          console.log("WOW: animating <" + box.tagName.toLowerCase() + ">")
        }
      }
    );
    wow.init();
    
	var percent =  document.getElementById("Ultra") ? parseFloat(document.getElementById("Ultra").value) : 0; 
	
	//Calculator
	function calc(){
		var money = parseFloat($("#money").val());
		switch (percent) {
		    case 0:
		        if( (money >= 10 && money < 1000)){
		        	var profitDaily = money / 100 * 170;
					var profitDaily = profitDaily.toFixed(2);

				

					$("#profitDaily").text(profitDaily);
		        } if (money < 10){
					$("#profitDaily").text("Error!");
				}
		        break;
			case 1:
		        if( (money >= 10 && money < 1000)){
		        	var profitDaily = money / 100 * 310;
					var profitDaily = profitDaily.toFixed(2);


					$("#profitDaily").text(profitDaily);
		        } if (money < 10){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 2:
		    	if( (money >= 10 && money < 3000)){
		        	var profitDaily = money / 100 * 435;
					var profitDaily = profitDaily.toFixed(2);

				

					$("#profitDaily").text(profitDaily);
		        } if (money < 10){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 3:
		    	if( (money >= 10 && money < 3000)){
		        	var profitDaily = money / 100 * 125;
					var profitDaily = profitDaily.toFixed(2);

				

					$("#profitDaily").text(profitDaily);
		        } if (money < 10){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 4:
		    	if( (money >= 10 && money < 500)){
		        	var profitDaily = money / 100 * 300;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money >= 501 && money < 1000) {
		        	var profitDaily = money / 100 * 600;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money >= 1001 && money < 5000) {
		        	var profitDaily = money / 100 * 900;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money >= 5001 && money < 10000) {
		        	var profitDaily = money / 100 * 1200;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money >= 10001 && money < 100000) {
		        	var profitDaily = money / 100 * 1400;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money < 10){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 5:
				if( (money >= 5000  && money < 25000)){
		        	var profitDaily = money / 100 *  300;
					var profitDaily = profitDaily.toFixed(2);
					
					$("#profitDaily").text(profitDaily);	
				}	
				if( (money >= 25001  && money < 50000)){
		        	var profitDaily = money / 100 *  600;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
		        } if (money < 5000){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 6:
		    if( (money >= 500  && money < 5000)){
		        	var profitDaily = money / 100 *  750;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
					
				}
				if( (money >= 5001  && money < 10000)){
		        	var profitDaily = money / 100 *  1500;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);	
					
		        } if (money < 500){
					$("#profitDaily").text("Error!");
				}
		        break;
		    case 7:
		    	if( (money >= 100 && money < 1000 )){
		        	var profitDaily = money / 100 *  1200;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);
					
				}	
				if( (money >= 1001 && money < 10000 )){
		        	var profitDaily = money / 100 *  2000;
					var profitDaily = profitDaily.toFixed(2);

					$("#profitDaily").text(profitDaily);	
					
		        } if (money < 100){
					$("#profitDaily").text("Error!");
				}
		        break;
		}
	}
	if($("#money").length){
		calc();
	}
	$("#money").keyup(function(){
		calc();
	});

	$("#Ultra").on('change', function() {
		percent = parseFloat(this.value);
		calc();
	})
});


/// New Code Starts from Here
jQuery(document).ready(function(){
	
	jQuery("#amttospd").keyup(function()
	{
		var perc = jQuery(".nav.nav-tabs li.active a").attr("perc");
		console.log( "Total Investment Amount being changed, Perc =" + perc );
		calcNew(perc);
	});
	
	// When Top TAB is clicked, the Deposit TEXT box gets "20$" default value
	jQuery("ul.nav.nav-tabs li a").click(function(){
		 
		var t = jQuery(this).attr("min");
		var pp = jQuery(this).attr("perc");
		console.log("min value is " + t + ", and Perc is : " + pp);
		jQuery("#amttospd").val(t);				
		console.log(jQuery(this).next().attr('id'));				
		jQuery(this).next().attr('checked', 'checked').prop('checked', true);
		calcNew(pp);
	});
	
	// Trigger a click on the first TAB when the page loads
	if( jQuery("ul.nav.nav-tabs li a").length ) jQuery("ul.nav.nav-tabs li a")[0].click();
	
});

function calculate(depositAmt, checkBoxValue = '', tt, perc)
{
	jQuery("#amttospd").val(depositAmt);
	console.log("Showing Arguments : " + depositAmt + ":" + checkBoxValue);
	console.log(tt);		
	console.log('active Class Added');
	// if( checkBoxValue ) jQuery("[name='h_id']").val(checkBoxValue);    
	var l = jQuery(tt).parents("tr").find("input[type='radio']");
	if(l)
	{
		// Select the INput
		window.ourtarget = l;
		jQuery(l).attr('checked', 'checked');
		jQuery(l).prop('checked', true);
		console.log('Updated the field');
	}   
	calcNew(perc);
}
function calcNew(perc) 
{
	// Get User Input
	// if( perc == 0 ) perc = jQuery(".nav.nav-tabs li.active a").attr("perc");
	var money = parseFloat($("#amttospd").val().replace(/^\s+|\s+$/,''));
	var plan = "";
	if( money == '' || isNaN(money) ) money = 0;
	// if(!perc) perc = 0;
	// Find the Percentage
	/*
	var matchText = "\$" + money
    jQuery(".tab-pane.active td").each(function()
	{  
	   var t = jQuery(this).text(); 
	   if(t.match(/\$20\.00/)) jQuery(this).addClass('LADDU'); });	
	*/
	
	// GET TOP Plans
	if( jQuery(".nav.nav-tabs li.active").length )
	{
		
		// var perc = jQuery(".nav.nav-tabs li.active a").attr("perc");
		var profit_percentage = 0;
		if( perc == 125 )
		{
			if( money >=20 && money <= 500 ) { profit_percentage = 103; plan = "plan1"; }
			if( money >=501 && money <= 1000 ) { profit_percentage = 105; plan = "plan2"; }
			if( money >=1001 && money <= 5000 ) { profit_percentage = 110; plan = "plan3"; }
			if( money >=5001 && money <= 10000 ) { profit_percentage = 120; plan = "plan4"; }
			if( money >=10001 && money <= 100000 ) { profit_percentage = 125; plan = "plan5"; }
			if( money >=25001 && money <= 50000 ) { profit_percentage = 130; plan = "plan6"; }
			if( money >=50001 && money <= 100000 ) { profit_percentage = 135; plan = "plan7"; }
		}
		else if( perc == 200 )
		{
			if( money >=20 && money <= 500 ) { profit_percentage = 115; plan = "plan1"; }
			if( money >=501 && money <= 1000 ) { profit_percentage = 120; plan = "plan2"; }
			if( money >=1001 && money <= 5000 ) { profit_percentage = 140; plan = "plan3"; }
			if( money >=5001 && money <= 10000 ) { profit_percentage = 180; plan = "plan4"; }
			if( money >=10001 && money <= 100000 ) { profit_percentage = 200; plan = "plan5"; }
			if( money >=25001 && money <= 50000 ) { profit_percentage = 220; plan = "plan6"; }
			if( money >=50001 && money <= 100000 ) { profit_percentage = 250; plan = "plan7"; }

		}
		else if( perc == 300 )
		{
			if( money >=20 && money <= 500 ) { profit_percentage = 130;  plan = "plan1"; }
			if( money >=501 && money <= 1000 ) { profit_percentage = 160;  plan = "plan2"; }
			if( money >=1001 && money <= 5000 ) { profit_percentage = 200;  plan = "plan3"; }
			if( money >=5001 && money <= 10000 ) { profit_percentage = 250;  plan = "plan4"; }
			if( money >=10001 && money <= 100000 ) { profit_percentage = 300;  plan = "plan5"; }
			if( money >=25001 && money <= 50000 ) { profit_percentage = 360;  plan = "plan6"; }
			if( money >=50001 && money <= 100000 ) { profit_percentage = 450; plan = "plan7"; }	 		
		}
		else if( perc == 450 )
		{
			if( money >=20 && money <= 500 ) { profit_percentage = 150; plan = "plan1"; }	 
			if( money >=501 && money <= 1000 ) { profit_percentage = 200; plan = "plan2"; }	 
			if( money >=1001 && money <= 5000 ) { profit_percentage = 350; plan = "plan3"; }	 
			if( money >=5001 && money <= 10000 ) { profit_percentage = 400; plan = "plan4"; }	 
			if( money >=10001 && money <= 100000 ) { profit_percentage = 450; plan = "plan5"; }	 
			if( money >=25001 && money <= 50000 ) { profit_percentage = 750; plan = "plan6"; }	 
			if( money >=50001 && money <= 100000 ) { profit_percentage = 900;	plan = "plan7"; }	  				
		}
		else if( perc == 1400 )
		{
			if( money >=20 && money <= 500 ) { profit_percentage = 300; plan = "plan1"; }	 
			if( money >=501 && money <= 1000 ) { profit_percentage = 600; plan = "plan2"; }	 
			if( money >=1001 && money <= 5000 ) { profit_percentage = 900; plan = "plan3"; }	 
			if( money >=5001 && money <= 10000 ) { profit_percentage = 1200; plan = "plan4"; }	 
			if( money >=10001 && money <= 100000 ) { profit_percentage = 1400; plan = "plan5"; }	
			if( money >=25001 && money <= 50000 ) { profit_percentage = 1200; plan = "plan6"; }	 
			if( money >=50001 && money <= 100000 ) { profit_percentage = 1400; plan = "plan7"; }	 	 				
		}
		else if( perc == 600 )
		{
			if( money >=5000 && money <= 25000 ) { profit_percentage = 400; plan = "plan1"; }
			if( money >=25001 && money <= 50000 ) { profit_percentage = 600; plan = "plan2"; }			
		}
		else if( perc == 1500 )
		{
			if( money >=500 && money <= 5000 ) { profit_percentage = 750; plan = "plan1"; }
			if( money >=5001 && money <= 10000 ) { profit_percentage = 1500; plan = "plan2"; }
		}
		else if( perc == 2000 )
		{
			if( money >=100 && money <= 1000 ) { profit_percentage = 1200; plan = "plan1"; }
			if( money >=1001 && money <= 10000 ) { profit_percentage = 2000; plan = "plan2"; }
		}
		
		// Start the calculation
		
		var total_profit = parseFloat(money * profit_percentage / 100);
		total_profit = total_profit.toFixed(2);
		jQuery("#total_profit").html(total_profit); 
		
		var total_return = parseFloat(money * profit_percentage / 100 - money);
		total_return = total_return.toFixed(2);
		jQuery("#total_return").html(total_return);
		
		console.log( "CalcNew : ",perc, money, profit_percentage, plan, total_profit, total_return);
		//
		// Remove Active class from Current PLANS
		jQuery(".tab-content .tab-pane.active table tr").removeClass('active');
		console.log("Money : " + money + ", plan : " + plan);
		if( money != 0 && plan != "")
		{
			// Add active class 
			setTimeout( function()
			{
			   jQuery(".tab-content .tab-pane.active table tr." + plan).addClass('active');
			}, 200);
			console.log(".tab-content .tab-pane.active table tr." + plan);
		}
		else
		{
			console.log("Exception");
		}
		
	}
}
