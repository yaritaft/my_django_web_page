function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function remove_html_element(element_id)
{
    var element = document.getElementById(element_id);
    element.parentNode.removeChild(element);
}

function read_json_page(my_json_page)
{

    var my_page=JSON.parse(my_json_page);
    remove_html_element("spinnerLoading");
    document.body.innerHTML = my_page["html"];
    document.getElementsByTagName("html")[0].style.visibility = "visible";
}

httpGetAsync("http://localhost:5000/home_page",read_json_page);
