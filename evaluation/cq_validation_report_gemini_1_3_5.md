# Báo cáo validate Competency Questions (CQ)

Thời gian sinh: 2026-07-08 21:10:49
Model tóm tắt: `gemini-3.1-flash-lite` | Model judge: `gemini-3.1-flash-lite`

## Tổng quan
- Tổng số CQ: 20
- PASS: 17 | FAIL: 3 | UNCLEAR: 0 | ERROR: 0

| CQ | Verdict | Confidence | Trường kiểm tra |
|---|---|---|---|
| CQ1 | PASS | 1.0 | education_level (HARD) |
| CQ2 | PASS | 0.95 | occupation + professional_persona (HARD) |
| CQ3 | PASS | 1.0 | age (HARD) |
| CQ4 | PASS | 0.95 | zone (SOFT, bổ trợ) |
| CQ5 | PASS | 0.95 | hobbies_and_interests (SOFT) + education_level (HARD) |
| CQ6 | PASS | 0.9 | career_goals_and_ambitions (GENERAL) |
| CQ7 | FAIL | 0.9 | marital_status (SOFT) |
| CQ8 | PASS | 0.95 | skills_and_expertise (HARD) |
| CQ9 | PASS | 0.95 | region (GENERAL) |
| CQ10 | PASS | 1.0 | travel_persona (SOFT) |
| CQ11 | FAIL | 0.9 | occupation/professional_persona (HARD) x arts_persona (SOFT) |
| CQ12 | PASS | 0.95 | sports_persona (SOFT) |
| CQ13 | PASS | 1.0 | sex |
| CQ14 | PASS | 1.0 | country (HARD, cố định) |
| CQ15 | PASS | 1.0 | persona (GENERAL) |
| CQ16 | FAIL | 0.9 | cultural_background (GENERAL) |
| CQ17 | PASS | 1.0 | zone + occupation (HARD) vs travel_persona (SOFT) - quan hệ uu_tien_hon |
| CQ18 | PASS | 0.95 | occupation x zone (HARD x SOFT combo) |
| CQ19 | PASS | 1.0 | arts_persona (SOFT) |
| CQ20 | PASS | 1.0 | hobbies_and_interests (SOFT) |


---
## CQ1: Trình độ học vấn của người dùng có ảnh hưởng đến độ phức tạp ngôn ngữ trong bản tóm tắt không?
**Trường kiểm tra:** education_level (HARD)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Bà Nga dùng câu ngắn, từ ngữ đời thường, không thuật ngữ; tóm tắt cho Oanh có thể dùng câu phức tạp hơn, lập luận nhiều tầng hơn rõ rệt.

### Person A — Bà Nga - Không học vấn, 88 tuổi
```
Bà con ở Đà Nẵng chú ý, ngoài khơi Thái Bình Dương đang có siêu bão Ba Vì rất mạnh. Theo dự báo, bão này ít khả năng đi thẳng vào Biển Đông, nhưng từ ngày 9 đến 11/7, hoàn lưu bão có thể làm gió mùa tây nam mạnh lên.

Vùng biển Bắc, giữa và Nam Biển Đông, bao gồm cả Hoàng Sa và Trường Sa, sẽ có gió mạnh cấp 6-7 và sóng cao từ 3 đến 5 mét, biển động rất dữ dội. Bà con làm nghề biển hoặc có người thân đi biển cần hết sức cẩn thận, theo dõi tin tức thường xuyên để giữ an toàn.

Các khu vực khác như Quảng Ninh chỉ là thông tin tham khảo về thiệt hại của cơn bão trước. Mùa bão năm nay được dự báo ít hơn mọi năm, nhưng thời tiết giờ khó lường, bà con cứ nên đề phòng để bảo vệ nhà cửa và sức khỏe.
```

### Person B — Oanh - Sau đại học, nhà nghiên cứu
```
Siêu bão Ba Vì (cấp 17, sức gió 200-280 km/h) đang hoạt động tại tây bắc Thái Bình Dương. Theo dự báo từ Trung tâm Dự báo Khí tượng Thủy văn quốc gia, xác suất bão đi vào Biển Đông dưới 10%. Tuy nhiên, hoàn lưu bão có khả năng tác động đến vùng biển phía đông bắc khu vực Bắc Biển Đông từ ngày 9 đến 11/7. Đồng thời, hiệu ứng hút gió từ siêu bão sẽ làm gió mùa tây nam mạnh lên, gây gió cấp 6-7 và sóng cao 3-5 m tại khu vực Biển Đông, bao gồm quần đảo Hoàng Sa và Trường Sa. Các khu vực khác ngoài Biển Đông chỉ chịu ảnh hưởng gián tiếp từ các hình thái thời tiết cực đoan tương tự.

Về bối cảnh môi trường, đây là hiện tượng thời tiết cực đoan cần được theo dõi sát sao do tính chất khó lường của biến đổi khí hậu, vốn có thể làm thay đổi quỹ đạo và cường độ bão nhanh chóng. Dữ liệu lịch sử cho thấy các cơn bão có cường độ mạnh, dù không đổ bộ trực tiếp, vẫn gây thiệt hại đáng kể về hạ tầng và sản xuất (như trường hợp bão Maysak tại Quảng Ninh với thiệt hại ước tính 20 tỷ đồng). Mùa bão năm 2026 được dự báo có tần suất thấp hơn trung bình nhiều năm, nhưng các cơ quan chuyên môn vẫn duy trì cảnh báo cao độ đối với các diễn biến cuối mùa.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản A sử dụng ngôn ngữ bình dân, câu ngắn và tập trung vào cảnh báo trực tiếp phù hợp với người lớn tuổi. Bản B sử dụng thuật ngữ chuyên môn, cấu trúc câu phức tạp và phân tích bối cảnh vĩ mô, đáp ứng đúng kỳ vọng về sự khác biệt trình độ học vấn giữa hai đối tượng.


---
## CQ2: Nghề nghiệp và lĩnh vực làm việc của người dùng có quyết định chủ đề văn bản nào được ưu tiên tóm tắt không?
**Trường kiểm tra:** occupation + professional_persona (HARD)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Minh nhấn vào giá vé, chi phí, cơ hội kinh doanh dịch vụ du lịch quanh lễ hội; tóm tắt cho Hiếu có thể trung lập hơn hoặc nhấn khía cạnh khác (không nhất thiết nhấn kinh doanh).

### Person A — Minh - Buôn bán lúa gạo
```
Siêu bão Ba Vì đang hoạt động ở phía tây bắc Thái Bình Dương. Các đài dự báo quốc tế đều nhận định bão ít khả năng đi vào Biển Đông (xác suất dưới 10%).

Tuy nhiên, từ ngày 9 đến 11/7, hoàn lưu bão có thể gây gió mạnh và sóng lớn ở vùng biển phía đông bắc Biển Đông. Ngoài ra, bão còn làm gió mùa tây nam mạnh lên, khiến vùng biển từ bắc đến nam Biển Đông (bao gồm cả Hoàng Sa, Trường Sa) có gió cấp 6-7, sóng cao 3-5m, biển động rất mạnh. Bà con làm nghề buôn bán, vận chuyển hàng hóa trên biển cần đặc biệt lưu ý theo dõi tin tức để đảm bảo an toàn cho tàu thuyền và hàng hóa.

Các khu vực khác như Đài Loan chỉ là hướng di chuyển dự kiến của bão.

Mùa bão năm nay dự báo ít bão hơn mọi năm, nhưng thời tiết vẫn khó lường. Trước đây, bão Maysak từng gây thiệt hại nặng nề về nhà cửa, tàu thuyền và hoa màu tại Quảng Ninh, gây thiệt hại khoảng 20 tỷ đồng. Cơ quan chức năng đang theo dõi sát sao để cập nhật tình hình.
```

### Person B — Dương Xuân Hiếu - Y tế / dược
```
Siêu bão Ba Vì (cấp 17, sức gió 200-280 km/h) đang hoạt động tại tây bắc Thái Bình Dương, dự báo di chuyển theo hướng tây tây bắc về phía Đài Loan (Trung Quốc). Xác suất bão đi vào Biển Đông dưới 10%, tuy nhiên hoàn lưu bão có khả năng gây ảnh hưởng đến vùng biển phía đông bắc khu vực Bắc Biển Đông từ ngày 9 đến 11/7.

Đáng chú ý, hiệu ứng hút gió từ siêu bão sẽ làm gió mùa tây nam mạnh lên, gây biển động rất mạnh tại khu vực Bắc, Giữa và Nam Biển Đông (bao gồm quần đảo Hoàng Sa và Trường Sa) trong giai đoạn 9-11/7, với cường độ gió cấp 6-7 và sóng cao từ 3-5 m. Các thông tin về thiệt hại do bão Maysak tại Quảng Ninh chỉ mang tính chất tham khảo.

Dự báo mùa mưa bão năm 2026 có số lượng bão và áp thấp nhiệt đới thấp hơn trung bình nhiều năm, nhưng diễn biến vẫn khó lường do tác động của biến đổi khí hậu, đòi hỏi sự theo dõi sát sao các bản tin dự báo khí tượng thủy văn để chủ động ứng phó.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A đã cá nhân hóa nội dung bằng cách thêm lời khuyên trực tiếp cho người làm nghề buôn bán, vận chuyển hàng hóa trên biển, phù hợp với nghề nghiệp của Minh. Bản tóm tắt B tập trung vào các thông số kỹ thuật và dự báo khí tượng mang tính trung lập, phù hợp với người làm trong lĩnh vực y tế/dược cần thông tin chính xác để chủ động ứng phó. Sự khác biệt này phản ánh đúng kỳ vọng về việc ưu tiên khía cạnh kinh doanh cho người dùng làm kinh doanh.


---
## CQ3: Độ tuổi của người dùng có làm thay đổi chủ đề được nhấn mạnh trong bản tóm tắt không?
**Trường kiểm tra:** age (HARD)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Phương Hạnh (trẻ) có thể nhấn cơ hội/khởi đầu tập luyện cơ bản; tóm tắt cho Bà Nga nhấn mạnh khía cạnh sức khỏe, vận động nhẹ nhàng, an toàn cho người lớn tuổi.

