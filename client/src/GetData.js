import React, {useState,useEffect} from "react";
import { useHistory } from 'react-router-dom';
import BuyCars from './BuyCars';
import './GetData.css'
import SellCars from './SellCars';
import Header from './Header';
import Nav from './Nav';
import Home from './Home'
import Car from './Car';
import Edit from './Edit';

import {Route, Switch, useParams} from "react-router-dom"


//////HOME COMPONENT///////
//do our requests in here//

function GetData(){
    const { id } = useParams();
    const [search, setSearch] = useState('')
    const [carData, setCarData] = useState([]);
    const [cars, setCars] = useState([]);
    const [deleted, setDeleted] = useState(false);
    
    const history = useHistory();
    
    const filteredCars = carData.filter(car => car.model.toLowerCase().includes(search.toLowerCase()) || car.make.toLowerCase().includes(search.toLowerCase()) ||car.year.toString().includes(search))

    
    useEffect(() => {
        fetch("/cars")
        .then(res => res.json())
        .then((data) => setCarData(data))
      },[deleted]);
    
      function handleNewCar(newCar) {
        setCars([...carData, newCar]);
    }
    
    function deleteItem(id){
        fetch(`/cars/${id}`, { 
          method: 'DELETE' ,
          headers: { 'Content-Type': 'application/json'},
        })
        .then(() => setDeleted(!deleted))
        .then(() => history.push('/cars'))
      }
            
      function updateCar(updatedCar) {
        const updatedCars = carData.map(ogCar => {
            if (ogCar.id === updatedCar.id)
                return updatedCar
            else
                return ogCar;
        })
        setCarData(updatedCars)
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
                    <BuyCars cars = {filteredCars}  />
                </Route>

                <Route exact path="/cars/:id">
                    <Header />
                    <Nav />
                    <Car  deleteItem={deleteItem} />
                </Route>

                <Route path="/SellCars">
                    <Header />
                    <Nav />
                    <SellCars handleNewCar={handleNewCar}/>
                </Route>
                <Route exact path="/edit/:id">
                    <Header />
                    <Nav />
                    <Edit updateCar={updateCar} />
                </Route>
            </Switch>
    </div>
    )
}

export default GetData;