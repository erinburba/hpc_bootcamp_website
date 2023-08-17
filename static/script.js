'use strict';

window.addEventListener('load', function () {

  console.log("Hello World!");

});

$(function() {
	$('a#test').on('click', function(e) {
		console.log(document.getElementById("bot_query").value);
		document.getElementById("status").innerHTML = "Querying...";
		$.ajax({
			data : {
			   query : document.getElementById("bot_query").value
				   },
			   type : 'POST',
			   url : '/query_chatbots',
			   timeout: 3000000
			  })
		  .done(function(result) {
			// $('#output').text(data.output).show();
			$.each(result, function(i, field){
				document.getElementById(i).innerHTML = field;
			//   $("div").append( i + " " + field + " ");
			});

			document.getElementById("status").innerHTML = "Done!";
		})
		.fail(function (jqXHR, exception) {
			console.log("ERROR");
			console.log(jqXHR);
			console.log(exception);
			document.getElementById("status").innerHTML = exception;
		});




	//   console.log("clicked");
	//   e.preventDefault()
	//   $.getJSON('/query_chatbots',
	//   {query: "what is energy justice"},
	//   function(result){
	// 	$.each(result, function(i, field){
	// 		document.getElementById(i).innerHTML = field;
	// 	//   $("div").append( i + " " + field + " ");
	// 	});
	//   });
	  return false;
	});
  });


function queryChatbots() {
	// console.log("Query time");
	var query = document.getElementById("bot_query").value
	console.log(query);

	return {
		"a": "answer A",
		"b": "answer B",
	}
}

