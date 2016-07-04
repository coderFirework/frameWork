var searchCaption = $("#search_title_caption");
var searchIcon = $("#search_title_icon");
var searchContent = $("#searchContent");
var searchContainer = $("#searchContainer");

function modiSearch(){
    alert(searchCaption);
    searchCaption.hide();
    searchContent.hide();
    searchContainer.width(24);

}
$(document).ready(new function(){
    searchIcon.click(modiSearch);
});