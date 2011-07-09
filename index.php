<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />

		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

		<title>Cochlea - 
<?php
	echo $_GET['room'];
?>
		</title>
		
		<script type='text/javascript' src='js/jquery-1.6.1.min.js'></script>
		
		<link type="text/css" href="css/jquery-ui-1.8.14.custom.css" rel="stylesheet" />
		<script type="text/javascript" src="js/jquery-ui-1.8.14.custom.min.js"></script>
		
		<script type='text/javascript' src='js/jquery.iframe-transport.js'></script>
		<script type='text/javascript' src='js/jquery.fileupload.js'></script>
		
		<script type='text/javascript' src='js/domination.js'></script>
		
		<link type='text/css' rel="stylesheet" href="css/style.css" />
		<script type='text/javascript' src='js/main.js'></script>
	</head>

	<body>
		<form id='fileupload' action='server/upload.php' method='POST' enctype='multipart/form-data'>
			<label class='fileinput-button'>
				<span>Upload Music...</span>
				<input id='upload-field' type='file' name='files[]' multiple />
			</label>
		</form>
		<div id='main-container'>
			<div id='now-playing-bar'>
				<div id='song-info-container'>

				</div>

				<div id='controls-container'>
					<div id='buttonsbar-container'>
						<button id='sync'>Sync</button>
						<button id='previous'>Previous</button>
						<button id='play'>Play</button>
						<button id='next'>Next</button>
					</div>

					<div id='seekbar-container'>
						<div id='seekbar'></div>
					</div>
				</div>
			</div>

			<div id='listeners-bar'>
				
			</div>

			<div id='main-bar'>
				<div id='chatbox-container'>
					<div id='chatbox-log-container'>
						
					</div>

					<div id='chatbox-entry-container'>
						
					</div>
				</div>

				<div id='playlist-container'>
					<table id='playlist-main'>
						<tr id='playlist-header'>
							<th id='song-title-header'>Title</th>
							<th id='song-artist-header'>Artist</th>
							<th id='song-album-header'>Album</th>
							<th id='song-votes-header' colspan='3'>Votes</th>
						</tr>
					</table>
					<table id='playlist-uploading'>
						
					</table>
				</div>
			</div>
		</div>
	</body>
</html>
