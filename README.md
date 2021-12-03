# Input-Generator

Input dosyaları main.py dosyası tarafından otomatik olarak oluşturulmuştur.

Dosyaları bilgisayarınıza kaydettikten sonra aşağıdaki kodları projenizin başına yazarak inputları test edebilirsiniz


Outputlarla karşılaştırmayı unutmayın!
Kolay gelsin :)
```python
import sys
sys.stdin = open("buraya_input_dosyası_gelecek.txt", "w", encoding = "utf-8")
```

### Örn:
```python
import sys
sys.stdin = open(".Inputs/inputs0.txt", "w", encoding = "utf-8")
