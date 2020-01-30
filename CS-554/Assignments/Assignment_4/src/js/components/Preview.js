import React from 'react';
const marked = require("marked");

class Preview extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div dangerouslySetInnerHTML={{ __html: marked(this.props.markdown) }}>
            </div>
        );
    }
}

export default Preview;