### Person A — Phương Hạnh - 21 tuổi, thất nghiệp tìm việc
```
Giai đoạn từ 40–60 tuổi là thời điểm quan trọng để phát hiện sớm các bệnh mạn tính và điều chỉnh lối sống nhằm giảm nguy cơ biến chứng. Các chuyên gia y tế khuyến nghị mọi người cần kết hợp khám sức khỏe định kỳ, dinh dưỡng hợp lý và vận động thường xuyên thay vì chỉ tập trung vào một bệnh cụ thể.

Về tim mạch, các bệnh như tăng huyết áp và rối loạn mỡ máu là nguyên nhân hàng đầu gây biến cố. Việc kiểm tra huyết áp, cholesterol, đường huyết và duy trì vận động ít nhất 150 phút mỗi tuần là biện pháp phòng ngừa hiệu quả. Đối với xương khớp, tình trạng thoái hóa và loãng xương đang phổ biến. Để duy trì sức khỏe hệ vận động, cần bổ sung canxi, vitamin D và thực hiện các bài tập chịu trọng lượng hoặc luyện tập sức mạnh.

Trong lĩnh vực ung bướu, tầm soát sớm có ý nghĩa quyết định đến kết quả điều trị. Mọi người cần tuân thủ lịch tầm soát dựa trên độ tuổi và tiền sử gia đình thay vì chỉ dựa vào giới tính. Cuối cùng, đối với các bệnh chuyển hóa như đái tháo đường hay gan nhiễm mỡ, cần duy trì chế độ ăn cân đối, hạn chế thực phẩm chế biến sẵn, kiểm soát cân nặng và ngủ đủ giấc để phát hiện sớm các bất thường trước khi xảy ra biến chứng. Các nội dung chuyên sâu về sự khác biệt bệnh lý giữa nam và nữ giới chỉ là thông tin tham khảo phụ.
```

### Person B — Bà Nga - 88 tuổi, nghỉ hưu
```
Bà Nga ơi, các bác sĩ có vài lời khuyên về sức khỏe cho người lớn tuổi như mình đây ạ:

Việc quan trọng nhất là mình phải đi khám sức khỏe định kỳ để phát hiện sớm bệnh tật. Ở tuổi của bà, cơ thể thay đổi nhiều nên cần chú ý các vấn đề sau:

- **Về xương khớp:** Người lớn tuổi rất dễ bị loãng xương và thoái hóa khớp. Bà nên ăn uống đủ chất, chú ý bổ sung canxi và vitamin D để xương chắc khỏe, tránh bị gãy xương.
- **Về bệnh chuyển hóa:** Các bệnh như tiểu đường hay mỡ máu đang tăng nhiều. Bà cần ăn uống điều độ, bớt đồ ngọt và đồ chế biến sẵn, giữ cân nặng ổn định và ngủ đủ giấc.
- **Về tim mạch:** Sau tuổi mãn kinh, phụ nữ cần kiểm tra huyết áp và đường huyết thường xuyên hơn.
- **Về tầm soát ung thư:** Dù là nam hay nữ, bà cũng nên đi tầm soát bệnh theo lịch của bác sĩ, đừng chỉ dựa vào giới tính mà chủ quan.

Các vấn đề về sức khỏe của nam giới hay các nhóm tuổi khác chỉ là thông tin tham khảo thêm, không cần quá bận tâm. Bà cứ giữ nếp sống lành mạnh, ăn uống hợp lý và đi khám đều đặn là tốt nhất cho sức khỏe tuổi già.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt B đã cá nhân hóa rõ rệt cho người cao tuổi thông qua cách xưng hô gần gũi, ngôn ngữ đơn giản và tập trung vào các vấn đề sức khỏe thiết yếu cho người già như loãng xương, tầm soát định kỳ và chế độ ăn uống điều độ. Ngược lại, bản A mang tính chất thông tin tổng quát, phù hợp với đối tượng trẻ tuổi hơn. Sự khác biệt này hoàn toàn khớp với kỳ vọng về việc nhấn mạnh khía cạnh sức khỏe và an toàn cho người lớn tuổi.


---
## CQ4: Khu vực sống (Đô Thị/Nông Thôn) có làm thay đổi phần nào của văn bản được giữ lại trong tóm tắt không?
**Trường kiểm tra:** zone (SOFT, bổ trợ)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Chị Mai (nông thôn) giữ lại phần giá nông sản/kênh phân phối truyền thống; tóm tắt cho Thảo (đô thị) giữ lại phần thương mại điện tử/logistics.

### Person A — Chị Mai - Buôn bán, Nông Thôn, Đà Nẵng
```
Việc tiêu thụ nông sản hiện nay đang kết hợp giữa kênh truyền thống và thương mại điện tử. Đối với người sản xuất tại nông thôn như ở Đà Nẵng, các kênh truyền thống như thương lái, hợp tác xã và chợ đầu mối vẫn đóng vai trò chủ chốt. Các kênh này giúp thu mua nông sản ngay tại chỗ, giảm chi phí vận chuyển và đảm bảo đầu ra ổn định cho các hộ sản xuất nhỏ lẻ mà không đòi hỏi quy trình phức tạp.

Các địa phương đang tiếp tục nâng cấp chợ đầu mối và trung tâm thu gom để hỗ trợ nông dân sơ chế, đóng gói và ổn định giá cả. Trong khi đó, tại các đô thị lớn, người tiêu dùng đang chuyển sang mua sắm qua ứng dụng trực tuyến, đòi hỏi hệ thống logistics và kho lạnh phát triển mạnh hơn.

Dù thương mại điện tử mở ra cơ hội tiếp cận khách hàng toàn quốc, nhưng việc áp dụng vẫn gặp khó khăn ở nông thôn do hạ tầng internet và dịch vụ vận chuyển chưa đồng đều. Do đó, mô hình kết hợp là hướng đi hiệu quả nhất: hợp tác xã và thương lái tập trung thu gom, sơ chế tại vùng sản xuất, còn các nền tảng số và doanh nghiệp logistics đảm nhận việc phân phối đến người tiêu dùng. Sự kết hợp này giúp nâng cao giá trị nông sản và tăng thu nhập cho người sản xuất.
```

### Person B — Phạm Thị Thảo - Buôn bán, Đô Thị, TP.HCM
```
Việc tiêu thụ nông sản hiện nay đang chuyển dịch theo mô hình kết hợp giữa kênh truyền thống và nền tảng số, tạo ra chuỗi cung ứng linh hoạt hơn.

Tại các đô thị lớn như TP.HCM, hành vi mua sắm đã thay đổi rõ rệt khi người tiêu dùng ưu tiên đặt hàng qua sàn thương mại điện tử và ứng dụng trực tuyến. Sự phát triển này đòi hỏi doanh nghiệp phải đầu tư mạnh vào hệ thống logistics (kho lạnh, trung tâm phân phối) và áp dụng công nghệ truy xuất nguồn gốc bằng mã QR để đảm bảo chất lượng sản phẩm. Các công cụ số hỗ trợ phân tích nhu cầu thị trường, dự báo sức mua và quản lý đơn hàng theo thời gian thực giúp tối ưu hóa lượng hàng tồn kho, giảm chi phí vận hành và nâng cao hiệu quả phân phối.

Đối với các vùng sản xuất nông nghiệp, mạng lưới truyền thống (thương lái, hợp tác xã, chợ đầu mối) vẫn giữ vai trò chủ chốt trong việc thu gom, sơ chế và đảm bảo đầu ra ổn định cho nông sản. Mô hình này đặc biệt phù hợp với các hộ sản xuất nhỏ lẻ nhờ quy trình giao dịch đơn giản và chi phí thấp. Các địa phương đang tiếp tục nâng cấp hệ thống chợ đầu mối và trung tâm thu gom để nâng cao năng lực bảo quản.

Dù thương mại điện tử mở ra cơ hội tiếp cận khách hàng toàn quốc, việc ứng dụng vẫn gặp thách thức về kỹ năng số của nông dân và hạ tầng logistics tại nông thôn. Do đó, sự kết hợp giữa kênh truyền thống (thu gom, sơ chế) và nền tảng số (phân phối đến đô thị) được xem là hướng đi tối ưu để nâng cao giá trị nông sản và tăng thu nhập cho người sản xuất. Các hoạt động tại các vùng nông thôn khác cũng đang được đẩy mạnh theo hướng tương tự.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A tập trung sâu vào vai trò của thương lái, hợp tác xã và các khó khăn hạ tầng tại nông thôn, phù hợp với nhu cầu của Chị Mai. Bản tóm tắt B nhấn mạnh vào hành vi mua sắm trực tuyến, logistics và công nghệ quản lý tại đô thị, đáp ứng đúng kỳ vọng cá nhân hóa cho Thảo. Sự khác biệt về trọng tâm nội dung giữa hai bản tóm tắt phản ánh chính xác bối cảnh sống của từng đối tượng.


---
## CQ5: Sở thích cá nhân có đủ để xác định góc độ tóm tắt phù hợp không, hay cần kết hợp với education_level?
**Trường kiểm tra:** hobbies_and_interests (SOFT) + education_level (HARD)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Dù cả hai đều có liên quan đến thể thao trong hồ sơ, văn phong tóm tắt cho A vẫn đơn giản hơn B do chênh lệch education_level, chứng tỏ hobbies không tự quyết định toàn bộ cách diễn đạt.

### Person A — Lê Văn Dung - Công nhân, Trung cấp/Cao đẳng
```
Giai đoạn 40–60 tuổi là thời điểm then chốt để tầm soát bệnh mạn tính và điều chỉnh lối sống nhằm ngăn ngừa biến chứng. Việc chăm sóc sức khỏe cần thực hiện toàn diện, kết hợp khám định kỳ, dinh dưỡng và vận động thay vì chỉ tập trung vào một bệnh lý đơn lẻ.

Về tim mạch, nam giới có nguy cơ mắc bệnh sớm hơn. Các chỉ số huyết áp, cholesterol và đường huyết cần được kiểm soát chặt chẽ. Bạn nên duy trì vận động ít nhất 150 phút mỗi tuần để phòng ngừa biến cố.

Đối với hệ xương khớp, dù loãng xương phổ biến ở nữ giới, nam giới lớn tuổi vẫn đối mặt với nguy cơ gãy xương do giảm mật độ xương. Việc bổ sung canxi, vitamin D và tập luyện các bài tập kháng lực là cần thiết để duy trì khối cơ và sức khỏe hệ vận động.

Trong lĩnh vực ung bướu, tầm soát sớm là yếu tố quyết định hiệu quả điều trị. Nam giới cần lưu ý đặc biệt đến ung thư phổi và ung thư gan, đồng thời tuân thủ lịch tầm soát dựa trên độ tuổi và tiền sử cá nhân.

Về các bệnh chuyển hóa như béo phì, đái tháo đường và gan nhiễm mỡ, nam giới thường có xu hướng mắc hội chứng chuyển hóa ở độ tuổi sớm hơn. Để kiểm soát, bạn cần duy trì chế độ ăn cân đối, hạn chế thực phẩm chế biến sẵn, đồ uống nhiều đường, đảm bảo ngủ đủ giấc và kiểm soát cân nặng. Các vấn đề sức khỏe khác ở các nhóm đối tượng khác được các chuyên gia đề cập ngắn gọn trong hội thảo.
```

