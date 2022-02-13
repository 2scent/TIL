# Centring

> flexbox를 사용하지 않고 중앙 정렬하는 방법

## text-align

```html
<div class="container">
  <span>Item</span>
</div>
```

```css
.container {
  text-align: center;
}
```

부모 요소의 `text-align` 속성에 `center`를 지정해주면 된다. _인라인 요소_ 에만 적용할 수 있다.

## margin

```html
<div class="container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
  <div class="item">Item 3</div>
</div>
```

```css
.item {
  margin: 0 auto;
  /* 예제를 위한 속성들 */
  text-align: center;
  width: 400px;
}
```

블록 요소는 기본적으로 남은 공간을 `margin`으로 채우기 때문에 예제와 같은 방법으로 `margin-left`와 `margin-right` 속성에 `auto`를 지정해주면 된다.

## translate

```html
<div class="container">
  <div class="item"></div>
</div>
```

```css
.container {
  position: relative;

  /* 디자인 요소 */
  width: 1000px;
  height: 1000px;
  background-color: red;
}

.item {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  /* 디자인 요소 */
  width: 200px;
  height: 200px;
  background-color: blue;
}
```

부모 요소의 `position`에 `relative`를 주고, 자식 요소의 `position`에 `absolute`를 주고, 자식 요소의 `top`와 `left`를 각각 `50%`로 지정하면 _자식 요소의 왼쪽 상단 모서리_ 가 _부모 요소의 정중앙_ 에 위치하게 된다.

이때 자식 요소의 `transform`에 `translate(-50%, -50%)`를 주면 자식 요소의 너비와 높이의 절반만큼 왼쪽 상단 방향으로 이동하기 때문에 결과적으로 자식 요소 정중앙과 부모 요소의 정중앙이 일치하게 되면서 중앙 정렬이 된다.
