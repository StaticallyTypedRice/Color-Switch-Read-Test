/*
    Color Switch Read Test

    Main JavaScript File (For the Django project only)

    Developed by Richie Zhang
    For IB Biology Internal Assessment
*/

// Sets the length of text displayed
var character_block_count = 30;
var character_block_size = 3;

// Sets the switching frequencies
var switchFreqInitial = [
	["Test Group 1: 2Hz", (1 / 2) * 1000],
	["Test Group 2: 4Hz", (1 / 4) * 1000],
	["Test Group 3: 6Hz", (1 / 6) * 1000],
	["Test Group 4: 8Hz", (1 / 8) * 1000],
	["Test Group 5: 10Hz", (1 / 10) * 1000],
];

// Randomizes the frequency order
// Snippet from https://css-tricks.com/snippets/javascript/shuffle-array/
function Shuffle(o) {
	for (var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
};

// Other variables
var switchFreqControl = ["Control: 0Hz", false];
var switchFreq = Shuffle(switchFreqInitial);
var color1 = $("#color1").val();
var color2 = $("#color2").val();
var testText = ["", "", "", "", "", ""];
var active = false;
var stage = -1;
var state;
var freq = 0;
var activeSwitcher;

// Add the control group to the start
switchFreq.unshift(switchFreqControl);

// The function for switching bwetten colors
function switcherChangeColors(stage, color1, color2) {
    if (stage) {
		$("html").css("color", color1);
		$("html").css("background-color", color2);
    } else {
		$("html").css("color", color2);
		$("html").css("background-color", color1);
    }
}

function switcherFlash(freq) {
	if (freq) {
		activeSwitcher = setInterval(
			function () {
				switcherChangeColors(state, $("#color1").val(), $("#color2").val());
				state = !state;
			}
		, freq);
	} else {
		state = true
		switcherChangeColors(state, $("#color1").val(), $("#color2").val());
	}
}

function startSwitcher() {
    // hide the introduction dialogue
	$("#introduction-wrap").hide();

    // show the experimentation text
	for (var i = 0; i < 6; i++) {
		for (var j = 0; j < character_block_count; j++) {
			for (var k = 0; k < character_block_size; k++) {
				testText[i] += String(Math.floor(Math.random() * (9 - 0)) + 0);
    		}
    		testText[i] += " ";
    	}
    }

	// Uploads Data to the server
	var uploadName = $("#trial-name").val()
	if (!uploadName || uploadName == "") {
		uploadName = "No Name Specified";
	}

	var uploadSwitchFreqOrder = "";
	for (var i = 0; i < 6; i++) {
		uploadSwitchFreqOrder += "[" + switchFreq[i][0] + "], ";
	}

    var uploadData = {
    	"name": uploadName,
    	"stage_order": uploadSwitchFreqOrder,
    	"comments": $("#trial-comments").val(),
    	"control": testText[0],
    	"stage_1": testText[1],
    	"stage_2": testText[2],
    	"stage_3": testText[3],
    	"stage_4": testText[4],
    	"stage_5": testText[5],
    };

	var upload = $.ajax({
    	method: "POST",
    	url: "/add/trial",
    	data: jQuery.param(uploadData),
	})
	upload.done(function (r) {
		if (r.submitted) {
			console.log("Upload Complete.");
		} else {
			alert(r.error.message);
			console.error(r.error.data);
		}
	});
	upload.fail(function (r) {
		alert("Server Error: " + r.status);
	});

	console.log(uploadSwitchFreqOrder);

	$("html").css("color", "#000000");
	$("html").css("background-color", "#ffffff");

	$("#instructions").show()
	active  = true

}

$(document).keydown(function (e) {
	if (active) {
		if (e.keyCode == 37) {
			// When the left arrow key (37) is pressed
			if (stage > 0) {
				window.clearInterval(activeSwitcher);
				stage--;

				document.title = "CSRT Stage " + [stage];
				$("#text").html("<span>" + testText[stage] + "</span>");
				$("#text").show();

				switcherFlash(switchFreq[stage][1]);
			}

		} else if (e.keyCode == 39 || e.keyCode == 13) {
			// When the right arrow key (39) or the ENTER key (13) is pressed
			if (stage < 5) {
				// A stage of 0 displays the control group
				// A stage of 1 to 5 shows the corresponding test group
				$("#instructions").hide()

				window.clearInterval(activeSwitcher);
				stage++;

				document.title = "CSRT Stage " + [stage];
				$("#text").html("<span>" + testText[stage] + "</span>");
				$("#text").show();

				switcherFlash(switchFreq[stage][1]);
			} else if (stage = 5) {
				window.clearInterval(activeSwitcher);
				$("html").css("color", "#000000");
				$("html").css("background-color", "#ffffff");
				$("#text").html("<span style=\"text-align: center;\"><br />End of current trial. Reload page to continue...</span>");
				document.title = "Done.";
				stage = null;
				active = false;
			}
		}
	}
});
