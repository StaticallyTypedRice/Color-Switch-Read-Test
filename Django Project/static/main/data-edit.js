// Uploads the edited data to the server

function dataEdit() {
	var upload = $.ajax({
		method: "POST",
		url: "/edit/data",
		data: $("form#data").serialize(),
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
}

