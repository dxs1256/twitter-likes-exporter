# Thumbnail Dedup Report

**Input**: `exports/likes_mini.json`  
**Total entries**: 147  
**With thumbnail**: 146  
**Without thumbnail**: 1  
**Threshold**: dHash ≤ 10, pHash ≤ 20  
**Duplicate groups found**: 1  
**Entries in duplicate groups**: 2  

## Duplicate Groups

### Group 1 (2 entries)

| # | Username | Tweet URL | Thumbnail | dHash/pHash |
|---|----------|-----------|-----------|-------------|
| 1 | @KateOFtf | https://x.com/KateOFtf/status/2091111890189730211 | https://pbs.twimg.com/amplify_video_thumb/201496714228707... | d=19993333… p=e819d257… |
| 2 | @KateOFtf | https://x.com/KateOFtf/status/2087996361006280854 | https://pbs.twimg.com/amplify_video_thumb/201496714228707... | d=19993333… p=e819d257… |

**Pairwise distances:**

- https://x.com/KateOFtf/status/2091111890189730211 ↔ https://x.com/KateOFtf/status/2087996361006280854  → dHash=0, pHash=0

## Entries Without Thumbnail

These entries have no `media_thumbnail` and were not included in thumbnail comparison. They are **not** filtered out.

| # | Username | Tweet URL |
|---|----------|-----------|
| 1 | @lance012210 | https://x.com/lance012210/status/2060276521156440191 |

## Kept Pairs (unique thumbnails)

One representative per duplicate group + all singletons.  Format: `thumbnail_url|video_url` ready for `video-dedup --deep --thumbs`.

