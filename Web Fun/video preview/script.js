console.log("page loaded...");

var video = document.getElementById("myVideo");
video.onmouseover = function () {
  video.play();
};
video.onmouseout = function () {
  video.pause();
  video.currentTime = 0; 
};