import React from 'react';
import ReactDOM from 'react-dom';
import Index from './pages/index';
import * as serviceWorker from './serviceWorker';

import 'normalize.css/normalize.css'
import './index.css'

ReactDOM.render(<Index />, document.getElementById('root'));

serviceWorker.unregister();