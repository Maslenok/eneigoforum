  function addtocart(id){
    a_addtocart(id, addtocart_cb);
  }
  function addtocart_cb(data){
    document.getElementById("divaddtocart").innerHTML = data;
	a_get_cart(getcart_cb);
  }
  function getcart_cb(data){
  	document.getElementById("cart").innerHTML = data;
  }
