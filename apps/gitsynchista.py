# coding: utf-8

# This is a self-extracting archive. Copy this script into a '.py' file located in the root
# directory of Pythonista and call the script. It will unzip the data and extract all files to an
# immediate sub directory of the root directory.
#
# This file was generated using pyzipista (see https://github.com/marcus67/pyzipista)
#
# Zipped Application:    gitsynchista
# Application Home Page: https://github.com/marcus67/gitsynchista

import zipfile
import base64
import io

zip_string='''
UEsDBBQAAAAIAFEQmEcptW2jmBoAAH9GAAAUAAAAZ2l0c3luY2hpc3RhL0xJQ0VOU0WdXG1z28iR&j6&YkpfLFXR9Np3yWVXV1dFSZTFRKYUkrKjbwHJoYgYBHgYQFpWKv&9_unuAQZ88e7FlY0tEpjp6denX0bWHv75PH6yn4fj4WRwbx_fru5H15b_G46nQ3Pkafz56kqfFrn91LN&rnNnP&7880dj7HWx3ZXpy7qy59cX9OGffu7xV&a2dM5Oi1X1lpTO3hZ1vkwqWqBnR&mi37P&va6q7S8fPqz8ql_ULx&_x9g&4K0k&56luZ1W9H7Vs7fpqlrb26woyp69KnyFFb4M7E_fPn786f3H&&jpo32aDowdvrpyVxBdqbdbV27SqnJLWxV2QQTaJF&aZeqrMp3XlbP07JyI2eDL1Hlji5Wt1vRmli5c7p1dFot643Lan563i3WSv6T5i00rLJ8XlU2yrHhzy745xS7_81i6ZDPPHJ6arV1Y3ttVUdoNHcb6wCD8t3Q_fcmF7Cr5Th__JTu7K_rSrIgby2KDb&yan6cTMV104qpv7dWODpNXZeKJ6Ir2Ygm73JVJZh&rOW1t7vV0dIY0r1y_lK1e6oS4XpG4sJX90Vb4zgSa37_nRzag09f0GDZtjkNb4Fk_KPGKaPS29qRCfXAi9aZLmg2kJdttRhLB5swfFozrKpNplemdjziY82mSfGcLeqe027J4KZONfVsXWLmu1kXpiUsbUg560tReZEoknU_LjdPXTilu53CLgnSI2DffmcDse_fpgPbEwdLcVy5Z9i_sfS5qu0hyPuvOCi3MeSXYkwCLglXr29rl9o34unXJdzCDmRoI6eErEFS6lStLnIYYoPLrQU&NtqT96YAP9SnK&IHqxSJNKiiFWSevIuBIOSJ7EjM6oM_eq_qUL6wJhm2MmPRKW9t0haXtW_rXF71mKzrLwqWvWKQuF1h6SYIpmWEvjuyvMuFF0ln6MXoVz6iidpSRXifds0TjQqjEIrnN3ZvQG&h_KToUlvueF2&NussCa3qsTHz2LJ1ZgVcrt6jEctgPepZK7iJelg6cWkCJvCxPzJinS0O6CpcFZrqcLV03kZVAODTaf5evCkilhN2WfEB5qm9m8k5nF7JonyUVL75wZZXQgemJLX2ZztMsrVJ1Q1hZOGqOSjTmZA8UKfs3xTJdQX2ZFbf0hfs12WwzekifOLqcrxdrmwSWE6&WDlZn6Kcq5ROzy7ArRwvxPjW5gZdU9Y_0I6WlcmIO3ErLBeYrzMhCV&tiZfzunjrTKzs2sF6japF60bcm0jxaZ0Aq0dDh16QS9MwmKANFGrggXlUUhv6VliaIBjbsjmkJ6T3FteqNZFq5rf&Fnn_84FglwbTLdVJLc&7pgvhHdq5qEkWrt3VKTAWPPH_ZuRcyc46CnmO2hsFeLGFa8wNHIRZjvB9TPcg8cQiycAkkxt6T3K0eBavCWOhAovBsjUHhVeEMM9yFyFxDcX1Fr&lGFOJN84LeLxGEdrwln64Ta0gQo9VBiGHiU3bD9PnGYReXeYkF24T8MVGYgz6j3sLHGkTkqsiImLegHKxAIc5jx4JEkuZJ1qM95EiIMcQIiuwbDqVlsawXQgbHEEiXtBMLkGvOIHpIIVrLaDh6Rw9s64oDjKjLLb7Odj3eJHZPIKlaE6KgyE17UbQHLysKIXx6jY1bfF0hzJLewbeyB3kt0iXvv4R3LOXEFL_COiAwknEmwvQmcOIQab5MX9NlDaJsMWdHIps0cIYsPreOdHPB1sZxaN0uQ39TGHJVUu766jRJJ6AuJGZWHub4JlkCy9hF5hKlkFigBxLzmzcQaimqqar1TtEGvDx9DL43zyUM1voBgm0h&8ZyOT4VdELxmlgThkIn6LXuS3XdiLYtBAysCiDAE&jvx_h6Npx8mdrB_MZeP4xvRrPRw3hqbx8m9OPj82j8uWdvRtPZZHT1hK&4wS8PN6Pb0fUAH2DLn&qMoo7BJtVN5jwdRzDNW1F_VzcBlEgy9CYBnxCIt1miygsNaX3QusgQaXyyU_y7ITRKImidyNLUTTAShgYgfRxr9EUGZ49C3xnBa0dc7BkGMA35HCOiM4B6doKkoGd8lHkips07h9XMxlHQsy7lI0ffYA2sS6SmryQ_UjZeRYhvD5wlb7_IgadMC52ctpVnlW2q252V7bYoWScYWfSMEtAkGTgBnH2sPz743yZQL_FIcH6WmMnIUOvkBSw7vyM3SV5hRSzuNS9gQwbyi6wGkMcWRQ3FJ3irX_cmSMaexbufAYYO4dfVTNjfJctl6dhnJt6eUSA5I&UekK9&FbRQKF_Bsk4ZSeeQjCyBQlu0LNqh6nAp&pYhWl35lO2fwimtHlQlgetcmbLOD1ivHjrAHrfsKXzj1cipkk8oNvErJgLuRQ7sveINIVsOCOxT04rDoz1QNBN2Pief6LbAYTlnKOS_QNzcEVhnL0bnPELxRd98E7RjGyUra2BvrOWxSwhCzSGXhZOw8LEviCbZ&Z6MNgA3Xeadj0ENxBsjbWDoNGcL2VBIqAmVkfGRz3ctGDZgzTZd1EXtM9mdfA47dtJd_mQLQ6doQ4dgwKBExk_Z1tLU8_ghFlmSbogrRHSAAZf2u3NbmAQ0QKGekdd8CF8AQ0iVO55QskAcPpl7l9MuCGx0tmZpg2cYUba5YoQKuqwjReCjBMem_5gkK0i6AuLap0lUjZQk7WEkq6CGXO1658k4MtVrMeaQu8lOgvZ2ukqioLHYqofBmRusFIExROBfQ5YeEDRrzqdWcxTs8YpyqvK4wgSPqZ7NiGejJ2oOkhsh96Qr7mlgFT2NUSe79q4jVAdvj4SSqR7uo0nmZLdH9JJUg9D3xjlREjmFd1FQ&0VCdHLRZgSLpPaSTjQAcpVmEj4XxFtmLJ0R5q0qx2t4_FW26ZBwMr&F58gKwQMtkXqp4slTChXmB3SwboIBzbIRv4g5alma55JPxzJvFJz5W0ZjZdWEdf7MS6jDufZcoAqW1_D3GIMXK2REHXhFPiLRXRJwIegzQhRbY1oum1WgQKeQQAj9cvzFRcDxDetDoM9JrxhkEsRdSp2GUwWUqsoEYYj8jB6eHC052ChBFFZCR&lLklSJkBq8MCwCqsevRwsyYkxzJQj1pnJJkbaEt_AskahL4eRLCIWAEhRa9CnPi5q8C6qEGoTZKDoezx71eAkvoB_cToTOAXApmekFBNboh1qB0NG8cNFWL7jSxhYfYXzR_MBtFhevsG8wGkZdloX4heUsZ76FfU3d255P5FVahHc_&HXh2F39ggDbCdmVd9kq1B_DDIg2XgKxjkN6ownCfCkZ5B2W98SJdTxQOM0hQvjfOi2lHiMr7i3WvzBNDYUf3UiBgetzGkwadeUtW_vgxNSkgAL0fUIpofVOizDMH6SW&IpgoZOW2eOwhDrEHHQkvshpNa7qAhmVDBBb2IGHvSPjg5phA69wb0MsfkVOVsEQYhMUwQLwsIX2UNPiWnZ7zoIiW0M_W9KeP_LaR_L3tkb9ua6aF8yezvlkE3GF3mbPw&mmeBjJTFLfiSlmP6awX43xpsYsWSMkiPpWcEKmywGpBbelEcn5BAMELEwpxK_ojqvoDURb6jYBY9YcLKQ0Qh9wIirHKt1LUi4pFrD86SX7higthbIZvdiL2giglEvxVeMvlU8ci4CLolog41RfmbiMRI9Jclei40EggImVogA9d2lJSmvOG9qtOLsx7ldXSiocimhSJ0I5IzvK7Ch&KkpCcxkqGyGb8keRAJ15lCOzSKX3s4GjS15ewKWwrKY8cg5w5dhCZh9qsX&kD38ARC7wc2Jfi6xGfX9FSa_vipLyKnXp7fkE_rZOaF4G9xdRJ16TdRpJytEg9x8&Rur7R9inHhmkxNKAfj5dIEQV83_gvhLq4SS9RV2xvwEgOxJ_zTRY3Eem4ZNlEHUKQ5EzQPlMbUrKG8SBFj4NFhSSt0ArpL_NNPBZ5jjUlVJf5ji4IcsgAPUesRxECn5qc5Ce2nyw2qim8AMgKKGmexwWsApvQasVm6RMSf&rUCRqC4aIOQLGLomFvQaQHZ4saeyJEXfPviZZKssRzzLyzhXX4uRcO5eU3LRpswrGR_wQdj3F4wqgcnS2pBidS2_PcZE2u0KCgODnygC1lXGxvvY4CAvveYV9jkchel84HTkw7pP4_&tkcJr&cpJ&QwaLU9qV5mCBeIooZWV4qoGZBSShf68ndeLIgChcPEsyoiUXf6YoRtu6Uh1YcSkxBxCFp6Ss7aDaEaoICHp4v6Evhlq&bbx83gafJo3WISsnvpRS3bHTeh6iw1y4r8il0yxbtU5FCmJCC7cIRRybJnLiITTmtGrbTcyIn9wcveWcISZaCnKN6cvuhneXLUNv5oAu_pw2qZEqpW3SQoldVntOTBLvi0Ua6mFkAgkU363SPJW6K9IsfV78cJlupbmMgG1C&AJxqZbJGPagWp5lSQwc2hPRKe9I8K9gOrCd8VvHEncBy&YOzhObC7f7EDW0HIfOHjcKm0pPg2nj186RtUu1UFcmHs05ATGQ00VrCZvkH4wANqTRjE7P5YSg_DupscsEmni48Qs9oaEYVUrO6ne_IujGNSY43u75kSgRV_uccQvT3GxlFLUnaqFcZ_5yj4L86gAtRKsDYkUWgM6NlslY0Yk_Q6vz1jqwweg40bY0awNXqRXVhrcs4Dq5ZlC5t8CB9gW4zWCUF6Mvasb53hyDlR0viYYF8HH9so58e6rdc6lxbraUM0VDJ9Eie9WiiBkMGf6zhQxQIikDSbGGsj8uoQt8jUFLB0oYUVQor&t1izIup08a6YM3j5AKGpsoL5FSbCvDEOeNwWBxcvvTu8N9osUkKshto6RGFKg0liGIpJBjpwV6hCzTmGHgLxA094ca3yoVK2ZG6LizdBEgAkCLKoJNKy4MMaRlO4jTEMaWw1JCdgNXHAigdBA9L&rfqs7EsWRpQqkji_4PIrqQ3cW5JjRyW_2lYD5FSTL0qVlzdPKCfW1zfGBi1nC0M1_Q4EvRttvV1YIeefATgkE1qPL7nQ_ZwkHCm4SkrOR_3Tqdp5UU6rPkrWnka554eB5Zh2JLgTb1fCc9Mq5WdPD1Xun_XMuLJ0vsF1LaQe9x0WiN7J9oSbcj44rxKzrWqDeGgaP&T49PKG7IN3tM3MtwdOrhj33polTpxik__RHS&40TV&F8w54BqfIjQw7WGDyaCT1l&UaGRsSIu5XEqNcf6CLrZldUobPtTvRFwzSFuqeUAoPWLVd1yd2qzuyJpmBtSf2dbXJN9a3qAFiviRVrbnD1TdeSdFhFQBIltvT&C8iptUBtKEXemM_xl5D9V9_OVhLXuZpCJtr0BRADKGn&R7184UqeYJQoOZX2syEgioDjwkMrlWfoHqBcY8_l8bxJdfRQW9dkrrXzFz0TaSFjYeYjKwJ051xHYXAooYqAHwMSypbDxq2nvghhGkN&ZCaVAv1miz0b6UmzTWwZ4QKlT_zbRMbT78r0hY5C4fW4ol8oGPcY4CH18ummzshMnbSKpH1BMeRFYWXr9U3ctInm9hzJkovv0Wsa_Q_ECOQdFPOE7ekEwOGQUhKk2wzSFHUmOE5GSG1Z7ChL2L3n6YLIuCOYEHYh5yeot_CJnKJpr2mDZUlhYYFpDS7aNz9RFsmggs4hR2TPw3mFDn9CGYiqwN45MQnYWepQcZzjx_ZwhuinlwhaTTWIhfwD8gXCRS2fg3oU&XPtMgBpyYUxVJeLUToGeRJ6eQkY46LOEvK0abmoN569tni4eZK1LtzFy0czqUZqkqGbEh6KmhJ7M6w6S5mLCpl4W&RPR52K27Yu2YMdKbmRZGqNz&yTWH00iOLboQqU_UlVd1o842pdmNnTUp3UDdJqp70gw7VsefKyu&k60YQGp4soDD0_HarBoV9KXbHSicw2v_6IWDB&rymvmhSqD08iIX4rwxlB_7dckAfDrP3CcnQFPd9O55gXTHWQWYvX0W2aTPwNDfySO5AY9DsgyS1N0HZ2XZqS8GCi_vMil3q3Z8fJUy2LKGVLCCzxS5daQ623TbOX56k_LItcBLCk6LPkIVOeurJ_zToDMMjhvVMraGgN9LXOSImU4ZNmWkLdoEZCccTrImVMONuzmlhNeToOhGIXFPd51ulNc8Q5scG9igHM3WG0kqjqqwP3jCj3p37orO1XKT7o&Ouew0p9NDuB5kEYE_W0qITP0twUqtIq&3zXtrXiLF1cdItGDgaJ4BQ58fIdOg6zAHboyXIpVQfoAEn7xeHx7Zrb550jRhMvFNakEWfEDzdH6cmQZlJ1X_1cFpBiTs4YYEOZgGkZIZ6j9rqBWyIi5tKZWiQSXCNXTBi&IANGg8SzP49IJDMnpQzlRe09zovlwYgBS&XnPo&BnJxJB6fC6EXpXlNu3YrIMd78Kpc2vFHZnxhOFwgAEAtror&peFOcLV6DbQd6SQE_hW8n2v02LXmAPRSZPOxW35DLE6CQYCfmFuiFpSMVy9jDy7QRb9HMUkqTgxSRhyEZW_tiEBWqq6g2QoQk45oODbcYnsjrzdyV7aRoSI25lrPiXH3v2YM8QjxlNE2ngfYMvhtTWmVY4azXJnEcscOARls6j8qnXTwdJsRCfzAQVZRhZKCzVRBwO6MHdTBH1OHg7G07Q5iwO8aCvRbZrhlgKQLMD68gNT1OzbHLGTK39FM&YMcwjRpZB0OFg_ETHoQT9xvPo3rt3nUseA9Ti6Zxgxgm5rrhweg0PdB7m0grMmyCQNONjN3cb3B_b7tT9nrJlzmKjYORecPhoCkx_mb2WS9sIIYx37mEQZZHKr9sacHw_EuRZGzdbHvla1A7QQXkcmoZ7KX32xoAfxSu_nQu0MhKxaZoUnZcAZLBhiU5GA0jzSsv4k_y3W9chBo&2G_DyWQwnj2zUnzs26vh9eBpOrSzu6F9nDx8ngy_2NE0zMne2NvJcGgfbu313WDyedjDc5MhnojXwtRstAA99cA&D&82G45n9nE4_TKazWi1q2c7eHykxQdX90N7P&hGLB7_7Xr4OLPf7oZj84Dlv42InulsgBdGY&ttMpqNxp95QYzmTkaf72b27uH_Zjjh_d0PtDu&aB8Hk9loODVEx9fRTfdQZ4MpkX1mv41mdw9Ps4Z4HG4wfrZ&GY1venY44oWGf3ucDKd0fkNrj74QxUP6cjS_vn_64dHgK1ph&DAjPtHJiM7ZA7MmPBtWJ2JoffNlOCH_jWeDq9H9iLbELPHtaDamLXjieCCUXz&dD_gQT5PHh_kQNR2wkBYhhk9G07&YwdQoY&&6NGgWIu7SGl8G42sW1J4gcVz7&PCEUELnvr&BAyY8AEYN7c3wdng9G30l8dKTtM306ctQ_T2dMYPu7_14eE30DibPdjqcfB1dgw9mMnwcjIj9mJqeTLDKw1gczqc_hEdaMvwKHXga3_O0k_Ffn_g8RzQBaww_k7aBmZHczbcRbQ4J7Qu&x6&QF63wn0mNHuyXwbOMaj_rehCZzSx3VytIKVrtHFw9gAdXRM_IySJCwBCI6GbwZfB5OO2ZRgl4ax0v79np4&B6hH&Q96R6JOt74QpZ0V_fIEX6QBexAxInjgY9VJHBBqFr46AjtPe_XZ63e_&pH&Ti&mEKZaNNZgPLFNPfV0M8PRmOiV9sToPr66cJmRaewBtEzfSJjG00ZqEYnJeteTS5CfbEfLa3g9H90_RAx2jnB2IhlmRdawQSlGx60WMdsKNb2ur6TqVnO1b7bO9IFFdDemxw83UEzyP7GLKF6Uh58qArKB9PeTs6Lb99ZMC&_8adDFMNOGuVSuyMgQJ9_AzPPCZUpOHQ41UNoUuKwFmxpSiusKmdtoyuxOksn0bVF74y4itDuYqU02rfBCpJATUzR2qBogPXrtdIRQQdyTQ8B6u0Mt2gIcGyueOD_aVOETS6PNr0lEOZMVyiC6Xbqkq0M9ViqGbkN0BMKVcQRzhl8skKRwPFzdub8DBPAXIrCt9oKwYNxOZ6qVxakclCQhKvbqetLUL5XvFcO5LMkz5Yitfway64MAIMQwEM9s8a3HBGwD&X8pbdFpwq8cQOz&vxQWtpTvCFSAAAYpJq1z_XTpqbRMe&_JPuXet&YuzgX&Qc1siTjfuXvMf5Z3RnqCOvy_ZCY0dKAnPb_2AyJ1kdH_o8dre4nb&2HYDYzOSdRkTtdQm5Xx42uW_bXrzKeXcW_uIQKPePMyDuuGq_tcbwjrRmqwZdkVkQK3syFUKZSwjYcCwhaF829yy0I8hl3IwHA8PgJiFqLLEfe4m5vyP0Th0rBq&wAzbLBXK_uIuEyuvRUUCP9bKdl_iMg&xIfuiByZStdCtbXl4icSVd&Z1YVy&681r&&s1_XEHBeBLKAfE0CCpm4kR5iEAuVwIZOwyllUVOZ5JbgAT0yXelmZQ4O4MZnTnUXvBw4fpIAlaWzehuln4Xf2h4zpGeY&&i5e5EZ6KVjMjp4NTnnND0q8D4oOJ&&Lm3Z8swZQsbZrAuucr_2wtKG&Ta6OBq_nBPiOL_OUbDl6wVqhC22pGK&50vrL6967eGse8R2ujB7txl2Ad83XMQvILemGoKRSH3uoy3W7yLCenLhMp6t0VGx&2sdrY70Mc0NG_rBofLtp07JJ2E8eQts4cVt1C069Huxy1ij2rmDpUM9Na480sJGZcSoitOR0nTG0tSkWcPMHdmU9CS7xdEwXeuYGxcXhPD3Ma&f4&SHmfNvk6lg9tc89e7InpYnsHDDWR_xJFPKXb02nm47N5MHevbG1deWLm_XRqPXD2TnkYuc_toKuO6XFuFay&anLX3UQKCSFcmx_14L5c073QePcG4xDajsMHDUvwO1FRuVTwXu2K5y134lR6IavNds5GMAbUEsIUAY6gT1s1pob9Hev4OjTAeDSRr9HKL11sdSMG8i79oqme02Z9Bjb1LFt9dyU7wnzIxgvvepCWzHVkaxc_e&Uhoq0wz&hUlgB3yRQ_&o8On4SbXV9IgreCe8I9NQUU7RG0xA&oTy5fLGCa6&Nr8noGmnVbGrihBM7Ys0IuGs5mX9EpTjTFhDJzvYcLxS7TiNqNQQr6Vh7jiHaMKum&GT4wuHqpF4hTewjRouMm9JEgW7skc&n4Lc&z3WxwpYv4fUEsDBBQAAAAIAMkNmEd7u8rCewAAAKIAAAAWAAAAZ2l0c3luY2hpc3RhL1JFQURNRS5tZCWNsQ4CMQxD936Fpdv5CIRAbGzMuRJopKpBSe5Q_Xp6x2TZz7InvCS8t1zEg9KtR9GGUK14quHvNzQy7D0b&suomml0pLLjI1FAuAxZZhi&1SXUOop68ANjkXDn_UQrnG1lO6Q0TTiSS8Z5aTlEG1WJnnZwbeOxVtriH1BLAwQUAAAACAA4YptHmgB6rxAAAAAOAAAAJgAAAGdpdHN5bmNoaXN0YS9idWlsZC9naXRzeW5jaGlzdGFfaWdub3JlS88sKa7MS87ILC5J5OICAFBLAwQUAAAACABHYptHC8Yq9hYAAAAUAAAAIwAAAGdpdHN5bmNoaXN0YS9idWlsZC9weXppcGlzdGFfaWdub3JlS88sKa7MS87ILC5JjK&KLNArqOQCAFBLAwQUAAAACABREJhHhkC_bt4DAACCDQAAFgAAAGdpdHN5bmNoaXN0YS9jb25maWcucHm9V9uO2zYQfddXTDdYiEINoXkt4IfdhYPdINgUubQIgkCgZUphV6IEkUrXf9&hTaJkOnH6UD1Y4mVmzpw5vJi3fTcoKLv_mHD7LdXARe1bTVfXuunbd52oeP0HHSQbkiSpm25PGzNLt_0btt4sr5l6Y&pIWnMlj6L8yqWiaQaQJGVDpYRbKpn1Srr936xU2e9JAvgcWAVo&yDUjUJM_1ExSSRrKpwA7hmYGgcBDTol2cLstusaRsVPmx7Gtl9OdS&dlxfT8AbUsWd2Zl4UgrasKOBXSPM0Cw21z9CqNKluoKcDE6roB1bx53WsJa0QPK5RdQOQJ3bcwDfajCwDLpxnxHLgpSqKnCvWShJkPH1QJKXQ8LFSJgvkS&cRDw49Z3NWk51uoskCOqaMs6cpL3pUj5ojTAO8CsIiWpLivHQD6R4Lpd_ouzQACy77&MD2Y03Sa7m9lilcAzEwNlqnxCafZZMVayQLfQRFM3M3NgdXJqdAq757Kg4NCnUSoSHMlK&ggiOjiwoWyG7fUMUc5mQKtxpHwlY983wXQJZUFBKj8k64IK71aFJtuwNr&LLQpe96PahpDCNWvGG5HdJqnxx4S1ME0anA3HieJBMsDsolg91zycxUcmVDjAM1ljqSzkpRLiT6QW75wbtNdZ0MtHJqX_nC2fFFblkWQFvDiq7iQCJ2&p_6rkiy3bfyse_xiCe0oC_y4NQaB9KZADiHW0hfpjCRPfd_ePdxFx34tHsf7f&r5v5ddOD1Tbw7XUrYrk3Dice9gQ8DKj&QfQT_b1Hvr27evI&jf3x71uDuPm6xe3iMD1ySwiuKq&X82j3R4IPTmRMFbn1PGM7LLVRfV52q72JJzACjQg2oXkh1eU4FMlXDMUwLtz0vWfz8L0o9S6h3PWFFtIa_mUWgEi5jWYwtG3hpD5j&j2WIPBPzoUDOcPATfCZu_x0YPRSBiduC9aew2_cE4vRgNj&uqOKi6siVdoc7EUS2TEOb3sDt2EybjxXcKtbnyHweO5bWmaKgwttZHjZI3MSdFs8IqbVbKLyAlj4xR5KEEm9naCYkV&ybPbkc9q25NeLxzHr9EcdshciGoRuKlklJaw3zsRP_YpCsVohGJQtNocazhqv7yWdP1pdsPjuwh8y2GfyyhZezVtYArna6A&75qmn7Qb10fXzE06vYd9fXmbBGBRfHJuamw7JZkOBoxbQXEXzY9ZJeTLKyt9cItyyMrKKXCTfBbGcz198z85WP3CkWaxm1OO6LSUrrC2gYIguWPAZaXZbmeZvA5WwT3TtONr27C643670ujnH9mAH3X8OlG44m&wJQSwMEFAAAAAgAURCYRxyeK79WAAAAbAAAACQAAABnaXRzeW5jaGlzdGEvZXRjL2dpdHN5bmNoaXN0YV9jb25maWdViksKgCAQQPdzCk9QQtCuk0jIZEMK&tCh8PbNpkXL9zEPHSfeOwDV4rw9KTKqTS2r1gCmie2BSxtyZEwk6QrcR3Y_dEaIxWG0FdlLmaBRKkwfz78VXlBLAwQUAAAACAC6XZtH&cubNYkCAADyBQAAKwAAAGdpdHN5bmNoaXN0YS9ldGMvZ2l0c3luY2hpc3RhX2NvbmZpZ19zYW1wbGWtVE2L3DAMvedXqOxh2ks6UCh7mUPpUCi0ZWC3lLKUwZMoY7OOFSxlhumvr_wk22Q&DoVCLral956kp1zBrXUM_hlg03YeoaLQuGMfjTgK0Di9aijC0QlfQqXRYkr4ST103lSoeRV1F6AGJCHleBeE9IjFFdQuYiUUxwiN7zrvqgFcrBG4KNSZel_Dd&cImpl5IgX3G0uFuLUYoIpoRLMDmCrnsqUoVS9wdmKX6lSOCXVmS3KCaXFiD3heFqj4WbLhMT6yQGei5gjGEr4a1cR9xKyz51RwRK_5J9Q4pW4itTnX01jWyKXQR7dQxVV0nbwqhqISluIyirhw5CntBx625qTX8aQCirszHmpz_pWSFk_Q63r9eQc6ne23m3x_UwyPmyTGW2KZ5XXaMTB1HZEZinTaXK_v1yniO0_AadamVyFBxjGV8JHaVs9A2m43jnERAlb7d0CdU_3YHDzWZaG9ihlxA4Is_3ROVDvDfKZY&z_mbkIcmabzWNhgzIeZJocJep&BhciDpTO0fWXBWDR1noNr8ekw0po4dR6qg2oerQkrpbrXAeY9WE2hjNhyojrgCGug6X0i69VWN3k&4GR8n7357v16PQGro71X8Ipi2p0s&0ln8nyzdTmbfRQ6XFhzynvMaryUk8tRD7adqsaOKruv0YvRhiXioriLessu7Wk22hc6uoQ&X52&IcVsrCl6_7Dj8&j5oruQr3YXsbrWqmT2X5CIWMKWIJDkBfPardTP1dtVWeQ693nR&oWQwjO7BJ&UcY&GNSOD9KIdDCqniNiS4GPiD96rVySawA1GHnZ&GMWyoDT5AWLS8PBeFlP_Xmg&Bm3gNvb4IsULUInlOfYlxRAxMfwBUEsDBBQAAAAIAFEQmEe_Tbr3ZAAAAIQAAAAhAAAAZ2l0c3luY2hpc3RhL2V0Yy9weXppcGlzdGFfY29uZmlnVYtLDoQgDED3nMITyG5MTOYkkwmpWKEJYFPKAk8vcef2fX4BCwqkvwFmt5Og11P69J0Cae3FR6oKj2ySBo6qXFdrh45tm&2ZbQbxrX4W_1ouYndQwgIZx7c1SvurcKOYuRtzA1BLAwQUAAAACABREJhH7EuTMRQNAABsOAAAHAAAAGdpdHN5bmNoaXN0YS9naXRzeW5jaGlzdGEucHm9G2tv28jxu37F1heBZKIjkrToBwM6IHDinIDUKWIXxTUPgqYomReKFEjKjtH0v3dmZ9_7lGzHd&kQkbuz89p57SxdbbZtN7D_tp9U9FjUVdkM8q1V40O1KeXzMh9K871u1_uqWcvXTk0M5Wa7qmr1fj50ALd4P1HU2mZVqYX9bVNkYmjSlXWbL2PiJ5GvgpR6J2j1amBIJpO3i4ts8fbs&Yc32eni3Rs2Z1G6roZq3bRdGeH0_W9nJ78uzi9euXAAhriuqn7Is_CCk&dnp4u34QXEQTSZvHr9enGxeH&26p0k8M9XFxdvPpyd45rvn9L0KUCt6&Yyr7kay24yoV8AEMKm63J4x8dii0yUMCaA0x5AyuuylgpKF2en75NJcWWgAe2X_ebXvFnWgAonx5at2m6TD4PFxKkci6NpnPcFGkDSs5&ZNK4RRZOr903Z9&ka3iJJRC9WqBPJer5cSp6KK9i1os77np2C2cTt5e9lMSTHExCUsWW5YllWNdWQZXFf1qsZQ6Iztr267asirzN6vcz7UjxukMsZ63eXGdphD&KctQ2MVL3Y1eX8NK&7ktPgVBhD1CmuB2j80YMWIZi13jWYYgBA1LOe5kzBFP&VwyaT6llPa45hXr9ItlE5MLqsOtBY291yBYFUfL4rh13XuGT_QsowMWRZP3RCu0IlYu0R7NZ82nOR8RcI4Q9wgT&T&ohNWaw0Nwvoa6bk0EwmM1e4GY80KTevWKsrSYhNZLJoN9u8K0mK7PKWY4&x7cWM4c9LzrpgvNhsaU4wxgH4M6IU1rbgxBfNqj1sc4gA1YRhyLAa24nV8JYbeyMWwNbF0ZeIPTOxpF25rfOijKM0mkWf0ijRI0_jGQStp_bQpwagnnz&Au7&jEVPzKnvX54gPJ8ZDz2cL_F8FYp8dAKBYQDD0mpgN9VwJZkHVa7Lbyya9hFusy1Sok2UwOYAnuIeoQc7sEz8c6xW7L3h1KZmTevlJFKIIMVVzOFsK9ax41VRQBQ6vJtd2w4ZcHnlRQA1gxLJZ40H843jbiL0INycwgzaaTNk_6JNtWJNO_iVNMX0AIYDix9&&94BL2hdaFRM8aQ2TKGivZJB5uNnMlzYaYgJxGCGCCVFLqIxHrd9imjS39uqiRXWGXMSrXDWQA59MPpgohZ0IKUwMKMGqpW0BmKgAL06kfq04qe3LwxwxAFNCOtikKACijLiVrxKEokkLLWDKgjkIBSsCysYU89KwoGvdQQHaIdY7zhK&1qZhcZU9agrC25lgkrdMSuD6s3T5q8Nn3jyDV8&SloleEKYgnJo4SNkszDBqwL0e05GBT7bPzBiQhh8kTiVgWBNZeT5ShQIc1Qc6Cxzy4W5erIqBl8UDpPm223ZLHm2SbzwpdO5Dn08CZTfwAp6EUDcSCQWyw0TsHrHzGBkuhJhEyOcIVEKuGlKxiCuQpMfe62wDhoTQd22haoZWhHmrbViaTBeERxtrgxW5lrDAIQijETtMEOETJsSS6QxCVX1_TVg79qNZFYrHnbeS_s8D7awrzFBHN1cHiUs7znTx8b2pzddNYApqqRobY2hnP0bbVDqgBKYOBxrrL2GcpoM1eKcqiRCCNay4wA0FQuzFoUUU&9MrJuvGAo83gAVzVgmJ&Lsv8vL1&m1kW31456Me1NeLvPrjA52RgLmKdPKwrstnAlcIlQxJqnCqjO4zt0WDTBT690Ue68HmnW89EAc4&WmpgjeoyA&Pv&M5njOjBwr5Hl&zER9nvd7_o_UHfuK1cesRWjf7l2NPH4ZosqDgJbrPlQprEyB54yONDpTwel_qJpdyUztjJnJSh01OOrDRchYyTBSJSjiqlr4aQthZhBca5HUuROsM3pIYpcnu7ukdsbkIff5fZI9wwC8K4ZMLOZHQRja8mgmJID0Ps1nbLpk00s2&Y1Nfz2e&uN4es6m&4l8_hzF5ivFS40cT0h&&ftzyZ1XXpCw9y0wpIp0ieH2IuZ&TonxsFw3EhUs9z7Pr9G7xXF2aIWfH1MHwAjDHCATipWNv1Q_xN7h0XbM3Zb6eRrLTCG&Y2LdJ9Ih7kb5WrY3DefM1KFR6ARDYaR0FDFkWCyzFSZTwdCZUmPv7zqvd2UM&n3nAuAOu3mTdw0q7egkbzDmA1LhMxgvRfDmBnUUPLWP1AsBlbn1A0fi9nEyoN9zs4bYUwyikcOfX85YcZU3a4p9nA6ySMDoWgL4RYJBXqNIoRzb9LFgTKQ26gRp7zJivpwmnBaul0bw16ykTXmTeW75Iny84W0nsDWN86Mm9lmBAR8xMhIrRo1mGeYHal8Z4SHh2YHAaQN&EUD8TXNg875pl9WqKpcjApigyxKORopvS4YJ38ihy5t_VXaZjTQ2kICrtLuuEJudi0pOY86tqjFwSFkJ2XFfxuXw_ipcIkeNKtEr8iDTuMB8n3hgl9tkOfmFEJ7HQ6xxMCjKWofIO21Qhd6eUAnc1UrqhfERDCEl_4eze1FWoWaUJB_j4DMRjq3sQTnIH2YKfdsNUAUFvXKGvd95sFvsNOCkkThBQRZ6OmwpJbk3AbLug&UbfLBrVE_vRimhrCtJJj5HhtlKrn7yIjh2b6sWDo8rVW5XUFrxsL7bbrmK2G05HLOCN3rJTDd5s8vr_hbtVDMhiTiy__1iNHe&uPeVM2pblBfGFpjR8zH87Ydc7c&1sj0Oxt1rt8UL2ExwgRP9kG_2j_tkRAROAnIJluoe585hIQktlFljk38t9QDYaw4rfDLCC8AyFVl_NFQDcDQeMFeNZ4HkELgKEaqGNmOKWup36ZWfIFxYUsdolZfSfuheF_Frd3i0Q1z8AgZRVQ15M4fEfjb7_RdWUJVGJJna86DvOq47sWwO1Bnm201zILGO_WZhYdcVlm9yzOiXBA&xiEuK&sSmPTqquChUtKzrPsPSrXGHj0R5UsARtS&tT706Y4lm1gm3j7tcAfp3xdKcdBuDbi4tq3QmPf&g52DJDCWtu11I1i0KaDl6V27aofRc&cChiI7&DjL_CYAzpsF9Qvz_zx0cPxsRrJFJ6JC_68qjJEgmTCAUiUYocmkOEdQiBxUQJmesNKINrDdsyxfqLqCiiImTiXkGk6PKKIPbuC&8urKGVX4Yhbk&qozxz3ch1mZhcrMRbSb7UO9FMkLRwi0UO3KgySC90yovDowdgcJC_HzlRm874FRWC9gvr_&CmK7F&1CeHI3xUuohOvN3Z5SRMc4PKe1OvDlqe2y2RC1HQEYp5&IzWvM92mZqWrzIDPq6OFapYX1lM7FbKLoQMuPHf&&nVFpGlRWqQ0SrwToTqXapLEBGGU2Nzqqal5XDxGqa8imSnQu&3G22YtcFgqpZls0wfx6umCfGLYPBnJV_9FdSR_yIPRUYeQsRr&rVVZL7hZRqVhg8maIRHvwmjB6esb&JzaRa4vy2KS7atj5cSAwAlZmfULqFjguA&XVnyMtZMrG5n5r1UNJ6Zu6plTH3Kk90FU&4TxxkSzQgoRbsrstuxvAEPN8LiRAzdcw3&m27dmiLtp5HV8OwjWYMEFar26zva7pTm7Gi7AZx77YDirztv5eYhMLGad&ftN3yAHMCStY0foF2Wqkr2DCmrty2fYUGJWKC2XcOVHDeza5zaXuQisDKyYjdHbUMs9i9Wy0rsTn1HdZ15H6ilDN8xiPslz0Wtg9Ul94dXbAECjAICcXGarWzRrgMHl6DRzAcoDjDAwvAJcFaGFmReffH_Al1YB&ElFD5PRXkZ_RH0ZBg5iEqCnD0UB2pKx&wMi9Yyq92bHeiSCtJ0Ce&GGqNzKeX7nNhVQKp4tJCaom8tyRNDi8brbPH145VTj8kJ8d2LzHNIvL_grqrqfxYQSo3uTU_UphHaRrJFE6zHBXmE9VhEKvkq6hOYigqqOUMDxye6iL_mIjvJ2&y_qv5ScXQbvHKc37R7SBfgWF1XduJbLdq67q9qavma_9&1ipdRDbLFKVjc39UXUdt9Dkb_xML6_sLS2h5dWV&HqlklXAJM24fffZcrMcTg9YV&XkCFh9kPSf8R&7VgmlXWGzRbCyiSu4UTDZO&n1XZlCPNcNSSWI7paAWQnWYkF_7Eyzt_kRdkxsEslwYV_zIvKcZ&ON6CFSOhxThskescByIDe&tZWXrFa4EO8gvWKn0kCvNeAj&ld_KcjuwN&wHG695z0pjnYjS3PLjIw2GfwSx47cQiE8GbplMaD8O8IG78Jh8AD6bD4onEBm7IVvvqnjPHiu2VNywv&tAHEjk7b8WaZryRKjjjB_xEuFkYruVi&W_RETglLfCCWjXUQscu8dIDGTy47ZueYsT_60TWoKmYrrNiE2YupBOp0as9LJnyxQXlpBvcPOoKX5zhQUEnC_wokXF_qLz06LYzdmYBpihA_31mxyCoHEyBx8CGUCcbn2dYKB9eaw2YSw_SPiPLz4jDX0jZ9gTEqjwIIm8ZBn&uizLkHqW8a&MiBEE_z9QSwMEFAAAAAgAURCYR5MG1zIDAAAAAQAAACAAAABnaXRzeW5jaGlzdGEvZ2l0c3luY2hpc3RhX2lnbm9yZeMCAFBLAwQUAAAACABREJhHzEr4_DIBAAAgAwAAGwAAAGdpdHN5bmNoaXN0YS9zeW5jX2NvbmZpZy5weZ2SPWvDMBCGd&_Kgw62IQRDoYRChqZdunRoCx2FYp9jg6Izp7ND&n1l2UlcnDZQoUX3vrqPR6r3DbFATrasd1HEaEgXyXBMoyg32jn4wu2L7p5DcNSWG_1wiKSPEYDfBZagVG1rUSpxaMogBAngzrUNcjLNtIBgWp7vjP4_unTIHTKsITaUa1ORk&iihp7XsMpW2SXY_jtW79ELb2Rx4vYzHIiLmYAN5ZUq0Ij22v1Dlp0a7mfZobxaeRLhetsKuulMjNKyhSTuO4kXEE9SxZ7bCO7dh10txMc&4N1CF1q9OlhAoxot1Uxi3JPgdU1YW1ciKyE1_Lzlk9tfLKHKyXFhsyEyqO0NPvNaPa1Zes8MzmuE93G0_X&&XBjigNtCd77zH&83nUI6PY83zd4q9RWib1BLAwQUAAAACABREJhHhbcHVRUBAABVAgAAFAAAAGdpdHN5bmNoaXN0YS90ZXN0LnB5dZG9bsQgEIR7noLmBBTh_khu8l_kO6WKIoRgjZEAW8BFytsHG3AcKans2Zn9vLu2fpljxmoOozXIVuVmY2zYZfoKSrQEiuBmqWmVrMtDhCG09kPEQwdxA&l1q1FibF7Dk01ZEoZxC&NUIvAJjvaeh8e7t2fW7UkG7SCmAn3&QGo6wC85gvQvNUBZMf_FjXP0Mudfsz31GiUnKpPK1gNL_AafqFsZQe7aQ0rSFEX6V36ad&Q_stS6D6WmchUNI86QMmW3qOyN29FFW62MVAv8fnv03sNp_aW8V5cyViFJ_sVBC_yMDuXlNLqZYrQOKIGszsef0N0KIn9hub76hW6OHbEQ60mEwMOAiRBe2iAEWXeq2yH0DVBLAQIUAxQAAAAIAFEQmEcptW2jmBoAAH9GAAAUAAAAAAAAAAAAAACkgQAAAABnaXRzeW5jaGlzdGEvTElDRU5TRVBLAQIUAxQAAAAIAMkNmEd7u8rCewAAAKIAAAAWAAAAAAAAAAAAAACkgcoaAABnaXRzeW5jaGlzdGEvUkVBRE1FLm1kUEsBAhQDFAAAAAgAOGKbR5oAeq8QAAAADgAAACYAAAAAAAAAAAAAAKSBeRsAAGdpdHN5bmNoaXN0YS9idWlsZC9naXRzeW5jaGlzdGFfaWdub3JlUEsBAhQDFAAAAAgAR2KbRwvGKvYWAAAAFAAAACMAAAAAAAAAAAAAAKSBzRsAAGdpdHN5bmNoaXN0YS9idWlsZC9weXppcGlzdGFfaWdub3JlUEsBAhQDFAAAAAgAURCYR4ZAvm7eAwAAgg0AABYAAAAAAAAAAAAAAKSBJBwAAGdpdHN5bmNoaXN0YS9jb25maWcucHlQSwECFAMUAAAACABREJhHHJ4rv1YAAABsAAAAJAAAAAAAAAAAAAAApIE2IAAAZ2l0c3luY2hpc3RhL2V0Yy9naXRzeW5jaGlzdGFfY29uZmlnUEsBAhQDFAAAAAgAul2bR&3LmzWJAgAA8gUAACsAAAAAAAAAAAAAAKSBziAAAGdpdHN5bmNoaXN0YS9ldGMvZ2l0c3luY2hpc3RhX2NvbmZpZ19zYW1wbGVQSwECFAMUAAAACABREJhHvk2692QAAACEAAAAIQAAAAAAAAAAAAAApIGgIwAAZ2l0c3luY2hpc3RhL2V0Yy9weXppcGlzdGFfY29uZmlnUEsBAhQDFAAAAAgAURCYR_xLkzEUDQAAbDgAABwAAAAAAAAAAAAAAKSBQyQAAGdpdHN5bmNoaXN0YS9naXRzeW5jaGlzdGEucHlQSwECFAMUAAAACABREJhHkwbXMgMAAAABAAAAIAAAAAAAAAAAAAAApIGRMQAAZ2l0c3luY2hpc3RhL2dpdHN5bmNoaXN0YV9pZ25vcmVQSwECFAMUAAAACABREJhHzEr4_DIBAAAgAwAAGwAAAAAAAAAAAAAApIHSMQAAZ2l0c3luY2hpc3RhL3N5bmNfY29uZmlnLnB5UEsBAhQDFAAAAAgAURCYR4W3B1UVAQAAVQIAABQAAAAAAAAAAAAAAKSBPTMAAGdpdHN5bmNoaXN0YS90ZXN0LnB5UEsFBgAAAAAMAAwAjAMAAIQ0AABFAGdlbmVyYXRlZCBieSBweXppcGlzdGEucHkgKHNlZSBodHRwczovL2dpdGh1Yi5jb20vbWFyY3VzNjcvcHl6aXBpc3RhKQ==
'''

def main():

  try:  

    print("Decoding base64 encoded ZIP archive into string...")
    binary_zip_string = base64.b64decode(zip_string, '_&')
    binary_zip_input = io.StringIO(binary_zip_string)
  
    print("Opening string as ZIP file...")
    zip_file = zipfile.ZipFile(binary_zip_input, "r")
  
    zip_file.printdir()
    
    print("Extracting ...")
    
    zip_file.extractall()
    
    print("All files successfully extracted into local directory.")
  
  except Exception as e:
    
    sys.stderr.write("ERROR '%s' while extracting files!" % str(e))
    
if __name__ == '__main__':
  main()
  
