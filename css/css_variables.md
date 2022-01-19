# CSS Variables

> 자주 사용하는 값은 변수에 저장해놓고 사용하자.

---

## 기본적인 문법

```css
div {
  --default-font-color: red;
}

p {
  color: var(--default-font-color);
}
```

`div`에서 변수를 선언하고, `p`에서 변수를 사용한다. 이때, 변수의 범위는 변수를 선언한 그 자신과 하위 요소에 한정된다.

```html
<div>
  <p>첫 번째 단락</p>
</div>
<p>두 번째 단락</p>
```

즉 이러한 문서가 있을 때, *첫 번째 단락*은 변수가 적용되어 **빨간색**으로 나오지만, *두 번째 단락*은 변수가 적용되지 않아 **기본 색상**으로 표시된다.

```css
p {
  color: var(--default-font-color, blue);
}
```

변수가 적용되지 않을 것을 대비해 대체 값을 지정할 수도 있다.

## 사용법

```css
:root {
  --default-font-color: red;
}
```

CSS에서는 `:root`에 변수를 선언해놓고 전역적으로 사용하는 것이 일반적이다.

### HTML

```html
<div>
  <p>첫 번째 단락</p>
</div>
<p>두 번째 단락</p>
```

### CSS

```css
:root {
  --default-font-color: red;
}

div {
  --default-font-color: blue;
}

p {
  color: var(--default-font-color);
}
```

하위 선택자에서 같은 이름의 변수를 다시 선언한다면 하위 선택자의 변수가 우선되어 *첫 번째 단락*은 **파란색**, *두 번째 단락*은 **빨간색**으로 표시된다.

# 참조

- [사용자 지정 CSS 속성 사용하기 (변수)](https://developer.mozilla.org/ko/docs/Web/CSS/Using_CSS_custom_properties)
