Title: Detailed Analysis of CloudDon, Cloud Data Breach of Korea e-commerce company

URL Source: https://medium.com/s2wblog/detailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d

Published Time: 2023-05-22T07:59:41Z

Markdown Content:
# Detailed Analysis of CloudDon, Cloud Data Breach of Korea e-commerce company | by S2W | S2W BLOG | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[## S2W BLOG](https://medium.com/s2wblog?source=post_page---publication_nav-30a8766b5c42-948c3a5df90d---------------------------------------)

·

[![Image 2: S2W BLOG](https://miro.medium.com/v2/resize:fill:38:38/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---post_publication_sidebar-30a8766b5c42-948c3a5df90d---------------------------------------)
S2W is a big data intelligence company specialized in the Dark Web, Deepweb and any other covert channels.

# **Detailed Analysis of CloudDon, Cloud Data Breach of Korea e-commerce company**

[![Image 3: S2W](https://miro.medium.com/v2/resize:fill:32:32/1*1DiWQYMzvUSAzrLJQX1z6g.png)](https://medium.com/@s2w?source=post_page---byline--948c3a5df90d---------------------------------------)

[S2W](https://medium.com/@s2w?source=post_page---byline--948c3a5df90d---------------------------------------)

9 min read

·

May 22, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fs2wblog%2F948c3a5df90d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&user=S2W&userId=b408bb1e7c46&source=---header_actions--948c3a5df90d---------------------clap_footer------------------)

--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F948c3a5df90d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---header_actions--948c3a5df90d---------------------bookmark_footer------------------)

Share

**Author**: S2W TALON

## Get S2W’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

**Last Modified** : May 22, 2023

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*ivaSvmsUfoxoDeZw10ealA.png)

Photo by [C Dustin](https://unsplash.com/@dianamia?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/K-Iog-Bqf8E?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## Executive Summary

*   2023년 1월 경 Breached 포럼의 **donjuji** 유저가 **온라인 쇼핑몰 A사의 회원 정보** 판매 게시글을 업로드하였고, 정확한 유출 경위 파악을 위해 피해기업의 침해사고 분석을 진행함
*   S2W Talon은 공격자 ‘Donjuji’의 클라우드 인프라 공격인 점에서 Operation name을 **“CloudDon”** 으로 명명
*   분석 결과, A사 개발 서버의 **환경변수 페이지가 외부에 노출**되어 **AWS IAM 크리덴셜 등 클라우드 인증 정보가 노출**된 것을 식별함
*   개발 서버의 **Middleware**내 **MiniProfiler**라이브러리로 인해 **‘pp=env’ 파라미터**가 활성화 되어 있었으며 이로 인해 IAM User 크리덴셜, NAVER, KAKAO, PAYCO 등에 접근 가능한 다수의 인증정보가 포함된 환경변수가 노출됨
*   **donjuji**는 유출된 회원정보 판매 게시글을 작성하기 2시간 전, 자신에 대한 scam 신고에 대응하기 위해 증빙 파일을 업로드하는 과정에서 **온라인 쇼핑몰 A사의**데이터 출처인 **S3 URL**을 사용하였음을 확인함
*   노출된 IAM User 크리덴셜의 account-id와 donjuji가 업로드한 S3 URL 내 **account-id가 일치함**을 확인 후 노출된 환경변수 내 크리덴셜이 **최초 침투 경로**임을 확인함
*   Donjuji는 AWS IAM 크리덴셜에 S3 접근 권한이 있는 것을 확인 후 **S3 Browser** 도구를 이용하여 내부 버킷 접근 후 데이터를 탈취함
*   S3 버킷 내부에는 AWS Glue를 이용하여 RDS 내 민감 정보들이 별도 암호화 없이 저장되고 있었으며, 유출된 데이터 외 추가적인 IAM 크리덴셜이 하드코딩 되어있는 스크립트 또한 존재하였음
*   CloudTrail 로그 추가 분석 결과 공격자의 접속 IP를 식별하였으며, 해당 침해사고 외에도 피해기업 내 cognito-idp접근, security-group 백도어 설치 시도 등이 있었음을 확인함

## Detailed Analysis

### **1. 침해사고 전체 흐름도**

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*amp3YYtjTVhv3K4NDif22w.png)

그림 1. 전체 침해사고 흐름도

### 2. 침해사고 상세 분석 과정

### 2.1. Breached 포럼에 업로드된 A사 유출 데이터 탐지

*   (2023–01–05) Breached 포럼에서 donjuji 유저가 “xxxx.co[.]kr|1.2m users|mysql hash” 제목의 게시글을 업로드함
*   국내 쇼핑몰 A 기업의 회원 정보를 판매하였으며 유출된 항목은 이메일 주소와 암호화된 비밀번호로, 총 1,183,323건의 회원들의 계정 정보가 유출됨

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*DQPI_lcUKpAJNJqlO9j-RA.png)

그림 2. Breached 포럼 donjuji 유저 판매 게시글

*   S2W 위협 연구 센터 Talon은 자사 모니터링 시스템을 통해 **온라인 쇼핑몰 A사의 정보유출**을 인지하였으며, 정확한 유출 경위 파악을 위해 침해사고 분석을 진행함

### 2.2. 공격표면 상세 분석

*   A사의 자산범위 식별 후 침해사고가 발생 가능한 **공격표면** 및 **유출계정**에 대한 데이터베이스 탐색을 진행함
*   공격표면 탐색 과정에서 A사 개발서버의 일부 페이지가 노출되어 구글 캐시에 의해 저장된 페이지가 검색이 가능한 상태임을 확인

Press enter or click to view image in full size

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*1ePzXOZHKA0I25yt_5Njug.png)

