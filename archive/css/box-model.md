# Box Model

![Box Model](images/box-model.png)

문서의 레이아웃을 계산할 때, 하나의 박스는 위 사진과 같이 네 부분으로 이루어진다.

- 컨텐츠 영역(Content Area)
- 패딩 영역(Padding Area)
- 테두리 영역(Border Area)
- 마진 영역(Margin Area)

CSS에서 `box-sizing` 속성이 기본값인 `content-box`일 때, `width`, `height` 같은 속성으로 크기를 지정하면 `padding`, `border`, `margin`을 제외한 컨텐츠 영역의 크기만을 지정하는 것이다.

`box-sizing` 속성이 `border-box`일 때, `width`, `height` 같은 속성으로 크기를 지정하면 `padding`, `border`를 포함하고, `margin`은 제외하는 테두리 영역의 크기를 지정하는 것이다. 사이즈 계산의 편의성 때문에 일반적으로 `border-box`를 많이 사용한다.

## 참조

- [CSS 기본 박스 모델 입문](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)
- [box-sizing](https://developer.mozilla.org/ko/docs/Web/CSS/box-sizing)
