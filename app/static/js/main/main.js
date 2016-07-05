var tips =$("#tips");
var searchIcon=$("#search_title_icon");
var searchContainer = $("#searchContainer");

function modiSearch(){
    searchContainer.hide();
    tips.show();
}
function showSearch(){
    searchContainer.show();
    tips.hide();
}
$(document).ready(new function(){
    searchIcon.click(modiSearch);
    tips.click(showSearch);
});