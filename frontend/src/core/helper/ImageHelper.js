import React from "react";

const ImageHelper = ({ event }) => {
  console.log("this function has been called")
  const imageurl = event
    ? event.image
    : ""
    console.log("----------------------")
    console.log(event.image)
    console.log("----------------------")

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