그림 3. 공격표면 탐색 과정에서 캐시된 웹페이지 확인

*   캐시된 페이지는 개발서버의 환경변수 페이지로 하드코딩된 **IAM User 크리덴셜**, NAVER, KAKAO, FACEBOOK 등에 접근 가능한 **다수의 인증정보** 환경변수가 노출됨

Press enter or click to view image in full size

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*zDG8L2rKgvAUrXMvhxyyZw.png)

그림 4. 페이지 내 노출된 환경변수 및 하드코딩된 크리덴셜

*   페이지 노출은 **인프라 내 개발서버 외부 노출** 및 Ruby기반 Middleware의 라이브러리인 **Mini-profiler의 잘못된 구성**으로 인한 pp 파라미터 활성화가 주요 원인이며 이 중 **pp=env**값인 환경변수 페이지가 노출 기간 동안 구글에 캐시됨 (분석 참조 [**LINK**](https://towardsdatascience.com/leaking-secrets-in-web-applications-46357831b8ed))

Press enter or click to view image in full size

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*ZmxQXMVeXuyBVQN4hJAc_Q.png)

그림 5. mini-profiler pp 파라미터 옵션 목록

*   노출된 크리덴셜을 통해 **account-id**를 식별하였으며, donjuji가 포럼 활동 과정에서 scam 신고 대응을 위해 사용한 S3 URL 주소 내 **account-id**와 대조 과정을 거침
*   이 과정 에서 동일한 account-id임을 확인하였으며 donjuji가 포럼활동에서 해당 크리덴셜 및 AWS서비스를 악용함을 확인함

Press enter or click to view image in full size

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*jAXcZUy0HCB8LJGtjSXKtA.png)

그림 6. 노출된 IAM 크리덴셜 account-id 식별

Press enter or click to view image in full size

![Image 11](https://miro.medium.com/v2/resize:fit:700/1*oRbHtjWMmToRQJRNRs4LYA.png)

그림 7. donjuji의 신고 대응 게시글 내 S3 URL

### 2.3. IAM 사용 이력 및 인프라 취약점 분석

*   Cloudtrail 로그를 통해 2022년 12월 경부터 탈취한 크리덴셜을 이용하여 여러 서비스에 접근 시도하는**IAM Enumeration**작업을 하였음을 확인함

Press enter or click to view image in full size

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*QGmy4YVHU1cCCT4U2PAucA.png)

그림 8. Cloudtrail 로그 통해 IAM enumeration 확인

*   해당 작업을 통해 donjuji는 크리덴셜 내 부여된 권한 및 접근 가능 서비스를 식별하였을 것으로 추정됨
*   식별된 정보를 바탕으로 2023년 1월경 **S3 Browser**를 사용하여 S3 Tran-sfer Acceleration 옵션 활성화, 버킷 목록 탐색 및 버킷 내 데이터 탈취를 진행함

Press enter or click to view image in full size

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*wtFINk8Px8KZFEyTTT87eg.png)

그림 9. Cloudtrail 로그 내 S3 Browser 사용한 접근 기록

