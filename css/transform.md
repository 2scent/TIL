# transform

> 요소에 행렬 변형, 원근, 회전, 크기 조절, 기울이기, 이동 등의 효과를 부여할 수 있다.

## transform function

- 행렬 변형: matrix(), matrix3d()
- 원근: perspective()
- 회전: rotate(), rotate3d(), rotateX(), rotateY(), rotateZ()
- 크기 조절: scale(), scale3d(), scaleX(), scaleY(), scaleZ()
- 기울이기: skew(), skewX(), skewY()
- 이동: translate(), translate3d(), traslateX(), traslateY(), translateZ()

## 사용법 예시

```css
.box {
  /* 요소의 크기를 1.5배로 늘리고,  수평 축으로 -50%, 수직 축으로 50% 이동한다.*/
  transform: scale(1.5) translate(-50%, 50%);
}
```

## Tip

- [CSS Triggers](https://csstriggers.com/)를 확인해보면, 가장 많이 사용하는 레이아웃 엔진인 _Blink_ 엔진과 _Gecko_ 엔진에서 `transform` 속성을 수정했을 경우, _Composite_ 만 다시 수행하는 것을 확인할 수 있다. 특정 요소의 위치를 자주 변환시키는 작업을 할 때, 성능 이슈가 있다면 `transform` 속성을 활용할 수 있다.

## 참조

- [transform](https://developer.mozilla.org/ko/docs/Web/CSS/transform)
- [\<transform-function\>](https://developer.mozilla.org/ko/docs/Web/CSS/transform-function)
