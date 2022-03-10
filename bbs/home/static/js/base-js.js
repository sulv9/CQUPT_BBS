(function () {
	var target = document.getElementById("left-sidebar-id")
	var t_height = target.clientHeight
	window.onscroll = function () {
		var overHeight = document.body.scrollTop || document.documentElement.scrollTop
		overHeight > t_height ? target.className = "left-sidebar-id" : target.className = "left-sidebar"
	};
})();
console.log('hello')