*   Talon팀 자체 AWS 점검 스크립트 진단을 진행하였으며 크리덴셜에 적용된 권한을 기준으로 **54 항목** 중 **27 항목** 미준수가 확인됨
*   미준수 항목 중 주요 항목은 다음과 같음

> _1. IAM 크리덴셜 권한 과부여(S3FullAccess, RDSFullAcess 등)_
> 
> 
> _2. IAM 크리덴셜 IP range 및 MFA 이용한 세션 토큰 미적용_
> 
> 
> _3. S3 버킷 KMS(Key Management System) 이용한 암호화 미적용_
> 
> 
> _4. S3 버킷 Object Lock 미적용_

*   또한 분석 과정에서 버킷 내 [그림 11]과 같은 스크립트를 확인하였으며 다음과 같은 추가 문제 사항들이 식별됨

> 1. 스크립트 내 추가적인**IAM 크리덴셜이 하드코딩**되어있음
> 
> 
> **2. AWS Glue** 리소스를 이용하여 **RDS 내 민감정보 데이터**를 크롤링한 이후 **특정 S3 버킷**에 저장
> 
> 
> 3. 크롤링된 버킷 내 민감정보 데이터는 별도의 **암호화가 되지 않음**

*   스크립트 분석을 통해 기존에 노출된 크리덴셜을 이용하여 추가 인프라 접근 진행을 한 것이 아닌 **S3 버킷 내 데이터를 탈취하였음**을 확인
*   Cloudtrail 추가분석을 진행하였으나 스크립트 내 하드코딩된 추가 크리덴셜에 대해서는 접근 및 사용기록이 확인되지 않음

Press enter or click to view image in full size

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*DOF6DaCJor_K07qR2HTqHA.png)

그림 10. Talon AWS 점검 스크립트 일부 결과

