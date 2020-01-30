import React from 'react';
import ReactDOM from 'react-dom';
import './css/custom.css';
import App from "./js/components/App.js";

ReactDOM.render(< App />, document.getElementById("app"));

if (module.hot) {
    module.hot.accept();
}