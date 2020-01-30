import React from 'react';
import Editor from './Editor.js';
import Preview from './Preview';
const marked = require("marked");

class App extends React.Component {
    constructor(props) {
        super(props);
        this.downloadMarkdown = this.downloadMarkdown.bind(this);
        this.downloadHTML = this.downloadHTML.bind(this);
        this.change = this.change.bind(this);
        this.udpate = this.update.bind(this);

        this.state = {
            text: "",
            filename: ""
        }
    }

    update(filename) {
        this.setState({ filename });
    }

    change(event) {
        let newfilename = event.target.value;
        this.update(newfilename);

        this.props.update_filename(newfilename);
    }

    downloadMarkdown() {
        const elem = document.createElement("a");
        const file = new Blob([this.state.text], {
            type: 'text/plain'
        });
        elem.href = URL.createObjectURL(file);
        if (this.state.filename == "") {
            elem.download = "markdownme.md"
        } else {
            elem.download = this.state.filename + ".md"
        }
        document.body.appendChild(elem);
        elem.click();
        window.URL.revokeObjectURL(url)
    }

    downloadHTML() {

        const header = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta http-equiv="X-UA-Compatible" content="ie=edge">\n<meta http-equiv="X-UA-Compatible" content="ie=edge">\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">\n<title>Markdown Writer</title>\n<style>\nfont-family:Arial,sans-serif;\ncode{color: red;}\nbody{margin: 10vh;}\n</style>\n</head>\n<body>\n';
        const body = marked(this.state.text);
        const footer = "</body>\n</html>";
        const html = header + body + footer;

        const elem = document.createElement("a");

        const file = new Blob([html], {
            type: "text/plain"
        });

        elem.href = URL.createObjectURL(file);
        if (this.state.filename == "") {
            elem.download = "markdownme.html"
        } else {
            elem.download = this.state.filename + ".html"
        } document.body.appendChild(elem);
        elem.click();
        window.URL.revokeObjectURL(url)
    }

    updateParentState(markdown) {
        this.setState({
            text: markdown
        });
    }

    render() {
        return (
            <div>
                <div class="row" >
                    <div class="col-6" >
                        <Editor updateParentState={
                            this.updateParentState.bind(this)
                        } />
                    </div>
                    <div class="col-6" >
                        <div class="card" >
                            <div class="card-body">
                                <Preview markdown={this.state.text} />
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-6">
                        <button class="btn btn-dark btn-block" data-toggle="modal" data-target="#markdown" > Download Markdown </button>
                    </div>
                    <div class="col-6">
                        <button class="btn btn-dark btn-block" data-toggle="modal" data-target="#html" > Download HTML </button>
                    </div>
                </div>
                <div class="modal fade" id="markdown" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Download the Markdown</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                <form>
                                    <label for="filename">Enter Filename</label>
                                    <input type="text" class="form-control" id="filname" placeholder="markdownme" onChange={this.change}></input>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" onClick={this.downloadMarkdown}>Save file</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal fade" id="html" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Download the HTML</h5>
                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div class="modal-body">
                                <form>
                                    <label for="filename">Enter Filename</label>
                                    <input type="text" class="form-control" id="filname" placeholder="markdownme" onChange={this.change}></input>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" onClick={this.downloadHTML}>Save file</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;