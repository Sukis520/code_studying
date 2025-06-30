from DrissionPage import ChromiumPage
from db import insert_item
from clean import clean_data
import time

def get_items_from_page(page):
    items = []
    goods = page.eles('xpath=//div[@id="content_items_wrapper"]/div[contains(@class, "search-content-col")]')
    print(f"本页商品元素数：{len(goods)}")
    for g in goods:
        try:
            # 商品图片
            img_ele = g.ele('xpath=.//img[contains(@class, "mainImg--")]')
            img_url = img_ele.attr('src') if img_ele else ''
            # 商品价格
            price_ele = g.ele('xpath=.//div[starts-with(@class, "priceInt--")]')
            price_val = price_ele.text if price_ele else ''
            price_val = ''.join([c for c in price_val if c.isdigit() or c == '.'])
            # 商品名称
            name_ele = g.ele('xpath=.//div[starts-with(@class, "title--")]/span')
            name_val = name_ele.text if name_ele else ''
            # 店铺名
            shop_ele = g.ele('xpath=.//span[contains(@class, "shopNameText--")]')
            shop_val = shop_ele.text if shop_ele else ''
            # 商品链接
            url_ele = g.ele('xpath=.//a[contains(@href, "item.taobao.com")]')
            url_val = url_ele.attr('href') if url_ele else ''
            if url_val and url_val.startswith('//'):
                url_val = 'https:' + url_val
            # 销量
            sales_ele = g.ele('xpath=.//span[contains(@class, "realSales--")]')
            sales_val = sales_ele.text if sales_ele else ''
            brand_val = ''

            print(f"商品名称: {name_val}, 价格: {price_val}, 店铺: {shop_val}, 链接: {url_val}")

            items.append({
                'name': name_val,
                'price': price_val,
                'img_url': img_url,
                'shop': shop_val,
                'url': url_val,
                'sales': sales_val,
                'brand': brand_val
            })
        except Exception as e:
            print(f"提取商品信息时出错: {e}")
            continue
    return items

def main(keyword='女装', max_pages=3):
    page = ChromiumPage()
    page.get(f'https://s.taobao.com/search?q={keyword}')
    time.sleep(5)  # 等待页面初始加载
    all_items = []
    for i in range(max_pages):
        time.sleep(3)  # 等待每页商品渲染
        items = get_items_from_page(page)
        all_items.extend(items)
        next_btn = page.ele('css selector=.next')
        if next_btn and 'disabled' not in next_btn.attrs.get('class', ''):
            next_btn.click()
        else:
            break
    clean_items = clean_data(all_items)
    for item in clean_items:
        insert_item(item)
    print(f'共采集并入库 {len(clean_items)} 条数据')
    page.quit()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()