

import {API}  from "../../backend";

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