# 마크업 작성


```js

React.createElement('h1', {className: 'question'}, 'Question');

//결과
<h1 className='question'>Question</h1>

```

``` js
var Divider = React.createClass({
  render: function () {
    return (
      <div className="divider">
        <h2>{this.props.children}</h2><hr />
      </div>
    );
  }
});

//사용
<Divider>Question</Divider>
```

