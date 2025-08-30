# React JS

Content from : LinkedIn

This was created by Facebook(now Meta).

ReactJS has a developer tool, which allows easy debugging and development.


Creating a project :

```bash
npx create-react-app react_project_name

```
Here ```npx``` is a package runner.

```npm start``` for starting the app.

React uses a syntax format called JSX, which is XML embeddings in JS.  
It is able to do so through a tool called **Babel**.

## Important

1. React.render
2. React.StrictMode
3. React.creatElement(elementTag, cssProps, innerHtml)

## Creating a component

Make a function that returns JSX.

You can pass props to a function, which can contain the data it needs to hold it.

```js
function Comp(props){
    console.log(props.yourKey);
}
```

It is better to have a list of elements as objects instead of strings or any other primitive : 

```jsx
const dishes = ["some1", "some2"];// throws error while rendering

const dishObjs = dishes.map((dish, i) => {id : i, dish : dish}); // do this
```

React.Fragment helps us to add a wrapper.

```jsx
<React.Fragement>
</React.Fragement>

# or

<>
</>

# in essence

ReactDOM.render(
    <>
        <App />
        <SomeOtherApp />
    </>
,
document.getElementById('root')
);
```

This is useful as wrapping the content in ```<div>``` adds extra nesting.

Important stuff : 

1. Conditional rendering
2. Array destructuring
3. useState Hook
4. useEffect
5. useReducer