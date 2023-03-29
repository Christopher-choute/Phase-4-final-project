import React from 'react'
import {useState,useEffect} from "react";
import {Route, Switch, useParams} from "react-router-dom"

function Car(){
    const { id } = useParams();
    const [singleCar, setSingleCar] = useState([]);

    const [make, setMake] = useState("");
    const [model, setModel] = useState("");
    const [year, setYear] = useState("");
    const [price, setPrice] = useState("");
    const [image, setImage] = useState("");
    const [used, setUsed] = useState(false);

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/cars/${id}`)
        .then(res => res.json())
        .then((data) => getCar(data))
      },[]);

      function getCar(car) {
        setMake(car.make);
        setModel(car.model);
        setYear(car.year);
        setPrice(car.price);
        setImage(car.image);
        setUsed(car.used);
      }

    return(
        <div>
            <p>Make: {make}</p>
        </div>
    )
}

export default Car;
