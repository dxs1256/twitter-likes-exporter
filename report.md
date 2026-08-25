# 缩略图去重报告

**输入文件**: `exports/likes_mini.json`  
**总条目数**: 147  
**有缩略图**: 146  
**无缩略图**: 1  
**判定阈值**: dHash ≤ 10, pHash ≤ 20  
**发现重复组**: 1  
**重复组内条目数**: 2  

## 重复组详情

### 第 1 组（2 条）

| 序号 | 用户名 | 推文链接 | 缩略图 | 指纹 |
|------|--------|----------|--------|------|
| 1 | @KateOFtf | https://x.com/KateOFtf/status/2091111890189730211 | [图片](https://pbs.twimg.com/amplify_video_thumb/2014967142287073280/img/P2aHxsXtWvF11GNC.jpg?format=jpg&name=medium) | d=19993333… p=e819d257… |
| 2 | @KateOFtf | https://x.com/KateOFtf/status/2087996361006280854 | [图片](https://pbs.twimg.com/amplify_video_thumb/2014967142287073280/img/P2aHxsXtWvF11GNC.jpg?format=jpg&name=medium) | d=19993333… p=e819d257… |

## 无缩略图条目

以下条目没有 `media_thumbnail` 字段，未参与缩略图比对，**不会被过滤掉**。

| 序号 | 用户名 | 推文链接 |
|------|--------|----------|
| 1 | @lance012210 | https://x.com/lance012210/status/2060276521156440191 |


*报告生成时间：2026-08-25 08:26:37 UTC*