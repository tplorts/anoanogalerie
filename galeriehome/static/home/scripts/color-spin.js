
var huerotation = 0;
colorSpinStep = function() {
	spinee = $(".color-spin");
	spinee.css("-webkit-filter", "hue-rotate(" + huerotation + "deg)");
	huerotation = (huerotation + 3) % 360;
};

window.setInterval(colorSpinStep, 250);

var blurIntervalId;
var bluree = $(".blur-in");
var blur = 10;
halveBlur = function() {
	bluree.css("-webkit-filter", "blur(" + blur + "px)");
	if( blur == 0 ) {
		clearInterval(blurIntervalId);
	}
	blur = blur / 1.1;
	if( blur < 0.03 ) {
		blur = 0;
	}
};
blurIntervalId = setInterval(halveBlur, 50);
