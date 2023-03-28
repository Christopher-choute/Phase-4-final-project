import React from "react";
import GetData from './GetData';
import Header from './Header';
import Nav from './Nav';
import SellCars from './SellCars';
import Home from './Home'


import {Route, Switch} from "react-router-dom"

////////App Component///////
function App() {
  return (
    <div className="App">
      <Switch>

        <Route exact path="/">
          <Header />
          <Nav />
          <Home />
        </Route>

        <Route exact path="/Cars">
          <Header />
          <Nav />
          <GetData />
        </Route>

        <Route exact path="/SellCars">
          <Header />
          <Nav />
          <SellCars />
        </Route>


      </Switch>  
    </div>
  );
}

export default App;
