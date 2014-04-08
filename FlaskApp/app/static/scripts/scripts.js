$(document).ready(function()
{
	
	$(".inner #ex1").click(function(e)
	{
		e.preventDefault()
		$(".peg").show();
		// Board 1
		$("#p11").hide();
		$("#p18").hide();
		$("#p20").hide();
		$("#p21").hide();
		$("#p22").hide();
		$("#p23").hide();
		$("#p24").hide();
		$("#p25").hide();
		$("#p26").hide();
		$("#p27").hide();
		$("#p28").hide();
		$("#p29").hide();
		$("#p30").hide();
		$("#p31").hide();
		$("#p32").hide();
		$("#p33").hide();
		$("#p34").hide();
		$("#p37").hide();
		$("#p38").hide();
		$("#p39").hide();
		$("#p44").hide();
		$("#p45").hide();
		$("#p46").hide();
		return;
	});

	
	$(".inner #ex2").click(function(e)
	{
		e.preventDefault()
		$(".peg").show();
		
		// Board 2
		$("#p2").hide();
		$("#p3").hide();
		$("#p4").hide();
		$("#p10").hide();
		$("#p11").hide();
		$("#p12").hide();
		$("#p14").hide();
		$("#p15").hide();
		$("#p16").hide();
		$("#p17").hide();
		$("#p20").hide();
		$("#p21").hide();
		$("#p22").hide();
		$("#p23").hide();
		$("#p24").hide();
		$("#p25").hide();
		$("#p26").hide();
		$("#p27").hide();
		$("#p28").hide();
		$("#p31").hide();
		$("#p32").hide();
		$("#p33").hide();
		$("#p34").hide();
		$("#p35").hide();
		$("#p36").hide();
		$("#p37").hide();
		$("#p39").hide();
		$("#p44").hide();
		$("#p45").hide();
		$("#p46").hide();
		return;
	});

	$(".inner #ex3").click(function(e)
	{
		e.preventDefault();
		$(".peg").show();
		//Board 3
		$("#p2").hide();
		$("#p10").hide();
		$("#p11").hide();
		$("#p12").hide();
		$("#p14").hide();
		$("#p18").hide();
		$("#p21").hide();
		$("#p24").hide();
		$("#p28").hide();
		$("#p29").hide();
		$("#p32").hide();
		$("#p35").hide();
		$("#p36").hide();
		$("#p37").hide();
		$("#p39").hide();
		$("#p44").hide();
		return;
	});
	

	//Hide the loading GIF
	$("#loadingGIF").hide()

	
	//Remove pegs from the board when clicked
	$(".peg").click(function()
	{
			$(this).fadeOut("slow");
	});

	
	//Returns the current board to be the initial state.
	//From this state we will need to find a solution
	$(".submit").click(function(e)
	{
		e.preventDefault();
		var board = prepareBoardState();

		$("#loadingGIF").show();
		$.ajax(
		{
			url:'/_find_solution/',
			method:'POST',
			data: {initialBoard: board},
			
			
			success: function(data)
			{
				$("#loadingGIF").hide()
				if (data!="")
				{
					res=data.split(',');
					arr = convert_to_int_array(res);
					animate_solution(false,arr);
				}

				else
				{
					$(".peg").animate({opacity: 0.25}, {duration: 200})
					$(".grid").animate({opacity: 0.25}, {duration: 200})
					$("loadingGIF").remove();
					$("#message").append("No solution found...");
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


//This function animates one step at a time
function animate_solution_helper(move)
{

	var time = 100;		//Time to delay animation
	var i=0				//Index variable
	var s1=move[i];		//First coordinate of the move
	var s2=move[i+1];	//Second coordinate of the move
	var s3=move[i+2];	//Third coordinate of the move
	

	//Remove spaces from the move string
	s1 = s1.replace(/\s+/g, '');
	s2 = s2.replace(/\s+/g, '');
	s3 = s3.replace(/\s+/g, '');
	
	//Check which direction to move
	
	//Move right
	if (s1-s2 == -1)
	{
		$("#p"+s1).delay(time).animate({marginLeft: "+=210px"}, {duration: 1000});
		$("#p"+s2).delay(time+1000).fadeOut({duration: 1000}, function(){$(this).remove()});
		$("#p"+s3).delay(time).animate({marginLeft: "-=210px"}, {duration: 1000});
	}

	//Move left
	else if (s1-s2 == 1)
	{
		$("#p"+s1).delay(time).animate({marginLeft: "-=210px"}, {duration: 1000});
		$("#p"+s2).delay(time+1000).fadeOut({duration: 1000}, function(){$(this).remove()});
		$("#p"+s3).delay(time).animate({marginLeft: "+=210px"}, {duration: 1000});
	}

	//Move down
	else if (s1-s2 < 0)
	{

		$("#p"+s1).delay(time).animate({marginTop: "+=210px"}, {duration: 1000});
		$("#p"+s2).delay(time+1000).fadeOut({duration: 1000}, function(){$(this).remove()});
		$("#p"+s3).delay(time).animate({marginTop: "-=210px"}, {duration: 1000});
	}
	
	//Move up
	else
	{
		$("#p"+s1).delay(time).animate({marginTop: "-=210px"}, {duration: 1000});
		$("#p"+s2).delay(time+1000).fadeOut({duration: 1000}, function(){$(this).remove()});
		$("#p"+s3).delay(time).animate({marginTop: "+=210px"}, {duration: 1000});
	}
	
	//Reset variables
	s1="";
	s2="";
	s3="";
}

//This function gets an array of moves and performs one move at a time.
//This function exists to animates move sequentaly
function animate_solution(flag, moves)
{		
	//Executes one move at a time every 2 seconds	
	setTimeout(function()
	{
		var tempID;			//variable to hold a peg ID
		var oneMove = [];	//The move to perform
		
		//Fetch one move
		oneMove.push(moves[0].replace(/\s+/g, ''));
		oneMove.push(moves[1].replace(/\s+/g, ''));
		oneMove.push(moves[2].replace(/\s+/g, ''));
		
		//Animate the move
		animate_solution_helper(oneMove);
		
		//Swap pegs ID
		tempID = "p"+oneMove[2];

		//Remove unecessary pegs
		$("#p"+oneMove[2]).remove()
		$("#p"+oneMove[0]).attr('id',tempID)

		//Pop the move that was performed
		moves.shift();
		moves.shift();
		moves.shift();
		
		// Return when there are no more moves to perform
		if (oneMove.length == 0)
			return
		//Else perform the next move
		else
			animate_solution(false, moves)

	},2000);
}



});