- `https://pbs.twimg.com/amplify_video_thumb/2014967142287073280/img/P2aHxsXtWvF11GNC.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2091718689943072768/img/D-W44Xv-wsXTFaad.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1845502065046409222/pu/img/eZTEotcv1OQm8Km8.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/2091484366958370816/img/ATMr7TaWHnDMIicC.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HQZZ1bAaYAASFo6.jpg|https://pbs.twimg.com/media/HQZZ1bAaYAASFo6.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2091367139009564672/img/BbeRu-NGvAtXZcDw.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090993575878328321/img/yMSm0iKHTUlkfoaI.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090875167882805248/img/OY6nwKQmP8YKEj3s.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090775522611466241/img/Ri5TIfBmBUri-GCK.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090507390336606208/img/3CZnTwg6F3Nu8eDM.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014927282297831427/img/MHXI61EEjztkIjpC.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090399115410632704/img/D529iqy1jHUhQzGW.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HQJPtJLa4AAl1E6.jpg|https://pbs.twimg.com/media/HQJPtJLa4AAl1E6.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2090100553921748992/img/UvNJ2Z0pvvena2JZ.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090047189288357888/img/XIz6VjRJW-Xk6V-E.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HQFJeG4bYAAYpHm.jpg|https://pbs.twimg.com/media/HQFJeG4bYAAYpHm.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2090009771839528960/img/6SO6iHAqctYLewmz.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2090004257760059392/img/6zl9knbfj52RyDym.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HQEi93sacAAe7MU.jpg|https://pbs.twimg.com/media/HQEi93sacAAe7MU.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2014945588975173632/img/t1Or_MixHttMQoPB.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089010873981714432/img/zEcGeimN-i9zIjxH.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089697284900462592/img/AgEizRLtOnOTkWj9.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089636451797340160/img/g3IB5OcjkDwMF3mR.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089442456177721345/img/CuI2PIO_yL6F7bl7.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089273643587006465/img/GJYvyan8bvke-0kj.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HP5y-iDWMAAe8DL.jpg|https://pbs.twimg.com/media/HP5y-iDWMAAe8DL.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2088997651912269824/img/l_ELpFJFlEhmex_l.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2089212115508658176/img/5kf6qyKvpeDuwQ2s.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/2089203650174603264/pu/img/2Fiwc-OZ0ZWRMrv3.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/2014963757282443264/img/1F341w1dqWacTmtF.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014965189863735301/img/uHyqowKbs0IpMt8e.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2088552344162062336/img/6n8z6jS3NW5IeNaa.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2088066426255163392/img/0X2aXxgwH3tLMCwz.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2088040731025793024/img/MFSqW1PxW8J4BUxL.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087915003345006592/img/-Yg2hdXgmkQD55mu.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087912114937643008/img/IWk0-m1YZPybvjJS.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087874106641260544/img/cq-wdk1prZU-2j-U.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014972257261793280/img/ja0k5tdZHAtM-lL6.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087636915696652288/img/iK7APqyHjnhgoRUC.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014976634949140481/img/MFeuk4t1tBFqwKx9.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014970935091326976/img/5Fc8QqmacyG8Tvya.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087562655263236096/img/katODnH48RRTMpHw.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014970317559758848/img/m-QfxjMiPzjQxuwc.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/2087466038224932864/pu/img/39NvPpqpltENSG1q.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/2087429651987857408/img/QV0Ov1dOq_kxsEQO.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2087148594067357697/img/u6YuElqko4H2YVR_.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2068460287767027712/img/6mG9drEdn_4vUsVI.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086898968978460672/img/___81P2Pu_PGPBxB.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086766940350230528/img/UqtQ249rlChmFKxH.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086685948922773504/img/E7-SrO8MpenDT08s.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2077801595325313024/img/CwAG0OLwZRSchCoy.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086462200743636992/img/iIOkjLBcZ0gH4BpV.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086381627748335616/img/unosAQzgL0s29aIj.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2086024708894740480/img/WAXvr02BbS7nywt-.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2085352559670099969/img/tPojLowk_zkiYNn4.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2085347367092396033/img/bRKDJRBq0v59HtT1.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2085182728241025024/img/hl9jVLhaEPL_7RQu.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2084580915448020992/img/P4VphrRM967ur6bE.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2084576320822857728/img/6Rp5RDhNkMXSe8qp.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HOx7HOLawAAG9TG.jpg|https://pbs.twimg.com/media/HOx7HOLawAAG9TG.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2084051863532388352/img/BGOGHsE4HUFW0sJb.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2083871516429799424/img/l_Po10TIuO62bR7I.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2083608084513951744/img/pzEITSF_d4I2E7MW.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2014964673821736964/img/EMnFdZue1s4pTW_V.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2082116463448526849/img/d0sk8IWp3IKOhEFn.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2081664511241850880/img/muyzx6lRPfvPu0oV.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2078617168758136833/img/S0VMFmw6BLdPW0jo.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2076673818865926144/img/Q8mJuBkEkbVpsM2_.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2075906993395519488/img/gXh0YJiLpqVqMSmw.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2075844611973824512/img/Wn8kvFEdMSxetOWY.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2074738025557286912/img/DDf0G-KGUmnwgj5P.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2039431430464548865/img/2tVlPZa0eaZON4pQ.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2071151852763467776/img/-90qmXnKKDvrPk3P.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2071102265591549952/img/yX2z_ADltHLp_Vjb.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2070469118084382720/img/_FwIY8cNqoq5Bf1O.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2070408945831710720/img/1kO5G5fDVOpS0W-w.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2070407920747986944/img/6z9fqNajQpLnevN9.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2069455121319170049/img/La02AjcFRCFkK1ex.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2069005706024378369/img/UdUkLZQiC_ds-IpX.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2068769270927110144/img/CWogNwAYIlj6cgNu.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2066780939980779520/img/EEwimEzIjGnvbp6D.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2066484311482834944/img/-QbHN2kcTInowEzc.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2065150519509741568/img/hYBKbtKsX_FqB6Tu.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2062793002419195904/img/1CQA5lqIWkjJzSb4.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2062792897964212224/img/1pCvjAZUni87bS-F.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2062792154565726208/img/TN6qyqbfq_oWtXSX.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2062791471514972160/img/c-p1lrFuZ9mAqItg.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2062532423234072576/img/eB6AQTYGo8ZRFIbv.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HJ8HWwzX0AAnhBd.jpg|https://pbs.twimg.com/media/HJ8HWwzX0AAnhBd.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2059423376494497796/img/pgKIKTvsPNXHcZL9.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2057813267645345792/img/aIVxzSZDmZYA2pzP.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2057061702965866496/img/SQPX-p_Jbj2ZQ759.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2056843339769458688/img/YXOagThFXxdqs5pV.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2056811206195699712/img/omWC-5XVaYJfeI3o.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2056748471374565377/img/GKdwPj9AzvWvpJh6.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2056258726701535233/img/nYB2Xd3yda60aez_.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2055940462180016128/img/85eli98Xck3-WVob.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2055931744982024193/img/Vvck63YxnbqnOtwW.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2054993520717332480/img/HcK95vWdbnxjem-_.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1525891270090137600/pu/img/KK55PU8081laKKXk.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/2052026511331651584/img/ExqdoNh7EOXHepR2.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2050172083947401216/img/ONhuWfCZVmdgQt7M.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2051305449778257920/img/x-7_nBUaN85O4wth.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/2049913515763228673/pu/img/FjQzGs-RBr3CK0iH.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/2049087982074986496/img/GL7i2SwASpPQkBZN.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2040414187244175360/img/PujFPTvIgDQILFE7.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/1876203438125789184/img/uc2jUL475ilBrclv.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/2023438074534039552/img/YAh3rGe9f4BX5tqI.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/HBKsEgYasAA2rm7.jpg|https://pbs.twimg.com/media/HBKsEgYasAA2rm7.jpg`
- `https://pbs.twimg.com/media/HALvb4aWEAAnozK.jpg|https://video.twimg.com/amplify_video/2018376406753824769/vid/avc1/1080x...`
- `https://pbs.twimg.com/amplify_video_thumb/2016838282760638465/img/OyHFxtn2SiWWMEV9.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/media/G-oPCpSbMAA7lB4.jpg|https://pbs.twimg.com/media/G-oPCpSbMAA7lB4.jpg`
- `https://pbs.twimg.com/media/G9sqPMPa4AAJIfi.jpg|https://pbs.twimg.com/media/G9sqPMPa4AAJIfi.jpg`
- `https://pbs.twimg.com/amplify_video_thumb/2004370717937487872/img/Wba9aurhxDrPPhFA.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/1995143974630391808/img/wAPkdCDbVSe8cxGJ.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1990541897194979329/pu/img/SHTQothI_4KLTVFO.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1989667491354722304/pu/img/2OcvuknwHKhD_s-X.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/1988337543243337729/img/QDkzjMQlKvuPxUJN.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1972218096430862336/pu/img/Sf-mUfWbQiNYqY-F.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/1942111412077375488/img/hH0Zm137ppq1M6GZ.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/amplify_video_thumb/1875441428110962694/img/dc5kAhL-I7Aw-CRE.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1766825285847232512/pu/img/AYIL91rGhg_pJvoe.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1728257434903252992/pu/img/VXzBXeZuo9nW_ROa.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/1710294959893479424/img/ICU-zj-IFpIFJSaA.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1654058343122747392/pu/img/OCRKBQvMAbSXPET2.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/amplify_video_thumb/1636235638969339904/img/Z7jbpIyqEwbNxNok.jpg|https://video.twimg.com/amplify_v...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1632518444724932609/pu/img/05jjHhn8qKhP_n09.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1632145186506838017/pu/img/MCiN4ScvLhlvXyFS.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1452794021827399682/pu/img/JffaJt1MnC9u921d.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1452793684521414660/pu/img/w9V1Z-0-qIPosH4R.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1452262722876420107/pu/img/kgrZh2pResKd5q1G.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1444322048973565956/pu/img/XdKxgDAcyuYK5DV_.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1387916361536524288/pu/img/FisfcJ8AqBnOgKiB.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1384178943289290758/pu/img/g612RxtRuxrteXZs.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1384178903787261958/pu/img/LOEUInvVHquTQmcq.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1383920640441274368/pu/img/PGUsPMVPLYYwPpwQ.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1381045246721687553/pu/img/JbjjfQHzC49NQicm.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1380003485198864385/pu/img/LbHuoNO3FAAvtyRp.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1379601103902363648/pu/img/1TwwDyQLoprm5D5p.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1375037490013163522/pu/img/jMA4Lfs9adJi6oPA.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/media/Ew4s7dHVEAECWyV.jpg|https://pbs.twimg.com/media/Ew4s7dHVEAECWyV.jpg`
- `https://pbs.twimg.com/ext_tw_video_thumb/1371958052467970054/pu/img/9Jo3JfIRcORcO3DU.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1316405076030705664/pu/img/rgqsxYFPPDjhUzHL.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/ext_tw_video_thumb/1274015506589196288/pu/img/13F_6DqZQiLp82_g.jpg|https://video.twimg.com/ext_tw_...`
- `https://pbs.twimg.com/media/EZMJ_PUXYAA56BM.jpg|https://pbs.twimg.com/media/EZMJ_PUXYAA56BM.jpg`

*Report generated at 2026-08-25 08:03:36 UTC*