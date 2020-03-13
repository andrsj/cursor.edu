var input = document.getElementByClassName("input")[0],
	output = document.getElementByClassName("output")[0],
	lol = {
		name: 'lol',
		price: 100 ,
		src: "lol.png"
	};

input.addEventListener('keyup', function(){
	// output.innerHTML = this.value;
	output.innerHTML = this.value.replace(
		// /\{\{\w*\}\}/g, "string" //replace all {{}} on string
		// /\{\{(\w*)\}\}/g , '$1'  //content in group will be 1$

		// /\{\{(\w*)\}\}/g , function(match){
		// 	return match //return first match in function
		// }
		
		// /\{\{(\w*)\}\}/g , function(match,value){
		// 	return value //return first match value
		// }

		/\{\{(\w*)\}\}/g , function(match, value){
			return lol[value]; //return element with match's key
		}
	);
}, false);





