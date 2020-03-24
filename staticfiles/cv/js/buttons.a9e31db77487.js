function read_pages(my_json_page)
{
    var my_page=JSON.parse(my_json_page);
    document.body.innerHTML = my_page["html"];
}

httpGetAsync("http://localhost:5000/about_me",read_pages);