![Image 15](https://miro.medium.com/v2/resize:fit:580/1*_jVLXsczizbOkUhX_qaZEg.png)

그림 11. 버킷내 확인된 AWS Glue 스크립트

### 2.4. Cloudtrail 및 Cloudwatch 로그 분석 결과

*   Donjuji 유저는 노출된 IAM 크리덴셜(S3FullAccess, RDSFullAccess)과 버킷 정보를 사용하여 S3 Browser 프로그램을 통해 접근 가능한 데이터를 탐색 후 민감정보를 탈취
*   이후 2023년 1월경 포럼글 작성을 위하여 추가적으로 S3 접근 및 사용하였으며 이 과정에서 2개의 IP를 사용하여 접근하였음을 확인

Press enter or click to view image in full size

![Image 16](https://miro.medium.com/v2/resize:fit:700/1*U6pkP27V1ynYMnseoxF9ug.png)

그림 12. donjuji 사용 IP 목록

*   Donjuji 유저와의 명확한 연관성은 식별되지 않았으나 2022년 12월 경, 2023년 1월 경 노출된 크리덴셜을 이용하여 **cognito-idp 서비스**에 접근 시도한 2개의 IP를 확인
*   또한 2022년 11월경 동일한 노출 크리덴셜을 이용하여 **security-group 백도어** 설치를 시도한 1개의 IP를 확인 (분석 참조 [**LINK**](https://www.reddit.com/r/aws/comments/umkjln/ses_email_service_ive_been_hacked/))

Press enter or click to view image in full size

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*EFVxv-VY036fQjwTeCyQ-A.png)

그림 13. 추가 공격 시도 IP 목록

Press enter or click to view image in full size

![Image 18](https://miro.medium.com/v2/resize:fit:700/1*UmVqcbQ8UkXzrVimAfCROg.png)

그림 14. security-group 백도어 설치 시도 이력

### 2.5. 클라우드 보안 위협 요소 제거 및 인프라 관리 방안

Press enter or click to view image in full size

![Image 19](https://miro.medium.com/v2/resize:fit:700/1*NDuFptuVEHRP8ZELyW5TLQ.png)

## Conclusion

*   전세계적으로 클라우드 서비스를 통해 서버와 데이터 베이스 인프라를 구축하는 방식이 보편화되고 있으며, 이에 따라 공격자들이 DDW에서 클라우드 인프라 관리 계정 및 탈취한 민감 정보를 판매하는 행위 또한 증가하고 있음
*   해당 침해사고는 다음과 같은 주요 원인에 의해 공격자의 접근 허용 및 데이터 탈취가 발생함

> 자산 식별 미흡 및 misconfiguration 으로 인한 **Attack Surface**발생
> 
> 
> IAM 크리덴셜 Access Control, MFA 미적용으로 인한 **Account TakeOver**
> 
> 
> Object Storage 내 민감정보 저장 및 **Encryption 미적용**

*   공격자는 Attack Surface에 노출된 구성 정보 및 주요 자산을 적극적으로 활용하고 있으므로 기업 자산에 대한 위협 요소에 대해 상시 모니터링이 필요함
*   또한 클라우드 자산 보호를 위하여 인프라 내 **자산 식별** 및 중요도 분류, **외부 접근 제어**, **최소한의 IAM 및 MFA 적용**, **민감정보 암호화**등의 조치를 권장함

## Appendix.A: IoCs

Press enter or click to view image in full size

![Image 20](https://miro.medium.com/v2/resize:fit:700/1*rKzgPNrR1t-8ZeOvFVJUHg.png)

> **71.202.232.31 (California, USA)**
> 
> 
> **157.97.121.215 (New Jersey, USA)**
> 
> 
> **159.203.143.99 (New Jersey, USA)**
> 
> 
> **167.172.20.150 (New Jersey, USA)**
> 
> 
> **182.3.41.124 (Jarkarta, Indonesia)**

Press enter or click to view image in full size

![Image 21](https://miro.medium.com/v2/resize:fit:700/0*cJYJnU_ZBly6e5T2.png)

Homepage: [https://s2w.inc](https://s2w.inc/)

Facebook: [https://www.facebook.com/S2WLAB](https://www.facebook.com/S2WLAB/)

Twitter: [https://twitter.com/S2W_Official](https://twitter.com/S2W_Official)

[Threat Intelligence](https://medium.com/tag/threat-intelligence?source=post_page-----948c3a5df90d---------------------------------------)

[Data Breach](https://medium.com/tag/data-breach?source=post_page-----948c3a5df90d---------------------------------------)

[Darkweb](https://medium.com/tag/darkweb?source=post_page-----948c3a5df90d---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----948c3a5df90d---------------------------------------)

[Cloud Security](https://medium.com/tag/cloud-security?source=post_page-----948c3a5df90d---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fs2wblog%2F948c3a5df90d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&user=S2W&userId=b408bb1e7c46&source=---footer_actions--948c3a5df90d---------------------clap_footer------------------)

--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fs2wblog%2F948c3a5df90d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&user=S2W&userId=b408bb1e7c46&source=---footer_actions--948c3a5df90d---------------------clap_footer------------------)

--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F948c3a5df90d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---footer_actions--948c3a5df90d---------------------bookmark_footer------------------)

[![Image 22: S2W BLOG](https://miro.medium.com/v2/resize:fill:48:48/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---post_publication_info--948c3a5df90d---------------------------------------)

[![Image 23: S2W BLOG](https://miro.medium.com/v2/resize:fill:64:64/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---post_publication_info--948c3a5df90d---------------------------------------)

[## Published in S2W BLOG](https://medium.com/s2wblog?source=post_page---post_publication_info--948c3a5df90d---------------------------------------)

[279 followers](https://medium.com/s2wblog/followers?source=post_page---post_publication_info--948c3a5df90d---------------------------------------)

·[Last published Feb 12, 2026](https://medium.com/s2wblog/inside-the-ecosystem-operations-dragonforce-11048db4cbb0?source=post_page---post_publication_info--948c3a5df90d---------------------------------------)

S2W is a big data intelligence company specialized in the Dark Web, Deepweb and any other covert channels.

[![Image 24: S2W](https://miro.medium.com/v2/resize:fill:48:48/1*1DiWQYMzvUSAzrLJQX1z6g.png)](https://medium.com/@s2w?source=post_page---post_author_info--948c3a5df90d---------------------------------------)

[![Image 25: S2W](https://miro.medium.com/v2/resize:fill:64:64/1*1DiWQYMzvUSAzrLJQX1z6g.png)](https://medium.com/@s2w?source=post_page---post_author_info--948c3a5df90d---------------------------------------)

[## Written by S2W](https://medium.com/@s2w?source=post_page---post_author_info--948c3a5df90d---------------------------------------)

[766 followers](https://medium.com/@s2w/followers?source=post_page---post_author_info--948c3a5df90d---------------------------------------)

·[22 following](https://medium.com/@s2w/following?source=post_page---post_author_info--948c3a5df90d---------------------------------------)

S2W is specializing in cybersecurity data analysis for cyber threat intelligence.

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--948c3a5df90d---------------------------------------)

![Image 26](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---post_responses--948c3a5df90d---------------------respond_sidebar------------------)

Cancel

Respond

## More from S2W and S2W BLOG

![Image 27: Detailed Analysis of LockBit 5.0](https://miro.medium.com/v2/resize:fit:679/format:webp/1*f1NG8LqSD1UbNbFVmVgAzQ.png)

[![Image 28: S2W BLOG](https://miro.medium.com/v2/resize:fill:20:20/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----0---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

In

[S2W BLOG](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----0---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

by

[S2W](https://medium.com/@s2w?source=post_page---author_recirc--948c3a5df90d----0---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[## Detailed Analysis of LockBit 5.0 ### Author: S2W TALON (HuiSeong Yang)](https://medium.com/s2wblog/detailed-analysis-of-lockbit-5-0-de92c03441f8?source=post_page---author_recirc--948c3a5df90d----0---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

Jan 19

[](https://medium.com/s2wblog/detailed-analysis-of-lockbit-5-0-de92c03441f8?source=post_page---author_recirc--948c3a5df90d----0---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---author_recirc--948c3a5df90d----0-----------------explicit_signal----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fde92c03441f8&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-lockbit-5-0-de92c03441f8&source=---author_recirc--948c3a5df90d----0-----------------bookmark_preview----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

![Image 29: Detailed Analysis of DragonForce Ransomware](https://miro.medium.com/v2/resize:fit:679/format:webp/1*a7zyd7ceV8ovfNwvcATwUg.png)

[![Image 30: S2W BLOG](https://miro.medium.com/v2/resize:fill:20:20/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----1---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

In

[S2W BLOG](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----1---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

by

[S2W](https://medium.com/@s2w?source=post_page---author_recirc--948c3a5df90d----1---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[## Detailed Analysis of DragonForce Ransomware ### Author: S2W TALON (Byeongyeol An)](https://medium.com/s2wblog/detailed-analysis-of-dragonforce-ransomware-25d1a91a4509?source=post_page---author_recirc--948c3a5df90d----1---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

Jan 14

[](https://medium.com/s2wblog/detailed-analysis-of-dragonforce-ransomware-25d1a91a4509?source=post_page---author_recirc--948c3a5df90d----1---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---author_recirc--948c3a5df90d----1-----------------explicit_signal----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F25d1a91a4509&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-dragonforce-ransomware-25d1a91a4509&source=---author_recirc--948c3a5df90d----1-----------------bookmark_preview----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

![Image 31: Unmasking CVE-2024-38178: The Silent Threat of Windows Scripting Engine](https://miro.medium.com/v2/resize:fit:679/format:webp/1*buHo6ydCb774gg64BFVRog.png)

[![Image 32: S2W BLOG](https://miro.medium.com/v2/resize:fill:20:20/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----2---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

In

[S2W BLOG](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----2---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

by

[S2W](https://medium.com/@s2w?source=post_page---author_recirc--948c3a5df90d----2---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[## Unmasking CVE-2024-38178: The Silent Threat of Windows Scripting Engine ### Author: Hosu Choi, Minyeop Choi | S2W Talon](https://medium.com/s2wblog/unmasking-cve-2024-38178-the-silent-threat-of-windows-scripting-engine-91ad954dbf83?source=post_page---author_recirc--948c3a5df90d----2---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

Oct 16, 2024

[](https://medium.com/s2wblog/unmasking-cve-2024-38178-the-silent-threat-of-windows-scripting-engine-91ad954dbf83?source=post_page---author_recirc--948c3a5df90d----2---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---author_recirc--948c3a5df90d----2-----------------explicit_signal----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F91ad954dbf83&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Funmasking-cve-2024-38178-the-silent-threat-of-windows-scripting-engine-91ad954dbf83&source=---author_recirc--948c3a5df90d----2-----------------bookmark_preview----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

![Image 33: Detailed Analysis of AiLock Ransomware](https://miro.medium.com/v2/resize:fit:679/format:webp/1*jtjKGtFHfT6pCcOWrokJSw.png)

[![Image 34: S2W BLOG](https://miro.medium.com/v2/resize:fill:20:20/1*3vCxewFUeWWkQ-O5X558rQ.jpeg)](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----3---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

In

[S2W BLOG](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d----3---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

by

[S2W](https://medium.com/@s2w?source=post_page---author_recirc--948c3a5df90d----3---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[## Detailed Analysis of AiLock Ransomware ### Author: S2W TALON (Huiseong Yang)](https://medium.com/s2wblog/detailed-analysis-of-ailock-ransomware-1d3263beff15?source=post_page---author_recirc--948c3a5df90d----3---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

Aug 13, 2025

[](https://medium.com/s2wblog/detailed-analysis-of-ailock-ransomware-1d3263beff15?source=post_page---author_recirc--948c3a5df90d----3---------------------26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---author_recirc--948c3a5df90d----3-----------------explicit_signal----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d3263beff15&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-ailock-ransomware-1d3263beff15&source=---author_recirc--948c3a5df90d----3-----------------bookmark_preview----26dd3f27_4c1f_4a9d_a14c_6e9be8aafc2e--------------)

[See all from S2W](https://medium.com/@s2w?source=post_page---author_recirc--948c3a5df90d---------------------------------------)

[See all from S2W BLOG](https://medium.com/s2wblog?source=post_page---author_recirc--948c3a5df90d---------------------------------------)

## Recommended from Medium

![Image 35: Hacking Microsoft IIS: From Recon to Advanced Fuzzing](https://miro.medium.com/v2/resize:fit:679/format:webp/1*YpG66o4sP1IYfsZCgVgv7Q.jpeg)

[![Image 36: InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:20:20/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://medium.com/bugbountywriteup?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

In

[InfoSec Write-ups](https://medium.com/bugbountywriteup?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

by

[𝙇𝙤𝙨𝙩𝙨𝙚𝙘](https://medium.com/@lostsec?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## Hacking Microsoft IIS: From Recon to Advanced Fuzzing ### A hands-on guide covering IIS recon, shortname testing and advanced fuzzing used in real bug bounty hunting.](https://medium.com/bugbountywriteup/hacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Feb 21

[8](https://medium.com/bugbountywriteup/hacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----0-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F013989524fe2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-microsoft-iis-from-recon-to-advanced-fuzzing-013989524fe2&source=---read_next_recirc--948c3a5df90d----0-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

![Image 37: Hexstrike AI MCP Orchestration Cursor Gemini OpenAI Codex llama](https://miro.medium.com/v2/resize:fit:679/format:webp/1*xVOL0ffrnBvXhmCNie1Tlg.png)

[![Image 38: AISecHub](https://miro.medium.com/v2/resize:fill:20:20/1*Undxeu1xXpuRdsv6Ic8q-A.jpeg)](https://medium.com/ai-security-hub?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

In

[AISecHub](https://medium.com/ai-security-hub?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

by

[Andrey Pautov](https://medium.com/@1200km?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## HexStrike AI: Install, Configure, and Run MCP with Gemini, OpenAI, Cursor, Llama ### A practical, end-to-end guide to installing HexStrike AI, wiring it as an MCP server, and running real tool-driven workflows (recon →…](https://medium.com/ai-security-hub/hexstrike-on-kali-linux-2025-4-a-comprehensive-guide-85a0e5752949?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Dec 18, 2025

[](https://medium.com/ai-security-hub/hexstrike-on-kali-linux-2025-4-a-comprehensive-guide-85a0e5752949?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----1-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F85a0e5752949&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fai-security-hub%2Fhexstrike-on-kali-linux-2025-4-a-comprehensive-guide-85a0e5752949&source=---read_next_recirc--948c3a5df90d----1-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

![Image 39: If You Understand These 5 AI Terms, You’re Ahead of 90% of People](https://miro.medium.com/v2/resize:fit:679/format:webp/1*qbVrf-wO9PYtthAj6E4RYQ.png)

[![Image 40: Towards AI](https://miro.medium.com/v2/resize:fill:20:20/1*JyIThO-cLjlChQLb6kSlVQ.png)](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

In

[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

by

[Shreyas Naphad](https://medium.com/@shreyasnaphad?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## If You Understand These 5 AI Terms, You’re Ahead of 90% of People ### Master the core ideas behind AI without getting lost](https://medium.com/towards-artificial-intelligence/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Mar 29

[199](https://medium.com/towards-artificial-intelligence/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319?source=post_page---read_next_recirc--948c3a5df90d----0---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----0-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc7622d353319&operation=register&redirect=https%3A%2F%2Fpub.towardsai.net%2Fif-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319&source=---read_next_recirc--948c3a5df90d----0-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

![Image 41: The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*LDxbtzfpSDt7WwGGCjRdhw.png)

[![Image 42: System Weakness](https://miro.medium.com/v2/resize:fill:20:20/1*gncXIKhx5QOIX0K9MGcVkg.jpeg)](https://medium.com/system-weakness?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

In

[System Weakness](https://medium.com/system-weakness?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

by

[BugHunter’s Journal](https://medium.com/@bughuntersjournal?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## The Bug Bounty Automation Stack That Can Generate $10K+ (Open Source Tools Only) ### Automation doesn’t find bugs. Automated workflows combined with manual validation do. While beginners waste time running Nuclei on random…](https://medium.com/system-weakness/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Dec 17, 2025

[5](https://medium.com/system-weakness/the-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7?source=post_page---read_next_recirc--948c3a5df90d----1---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----1-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F93ed3e8b3ee7&operation=register&redirect=https%3A%2F%2Fsystemweakness.com%2Fthe-bug-bounty-automation-stack-that-can-generate-10k-open-source-tools-only-93ed3e8b3ee7&source=---read_next_recirc--948c3a5df90d----1-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

![Image 43: AI Agents: Complete Course](https://miro.medium.com/v2/resize:fit:679/format:webp/1*PvPPSGJ9779FTWmtK_Yeyw.png)

[![Image 44: Data Science Collective](https://miro.medium.com/v2/resize:fill:20:20/1*0nV0Q-FBHj94Kggq00pG2Q.jpeg)](https://medium.com/data-science-collective?source=post_page---read_next_recirc--948c3a5df90d----2---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

In

[Data Science Collective](https://medium.com/data-science-collective?source=post_page---read_next_recirc--948c3a5df90d----2---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

by

[Marina Wyss](https://medium.com/@gratitudedriven?source=post_page---read_next_recirc--948c3a5df90d----2---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## AI Agents: Complete Course ### From beginner to intermediate to production.](https://medium.com/data-science-collective/ai-agents-complete-course-f226aa4550a1?source=post_page---read_next_recirc--948c3a5df90d----2---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Dec 6, 2025

[234](https://medium.com/data-science-collective/ai-agents-complete-course-f226aa4550a1?source=post_page---read_next_recirc--948c3a5df90d----2---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----2-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff226aa4550a1&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdata-science-collective%2Fai-agents-complete-course-f226aa4550a1&source=---read_next_recirc--948c3a5df90d----2-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

![Image 45: 20+ Vulnerabilities in a Static Website](https://miro.medium.com/v2/resize:fit:679/format:webp/1*jJ5-6zmfCDldKx5g1gj-Jg.png)

[![Image 46: Saurabh Jain](https://miro.medium.com/v2/resize:fill:20:20/1*gXBGFSeHBrBmuEzFs-eAkQ.png)](https://medium.com/@saurabh-jain?source=post_page---read_next_recirc--948c3a5df90d----3---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[Saurabh Jain](https://medium.com/@saurabh-jain?source=post_page---read_next_recirc--948c3a5df90d----3---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[## 20+ Vulnerabilities in a Static Website ### Bug Bounty Cheat Codes](https://medium.com/@saurabh-jain/20-vulnerabilities-in-a-static-website-2f32a4902377?source=post_page---read_next_recirc--948c3a5df90d----3---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

Nov 18, 2025

[](https://medium.com/@saurabh-jain/20-vulnerabilities-in-a-static-website-2f32a4902377?source=post_page---read_next_recirc--948c3a5df90d----3---------------------edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fs2wblog%2Fdetailed-analysis-of-clouddon-cloud-data-breach-of-korea-e-commerce-company-948c3a5df90d&source=---read_next_recirc--948c3a5df90d----3-----------------explicit_signal----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2f32a4902377&operation=register&redirect=https%3A%2F%2Fsaurabh-jain.medium.com%2F20-vulnerabilities-in-a-static-website-2f32a4902377&source=---read_next_recirc--948c3a5df90d----3-----------------bookmark_preview----edeb42b8_ceda_4b50_965b_c845923bbde9--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--948c3a5df90d---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----948c3a5df90d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----948c3a5df90d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----948c3a5df90d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----948c3a5df90d---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----948c3a5df90d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----948c3a5df90d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----948c3a5df90d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----948c3a5df90d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----948c3a5df90d---------------------------------------)