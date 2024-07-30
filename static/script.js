// CONTINUUM UI

$(function() {
	function LockScreenCheckPass() {
		let password = $(".systemLockInput").val();
		$(".lockScreenLogIn").addClass("wait");
		$(".systemLockInput").blur();
		if (password === "123") {
			setTimeout(function() {
				$(".lockScreen").removeClass("locked");
				$(".lockScreenLogIn").removeClass("wait");
			}, 200);
		} else {
			setTimeout(function() {
				$(".lockScreenLogIn")
					.addClass("wrong")
					.removeClass("wait");
				$(".systemLockInput").focus();
			}, 2000);
		}
	}

	$(".systemLockInput").keyup(function(e) {
		if (e.keyCode === 13 || e.which == 13) {
			LockScreenCheckPass();
		} else {
			$(".lockScreenLogIn").removeClass("wrong");
			if (!($(".systemLockInput").val() == "")) {
				$(".login").removeClass("empty");
			} else {
				$(".login").addClass("empty");
			}
		}
	});
});









