function foo() {
    var link = $('a:first()');
    // var link = $('a:eq(3)');
    if (link){
	link.click();
    }
    else{
	return "no link";
    }
}