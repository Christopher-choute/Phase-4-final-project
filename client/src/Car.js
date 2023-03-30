import React from 'react'
import {useState,useEffect} from "react";
import {Route, Switch, useParams} from "react-router-dom"
import './Car.css'

function Car({deleteItem}){
    const { id } = useParams();
    const [singleCar, setSingleCar] = useState([]);

    const [make, setMake] = useState("");
    const [model, setModel] = useState("");
    const [year, setYear] = useState("");
    const [price, setPrice] = useState("");
    const [image, setImage] = useState("");
    const [dealer, setDealer] =useState ("");
    const [used, setUsed] = useState(false);

    useEffect(() => {
        fetch(`/cars/${id}`)
        .then(res => res.json())
        .then((data) => getCar(data))
      },[]);

    // useEffect(() => {
    //   fetch(`http://127.0.0.1:5555/dealership_cars/${id}`)
    //   .then(res => res.json())
    //   .then((data) => getCar(data))
    // },[]);
      
        // useEffect(() => {
        //   fetch('http://127.0.0.1:5555/cars/${id}', 
        //   { method: 'DELETE' })
        //         .then(() => setStatus('Delete successful'));
        
        // }, []);
    
     console.log(id)


      function getCar(car) {
        setMake(car.make);
        setModel(car.model);
        setYear(car.year);
        setPrice(car.price);
        setImage(car.image);
        setUsed(car.used);
      }
      const linkStyle = {
        textDecoration: "none"
    }

    return(
        <div className = 'cont'>
            <img src = {image} className = 'carImg'/>
            <h1>Make: {make}</h1>
            <h1>Model: {model}</h1>
            <h2 className ='h2' > Year: {year}</h2>
            <h2 className ='h2'>Price: ${price}</h2>
            <h2 className ='h2'>Condition: {used ? 'This Car is Used' : "This Car is Brand New"}</h2>
            <button onClick = {() => deleteItem(id)}   className = 'btn' >BUY (QTY: 1)</button>
        </div>
      )

    }
export default Car;
