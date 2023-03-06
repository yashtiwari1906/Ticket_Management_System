import React from "react";

const ImageHelper = ({ event }) => {
  
  const imageurl = event
    ? event.image
    : ""
   

  return (
    <div className="rounded border border-success p-2">
      <img class = "card-img-top"
        src={imageurl}
        style={{ maxHeight: "100%", maxWidth: "100%" }}
        className="mb-3 rounded"
        alt=""
        />
    </div>
  );
};

export default ImageHelper;