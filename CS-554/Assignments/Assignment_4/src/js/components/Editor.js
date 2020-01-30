import React from 'react';
import Form from 'react-bootstrap/Form';

class Editor extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: ""
        };

        this.updateText = this.updateText.bind(this)
        this.change = this.change.bind(this)
    };

    updateText(text) {
        this.setState({ text });
        console.log(event.target.value)
    };

    change(event) {
        let text = event.target.value;
        this.updateText(text)

        this.props.updateParentState(text)
    }


    render() {
        let { text } = this.state.text;
        return (
            <Form.Group>
                <Form.Control
                    className="editor"
                    as="textarea"
                    rows="3"
                    placeholder="Enter some markdown..."
                    value={text}
                    onChange={this.change}>
                </Form.Control>
            </Form.Group>

            // <form id="editor">
            //     <form>
            //         <div class="form-group">
            //             <textarea
            //                 type="text"
            //                 class="editor"
            //                 placeholder="Enter some markdown..."
            //                 onChange={this.change}
            //                 value={text}>

            //             </textarea>
            //         </div>
            //     </form>
            // </form>
        );
    }
}

export default Editor;
