import 'babel-polyfill'
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { Router, hashHistory } from 'react-router'
import { syncHistoryWithStore } from 'react-router-redux'
import configureStore from './store/configureStore'
import routes from './routes'

import './style/index.scss'

const store = configureStore()
const history = syncHistoryWithStore(hashHistory, store)

ReactDOM.render(
  <Provider store={store}>
    <Router history={history} routes={routes}>
    </Router>
  </Provider>
  ,
  document.getElementById('content')
)
