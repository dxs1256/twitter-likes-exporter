# Twitter 点赞导出器

通过 GitHub Actions 自动同步并导出 Twitter/X 点赞列表。

## 配置步骤

### 1. 获取 Twitter Cookie

1. 浏览器登录 x.com
2. 按 F12 打开开发者工具 → Application → Cookies → https://x.com
3. 复制以下值：
   - `auth_token`
   - `ct0`
4. 获取用户 ID：访问 https://x.com/settings/your_account 或使用在线工具获取纯数字 ID

### 2. 添加 GitHub Secrets

进入仓库 → Settings → Secrets and variables → Actions → New repository secret：

| Secret 名称 | 值 |
|-------------|-----|
| `X_AUTH_TOKEN` | Cookie 中的 auth_token |
| `X_CT0` | Cookie 中的 ct0 |
| `X_USER_ID` | 你的 Twitter 用户 ID（纯数字） |

### 3. 运行工作流

- 进入 Actions → Sync Twitter Likes → Run workflow
- 可选：选择 `full_sync: true` 进行全量同步（重置后获取全部历史点赞）
- 默认模式：增量同步（从上次位置继续）

### 4. 导出结果

运行完成后 `exports/` 目录会生成：
- `likes_mini.json` - 核心信息精简版 JSON
- `likes_links.txt` - 纯文本推文链接列表（每行一个）

链接格式：`https://x.com/{用户名}/status/{推文ID}`

## 注意事项

- **Cookie 有效期**：通常 2-4 周过期，同步失败时需更新 Secrets
- **速率限制**：点赞过多时单次运行耗时较长，请耐心等待
- **账号风控**：频繁请求可能触发验证，需手动登录解除
- **隐私安全**：公开仓库会暴露全部点赞内容，建议设为 Private
- **仓库体积**：点赞过万后 JSON 较大，注意 GitHub 单文件 100MB 限制
