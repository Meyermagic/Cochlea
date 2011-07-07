<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />

		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

		<title>Group Listen</title>

		<script type='text/javascript' src='js/jquery-1.6.1.min.js'></script>
		
		<link type='text/css' rel="stylesheet" href="css/style.css" />
		<script type='text/javascript' src='js/main.js'></script>
	</head>

	<body>
		<div id='main-container'>
			<div id='now-playing-bar'>
				<div id='song-info-container'>

				</div>

				<div id='controls-container'>
					<div id='buttonsbar-container'>
						<button id='previous'>previous</button>
						<button id='play'>play/pause</button>
						<button id='next'>next</button>
					</div>

					<div id='seekbar-container'>

					</div>
				</div>
			</div>

			<div id='listeners-bar'>
<?php
echo $_GET['room'];
?>
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
