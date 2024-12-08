# py-hangul-utils

> [JS로 된 프로젝트](https://github.com/hyukson/hangul-util)를 파이썬으로 변환한 라이브러리입니다.

한글의 자모음의 분리,결합,검색 및 날짜와 숫자를 한글로 변환하는 등의 한글 기능 라이브러리입니다.

## 설치

```bash
pip install py-hangul-utils
```

## Functions

- [한글 분리](https://github.com/Mineru98/py-hangul-utils#%ED%95%9C%EA%B8%80-%EB%B6%84%EB%A6%AC) [ divide ]
- [한글 결합](https://github.com/Mineru98/py-hangul-utils#%ED%95%9C%EA%B8%80-%EA%B2%B0%ED%95%A9) [ combine ]
- [초성 검색](https://github.com/Mineru98/py-hangul-utils#%EC%B4%88%EC%84%B1%EA%B2%80%EC%83%89) [ includes_by_cho ]
- [비슷한 단어 찾기](https://github.com/Mineru98/py-hangul-utils#%EB%B9%84%EC%8A%B7%ED%95%9C-%EB%8B%A8%EC%96%B4-%EC%B0%BE%EA%B8%B0) [ distance ]
- [문자 정렬](https://github.com/Mineru98/py-hangul-utils#%EB%AC%B8%EC%9E%90-%EC%A0%95%EB%A0%AC) [ sort_hangul ]
- [한영 변환](https://github.com/Mineru98/py-hangul-utils#%ED%95%9C%EC%98%81-%EB%B3%80%ED%99%98) [ convert_key ]
- [한글 발음 변환](https://github.com/Mineru98/py-hangul-utils#%ED%95%9C%EA%B8%80-%EB%B0%9C%EC%9D%8C-%ED%8C%8C%EC%8B%B1) [ normalize ]
- [숫자 변환](https://github.com/Mineru98/py-hangul-utils#%EC%88%AB%EC%9E%90%EB%A5%BC-%ED%95%9C%EA%B8%80%EB%A1%9C) [ format_number ]
- [날짜 포맷](https://github.com/Mineru98/py-hangul-utils#%EB%82%A0%EC%A7%9C-%ED%8F%AC%EB%A7%B7) [ format_date ]
- [조사](https://github.com/Mineru98/py-hangul-utils#%EC%A1%B0%EC%82%AC) [ josa ]
- [문자 암호화](https://github.com/Mineru98/py-hangul-utils#%EB%AC%B8%EC%9E%90-%EC%95%94%ED%98%B8%ED%99%94) [ encode, decode ]
- [언어 감지](https://github.com/Mineru98/py-hangul-utils#%EC%96%B8%EC%96%B4-%EA%B5%AC%EB%B3%84) [ get_local ]
- [한글 판별](https://github.com/Mineru98/py-hangul-utils#ishangul-ischo-isjung-isjong) [ is_hangul, is_cho, is_jung, is_jong ] <br/><br/>

## 한글 분리

`divide_hangul(word: str, is_split: bool = True)`

```python
from hangul_utils import divide_hangul

divide_hangul("값싼")
# ['ㄱ', 'ㅏ', 'ㅂ', 'ㅅ', 'ㅆ', 'ㅏ', 'ㄴ']
```

문자를 초성, 중성, 종성으로 분리한 후 배열에 담아 반환해줍니다. <br/><br/>

```python
divide_hangul("값싼", False)
# ['ㄱ', 'ㅏ', 'ㅄ', 'ㅆ', 'ㅏ', 'ㄴ]
```

`isSplit` 타입이 `False`이면 중성, 종성 값이 분리되지 않습니다. <br/><br/>

```python
from hangul_utils import divide_hangul_by_groups

divide_hangul_by_groups("값싼")
# [ ['ㄱ', 'ㅏ', 'ㅂ', 'ㅅ'], ['ㅆ', 'ㅏ', 'ㄴ'] ]

divide_hangul_by_groups("값싼", is_split=False)
# [ ['ㄱ', 'ㅏ', 'ㅄ'], ['ㅆ', 'ㅏ', 'ㄴ'] ]
```

`divide_hangul_by_groups`함수는 한글자별 분리된 글자가 배열에 묶여 반환됩니다. <br/><br/>

```python
from hangul_utils import divide_hangul_by_groups

divide_hangul_by_groups("값싼", result_type="dict")
# [ {cho: 'ㄱ', jung: 'ㅏ', jong: 'ㅂㅅ'}, {cho: 'ㅆ', jung: 'ㅏ', jong: 'ㄴ'} ]
```

`result_type`으로는 `'dict' | 'list' | 'str' | 'index'` 타입이 존재하며, 기본은 `'list'` 타입으로 반환됩니다. <br/><br/>

### 그 외

```python
from hangul_utils import divide_by_jung, divide_by_jong

divide_by_jung("ㅝ")
# ㅜㅓ

divide_by_jong("ㄺ")
# ㄹㄱ
```

중성, 종성을 분리해줍니다. <br/><br/>

## 한글 결합

`combine_hangul(word: Union[str, List[str]])`

```python
from hangul_utils import combine_hangul

combine_hangul("ㅇㅏㄴㄴㅕㅇ")
# 안녕

combine_hangul(["ㄱ", "ㅏ", "ㅂ", "ㅅ", "ㅆ", "ㅏ", "ㄴ"])
# 값싼
```

문자를 한글로 결합하여 반환합니다.

```python
combine_hangul([["ㄱ", "ㅏ", "ㅂ"], "ㅅ", "ㅏ"])
# 갑사
```

2차원 배열로 결합할 그룹을 지정할 수 있습니다.

### 그 외

```python
from hangul_utils import combine_by_jung, combine_by_jong

combine_by_jung("ㅜㅓ")
# ㅝ

combine_by_jong("ㄹㄱ")
# ㄺ
```

중성, 종성을 결합해줍니다. <br/><br/>

## 초성검색

`includes_by_cho(search: str, word: str)`

```python
from hangul_utils import includes_by_cho

includes_by_cho("ㅅㄱ", "사과")
# True

includes_by_cho("ㅅ고", "사과")
# False
```

문자를 초성검색 정규식으로 변환하여 비교한 결과를 반환합니다.

```python
import re
from hangul_utils import make_regex_by_cho

regex = make_regex_by_cho("ㅅㄱ")
# re.compile('([사-싷][가-깋])')

input_string = "사과수박"
re.sub(regex, r"<mark>\g<0></mark>", input_string)
# <mark>사과</mark>수박
```

문자를 초성 정규식으로 변환시켜 반환됩니다. (`초성 정규식`을 사용할 수 있습니다.) <br/><br/>

## 숫자를 한글로

`format_number(format: Optional[Union[int, str]])`

```python
from hangul_utils import format_number, format_number_all

format_number(123456789)
# 1억 2345만 6789

format_number_all(123456789)
# 일억 이천삼백사십오만 육천칠백팔십구
```

숫자를 한글로 변환 시켜 주는 함수입니다. <br/><br/>

## 날짜 포맷

`format_date(date: Union[str, datetime], format_style: str)`

```python
from datetime import datetime
from hangul_utils import format_date

format_date("2024-12-25 12:25:31")
# 2024년12월25일 12시25분31초

format_date(datetime.fromisoformat("2024-12-25 12:25:31"))
# 2024년12월25일 12시25분31초

format_date("2024-12-25", "YYYY년 MM월 DD일")
# 2024년 12월 25일
```

날짜를 주어진 `formatStyle` 형식에 맞춰서 변환시켜줍니다. <br/><br/>

## 비슷한 단어 찾기

`correct_by_distance(word: str, word_list: List[str], is_split: Optional[bool], distance: Optional[int], max_slice: Optional[int])`

```python
from hangul_utils import correct_by_distance

correct_by_distance("사과", ["사자", "호랑이", "사고"])
# [ '사고', '사자' ]
```

레벤슈타인 거리 알고리즘을 이용하여 `단어 근접수치`를 비교해 반환해줍니다. <br/><br/>

### 옵션지정

```python
correct_by_distance("number", ["number", "str", "bool"], distance=4, max_slice=1, is_split=False)
# [ 'number' ]
```

옵션을 지정하여 필터되는 수치를 조절하거나, 한글분해 작업을 해제할 수 있습니다. <br/><br/>

## 문자 정렬

`sort_by_asc(array: List[Any], compare: Union[List[str], str])`

```python
from hangul_utils import sort_by_asc, sort_by_desc

sort_by_asc(["사과", "귤", "바나나"])
# [ "귤", "바나나", "사과" ]

sort_by_desc(["사과", "귤", "바나나"])
# [ "사과", "바나나", "귤" ]
```

[예정] 문자(한글,영어)를 `ASC(오름차순), DESC(내림차순)` 정렬시켜줍니다.

```python
array = [
  { 'name': ['귤'], 'age': 72 },
  { 'name': ['사과'], 'age': 25 },
  { 'name': ['귤'], 'age': 45 },
]

sort_by_asc(array, ["name", "age"])
# [{'name': ['귤'], 'age': 25}, {'name': ['귤'], 'age': 72}, {'name': ['사과'], 'age': 45}]
```

`compare`의 값으로 객체의 값을 특정할 수 있습니다. `(배열 - 다중조건)` <br/><br/>

### 별도의 조건 지정하기

`sort_by_groups(array: List[Any], groups: List[Union[int, str]], order_asc: bool, compare: Optional[str])`

```python
from hangul_utils import sort_by_groups

groups = ["회장", "사장", "부장", "대리", "사원"]

sort_by_groups(["대리", "사원", "사장", "회장", "부장"], groups)
# [ '회장', '사장', '부장', '대리', '사원' ]
```

`특정 배열`을 기준으로 정렬을 시켜줄 수 있습니다.

> 기존 정렬 로직상 '회장'은 '사원'보다 뒤에 위치해야하지만, `기준배열`으로 인해서 앞에 위치합니다.

<br/>

## 한영 변환

`convert_key(word: str, to_language: Literal['ko', 'en'], is_combine: bool = True)`

```python
from hangul_utils import convert_key

convert_key("사과", "en")
# tkrhk

convert_key("tkrhk", "ko")
# 사과
```

`to_language` 타입 **키보드 키** 에 맞게 문자를 변환시켜줍니다.

```python
convert_key("tkrhk", "ko", False)
# ㅅㅏㄱㅗㅏ
```

`isCombine` 속성을 비활성화 할 시, 한글이 결합되지 않습니다. <br/><br/>

## 한글 발음 파싱

`normalize(text: str, is_space: bool)`

```python
from hangul_utils import normalize

normalize("이탈리아")
# 'i tar ri a'

normalize("이탈리아", False)
# 'itarria'
```

한글 발음을 영어로 변환하여줍니다. <br/><br/>

## 조사

`format_josa(word: str)`

```python
from hangul_utils import format_josa

format_josa("인생[이란/란]")
# '인생이란'

format_josa("인생[란/테스트]")
# '인생이란'
```

`단어[조사1/조사2]` 형식의 텍스트를 `단어[조사]`로 알맞게 변환됩니다.

> '은/는', '이/가'와 같은 많이 알려진 조사는 자동으로 포맷됩니다. `[란/테스트] -> [이란/란]`

### 그 외

`josa(word: str, josa: str)`

```python
from hangul_utils import josa

josa("인생", "란")
# '이란'
```

단어에 따른 `조사` 정보만을 반환 받습니다. <br/><br/>

## 문자 암호화

`encode(input: any), decode(input: any)`

```python
from hangul_utils import encode, decode

encode("테스트123")
# 1VWV5U1VsV1JrcEVWVlU0Ymt...

encode(["바나나", "자두", "귤"])
# 3Mnl6SlRJMVNqUURWbFFVU2p...
```

문자를 암호화 시켜주며 `객체와 배열` 데이터도 암호화 대상입니다.

```python
encode1 = encode("테스트123")
decode(encode1)
# 테스트123

encode2 = encode(["바나나", "자두", "귤"])
decode(encode2)
# ['바나나', '자두', '귤']
```

`encode`로 변환된 암호문자를 `decode` 함수로 복호화 시킬 수 있습니다. <br/><br/>

## 언어 구별

`get_local_by_groups(word: str, is_percent: bool)`

```python
from hangul_utils import get_local_by_groups

get_local_by_groups("a1")
# ['en', 'number']
```

각 문자에 대한 언어를 배열에 담아서 반환해줍니다.

```python
get_local_by_groups("안녕하세요! Hello, world! 1234 #", True)
# {'ko': 18.52, 'en': 37.04, 'number': 14.81, 'special': 29.63, 'etc': 0.0}
```

`is_percent` 값을 통해서, 언어가 사용된 퍼센트를 나타내는 객체를 반환 받을 수 있습니다. <br/><br/>

## is_hangul, is_cho, is_jung, is_jong

`is_hangul(word: str), is_hangul_groups(word: str)`

```python
from hangul_utils import is_hangul, is_cho, is_jung, is_jong

is_hangul("사과")
# True

is_cho("ㅅㄱ")
# True

is_jung("ㅏㅘ")
# True

is_jong("ㄳ")
# True
```

입력된 문자가 한글, 초성, 중성, 종성인지 판별합니다.

```python
from hangul_utils import is_hangul_by_groups, is_cho_by_groups, is_jung_by_groups, is_jong_by_groups

is_hangul_by_groups("사!")
# [True, False]

is_cho_by_groups("ㅅㅏ")
# [True, False]

is_jung_by_groups("ㅅㅘ")
# [False, True]

is_jong_by_groups("ㄳㅏㅅ")
# [True, False, True]
```

입력된 모든 문자의 한글, 초성, 중성, 종성 여부를 판별하여 배열에 담아 반환됩니다. <br/><br/>

## 기타 함수(utils)

### is_number

`is_number(input: any)`

```python
from hangul_utils import is_number

is_number(None)
# False

is_number(0)
# True
```

입력값의 숫자 여부를 판별합니다.

### reverse_by_object

`reverse_by_object(object: any)`

```python
from hangul_utils import reverse_by_object

reverse_by_object({ 'a': 1, 'b': 2, 'c': 3 })
# { 1: 'a', 2: 'b', 3: 'c' }
```

객체의 `Key, Value` 값을 서로 바꿔 재구성한 데이터를 반환해줍니다.

### get_nested_property

`get_nested_property(key: Union[str, List[str]], object: any)`

```python
from hangul_utils import get_nested_property

object = { 'a': { 'b': 2 } }

object['a.b']
# error

get_nested_property("a.b", object)
# 2
```

`object.a.b` 접근을 문자열로 가능하도록 만들어주는 함수입니다.

### chunk_at_end

`chunk_at_end(value: str, n: int)`

```python
from hangul_utils import chunk_at_end

chunk_at_end("12345678", 4)
# [ '5678', '1234' ]

"".join(chunk_at_end("12345678", 1))
# '87654321'
```

문자를 **뒤에서부터** n개씩 자른 아이템을 배열에 담아 반환해줍니다.

### split_by_key

`split_by_key(key: str)`

```python
from hangul_utils import split_by_key

split_by_key("a.b")
# ['a', 'b'];

split_by_key("a[5]")
# ['a', 5];
```

Key를 차례대로 구분한 값을 배열에 담아 반환해줍니다.