### Person B — Dương Xuân Hiếu - Y tế/dược, Sau đại học
```
Giai đoạn 40–60 tuổi là thời điểm then chốt để tầm soát bệnh mạn tính và điều chỉnh lối sống nhằm giảm thiểu biến chứng. Các chuyên gia y tế khuyến nghị phương pháp tiếp cận đa chuyên khoa thay vì đơn lẻ, kết hợp khám định kỳ, dinh dưỡng và vận động.

**Về tim mạch:** Tăng huyết áp, rối loạn mỡ máu và bệnh động mạch vành là các nguyên nhân hàng đầu. Nam giới có nguy cơ mắc bệnh sớm hơn, đòi hỏi kiểm soát chặt chẽ huyết áp, cholesterol, đường huyết và duy trì vận động tối thiểu 150 phút/tuần.

**Về xương khớp:** Thoái hóa khớp và loãng xương là vấn đề phổ biến. Nam giới lớn tuổi cần chú ý nguy cơ gãy xương do giảm mật độ xương. Giải pháp chuyên môn bao gồm bổ sung canxi, vitamin D và thực hiện các bài tập kháng lực để duy trì khối cơ và sức khỏe hệ vận động.

**Về ung bướu:** Tầm soát sớm là yếu tố quyết định tiên lượng. Nam giới cần đặc biệt lưu ý các bệnh lý như ung thư phổi và ung thư gan. Việc tuân thủ lịch tầm soát phải dựa trên độ tuổi, tiền sử gia đình và yếu tố nguy cơ cá nhân thay vì chỉ dựa vào giới tính.

**Về bệnh chuyển hóa:** Tỷ lệ thừa cân, béo phì, đái tháo đường típ 2 và gan nhiễm mỡ không do rượu đang gia tăng. Nam giới có xu hướng mắc hội chứng chuyển hóa ở độ tuổi sớm hơn. Chiến lược can thiệp bao gồm duy trì chế độ ăn cân đối, hạn chế thực phẩm chế biến sẵn, kiểm soát cân nặng và tái khám định kỳ để phát hiện sớm các bất thường chuyển hóa.

*(Các nội dung liên quan đến đối tượng nữ giới và các xu hướng văn hóa khác đã được lược bỏ để tập trung vào chuyên môn y tế thực tế cho nam giới).*
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt B sử dụng thuật ngữ chuyên môn sâu (tiên lượng, đa chuyên khoa, bệnh động mạch vành, đái tháo đường típ 2) phù hợp với trình độ sau đại học, trong khi bản A diễn đạt bằng ngôn ngữ phổ thông, dễ hiểu. Sự khác biệt về văn phong và độ phức tạp lập luận giữa hai bản tóm tắt phản ánh rõ rệt ảnh hưởng của education_level, xác nhận rằng sở thích cá nhân không phải là yếu tố duy nhất quyết định cách trình bày thông tin.


---
## CQ6: Mục tiêu nghề nghiệp có làm tăng mức độ ưu tiên của nội dung mang tính định hướng tương lai (xu hướng thị trường, cơ hội đầu tư) trong tóm tắt không?
**Trường kiểm tra:** career_goals_and_ambitions (GENERAL)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Thảo giữ lại phần xu hướng thị trường/thương mại điện tử (cơ hội mở rộng); tóm tắt cho Minh thiên về mô tả hiện trạng giá cả ổn định, ít nhấn cơ hội mở rộng.

### Person A — Trần Thùy Thảo - muốn mở rộng kinh doanh ra quốc tế
```
Việc tiêu thụ nông sản hiện nay đang chuyển dịch theo hướng kết hợp giữa kênh truyền thống và nền tảng số. Đối với người làm kinh doanh nông sản tại nông thôn như bạn, các kênh truyền thống (thương lái, hợp tác xã, chợ đầu mối) vẫn giữ vai trò cốt lõi. Các kênh này giúp thu mua sản phẩm ngay tại chỗ, giảm chi phí vận chuyển và đảm bảo đầu ra ổn định cho nông sản theo mùa. Các hợp tác xã hiện nay cũng hỗ trợ đắc lực trong việc phân loại, sơ chế và đóng gói, giúp quy trình giao dịch đơn giản và tiết kiệm chi phí hơn cho các hộ sản xuất.

Tại các đô thị lớn, người tiêu dùng đang chuyển sang mua sắm qua sàn thương mại điện tử và ứng dụng trực tuyến, đòi hỏi sự đầu tư vào logistics và công nghệ truy xuất nguồn gốc. Tuy nhiên, việc áp dụng số hóa tại nông thôn vẫn còn nhiều thách thức về hạ tầng internet và kỹ năng vận hành.

Hướng đi phù hợp nhất hiện nay là mô hình kết hợp: hợp tác xã và thương lái đảm nhận khâu thu gom, sơ chế tại vùng sản xuất, trong khi các nền tảng số và doanh nghiệp logistics đảm nhận việc phân phối đến người tiêu dùng thành phố. Sự kết hợp này giúp nâng cao giá trị nông sản, ổn định giá cả và mở rộng thị trường tiêu thụ bền vững cho người sản xuất.
```

### Person B — Minh - mong muốn ổn định, ít tham vọng mở rộng
```
Việc tiêu thụ nông sản hiện nay đang có sự kết hợp giữa cách làm truyền thống và công nghệ số.

Tại các vùng nông thôn như Hà Nội, kênh phân phối truyền thống qua thương lái, hợp tác xã và chợ đầu mối vẫn giữ vai trò chủ chốt. Cách này giúp bà con nông dân bán hàng nhanh ngay sau khi thu hoạch, giảm chi phí vận chuyển và không cần lo lắng về công nghệ phức tạp. Các hợp tác xã hiện nay còn hỗ trợ thêm việc phân loại, đóng gói và kết nối với doanh nghiệp để đầu ra ổn định hơn, giúp giảm tình trạng được mùa mất giá.

Ở các đô thị lớn, người dân đang chuyển dần sang mua sắm qua mạng và ứng dụng điện thoại.

Dù công nghệ số giúp mở rộng thị trường, nhưng việc áp dụng vẫn còn khó khăn do hạ tầng internet và logistics ở nông thôn chưa đồng bộ, cùng với hạn chế về kỹ năng số của người sản xuất. Vì vậy, mô hình kết hợp là hiệu quả nhất: thương lái và hợp tác xã tập trung thu gom, sơ chế tại chỗ, còn các sàn thương mại điện tử và đơn vị vận chuyển lo khâu phân phối đến người tiêu dùng. Sự phối hợp này giúp nâng cao giá trị nông sản và tăng thu nhập cho người làm kinh doanh như anh.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.9

- **Lý do:** Bản tóm tắt A cho Thảo tập trung vào việc phân tích xu hướng chuyển dịch và mô hình kết hợp như một chiến lược để mở rộng thị trường, phù hợp với mục tiêu kinh doanh quốc tế. Bản tóm tắt B cho Minh nhấn mạnh vào tính ổn định, giảm rủi ro và sự đơn giản của kênh truyền thống, phản ánh đúng kỳ vọng về việc ưu tiên sự ổn định thay vì mở rộng.


