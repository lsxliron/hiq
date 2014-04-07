$(document).ready(function()
{



// $("#p9").animate({marginTop	: "+=210px"}, {duration: 1000, queue: "global"});
// $("#p16").fadeOut({duration: 1000, queue: "global"});
// $.fxqueue("global").start();	
	// console.log($.fxqueue("global").length)
	var queue = $(".grid").queue("global")
	

	// $("#p11").hide()
	// $("#p18").hide()
	// $("#p20").hide()
	// $("#p21").hide()
	// $("#p22").hide()
	// $("#p23").hide()
	// $("#p24").hide()
	// $("#p25").hide()
	// $("#p26").hide()
	// $("#p27").hide()
	// $("#p28").hide()
	// $("#p29").hide()
	// $("#p30").hide()
	// $("#p31").hide()
	// $("#p32").hide()
	// $("#p33").hide()
	// $("#p34").hide()
	// $("#p37").hide()
	// $("#p38").hide()
	// $("#p39").hide()
	// $("#p44").hide()
	// $("#p45").hide()
	// $("#p46").hide()

	$("#p2").hide()
	$("#p3").hide()
	$("#p4").hide()
	$("#p10").hide()
	$("#p11").hide()
	$("#p12").hide()
	$("#p14").hide()
	$("#p15").hide()
	$("#p16").hide()
	$("#p17").hide()
	$("#p20").hide()
	$("#p21").hide()
	$("#p22").hide()
	$("#p23").hide()
	$("#p24").hide()
	$("#p25").hide()
	$("#p26").hide()
	$("#p27").hide()
	$("#p28").hide()
	$("#p31").hide()
	$("#p32").hide()
	$("#p33").hide()
	$("#p34").hide()
	$("#p35").hide()
	$("#p36").hide()
	$("#p37").hide()
	$("#p39").hide()
	$("#p44").hide()
	$("#p45").hide()
	$("#p46").hide()

	// $("#p2").hide()
	// $("#p10").hide()
	// $("#p11").hide()
	// $("#p12").hide()
	// $("#p14").hide()
	// $("#p18").hide()
	// $("#p21").hide()
	// $("#p24").hide()
	// $("#p28").hide()
	// $("#p29").hide()
	// $("#p32").hide()
	// $("#p35").hide()
	// $("#p36").hide()
	// $("#p37").hide()
	// $("#p39").hide()
	// $("#p44").hide()
	







	//Remove pegs from the board when clicked
	$(".peg").click(function()
	{
			$(this).fadeOut("slow")
			console.log($(this).attr('id'));
	});

	
	//Returns the current board to be the initial state.
	//From this state we will need to find a solution
	$(".submit").click(function(e)
	{
		e.preventDefault();
		var board = prepareBoardState()	

		$.ajax(
		{
			url:'/_find_solution/',
			method:'POST',
			data: {initialBoard: board},

			success: function(data)
			{
				if (data!="")
				{
					res=data.split(',');
					arr = convert_to_int_array(res)
					animate_solution(arr)
				        
				}

				else
				{
					console.log("NO SOLUTION FOUND")

				}

			}
		});
	});
	
//Create an array from the initial board state
function prepareBoardState()
{
	board_state=[];
	for (var i=0; i<49; i++)
	{
		if ($("#p"+i.toString()).length>0)
		{
			if ($("#p"+i.toString()).is(":visible"))
			
				board_state.push(1);
			else
				board_state.push(0);
		}
		else
			board_state.push(-1);
	}
	var boardStr = board_state.toString();
	return boardStr;
}

//Convert the string array to integers array
function convert_to_int_array(str)
{
	arr = []
	for (var i=0; i<str.length; i++)
		arr.push(str[i])
	return arr
}


//Animates the steps for the solution
function animate_solution(move)
{
	for (var i=0; i<move.length-2; i=i+3)
	{
		var s1=move[i];
		var s2=move[i+1];
		var s3=move[i+2];
		var hiddenID = 100

		s1 = s1.replace(/\s+/g, '');
		s2 = s2.replace(/\s+/g, '');
		s3 = s3.replace(/\s+/g, '');
		
		//Check which direction to move
		//Move right
		if (s1-s2 == -1)
		{
			$("#p"+s1).animate({marginLeft: "+=210px"}, {duration: 50, queue: "global"});
			$("#p"+s2).fadeOut({duration: 1000, queue: "global"});

			$("#p"+s2).attr('id',"p"+hiddenID)
			$("#p"+s1).attr('id',"p"+s3.toString())
			
		}

		//Move left
		else if (s1-s2 == 1)
		{
			$("#p"+s1).animate({marginLeft: "-=210px"}, {duration: 50, queue: "global"});
			$("#p"+s2).fadeOut({duration: 1000, queue: "global"});

			$("#p"+s2).attr('id',hiddenID)
			$("#p"+s1).attr('id',"p"+s3.toString())
			
		}

		//Move down
		else if (s1-s2 < 0)
		{

			$("#p"+s1).animate({marginTop: "+=210px"}, {duration: 50, queue: "global"});
			$("#p"+s2).fadeOut({duration: 1000, queue: "global"});

			$("#p"+s2).attr('id',hiddenID)
			$("#p"+s1).attr('id',"p"+s3.toString())
			
		}
		
		//Move up
		else
		{
			console.log("up");
			console.log("Moving "+ s1 + "to " +s3)
			console.log(s2 + "disappeard")
			
			
			$("#p"+s1).animate({marginTop: "-=210px"}, {duration: 50, queue: "global"});
			$("#p"+s2).fadeOut({duration: 1000, queue: "global"});
	

			$("#p"+s2).attr('id',hiddenID)
			$("#p"+s1).attr('id',"p"+s3.toString());
			
		}

		hiddenID=hiddenID +10
	}
	
	
	$.fxqueue("global").start();
	
	
	
	
}

});
