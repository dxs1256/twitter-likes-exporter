# Twitter 点赞导出器

通过 GitHub Actions 自动同步并导出 Twitter/X 点赞列表，支持缩略图智能去重。

## 功能

- **自动同步**：定时通过 GitHub Actions 拉取 X 点赞列表，全量刷新，点赞/取消点赞实时镜像
- **精简导出**：输出精简 JSON（`likes_mini.json`）和纯链接列表（`likes_links.txt`）
- **缩略图去重**：下载视频封面缩略图，通过 dHash + pHash 感知哈希比对，自动找出重复视频并生成报告
- **可选发布**：自动发布到 [boomurl xlikes](https://xlikes.boomurl.me/index.json) 站点

## 快速开始

### 1. 获取 Twitter Cookie

1. 浏览器登录 [x.com](https://x.com)
2. 按 F12 打开开发者工具 → Application → Cookies → `https://x.com`
3. 复制以下两个值：
   - `auth_token`
   - `ct0`
4. 获取用户 ID：访问 [x.com/settings/your_account](https://x.com/settings/your_account) 获取纯数字 ID

### 2. 添加 GitHub Secrets

进入仓库 → Settings → Secrets and variables → Actions → New repository secret：

| Secret 名称 | 值 |
|-------------|-----|
| `X_AUTH_TOKEN` | Cookie 中的 `auth_token` |
| `X_CT0` | Cookie 中的 `ct0` |
| `X_USER_ID` | 你的 Twitter 用户 ID（纯数字） |

> 如需发布到 boomurl，额外添加 `BOOMURL_KEY` Secret。

### 3. 运行工作流

进入 Actions → **Sync Twitter Likes** → Run workflow，每次运行都会全量同步。

### 4. 查看导出结果

运行完成后 `exports/` 目录会生成：

| 文件 | 说明 |
|------|------|
| `likes_mini.json` | 精简版 JSON，包含用户名、推文链接、媒体URL、缩略图、正文 |
| `likes_links.txt` | 纯链接列表，每行一条 `https://x.com/{用户名}/status/{推文ID}` |
| `full_archive.json` | tweetxvault 完整归档原始数据 |

## 缩略图去重

对导出的点赞视频做封面级别的智能去重，快速找出重复搬运的视频。

### 原理

下载每条推文的视频封面缩略图，计算 **dHash（差异哈希）+ pHash（感知哈希）** 双指纹，通过汉明距离聚类找出封面相似的推文组。

- dHash 能抵抗亮度、对比度变化
- pHash 能抵抗缩放、压缩
- 双哈希交叉验证降低误判率

### 运行方式

**方式一：GitHub Actions（推荐）**

进入 Actions → **Thumbnail Dedup** → Run workflow

**方式二：本地运行**

```bash
pip install imagehash pillow
python scripts/thumbnail_dedup.py
```

### 输出文件

| 文件 | 位置 | 说明 |
|------|------|------|
| `report.md` | 仓库根目录 | 去重报告，中文，包含重复组详情和缩略图链接 |
| `thumb_kept_pairs.txt` | `exports/` | 去重后的条目列表 |
| `thumb_duplicate_groups.json` | `exports/` | 机器可读的重复组 JSON |

### 可调参数（环境变量）

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `THUMB_THRESHOLD` | `10` | dHash 汉明距离阈值（0-64，越小越严格） |
| `THUMB_HASH_SIZE` | `8` | 哈希精度（8 = 64 位） |
| `THUMB_INPUT` | `exports/likes_mini.json` | 输入文件 |
| `THUMB_CACHE` | `.thumb_cache` | 缩略图缓存目录 |
| `THUMB_OUTDIR` | `exports` | 输出目录 |

## 工作原理

```
Sync Twitter Likes 工作流
├── 认证配置（cookie → tweetxvault）
├── 全量拉取点赞列表
├── 导出完整归档
├── 清理已取消点赞的推文
├── 生成精简 JSON 和链接列表
├── 发布到 boomurl（可选）
└── 自动 commit 回仓库

Thumbnail Dedup 工作流
├── 读取 exports/likes_mini.json
├── 下载缩略图（带缓存，重跑跳过已下载）
├── 计算 dHash + pHash 双哈希
├── 并查集聚类相似封面
└── 生成 report.md 报告
```

## 注意事项

- **Cookie 有效期**：通常 2-4 周过期，同步失败时需更新 Secrets
- **速率限制**：点赞过多时单次运行耗时较长，请耐心等待
- **账号风控**：频繁请求可能触发验证，需手动登录解除
- **隐私安全**：公开仓库会暴露全部点赞内容，建议设为 **Private**
- **仓库体积**：点赞过万后 JSON 较大，注意 GitHub 单文件 100MB 限制
- **缩略图缓存**：`.thumb_cache/` 目录用于缓存下载的缩略图，重跑时会自动复用，删除可释放磁盘

## 文件结构

```
├── .github/workflows/
│   ├── sync-likes.yml          # 点赞同步工作流（定时 + 手动触发）
│   └── thumbnail-dedup.yml     # 缩略图去重工作流（手动触发）
├── scripts/
│   ├── configure_auth.py       # 写入 tweetxvault 认证配置
│   ├── extract_minimal.py      # 从归档提取精简 JSON
│   ├── extract_links.py        # 从归档提取链接列表
│   ├── prune_unliked.py        # 清理已取消点赞的推文
│   ├── publish_boomurl.py      # 发布到 boomurl
│   └── thumbnail_dedup.py      # 缩略图感知哈希去重
├── exports/                    # 导出目录
├── report.md                   # 缩略图去重报告（生成后）
├── requirements.txt            # Python 依赖
└── README.md
```

## 依赖

| 包 | 用途 |
|----|------|
| `tweetxvault` | 抓取 X/Twitter 点赞列表 |
| `lancedb` | tweetxvault 底层向量数据库 |
| `imagehash` | 图片感知哈希计算（dHash / pHash） |
| `pillow` | 图片处理 |
