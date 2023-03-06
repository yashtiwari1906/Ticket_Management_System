

import {API}  from "../../backend";
console.log("===============")
console.log(fetch(`${API}event/`, {
  mode:'cors',
  method: "GET"
})
.then((response) => {
  
  return response.json();
}))
console.log("===============")
export const getEvents = () => {
  
    return fetch(`${API}event/`, { method: "GET" })
    .then((response) => {
      
      return response.json();
    })
    .catch((err) => console.log(err));
};



export const getSeats = () => {
  
    return fetch(`${API}booking/`, { method: "GET" })
    .then((response) => {
      
      return response.json();
    })
    .catch((err) => console.log(err));
};