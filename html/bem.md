# BEM (Block Element Modifier)

> BEM은 Block, Element, Modifier의 앞글자만 딴 용어로 프론트엔드 개발에서 클래스 명을 정하는 네이밍 컨벤션이다.

---

`Block__Element--Modifier` 형식으로 작성한다.

## Block

- 어딘가에 종속적이지 않고 그 자체로서 의미가 있어야 하며, 일반적으로 Element의 컨테이너 역할을 한다.
- `header`, `container`, `menu` 같이 무언가를 담을 수 있는 것뿐만 아니라 `button`, `checkbox`, `input` 같이 무언가를 담지 않더라도 그 자체로서 의미를 가진다면 Block이 될 수 있다.

## Element

- Block을 구성하는 요소다. Block에 의존적이며, 자신이 속한 Block 내에서만 의미를 가진다.
- `header title`, `menu item`, `checkbox caption` 등이 있다.

## Modifier

- Block 또는 Element의 속성을 나타낸다.
- `disabled`, `checked`, `big`, `red` 등이 있다.

![bem](images/bem.jpg)

## 예제

위 이미지에 표시된 요소들을 BEM 방식으로 html을 작성한다면 아래와 같이 쓸 수 있다. 클래스 명이 중요하다!

```html
<img class="logo" />

<input class="input" />

<ul class="menu">
  <li class="menu__item">...</li>
  <li class="menu__item">...</li>
  <li class="menu__item">...</li>
  <li class="menu__item">...</li>
</ul>

<button class="button">...</button>

<input class="input--big" />

<button class="button--green">...</button>
```

## 참조

- [Get BEM](http://getbem.com/)
