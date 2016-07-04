var searchCaption = $("#search_title_caption");
var searchIcon = $("#search_title_icon");
var searchContent = $("#searchContent")
var searchContainer = $("#searchContainer")

function modiSearch(){
    alert("hi");
    searCaption.hidden();
    searchContent.hidden();
    searchContainer.width(24);

}
$(document).ready(new function(){
    searchIcon.click(modiSearch);
});