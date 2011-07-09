function getAvailableHeight(element) {
	var avail = element.parent().height();
	var used = 0;
	element.siblings().each(function () {
		used += $(this).height();
	});
	return avail - used;
}

function getAvailableWidth(element) {
	var avail = element.parent().width();
	var used = 0;
	element.siblings().each(function () {
		used += $(this).width();
	});
	return avail - used;
}

function windowResize() {
	var w = $(window);
	var mc = $('#main-container');
	mc.width(w.width());
	mc.height(w.height());
	var mb = $('#main-bar');
	mb.height(getAvailableHeight(mb));
	var cc = $('#controls-container');
	cc.width(getAvailableWidth(cc));
	var cbc = $('#chatbox-container');
	var pc = $('#playlist-container');
	pc.width(getAvailableWidth(pc));
	if (pc.width() < 500) {
		cbc.css('width', '50%');
		pc.width(getAvailableWidth(pc));
	}
	else {
		cbc.css('width', '500px');
	}
}

function buttonSetup() {
	$('button').button();
	$('#play').button({
		text: false,
		icons: {
			primary: 'ui-icon-play'
		}
	});
	$('#next').button({
		text: false,
		icons: {
			primary: 'ui-icon-seek-end'
		}
	});
	$('#previous').button({
		text: false,
		icons: {
			primary: 'ui-icon-seek-first'
		}
	});
	$('#sync').button({
		text: false,
		icons: {
			primary: 'ui-icon-link'
		}
	});
}

function constructPlaylistEntry(title, artist, album, votes) {
	return TR({'class': 'playlist-entry'},
		TD({'class': 'playlist-entry-title'}, title),
		TD({'class': 'playlist-entry-artist'}, artist),
		TD({'class': 'playlist-entry-album'}, album),
		TD({'class': 'playlist-entry-votes'}, votes),
		TD({'class': 'playlist-entry-upvote'}, 
			BUTTON({'class': 'upvote-button'}, 'upvote').button({text: false, icons: {primary: 'ui-icon-plusthick'}})
		),
		TD({'class': 'playlist-entry-downvote'},
			BUTTON({'class': 'downvote-button'}, 'downvote').button({text: false, icons: {primary: 'ui-icon-minusthick'}})
		)
	);
}

function constructChatMessage(user, timestamp, message) {
	
}

function uploaderSetup() {
	$('#fileupload').fileupload({
		fileInput: $('#upload-field')
	});
}

function playerCanPlay() {
	player.play();
}

function playerSetup() {
	player = document.createElement('audio');
	$(player).bind('canplay', playerCanPlay);
}

function documentReady() {
	windowResize();
	$(window).resize(windowResize);
	uploaderSetup();
	buttonSetup();
	playerSetup();
	$('#playlist-main').append(constructPlaylistEntry('TestSong', 'TestArtist', 'TestAlbum', '10'));
	$('#playlist-main').append(constructPlaylistEntry('TestSong', 'TestArtist', 'TestAlbum', '10'));
}

$(document).ready(documentReady);
