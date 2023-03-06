import { API } from "../../backend";




export const signup = user =>{
    const formData = new FormData() 
    
    for (const name in user){
        formData.append(name, user[name])
    }
    return fetch(`${API}booking/book/`, {
        method: "POST", 
        body: formData
    })
    .then(response=> {
        return response.json();
    })
    .catch(err => console.log(err));
}

export const Tickets = user =>{
    const formData = new FormData() 
    
    for (const name in user){
        formData.append(name, user[name])
    }
    return fetch(`${API}booking/tickets/`, {
        method: "POST", 
        body: formData
    })
    .then(response=> {
        return response.json();
    })
    .catch(err => console.log(err));
}

export const userDetailsFetch = user =>{
    const formData = new FormData() 
    
    for (const name in user){
        formData.append(name, user[name])
    }
    return fetch(`${API}booking/userdetails/`, {
        method: "POST", 
        body: formData
    })
    .then(response=> {

        return response.json();
    })
    .catch(err => console.log(err));
}