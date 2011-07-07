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

function documentReady() {
	windowResize();
	$(window).resize(windowResize);
}

$(document).ready(documentReady);
