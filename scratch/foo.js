function foo() {
    var link = $('a:eq(3)');
    // return link.html();
    var link = $('a:eq(3)');
    if (link){
        link.click();
    }
    else{
        return "no link";
    }
};