---
## CQ7: Tình trạng hôn nhân có làm thay đổi góc độ được nhấn mạnh khi tóm tắt văn bản về gia đình/du lịch không?
**Trường kiểm tra:** marital_status (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Hoa (đã kết hôn) nhấn vào điểm đến phù hợp gia đình/trẻ nhỏ; tóm tắt cho Hương (ly thân) nhấn vào trải nghiệm cá nhân/độc lập.

### Person A — Huỳnh Thanh Hoa - Đã kết hôn
```
Thị trường du lịch hè năm nay đang trên đà tăng trưởng tích cực với sự phân hóa rõ rệt theo từng nhóm khách hàng. Đối với người yêu thích khám phá như bạn, đây là cơ hội tuyệt vời để bước ra khỏi những cung đường quen thuộc, tìm đến những vùng đất mới để đắm mình vào hơi thở văn hóa bản địa và học hỏi từ những câu chuyện đời thường của người dân địa phương. Hãy tưởng tượng mỗi chuyến đi là một hành trình mở, nơi bạn không chỉ là khách lữ hành mà còn là người kết nối, cảm nhận sự chân thực của cuộc sống qua từng điểm đến.

Trong khi các đoàn khách công sở ưu tiên nghỉ dưỡng ven biển và các gia đình chọn tour trọn gói để thuận tiện cho con trẻ, thì nhóm khách trẻ lại ưa chuộng sự linh hoạt và tự túc. Các thị trường du lịch khác cũng đang phục hồi ổn định, góp phần làm phong phú thêm bức tranh du lịch chung.

Với tư cách là một người làm trong ngành logistics, bạn có thể thấy rõ sự chuyển dịch này cũng giống như việc tối ưu hóa các tuyến đường: mỗi nhóm khách hàng là một "lộ trình" riêng biệt đòi hỏi sự linh hoạt và cá nhân hóa. Xu hướng ứng dụng công nghệ để tư vấn và đặt dịch vụ đang trở thành tiêu chuẩn mới, giúp hành trình khám phá trở nên suôn sẻ và trọn vẹn hơn. Đây chính là thời điểm để những tâm hồn yêu xê dịch như bạn lên kế hoạch cho những chuyến đi đầy cảm hứng, nơi mỗi điểm dừng chân đều là một bài học quý giá về văn hóa và con người.
```

### Person B — Ly thân, occupation không chuyên biệt (tránh Topic 'kinh doanh' lấn át marital_status)
```
Thị trường du lịch hè năm nay đang trên đà tăng trưởng tốt với nhiều lựa chọn đa dạng. Thay vì đi theo lối mòn, các chuyến đi giờ đây được thiết kế linh hoạt hơn, giúp người đi có thể tự do khám phá những vùng đất mới theo ý mình.

Với những người yêu thích tìm hiểu về cội nguồn và những giá trị xưa cũ, các tour khám phá di tích lịch sử và văn hóa địa phương đang trở thành điểm sáng, mang lại những trải nghiệm sâu sắc và đầy cảm xúc như được chạm tay vào dòng chảy thời gian. Những chuyến đi này không chỉ là dịp để nghỉ ngơi, mà còn là hành trình tìm về những câu chuyện, những dấu ấn văn hóa đã làm nên bản sắc của mỗi vùng miền.

Bên cạnh đó, thị trường cũng ghi nhận sự quan tâm từ các nhóm khách công sở, gia đình và người trẻ với nhiều hình thức từ nghỉ dưỡng biển đến các chuyến đi ngắn ngày tiết kiệm. Các đơn vị lữ hành hiện nay đã chú trọng hơn vào việc ứng dụng công nghệ để việc đặt dịch vụ trở nên thuận tiện, nhanh chóng, giúp mọi người dễ dàng lên kế hoạch cho những chuyến đi ý nghĩa. Nhìn chung, dù bạn chọn hình thức nào, du lịch hè vẫn là cơ hội tuyệt vời để tái tạo năng lượng và mở mang tầm mắt sau những ngày làm việc vất vả.
```

### Đánh giá LLM judge
- **Verdict:** FAIL

- **Confidence:** 0.9

- **Lý do:** Bản tóm tắt A (cho Hoa) tập trung vào trải nghiệm cá nhân và công việc logistics thay vì nhấn mạnh vào yếu tố gia đình/trẻ nhỏ như kỳ vọng. Bản tóm tắt B mang tính chất chung chung, không làm nổi bật được trải nghiệm độc lập hay cá nhân hóa cho người ly thân mà chỉ liệt kê các nhóm khách hàng một cách dàn trải.


---
## CQ8: Kỹ năng hiện có của người dùng có tác động loại bỏ phần hướng dẫn cơ bản (nhập môn) trong tóm tắt không?
**Trường kiểm tra:** skills_and_expertise (HARD)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Anh Dũng (thiết kế chuyên sâu) lược bỏ phần hướng dẫn cơ bản (mở phần mềm, công cụ cơ bản), chỉ giữ phần nâng cao (typography, motion design); tóm tắt cho Lê Văn Dung có thể giữ lại nhiều hơn hoặc trình bày khác do không có nền tảng thiết kế.

### Person A — Anh Dũng - Freelance designer nhiều năm kinh nghiệm
```
Xu hướng thiết kế UX/UI năm 2025 tập trung vào việc ứng dụng AI để tối ưu hóa trải nghiệm người dùng thông qua các giải pháp cá nhân hóa giao diện, tích hợp chatbot thông minh xử lý ngôn ngữ tự nhiên và tự động hóa bố cục trang web.

Trong định hướng thiết kế tối giản, mục tiêu cốt lõi là duy trì tính thẩm mỹ và sự tập trung của người dùng bằng cách sử dụng không gian âm hợp lý, bảng màu tinh tế và các hiệu ứng tương tác vi mô (micro-interactions) để tăng tính hấp dẫn. Các xu hướng này hỗ trợ trực tiếp cho công việc freelance thiết kế, giúp tối ưu hóa quy trình phác thảo giao diện và nâng cao trải nghiệm người dùng trên các dự án web.
```

### Person B — Lê Văn Dung - Công nhân, kỹ năng cơ bản
```
Năm 2025, xu hướng thiết kế giao diện (UX/UI) tập trung mạnh vào việc ứng dụng trí tuệ nhân tạo (AI) để tối ưu hóa trải nghiệm người dùng.

AI đóng vai trò quan trọng trong việc tự động phân tích hành vi để điều chỉnh giao diện cá nhân hóa theo sở thích từng người. Các trợ lý ảo (chatbot) thông minh giúp xử lý ngôn ngữ tự nhiên, hỗ trợ khách hàng nhanh chóng. Ngoài ra, AI còn tự động đề xuất bố cục trang web hoặc ứng dụng sao cho hiệu quả nhất.

Bên cạnh công nghệ, xu hướng thiết kế còn hướng đến sự tối giản để người dùng dễ dàng thao tác. Các yếu tố chính bao gồm: sử dụng không gian âm để giảm bớt các chi tiết thừa, chọn lọc màu sắc tinh tế để tạo điểm nhấn, và chú trọng các hiệu ứng tương tác nhỏ (micro-interactions) để tăng sự thú vị khi sử dụng.

Các xu hướng thiết kế khác ngoài phạm vi này chỉ mang tính chất bổ trợ phụ.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A lược bỏ các giải thích định nghĩa cơ bản (như giải thích chatbot hay không gian âm là gì) và tập trung vào ứng dụng chuyên sâu cho công việc freelance, phù hợp với người có kinh nghiệm. Bản B giữ lại các giải thích mang tính nhập môn, diễn giải chi tiết các khái niệm để người không chuyên dễ tiếp cận, hoàn toàn khớp với kỳ vọng về sự cá nhân hóa theo trình độ người dùng.


---
## CQ9: Vùng địa lý cư trú có làm tăng mức độ ưu tiên của nội dung địa phương trong tóm tắt không?
**Trường kiểm tra:** region (GENERAL)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho person A (Cần Thơ) giữ lại phần ĐBSCL/canh tác thông minh chống xâm nhập mặn rõ rệt hơn; tóm tắt cho person B (Hải Phòng) giữ lại phần nông nghiệp đô thị công nghệ cao ở ĐBSH rõ rệt hơn, cả hai đều lược bớt phần miền Trung/Tây Nguyên (không liên quan trực tiếp đến region của cả 2 person).

### Person A — Cô (Cần Thơ) - Buôn bán, gắn với chợ nổi miền Tây
```
Trước thách thức của biến đổi khí hậu, ngành nông nghiệp đang có những thay đổi quan trọng để thích ứng với điều kiện tự nhiên.

Tại Đồng bằng sông Cửu Long, đặc biệt là các vùng nông thôn như Cần Thơ, nông dân đã chuyển từ tư duy chống chọi sang "thuận thiên". Thay vì độc canh cây lúa rủi ro cao, các hợp tác xã đang áp dụng mô hình luân canh linh hoạt: nuôi tôm thẻ chân trắng, tôm sú vào mùa mặn (tháng 2 đến tháng 4) và trồng lúa chịu mặn khi mùa mưa đến. Việc ứng dụng công nghệ số, cụ thể là các trạm đo độ mặn tự động kết nối qua điện thoại, giúp người dân chủ động kiểm soát nguồn nước, bảo vệ hiệu quả các vùng cây ăn trái đặc sản.

Trong khi đó, các vùng miền khác cũng có những hướng đi riêng: nông nghiệp công nghệ cao tại Đồng bằng sông Hồng tập trung vào mô hình nhà màng, thủy canh đa tầng để cung ứng thực phẩm cho đô thị; còn khu vực miền Trung và Tây Nguyên áp dụng hệ thống tưới tiết kiệm và mô hình chăn nuôi tuần hoàn để chống hạn hán, hoang mạc hóa.

Những chuyển dịch này giúp xây dựng nền nông nghiệp bền vững, tận dụng tốt lợi thế tự nhiên và đặc thù kinh tế của từng địa phương.
```

### Person B — Oanh - Hải Phòng, vùng đồng bằng sông Hồng
```
Tại Hải Phòng và các đô thị lớn thuộc Đồng bằng sông Hồng, nông nghiệp đang chuyển dịch mạnh mẽ sang mô hình công nghệ cao để thích ứng với tốc độ đô thị hóa và biến đổi khí hậu. Thay vì canh tác truyền thống trên diện tích đất hạn hẹp, các mô hình nhà màng, nhà kính thông minh kết hợp thủy canh và khí canh đa tầng đang được triển khai khép kín ngay sát các khu công nghiệp.

Quy trình sản xuất tại đây được tối ưu hóa thông qua hệ thống máy tính điều khiển tự động các thông số kỹ thuật: châm phân, độ ẩm, ánh sáng LED và nhiệt độ phòng. Phương thức này cho phép sản xuất rau và hoa cao cấp quanh năm, không bị ảnh hưởng bởi thời tiết cực đoan của mùa đông Bắc Bộ. Về hiệu quả kinh tế và kỹ thuật, năng suất nông nghiệp đô thị công nghệ cao hiện đạt gấp 4 đến 5 lần so với canh tác truyền thống, đồng thời thiết lập chuỗi cung ứng thực phẩm an toàn trực tiếp cho cư dân thành thị, giúp tối ưu hóa chi phí vận chuyển.

Các vùng miền khác như Đồng bằng sông Cửu Long đang áp dụng mô hình canh tác thuận thiên thích ứng xâm nhập mặn, trong khi miền Trung và Tây Nguyên tập trung vào nông nghiệp tuần hoàn và tưới tiết kiệm để chống hạn hán.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A tập trung chi tiết vào mô hình thuận thiên và ứng dụng đo độ mặn tại ĐBSCL, trong khi bản B tập trung sâu vào nông nghiệp công nghệ cao tại ĐBSH. Cả hai bản đều đẩy nội dung về miền Trung/Tây Nguyên xuống phần cuối với dung lượng rất ngắn, đáp ứng đúng kỳ vọng về việc ưu tiên nội dung địa phương và lược bớt thông tin không liên quan.


---
## CQ10: Phong cách du lịch (travel_persona) có làm thay đổi phần nào của văn bản du lịch được giữ lại trong tóm tắt không?
**Trường kiểm tra:** travel_persona (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Hiếu giữ lại rõ rệt phần nội dung thiên nhiên/sinh thái (Bạch Mã, thác Đỗ Quyên); tóm tắt cho Hà giữ lại rõ rệt phần nội dung di tích lịch sử/văn hóa (Đại Nội, chùa Thiên Mụ).

### Person A — Dương Xuân Hiếu - thích khám phá thiên nhiên, Vườn quốc gia Cát Tiên
```
Hành trình khám phá Vườn quốc gia Bạch Mã là điểm nhấn chính cho nhu cầu trải nghiệm thiên nhiên và sinh thái. Cách trung tâm thành phố Huế khoảng 40 km, khu vực này sở hữu hệ sinh thái rừng nguyên sinh phong phú với độ cao gần 1.450 m, khí hậu mát mẻ quanh năm và nhiều loài động thực vật quý hiếm được bảo tồn. Các cung đường mòn dẫn tới thác Đỗ Quyên mang lại trải nghiệm thực tế về sự thay đổi của môi trường tự nhiên, nơi tiếng nước đổ và hương rừng tạo nên bầu không khí đặc trưng.

Bên cạnh đó, hành trình cũng bao gồm việc tham quan các di tích lịch sử tại cố đô Huế như Đại Nội và chùa Thiên Mụ. Các hoạt động du lịch khác như thưởng thức ẩm thực địa phương hay lưu trú tại khu vực trung tâm chỉ là những trải nghiệm bổ trợ ngắn hạn. Tổng thể chuyến đi là sự kết hợp giữa việc khám phá thiên nhiên hoang sơ và tìm hiểu các giá trị di sản văn hóa truyền thống.
```

### Person B — Ngô Thị Hà - thích điểm đến có giá trị lịch sử, văn hóa
```
Hành trình khám phá Huế là sự giao thoa tuyệt vời giữa thiên nhiên hùng vĩ và chiều sâu văn hóa lịch sử, nơi mỗi bước chân đều mang lại những cảm xúc lắng đọng.

Buổi chiều tại cố đô là điểm nhấn đặc biệt, đưa ta trở về với không gian uy nghi của Đại Nội bên dòng sông Hương hiền hòa. Những cổng thành rêu phong, mái ngói lưu ly và các công trình kiến trúc triều Nguyễn như những trang sử sống động, lưu giữ dấu ấn của hàng trăm năm thăng trầm. Tiếng chuông chùa Thiên Mụ ngân vang trên đồi Hà Khê trong ánh hoàng hôn vàng nhạt tạo nên một bức tranh thanh tịnh, cổ kính, khiến nhịp sống hối hả thường nhật như chậm lại, nhường chỗ cho sự chiêm nghiệm về giá trị truyền thống.

Khi phố lên đèn, hành trình thêm trọn vẹn với những hương vị ẩm thực đặc trưng như bún bò, cơm hến hay bánh bèo nóng hổi từ các quán nhỏ ven đường. Việc lựa chọn lưu trú gần khu vực Đại Nội hay dọc bờ nam sông Hương sẽ giúp bạn thuận tiện hơn trong việc cảm nhận trọn vẹn hơi thở của vùng đất cố đô này.

Bên cạnh đó, chuyến đi còn có nhánh trải nghiệm thiên nhiên tại Vườn quốc gia Bạch Mã với khí hậu mát mẻ và hệ sinh thái rừng nguyên sinh phong phú.

Rời Huế, điều đọng lại không chỉ là cảnh sắc, mà là cảm giác về một vùng đất nơi lịch sử và thiên nhiên song hành, tạo nên sức hấp dẫn bền bỉ, đầy tự hào.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt A tập trung chi tiết vào Vườn quốc gia Bạch Mã và thác Đỗ Quyên, phù hợp với sở thích thiên nhiên của Hiếu. Bản tóm tắt B dành phần lớn dung lượng mô tả Đại Nội và chùa Thiên Mụ với ngôn từ giàu cảm xúc, phản ánh đúng sở thích văn hóa lịch sử của Hà. Sự phân bổ nội dung giữa hai bản tóm tắt hoàn toàn khớp với kỳ vọng đã đề ra.


---
## CQ11: Người dùng có nghề nghiệp sáng tạo thì bản tóm tắt về văn hóa nghệ thuật có cần giữ lại phần kỹ thuật chuyên môn không?
**Trường kiểm tra:** occupation/professional_persona (HARD) x arts_persona (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Anh Dũng giữ lại phần phân tích kỹ thuật (lớp màu, phối màu, trường phái); tóm tắt cho Lê Văn Dung chỉ giữ phần giới thiệu sự kiện và cảm nhận tổng thể.

### Person A — Anh Dũng - Freelance designer (nghề sáng tạo)
```
Triển lãm "Sắc màu và Ký ức" tại Bảo tàng Mỹ thuật Việt Nam đang là điểm hẹn văn hóa đầy cảm hứng, nơi 82 tác phẩm của 27 họa sĩ cùng hội tụ để kể những câu chuyện về đời sống. Không gian trưng bày được sắp xếp tinh tế, dẫn dắt người xem đi từ những gam màu tươi sáng của nhịp sống đô thị hiện đại đến những khoảng lặng hoài niệm của phong cảnh làng quê, miền núi.

Với một người làm sáng tạo như bạn, triển lãm này không chỉ là nơi thưởng lãm mà còn là nguồn cảm hứng dồi dào. Sự kết hợp giữa các họa sĩ gạo cội và những gương mặt trẻ tạo nên một dòng chảy nghệ thuật đa chiều, nơi mỗi nét vẽ đều như một nốt trầm xao xuyến, khơi gợi những ký ức và cảm xúc riêng biệt trong lòng người xem. Những bức tranh về đời sống thường nhật, về những điều bình dị quanh ta được khắc họa đầy tinh tế, nhắc nhở chúng ta hãy chậm lại để quan sát và cảm nhận vẻ đẹp của cuộc sống.

Các hoạt động giao lưu giữa họa sĩ và công chúng, cùng chương trình hướng dẫn nghệ thuật cho học sinh, hứa hẹn sẽ tạo nên một không gian kết nối cộng đồng sáng tạo đầy cởi mở. Đây thực sự là một dịp quý giá để những người yêu hội họa tìm thấy sự đồng điệu, nơi nghệ thuật không chỉ nằm trên khung vải mà còn sống động trong từng cuộc trò chuyện, từng góc nhìn về văn hóa và con người.

*(Các hoạt động triển lãm tại các vùng miền khác ngoài Cần Thơ chỉ mang tính chất tham khảo chung cho cộng đồng yêu nghệ thuật trên cả nước).*
```

### Person B — Lê Văn Dung - Công nhân/lao động phổ thông
```
Triển lãm hội họa "Sắc màu và Ký ức" tại Bảo tàng Mỹ thuật Việt Nam đang là điểm hẹn văn hóa đầy cảm xúc, nơi những nét vẽ không chỉ là nghệ thuật mà còn là những mảnh ghép ký ức đời thường. Với 82 tác phẩm từ 27 họa sĩ, không gian triển lãm như một bản hòa ca giữa nhịp sống đô thị hối hả và vẻ đẹp bình dị của làng quê, miền núi.

Đối với những người yêu cái đẹp truyền thống, triển lãm là nơi để ta dừng chân, ngắm nhìn những bức tranh về chợ truyền thống hay cảnh sinh hoạt đời thường – những hình ảnh thân thuộc gợi nhắc về bản sắc văn hóa Việt Nam. Những mảng màu trầm lắng hay tươi sáng trong tranh như những nốt nhạc, khơi gợi trong lòng người xem những câu chuyện riêng, những ký ức về cuộc sống mà đôi khi vì bận rộn ta đã vô tình lãng quên. Sự kết hợp giữa các họa sĩ gạo cội và những gương mặt trẻ tạo nên một dòng chảy nghệ thuật liền mạch, nơi mỗi bức tranh là một lời mời gọi ta hãy chậm lại, quan sát và trân trọng những điều bình dị quanh mình.

Các hoạt động nghệ thuật tại các vùng miền khác trên cả nước cũng đang diễn ra sôi nổi với nhiều hình thức trưng bày đa dạng.

Tại không gian này, sự kết nối giữa người xem và tác phẩm không chỉ nằm ở việc thưởng lãm, mà còn là những cuộc trò chuyện, chia sẻ cảm nhận giữa những người cùng chung niềm yêu thích văn hóa. Triển lãm không chỉ là nơi trưng bày, mà còn là điểm đến để mỗi người tìm thấy sự đồng điệu, nuôi dưỡng tâm hồn sau những giờ làm việc căng thẳng. Với các chương trình giao lưu và hướng dẫn sắp tới, đây thực sự là một không gian mở, nơi nghệ thuật được lan tỏa và trở nên gần gũi hơn với mọi người.
```

### Đánh giá LLM judge
- **Verdict:** FAIL

- **Confidence:** 0.9

- **Lý do:** Cả hai bản tóm tắt đều tập trung vào cảm xúc và mô tả chung chung, thiếu vắng hoàn toàn các phân tích kỹ thuật chuyên môn (lớp màu, phối màu, trường phái) mà người làm sáng tạo như Anh Dũng cần. Bản A không thể hiện rõ sự khác biệt về chuyên môn so với bản B, do đó không đáp ứng được kỳ vọng cá nhân hóa theo yêu cầu.


---
## CQ12: Mức độ tham gia thể thao có quyết định phần nào của văn bản sức khỏe được ưu tiên trong tóm tắt không?
**Trường kiểm tra:** sports_persona (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Phương Chi có thể giữ phần dinh dưỡng thể thao/phục hồi cơ chuyên sâu hơn; tóm tắt cho Bà Nga giữ phần khuyến nghị sức khỏe cơ bản, vận động nhẹ.

### Person A — Phương Chi - năng động, tập bóng bàn/đi bộ thường xuyên
```
Giai đoạn 40–60 tuổi là thời điểm then chốt để tầm soát bệnh mạn tính và điều chỉnh lối sống nhằm ngăn ngừa biến chứng. Đối với nữ giới trung niên, việc quản lý sức khỏe cần tập trung vào các nhóm bệnh lý đặc thù sau:

**Sức khỏe tim mạch và chuyển hóa:**
Sau giai đoạn mãn kinh, nguy cơ tim mạch ở nữ giới tăng đáng kể do thay đổi nội tiết. Các chỉ số huyết áp, cholesterol và đường huyết cần được kiểm soát chặt chẽ. Tình trạng thừa cân, béo phì, đái tháo đường típ 2 và gan nhiễm mỡ không do rượu đang gia tăng ở nữ giới sau tuổi trung niên. Giải pháp phòng ngừa hiệu quả bao gồm duy trì chế độ ăn cân đối, hạn chế thực phẩm chế biến sẵn, đồ uống nhiều đường, đảm bảo giấc ngủ và kiểm soát cân nặng. Hoạt động thể lực cần duy trì tối thiểu 150 phút mỗi tuần.

**Sức khỏe xương khớp:**
Thoái hóa khớp và loãng xương là tình trạng phổ biến, đặc biệt với tỷ lệ cao ở nữ giới sau mãn kinh. Để duy trì khối cơ và sức khỏe hệ vận động, cần bổ sung đầy đủ canxi, vitamin D, kết hợp các bài tập chịu trọng lượng và luyện tập sức mạnh.

**Tầm soát ung bướu:**
Tầm soát sớm đóng vai trò quyết định trong tiên lượng điều trị. Mặc dù ung thư vú phổ biến hơn ở nữ giới, việc tuân thủ lịch tầm soát cần dựa trên độ tuổi, tiền sử gia đình và các yếu tố nguy cơ cá nhân thay vì chỉ dựa vào giới tính.

*Lưu ý về các nhóm đối tượng khác:* Các bệnh lý tim mạch, ung thư phổi, ung thư gan và hội chứng chuyển hóa ở nam giới cũng được thảo luận với các đặc điểm khởi phát sớm hơn.
```

### Person B — Bà Nga - chỉ tập nhẹ nhàng, dưỡng sinh
```
Bà Nga ơi, các bác sĩ có vài lời khuyên về sức khỏe cho người lớn tuổi như mình đây ạ:

Việc quan trọng nhất là mình phải đi khám sức khỏe định kỳ để phát hiện sớm bệnh tật. Ở tuổi của bà, cơ thể thay đổi nhiều nên cần chú ý các vấn đề sau:

- **Về xương khớp:** Người lớn tuổi rất dễ bị loãng xương và thoái hóa khớp. Bà nên ăn uống đủ chất, chú ý bổ sung canxi và vitamin D để xương chắc khỏe, tránh bị gãy xương.
- **Về bệnh chuyển hóa:** Các bệnh như tiểu đường hay mỡ máu đang tăng nhiều. Bà cần ăn uống điều độ, bớt đồ ngọt và đồ chế biến sẵn, giữ cân nặng ổn định và ngủ đủ giấc.
- **Về tim mạch:** Sau tuổi mãn kinh, phụ nữ cần kiểm tra huyết áp và đường huyết thường xuyên hơn.
- **Về tầm soát ung thư:** Dù là nam hay nữ, bà cũng nên đi tầm soát bệnh theo lịch của bác sĩ, đừng chỉ dựa vào giới tính mà chủ quan.

Các vấn đề về sức khỏe của nam giới hay các nhóm tuổi khác chỉ là thông tin tham khảo thêm, không cần quá bận tâm. Bà cứ giữ nếp sống lành mạnh, ăn uống hợp lý và đi khám đều đặn là tốt nhất cho sức khỏe tuổi già.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A tập trung vào các thuật ngữ chuyên môn như 'luyện tập sức mạnh', 'duy trì khối cơ' phù hợp với người năng động. Bản tóm tắt B sử dụng ngôn ngữ gần gũi, tập trung vào các khuyến nghị cơ bản và nhẹ nhàng, phản ánh đúng sự cá nhân hóa theo hồ sơ người dùng.


---
## CQ13: Giới tính có làm thay đổi góc độ ưu tiên trong tóm tắt khi văn bản đề cập đến nhiều nhóm đối tượng không?
**Trường kiểm tra:** sex

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Hải giữ lại phần khuyến nghị dành cho nam giới (tim mạch, tuyến tiền liệt); tóm tắt cho Linh giữ lại phần dành cho nữ giới (xương khớp, tầm soát ung thư vú).

### Person A — Trần Văn Hải - Nam, 48 tuổi
```
Ở tuổi 48, anh cần chú trọng chăm sóc sức khỏe định kỳ để duy trì công việc kinh doanh. Đối với nam giới, bác sĩ khuyến cáo nên tầm soát tim mạch (đo huyết áp, mỡ máu, điện tâm đồ) và xét nghiệm PSA kiểm tra tuyến tiền liệt mỗi 1-2 năm, vì đây là nhóm bệnh lý phổ biến ở độ tuổi này. Ngoài ra, anh nên duy trì khám sức khỏe tổng quát hàng năm, thực hiện chế độ ăn uống cân bằng, hạn chế muối, đường và tránh lạm dụng rượu bia, thuốc lá. Các khuyến nghị sức khỏe dành cho nữ giới không áp dụng trong trường hợp này.
```

### Person B — Chị Linh - Nữ, 45 tuổi
```
Ở tuổi 45, chị cần đặc biệt chú ý đến sức khỏe xương khớp vì mật độ xương giảm nhanh sau giai đoạn tiền mãn kinh. Chị nên bổ sung canxi và vitamin D, đồng thời thực hiện chụp nhũ ảnh định kỳ mỗi 1-2 năm để tầm soát ung thư vú.

Ngoài ra, để duy trì sức khỏe tổng quát, chị cần khám định kỳ mỗi năm một lần, thực hiện chế độ ăn cân bằng, hạn chế muối, đường và tránh sử dụng rượu bia, thuốc lá. Đối với nam giới, các bác sĩ khuyến cáo tầm soát tim mạch và tuyến tiền liệt định kỳ.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt A tập trung vào các khuyến nghị sức khỏe nam giới (tim mạch, tuyến tiền liệt) cho anh Hải, trong khi bản B tập trung vào sức khỏe nữ giới (xương khớp, ung thư vú) cho chị Linh. Cả hai bản tóm tắt đều thể hiện rõ sự cá nhân hóa theo giới tính đúng như kỳ vọng, với các nội dung không phù hợp được lược bỏ hoặc đẩy xuống phần phụ.


---
## CQ14: Quốc gia cư trú (cố định Việt Nam) có đóng vai trò ràng buộc cứng loại bỏ/chú thích nội dung không phù hợp ngữ cảnh Việt Nam trong tóm tắt không?
**Trường kiểm tra:** country (HARD, cố định)

**Loại test:** single_constraint

**Kỳ vọng (expected_effect):** Bản tóm tắt không trình bày chính sách thuế EU hoặc luật California như thể áp dụng trực tiếp cho người đọc tại Việt Nam; nội dung nước ngoài bị lược bỏ hoặc được chú thích rõ là không áp dụng trực tiếp.

### Person A — Trần Thùy Thảo - dùng làm đại diện chung
```
Các doanh nghiệp xuất khẩu Việt Nam đang phải chuẩn bị để thích ứng với Cơ chế điều chỉnh biên giới carbon (CBAM) của Liên minh châu Âu (EU). Lưu ý rằng các quy định này của EU không áp dụng trực tiếp tại Việt Nam, nhưng ảnh hưởng gián tiếp đến các doanh nghiệp có hoạt động xuất khẩu sang thị trường này.

Đối với hoạt động kinh doanh của bạn tại Đồng Nai, việc nắm bắt các yêu cầu về minh bạch chuỗi cung ứng và truy xuất nguồn gốc là rất quan trọng để nâng cao năng lực cạnh tranh. Các chuyên gia nhấn mạnh rằng thách thức lớn nhất không nằm ở thiết bị mà là năng lực quản lý dữ liệu và phối hợp giữa các bộ phận trong quy trình sản xuất. Dù chi phí xây dựng hệ thống đo lường và kiểm định là một rào cản đối với các doanh nghiệp vừa và nhỏ, đây cũng là cơ hội để cải thiện hiệu quả sử dụng năng lượng và giảm chi phí vận hành lâu dài.

Các hiệp hội ngành hàng hiện đang hỗ trợ doanh nghiệp thông qua các chương trình đào tạo và hướng dẫn kỹ thuật để chuẩn hóa dữ liệu phát thải. Các ngành hàng khác như thép, xi măng, nhôm, phân bón, dệt may và điện tử cũng đang chịu tác động hoặc chủ động triển khai các chương trình giảm phát thải tương tự.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt đã thực hiện tốt việc chú thích rõ ràng rằng quy định CBAM của EU không áp dụng trực tiếp tại Việt Nam mà chỉ có ảnh hưởng gián tiếp. Nội dung được trình bày khách quan, giúp người đọc tại Việt Nam hiểu đúng phạm vi tác động của chính sách nước ngoài đối với hoạt động kinh doanh nội địa.


---
## CQ15: Giá trị sống và thế giới quan (persona) có ảnh hưởng đến văn phong và ngữ điệu của bản tóm tắt không?
**Trường kiểm tra:** persona (GENERAL)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Hương súc tích, thiên về số liệu/kết luận rõ ràng; tóm tắt cho Bà Nga có thể nhẹ nhàng, gần gũi đời thường hơn.

### Person A — Đỗ Thanh Hương - quản lý, thực dụng, tham vọng
```
Kết quả khảo sát thị trường lao động quý II trên 2.400 người cho thấy bức tranh việc làm đang ổn định, nhưng áp lực về thu nhập và chi phí sinh hoạt vẫn là mối quan tâm hàng đầu. Tại TP. Hồ Chí Minh, người lao động đang đối mặt với thực tế: 68% nhận định chi phí sinh hoạt tăng nhanh hơn thu nhập, 54% thường xuyên làm thêm giờ. Về tâm thế, 61% hài lòng với công việc, 27% chưa hài lòng nhưng chưa nghỉ việc, và 12% đang chủ động tìm kiếm cơ hội mới.

Đối với các quản lý và doanh nghiệp, kỳ vọng của người lao động đã chuyển dịch: 72% ưu tiên cơ hội phát triển kỹ năng, 69% quan tâm phúc lợi, 64% chú trọng sức khỏe tinh thần và 58% mong muốn làm việc linh hoạt. Đặc biệt, mô hình làm việc kết hợp (hybrid) đang được đánh giá cao trong việc cân bằng giữa công việc và cuộc sống. Các khu vực khác như Hà Nội, Đà Nẵng, Cần Thơ và các tỉnh công nghiệp cũng ghi nhận những xu hướng tương tự về áp lực tài chính và nhu cầu phát triển bản thân.

Kết quả này khẳng định, đối với lực lượng lao động hiện nay, sự gắn bó với doanh nghiệp không còn chỉ dựa vào mức lương mà phụ thuộc vào chiến lược phát triển nghề nghiệp, sự linh hoạt trong vận hành và chất lượng môi trường làm việc. Đây là những tiêu chí cốt lõi mà các nhà quản lý cần nắm bắt để xây dựng chiến lược nhân sự và duy trì hiệu quả kinh doanh bền vững.
```

### Person B — Bà Nga - tận hưởng tuổi già, bình yên
```
Kết quả khảo sát về việc làm tại các thành phố lớn như Đà Nẵng và các nơi khác cho thấy nhiều người đang lo lắng vì chi phí sinh hoạt tăng nhanh hơn thu nhập. Nhiều người lao động hiện nay phải làm thêm giờ và đang tìm cách cân đối giữa công việc với cuộc sống gia đình.

Tại Đà Nẵng, tình hình việc làm đang dần ổn định. Các khu vực khác như Hà Nội hay TP. Hồ Chí Minh cũng ghi nhận những khó khăn tương tự về thu nhập và áp lực công việc.

Người lao động hiện nay không chỉ nhìn vào tiền lương mà còn rất coi trọng cơ hội học hỏi kỹ năng mới và mong muốn doanh nghiệp quan tâm hơn đến sức khỏe tinh thần của nhân viên. Nhiều người cũng muốn có cách làm việc linh hoạt hơn để đảm bảo cuộc sống. Những yếu tố này đang trở thành tiêu chí quan trọng để họ quyết định có gắn bó lâu dài với công việc hay không.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt A thể hiện rõ tư duy quản lý với việc sử dụng dày đặc số liệu thống kê và kết luận mang tính chiến lược, phù hợp với persona thực dụng. Bản tóm tắt B lược bỏ các con số, tập trung vào khía cạnh đời sống và cảm xúc, tạo cảm giác gần gũi, nhẹ nhàng đúng với kỳ vọng cho persona Bà Nga.


---
## CQ16: Nền tảng văn hóa có làm thay đổi mức độ cộng hưởng của người dùng với cùng một văn bản không?
**Trường kiểm tra:** cultural_background (GENERAL)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Bà Nga nhấn vào phong tục truyền thống (thắp hương, gói bánh chưng, đi chùa); tóm tắt cho Hiếu có thể giữ cả phần xu hướng hiện đại (du lịch nước ngoài, tiệc Tết hiện đại).

### Person A — Bà Nga - gắn bó văn hóa truyền thống Đà Nẵng (bài chòi, lễ hội)
```
Tết Nguyên Đán đang đến gần, không khí tại TP. Hồ Chí Minh rất nhộn nhịp với nhiều hoạt động mua sắm và trang trí đường phố.

Tại các chợ hoa và trung tâm thương mại, người dân đi mua sắm rất đông. Các mặt hàng như hoa mai, cúc, vạn thọ và thực phẩm thiết yếu được bày bán nhiều. Giá cả các loại hoa có tăng nhẹ do chi phí vận chuyển, nhưng giá thực phẩm như thịt, trứng, rau xanh vẫn ổn định nhờ nguồn cung dồi dào. Các dịch vụ như dọn dẹp nhà cửa hay chuyển phát nhanh có giá cao hơn ngày thường.

Giao thông tại các cửa ngõ thành phố đang rất đông đúc do nhiều người di chuyển về quê đón Tết. Các đơn vị vận tải đã tăng thêm chuyến để phục vụ bà con.

Các địa phương khác cũng đang tất bật chuẩn bị đón xuân theo cách riêng. Dù mỗi nhà có cách chuẩn bị khác nhau, nhưng không khí Tết vẫn rất rộn ràng và ấm áp.
```

### Person B — Dương Xuân Hiếu - sống chung cư hiện đại, pha trộn văn hóa
```
Cận Tết Nguyên Đán, thị trường tại TP. Hồ Chí Minh ghi nhận nhịp độ mua sắm sôi động với các chợ hoa truyền thống và hệ thống siêu thị tăng cường khuyến mại thực phẩm, quà biếu. Lưu lượng giao thông tại các cửa ngõ thành phố tăng mạnh, đòi hỏi lực lượng chức năng phải điều tiết liên tục để giảm ùn tắc. Về giá cả, các mặt hàng thiết yếu như thịt, trứng, rau xanh giữ mức ổn định nhờ nguồn cung dồi dào, trong khi giá hoa tươi và dịch vụ cận Tết có xu hướng tăng nhẹ. Các địa phương khác cũng đang hoàn tất công tác chuẩn bị đón xuân.

Đối với tỉnh Đồng Nai, các hoạt động chuẩn bị Tết đang diễn ra khẩn trương, tập trung vào việc đảm bảo nguồn cung hàng hóa thiết yếu và ổn định giá cả thị trường tại các khu dân cư, đáp ứng nhu cầu mua sắm truyền thống của người dân địa phương. Công tác trang trí đường phố và tổ chức các chương trình văn hóa nghệ thuật cũng đã được hoàn tất, tạo không khí đón xuân nhộn nhịp. Các gia đình tại đây vẫn duy trì nếp sống chuẩn bị mâm cỗ truyền thống và sum họp, phản ánh giá trị văn hóa đặc trưng của khu vực.
```

### Đánh giá LLM judge
- **Verdict:** FAIL

- **Confidence:** 0.9

- **Lý do:** Cả hai bản tóm tắt đều tập trung vào thông tin thị trường và giao thông chung chung, thiếu hẳn các yếu tố văn hóa đặc thù như phong tục truyền thống (cho Bà Nga) hay xu hướng hiện đại/quốc tế (cho Hiếu) như kỳ vọng. Sự khác biệt giữa hai văn bản chủ yếu nằm ở cách diễn đạt và thông tin địa phương (Đồng Nai), không phản ánh được sự cá nhân hóa theo nền tảng văn hóa của người dùng.


---
## CQ17: Khi trường HARD (zone, occupation) và trường SOFT (travel_persona) xung đột nhau, tóm tắt có ưu tiên theo HARD không?
**Trường kiểm tra:** zone + occupation (HARD) vs travel_persona (SOFT) - quan hệ uu_tien_hon

**Loại test:** single_constraint

**Kỳ vọng (expected_effect):** Tóm tắt giữ lại phần khám phá tự túc bằng xe máy, ẩm thực vỉa hè, chi phí hợp lý (phù hợp HARD: nông thôn, buôn bán) hơn là phần resort 5 sao/tour cao cấp (dù travel_persona SOFT có xu hướng quốc tế/cao cấp).

### Person A — Chị Mai - Nông Thôn/Buôn bán (HARD) nhưng travel_persona thích quốc tế (SOFT)
```
Hạ Long là lựa chọn lý tưởng cho chuyến đi ngắn ngày, chỉ cách Hà Nội hơn hai giờ di chuyển. Điểm đặc biệt là sự kết hợp giữa hai không gian đối lập: Bãi Cháy hiện đại với các khu nghỉ dưỡng, vui chơi và Hòn Gai bình dị, nơi lưu giữ những góc phố ẩm thực lâu đời cùng nhịp sống đời thường của người dân vùng biển.

Hai khu vực này chỉ cách nhau khoảng 10-15 phút di chuyển, rất thuận tiện để chị kết hợp tham quan, thưởng thức đặc sản và nghỉ dưỡng trong cùng một hành trình bằng xe cá nhân. Những con phố tại Hòn Gai tựa như một bức tranh quê mộc mạc, nơi hương vị biển cả hòa quyện trong từng nếp sống, hứa hẹn mang đến cho chị những trải nghiệm thư thái, đậm đà tình người sau những ngày buôn bán bận rộn. Các điểm đến khác ngoài Hạ Long chỉ là những lựa chọn tham khảo thêm.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt đã ưu tiên các yếu tố phù hợp với profile HARD (nông thôn, buôn bán) như trải nghiệm bình dị, ẩm thực vỉa hè, di chuyển bằng xe cá nhân và sự thư thái sau công việc. Nội dung hoàn toàn bỏ qua các gợi ý về du lịch quốc tế hoặc resort cao cấp, cho thấy hệ thống đã xử lý tốt sự xung đột giữa dữ liệu HARD và SOFT.


---
## CQ18: Sự kết hợp giữa nghề nghiệp và khu vực sống có tạo ra yêu cầu tóm tắt đặc thù không?
**Trường kiểm tra:** occupation x zone (HARD x SOFT combo)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Cùng nghề buôn bán nhưng tóm tắt cho Minh (nông thôn) giữ phần giá nông sản/kênh phân phối truyền thống; tóm tắt cho Thảo (đô thị) giữ phần thương mại điện tử/logistics.

### Person A — Minh - Buôn bán, Nông Thôn
```
Việc tiêu thụ nông sản hiện nay đang có sự kết hợp giữa cách làm truyền thống và công nghệ số.

Tại các vùng nông thôn như Hà Nội, kênh phân phối truyền thống qua thương lái, hợp tác xã và chợ đầu mối vẫn giữ vai trò chủ chốt. Cách này giúp bà con nông dân bán hàng nhanh ngay sau khi thu hoạch, giảm chi phí vận chuyển và không cần lo lắng về công nghệ phức tạp. Các hợp tác xã hiện nay còn hỗ trợ thêm việc phân loại, đóng gói và kết nối với doanh nghiệp để đầu ra ổn định hơn, giúp giảm tình trạng được mùa mất giá.

Ở các đô thị lớn, người dân đang chuyển dần sang mua sắm qua mạng và ứng dụng điện thoại.

Dù công nghệ số giúp mở rộng thị trường, nhưng việc áp dụng vẫn còn khó khăn do hạ tầng internet và logistics ở nông thôn chưa đồng bộ, cùng với hạn chế về kỹ năng số của người sản xuất. Vì vậy, mô hình kết hợp là hiệu quả nhất: thương lái và hợp tác xã tập trung thu gom, sơ chế tại chỗ, còn các sàn thương mại điện tử và đơn vị vận chuyển lo khâu phân phối đến người tiêu dùng. Sự phối hợp này giúp nâng cao giá trị nông sản và tăng thu nhập cho người làm kinh doanh như anh.
```

### Person B — Phạm Thị Thảo - Buôn bán, Đô Thị
```
Việc tiêu thụ nông sản hiện nay đang chuyển dịch theo mô hình kết hợp giữa kênh truyền thống và nền tảng số, tạo ra chuỗi cung ứng linh hoạt hơn.

Tại các đô thị lớn như TP.HCM, hành vi mua sắm đã thay đổi rõ rệt khi người tiêu dùng ưu tiên đặt hàng qua sàn thương mại điện tử và ứng dụng trực tuyến. Sự phát triển này đòi hỏi doanh nghiệp phải đầu tư mạnh vào hệ thống logistics (kho lạnh, trung tâm phân phối) và áp dụng công nghệ truy xuất nguồn gốc bằng mã QR để đảm bảo chất lượng sản phẩm. Các công cụ số hỗ trợ phân tích nhu cầu thị trường, dự báo sức mua và quản lý đơn hàng theo thời gian thực giúp tối ưu hóa lượng hàng tồn kho, giảm chi phí vận hành và nâng cao hiệu quả phân phối.

Đối với các vùng sản xuất nông nghiệp, mạng lưới truyền thống (thương lái, hợp tác xã, chợ đầu mối) vẫn giữ vai trò chủ chốt trong việc thu gom, sơ chế và đảm bảo đầu ra ổn định cho nông sản. Mô hình này đặc biệt phù hợp với các hộ sản xuất nhỏ lẻ nhờ quy trình giao dịch đơn giản và chi phí thấp. Các địa phương đang tiếp tục nâng cấp hệ thống chợ đầu mối và trung tâm thu gom để nâng cao năng lực bảo quản.

Dù thương mại điện tử mở ra cơ hội tiếp cận khách hàng toàn quốc, việc ứng dụng vẫn gặp thách thức về kỹ năng số của nông dân và hạ tầng logistics tại nông thôn. Do đó, sự kết hợp giữa kênh truyền thống (thu gom, sơ chế) và nền tảng số (phân phối đến đô thị) được xem là hướng đi tối ưu để nâng cao giá trị nông sản và tăng thu nhập cho người sản xuất. Các hoạt động tại các vùng nông thôn khác cũng đang được đẩy mạnh theo hướng tương tự.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 0.95

- **Lý do:** Bản tóm tắt A tập trung sâu vào vai trò của thương lái, hợp tác xã và các khó khăn về hạ tầng tại nông thôn, phù hợp với nhu cầu của Minh. Bản tóm tắt B nhấn mạnh vào thương mại điện tử, logistics, kho lạnh và phân tích dữ liệu thị trường, phản ánh đúng trọng tâm kinh doanh tại đô thị của Thảo. Sự phân hóa nội dung giữa hai bản tóm tắt hoàn toàn khớp với kỳ vọng về cá nhân hóa theo khu vực sống.


---
## CQ19: Mức độ tham gia nghệ thuật (arts_persona) có ảnh hưởng đến khả năng tiếp nhận văn phong giàu hình ảnh/ẩn dụ trong bản tóm tắt không?
**Trường kiểm tra:** arts_persona (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Oanh có thể dùng ngôn ngữ giàu hình ảnh/ẩn dụ hơn khi mô tả triển lãm; tóm tắt cho Dung trực tiếp, tường minh hơn.

### Person A — Oanh - đam mê hội họa, thường xuyên dự triển lãm (arts cao)
```
Triển lãm hội họa "Sắc màu và Ký ức" tại Bảo tàng Mỹ thuật Việt Nam hiện đang là điểm hẹn văn hóa đầy cảm hứng, quy tụ 82 tác phẩm của 27 họa sĩ. Không gian trưng bày được phân bổ khoa học theo từng chủ đề, dẫn dắt người xem đi từ những gam màu tươi sáng của nhịp sống đô thị chuyển động đến những mảng màu trầm mặc, lắng đọng của ký ức và phong cảnh làng quê.

Đối với một người nghiên cứu như tôi, triển lãm không chỉ là sự thưởng lãm đơn thuần mà là một lát cắt thực tế về đời sống đương đại. Sự kết hợp giữa các họa sĩ dày dạn kinh nghiệm và những gương mặt trẻ tạo nên một đối thoại nghệ thuật đa chiều, nơi mỗi bức tranh trở thành một văn bản tự sự, khơi gợi những tầng cảm xúc sâu sắc về trải nghiệm cá nhân. Việc quan sát cách các tác giả sử dụng ngôn ngữ hội họa để khắc họa những điều bình dị thường nhật là một bài học quý giá về khả năng quan sát và tư duy hình ảnh.

Sự kiện còn là một không gian học thuật mở, nơi các buổi giao lưu giữa họa sĩ và công chúng được tổ chức nhằm thúc đẩy sự kết nối và lan tỏa giá trị văn hóa. Đây thực sự là một điểm đến lý tưởng để chiêm nghiệm về sự giao thoa giữa truyền thống và hiện đại, đồng thời tìm kiếm những chất liệu mới cho các dự án nghiên cứu về văn hóa và nghệ thuật. Các hoạt động triển lãm tại các địa phương khác cũng đang diễn ra với quy mô tương tự.
```

### Person B — Anh Tuấn - thợ xây dựng, ít quan tâm nghệ thuật (arts thấp, dùng ngôn ngữ dè dặt 'có thể thích')
```
Triển lãm tranh "Sắc màu và Ký ức" đang diễn ra tại Bảo tàng Mỹ thuật Việt Nam ở Hà Nội. Đây là nơi trưng bày nhiều tác phẩm về đời sống, con người và cảnh vật.

Không gian triển lãm được sắp xếp ngăn nắp theo từng chủ đề, giúp người xem dễ dàng quan sát. Các bức tranh khắc họa cảnh làng quê yên bình, nhịp sống phố thị và những khoảnh khắc đời thường rất gần gũi. Sự kiện này là dịp để mọi người, từ các gia đình đến người cao tuổi, có thể đến tham quan, thư giãn và tìm thấy những câu chuyện quen thuộc trong cuộc sống.

Ngoài ra, triển lãm còn có các hoạt động giao lưu với họa sĩ và chương trình hướng dẫn cho học sinh. Sự kiện kéo dài trong ba tuần, là một điểm đến văn hóa ý nghĩa tại Thủ đô. Các tác phẩm về phong cảnh và đời sống ở những vùng miền khác cũng được giới thiệu ngắn gọn tại đây.
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt A sử dụng ngôn ngữ giàu hình ảnh và ẩn dụ như 'lát cắt thực tế', 'đối thoại nghệ thuật đa chiều', 'văn bản tự sự', phù hợp với người có mức độ tham gia nghệ thuật cao. Bản tóm tắt B sử dụng ngôn ngữ trực tiếp, tường minh, tập trung vào thông tin thực tế và sự tiện lợi, phản ánh đúng kỳ vọng cho người dùng có mức độ quan tâm nghệ thuật thấp.


---
## CQ20: Đam mê và sở thích cá nhân có làm tăng ngưỡng chấp nhận độ dài tóm tắt của người dùng trong chủ đề họ yêu thích không?
**Trường kiểm tra:** hobbies_and_interests (SOFT)

**Loại test:** pair_comparison

**Kỳ vọng (expected_effect):** Tóm tắt cho Phương Hạnh (B) có thể dài hơn, giữ lại nhiều chi tiết về công thức truyền thống cầu kỳ; tóm tắt cho Anh Thanh (A) ngắn gọn hơn, chỉ giữ phần công thức nhanh gọn cơ bản.

### Person A — Anh Thanh - sở thích đa dạng (lễ hội, cờ, làm vườn), không gắn bó sâu với ẩm thực
```
Hiện nay, ẩm thực Việt đang có hai xu hướng song hành: giữ cách nấu truyền thống và cách nấu nhanh để tiện lợi.

Với món bún bò Huế, cách nấu truyền thống đòi hỏi sự tỉ mỉ: xương phải được làm sạch, ninh liên tục từ 8 đến 10 tiếng. Người nấu phải thường xuyên hớt bọt, rang hành gừng để tạo mùi thơm, và lọc mắm ruốc kỹ càng để vị ngọt được tự nhiên. Chất lượng món ăn phụ thuộc vào việc chọn xương ống, xương gân, đập dập sả để tiết tinh dầu và tự làm sa tế từ ớt khô, dầu điều. Các nghệ nhân cho rằng, việc kiểm soát lửa và các công đoạn thủ công này là kinh nghiệm quý báu cần được gìn giữ, vì rút gọn quá nhiều sẽ làm mất đi hương vị đặc trưng của món ăn.

Ngược lại, các phiên bản nấu nhanh sử dụng nồi áp suất, gia vị chế biến sẵn và nguyên liệu sơ chế để tiết kiệm thời gian cho người bận rộn.

Các món ăn ở miền Trung như bún bò Huế được bàn luận nhiều tại lễ hội, còn các vùng miền khác chỉ được nhắc đến như một phần của sự đa dạng văn hóa. Việc chọn cách nấu nào là tùy vào thời gian và mục đích của mỗi người, nhưng những giá trị truyền thống vẫn là nền tảng quan trọng để bảo tồn văn hóa.
```

### Person B — Phương Hạnh - đam mê ẩm thực Hải Phòng cụ thể, thường tự nấu ăn tại nhà
```
Ẩm thực Việt hiện nay đang là sự giao thoa giữa việc gìn giữ những giá trị truyền thống quý báu và nhu cầu tối ưu hóa thời gian của nhịp sống hiện đại.

Đối với những món ăn đòi hỏi sự tỉ mỉ như bún bò Huế, các nghệ nhân nhấn mạnh rằng linh hồn của món ăn nằm ở sự kiên nhẫn. Để có nồi nước dùng trong veo, ngọt thanh và dậy mùi thơm đặc trưng, người nấu phải dành từ 8 đến 10 giờ ninh xương, tỉ mẩn hớt bọt, rang hành gừng và khéo léo hòa quyện mắm ruốc theo từng giai đoạn. Những kỹ thuật này không chỉ là bí quyết nấu nướng, mà còn là di sản kinh nghiệm được truyền lại qua nhiều thế hệ, giúp món ăn đạt đến độ hoàn hảo về màu sắc và hương vị tự nhiên.

Ngược lại, để phù hợp với cuộc sống bận rộn, nhiều người trẻ lựa chọn các phiên bản rút gọn. Thay vì dành cả ngày trong bếp, việc sử dụng nồi áp suất giúp rút ngắn thời gian ninh xương xuống còn khoảng một giờ. Các nguyên liệu như sa tế, gia vị hay nước dùng cô đặc được chuẩn bị sẵn giúp việc nấu nướng trở nên nhanh chóng, đáp ứng nhu cầu bữa ăn hàng ngày mà vẫn giữ được khoảng 80-90% hương vị truyền thống.

Tại các lễ hội ẩm thực, bên cạnh những buổi trình diễn kỹ thuật nấu nướng công phu, các khu vực hướng dẫn mẹo nấu nhanh cũng thu hút đông đảo người tham gia. Các chuyên gia cho rằng, hai xu hướng này không hề đối lập. Việc lựa chọn cách nấu truyền thống hay hiện đại phụ thuộc vào quỹ thời gian và mong muốn trải nghiệm của mỗi người.

*Lưu ý: Các xu hướng ẩm thực tại các vùng miền khác ngoài Hải Phòng chỉ được đề cập ngắn gọn trong bối cảnh chung của lễ hội.*
```

### Đánh giá LLM judge
- **Verdict:** PASS

- **Confidence:** 1.0

- **Lý do:** Bản tóm tắt B dài hơn và tập trung sâu vào các kỹ thuật nấu nướng truyền thống (như cách tạo nước dùng trong, sự kiên nhẫn của nghệ nhân) so với bản A. Bản A tập trung vào sự tiện lợi và các thông tin chung, trong khi bản B cung cấp chi tiết chuyên sâu phù hợp với người đam mê ẩm thực, phản ánh đúng kỳ vọng về sự cá nhân hóa.
