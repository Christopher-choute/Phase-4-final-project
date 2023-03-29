import React, {useState,useEffect} from "react";
import BuyCars from './BuyCars';
import './GetData.css'
import SellCars from './SellCars';
import Header from './Header';
import Nav from './Nav';
import Home from './Home'
import Car from './Car';

import {Route, Switch, useParams} from "react-router-dom"


//////HOME COMPONENT///////
//do our requests in here//

function GetData(){
    const { id } = useParams();
    const [search, setSearch] = useState('')
    const [carData, setCarData] = useState([]);
    const [cars, setCars] = useState([])
    
    
    const filteredCars = carData.filter(car => car.model.toLowerCase().includes(search.toLowerCase()) || car.make.toLowerCase().includes(search.toLowerCase()) ||car.year.toString().includes(search))

    
    useEffect(() => {
        fetch("http://127.0.0.1:5555/cars")
        .then(res => res.json())
        .then((data) => setCarData(data))
      },[]);
    
      function handleNewCar(newCar) {
        setCars([...carData, newCar]);
    }
    
      

    return (
        <div>
            <Switch>
                <Route exact path="/cars">
                    <Header />
                    <Nav />
                    <div className="search-container">
                        <input className="search-input" type="text" placeholder="Search for Make, Model or Year"  value={search} onChange= {(e) => setSearch(e.target.value)}  />
                    </div>
                    <BuyCars cars = {filteredCars} />
                </Route>

                <Route path="/cars/:id">
                    <Header />
                    <Nav />
                    <Car />
                </Route>

                <Route exact path="/SellCars">
                    <Header />
                    <Nav />
                    <SellCars handleNewCar={handleNewCar}/>
                </Route>
            </Switch>
    </div>
    )
}

export default GetData;