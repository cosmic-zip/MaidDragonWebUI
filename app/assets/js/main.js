function tg_btn() {
	var x = document.getElementById("sidebar");
	if (x.style.display === "none") {
		x.style.display = "block";
	} else {
		x.style.display = "none";
	}
}

function displayValue(span_id, chat_val) {
	var displayContainer = document.getElementById(span_id);
	displayContainer.innerHTML = chat_val;

}

function onload_chat() {
	// Create a new XMLHttpRequest object
	var xhr = new XMLHttpRequest();

	// Configure the AJAX request
	xhr.open('GET', '/history', true);

	// Set up the event listener to handle the response
	xhr.onload = function () {
		if (true) {
			// Request was successful
			var responseData = JSON.parse(xhr.responseText);
			var resultDiv = document.getElementById('chat');

			for (count in responseData["data"]) {
				if (responseData["data"][count][1] == "user") {
					resultDiv.innerHTML += `
					<div class="chat_ctn chat_ctn_user">
						<div class="user chat_card">
							<h3>User</h3>
						`
						+ JSON.stringify(responseData["data"][count][2]) +
						`
						</div>
						<div class="chat_img_ctn">
							<img class="chat_img" alt="" src="assets/img/user.jpg">
						</div>
					</div>
					` // end
				} else if (responseData["data"][count][1] == "maid") {
					resultDiv.innerHTML += `
					<div class="chat_ctn">
						<div class="chat_img_ctn">
							<img class="chat_img" alt="" src="assets/img/maid.jpg">
						</div>
						<div class="maid chat_card">
							<h3>Maid</h3>
					`
						+ JSON.stringify(responseData["data"][count][2]) +
						`
						</div>
					</div>
					` // end
				}

				console.log(responseData["data"]);
				count += 1;
			}

		} else {
			// Request failed
			console.error('Request failed with status ' + xhr.status);
		}
	};

	// Handle network errors
	xhr.onerror = function () {
		console.error('Network error occurred');
	};

	// Send the request
	xhr.send();
}
function sendAjaxRequest() {
	// Get the prompt parameter from the input field
	const promptParameter = document.getElementById('prompt_input').value.trim();

	if (promptParameter !== '') {
		// Create a new XMLHttpRequest object
		const xhr = new XMLHttpRequest();

		// URL to send the POST request to
		const url = `/chat/?prompt=${encodeURIComponent(promptParameter)}`;

		// Set up the request
		xhr.open('POST', url, true);
		xhr.setRequestHeader('Content-Type', 'application/json');

		// Handle the response
		xhr.onload = function () {
			if (xhr.status === 200) {
				// Request was successful
				console.log('Response:', xhr.responseText);
				location.reload();
			} else {
				// Request failed
				console.error('Request failed. Status:', xhr.status);
			}
		};

		// Send the request
		xhr.send();
	} else {
		console.log("Error: Input is empty.");
	}
}
