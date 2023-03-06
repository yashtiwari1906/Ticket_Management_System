

export const addItemToCart =(item, next) =>{
    let cart  = []
    if(typeof window !=undefined){
        if(localStorage.getItem("cart")){
            cart=JSON.parse(localStorage.getItem("cart"))
        }
        localStorage.setItem("cart",JSON.stringify([]));
        cart = [item];
        localStorage.setItem("cart",JSON.stringify(cart));
        
    }
};

export const addTicket =(row, col) =>{
    let Row = 0; 
    let Col = 0;
   
    if(typeof window !=undefined){
        if(localStorage.getItem("Row")){
          Row=JSON.parse(localStorage.getItem("Row"))
          Col=JSON.parse(localStorage.getItem("Col"))
        }
        localStorage.setItem("Row",JSON.stringify(0));
        Row = row;
        localStorage.setItem("Row",JSON.stringify(row));
        localStorage.setItem("Col",JSON.stringify(0));
        Col = col;
        localStorage.setItem("Col",JSON.stringify(col));
        
    }
};

export const loadCart =() =>{
    if(typeof window!=undefined){
        if(localStorage.getItem("cart")){
            return JSON.parse(localStorage.getItem("cart"))
        }
    }

}

export const removeItemFromCart = refTicket =>{
    let cart=[]
    if(typeof window != undefined){
        if(localStorage.getItem("cart")){
            cart = JSON.parse(localStorage.getItem("cart"));
        }
       
        localStorage.setItem("cart",JSON.stringify([]));
    }
    return cart;

};