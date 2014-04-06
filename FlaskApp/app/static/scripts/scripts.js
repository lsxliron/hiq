$(document).ready(function()
{
// $("input[id=array]").val("aaa");

	$("#p11").hide()
	$("#p18").hide()
	$("#p20").hide()
	$("#p21").hide()
	$("#p22").hide()
	$("#p23").hide()
	$("#p24").hide()
	$("#p25").hide()
	$("#p26").hide()
	$("#p27").hide()
	$("#p28").hide()
	$("#p29").hide()
	$("#p30").hide()
	$("#p31").hide()
	$("#p32").hide()
	$("#p33").hide()
	$("#p34").hide()
	$("#p37").hide()
	$("#p38").hide()
	$("#p39").hide()
	$("#p44").hide()
	$("#p45").hide()
	$("#p46").hide()


	//Remove pegs from the board when clicked
	$(".peg").click(function(){
			$(this).fadeOut("slow")
	});

	
	//Returns the current board to be the initial state.
	//From this state we will need to find a solution
	
	$(".submit").click(function(e){
	 //    alert("hi");
		// board_state=[];
		// for (var i=0; i<46; i++)
		// {
		// 	if ($("#"+i.toString()).length>0)
		// 	{
		// 		if ($("#"+i.toString()).is(":visible"))
				
		// 			board_state.push(1);
		// 		else
		// 			board_state.push(0);
		// 	}
		// 	else
		// 		board_state.push(-1);			
		// }


		// console.log(board_state);
		e.preventDefault();
		var board = prepareBoardState()

		

		$.ajax(
		{
			url:'/_find_solution/',
			method:'POST',
			
			data: { initialBoard: board },

			success: function(data)
			{
				res=data.split(',');
				arr = convert_to_int_array(res)
				console.log(arr)

				a=[]
				a.push(2)
				a.push(3)
				a.push(4)
				a.push(14)
				a.push(15)
				a.push(16)	
				animate_solution(arr)

			}
		});

		

	});
	
});

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

	// console.log(board_state);
	return boardStr;
}

function convert_to_int_array(str)
{
	arr = []
	for (var i=0; i<str.length; i++)
		arr.push(str[i])
	return arr
}

function animate_solution(move)
{
	for (var i=0; i<move.length-2; i+=3)
	{
		

		var s1=move[i]
		var s2=move[i+1]
		var s3=move[i+2]
		move_pegs(s1.toString(),s2.toString(),s3.toString())
		
	}
}

function move_pegs(s1, s2, s3)
{
		//Check which direction to move
		//Move right
		if (s1-s2 == -1)
		{
			console.log("right")	
			console.log(s1)
			console.log(s2)
			console.log(s3)
			$("#p"+s1.toString()).animate({right:'50px'});
			$("#p"+s2.toString()).fadeOut("slow")
			$("#p"+s3.toString()).fadeOut("slow")

		}

		//Move left
		else if (s1-s2 == 1)
		{
			console.log("left")	
			console.log(s1)
			console.log(s2)
			console.log(s3)
			$("#p"+s1.toString()).animate({left:'50px'});
			$("#p"+s2.toString()).fadeOut("slow")
			$("#p"+s3.toString()).fadeOut("slow")

		}
		//Move down
		else if (s1-s2 < 1)
		{
			console.log("down")	
			console.log(s1)
			console.log(s2)
			console.log(s3)
			$("#p"+s1.toString()).animate({down:50});
			$("#p"+s2.toString()).fadeOut("slow")
			$("#p"+s3.toString()).fadeOut("slow")

		}
		//Move up
		else
		{
			console.log("up")	
			console.log(s1)
			console.log(s2)
			console.log(s3)
			$("#p"+s1.toString()).animate({up:50});
			$("#p"+s2.toString()).fadeOut("slow")
			$("#p"+s3.toString()).fadeOut("slow")

		}
	
}




