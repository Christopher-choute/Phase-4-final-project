import React from 'react'
import {useState,useEffect} from "react";
import {Route, Switch, useParams} from "react-router-dom"
import './Car.css'

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
        <div className = 'cont'>
            <img src = {image} className = 'carImg'/>
            <h1>Make: {make}</h1>
            <h1>Model: {model}</h1>
            <h2 className ='h2' > Year: {year}</h2>
            <h2 className ='h2'>Price: ${price}</h2>
            <h2 className ='h2'>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</h2>
            <button className = 'btn' >BUY</button>
        </div>
    )
}

export default Car;
