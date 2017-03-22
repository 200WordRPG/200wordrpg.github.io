
(function() {
	function isLink(link) {
		var parser = document.createElement('a');
		parser.href = link;

		if(/^https?/.test(parser.protocol)) {
			return true;
		}

		return false;
	}

	function makeLink(element, link, linkText) {
		var anchor = document.createElement('a');
		anchor.href = link;
		anchor.innerHTML = linkText;
		element.innerHTML = '';
		element.appendChild(anchor);
	}
	
	
	var linkElement = document.getElementById('entry-link');
	var linkText = linkElement.innerHTML;

	if(/no link/i.test(linkText)) {
		return;
	}

	if(/^https?/.test(linkText)) {
		makeLink(linkElement, linkText, linkText);
		return;
	}

	var possibleLink = "http://" + linkText;

	if(isLink(possibleLink)) {
		makeLink(linkElement, possibleLink, linkText);
		return;
	}

})();