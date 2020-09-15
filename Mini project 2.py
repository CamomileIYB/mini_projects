#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


bookings = pd.read_csv('/home/jupyter-i.babuhivskaya-1/shared/homeworks/python_ds_miniprojects/1/bookings.csv', sep = ';')


# In[4]:


bookings_head = bookings.head(7)


# In[ ]:


# 1. Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. 
# Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные. 
# 2. Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.
# 3. Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.
# 4. На сколько ночей в среднем бронируют отели разных типов?
# 5. Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). 
# Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?
# 6. Проанализируйте даты запланированного прибытия. 
# – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?
# – Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов
# 7. Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
# 8. Создайте колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми?
# 9. Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка 
# (total_kids), в противном случае – False. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, 
# выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.


# In[5]:


bookings_head


# In[6]:


bookings.dtypes


# In[14]:


names = bookings.columns.str.lower().str.replace(' ', '_')


# In[17]:


names


# In[25]:


new_columns = names.values


# In[28]:


old_columns = bookings.columns


# In[29]:


old_columns


# In[32]:


bookings.columns = new_columns


# In[33]:


bookings


# In[36]:


bookings.is_canceled.unique()


# In[40]:


bookings.query('is_canceled == 0')     .groupby('country', as_index = False)     .agg({'hotel': 'count'})     .sort_values('hotel', ascending = False)


# In[47]:


bookings.groupby('hotel', as_index = False)     .agg({'stays_total_nights': 'mean'})     .stays_total_nights.round(2)


# In[66]:


bookings.query('reserved_room_type != assigned_room_type')     .agg({'hotel': 'size'})


# In[ ]:


bookings.groupby(['arrival_date_year', 'arrival_date_month'], as_index = False)     .agg({'hotel': 'count'})     .sort_values('arrival_date_month')


# In[108]:


bookings.query('is_canceled = 1' and 'hotel == "City Hotel"')     .groupby(['arrival_date_year', 'arrival_date_month'], as_index = False)     .agg({'is_canceled': 'count'})     .sort_values(['arrival_date_year', 'is_canceled'])


# In[106]:


bookings.head()


# In[115]:


bookings.adults.describe().round(2)


# In[114]:


bookings.children.describe().round(2)


# In[113]:


bookings.babies.describe().round(2)


# In[116]:


bookings['total_kids'] = bookings.children + bookings.babies


# In[117]:


bookings.head()


# In[122]:


bookings.groupby('hotel', as_index = False)     .agg({'total_kids': 'mean'}).round(2)


# In[142]:


bookings['has_kids'] = bookings.total_kids >= 1


# In[149]:


canceled_orders = bookings.query('is_canceled == 1')         .groupby('has_kids', as_index = False)         .is_canceled.count()


# In[152]:


all_orders = bookings         .groupby('has_kids', as_index = False)         .is_canceled.count()


# In[154]:


(canceled_orders['is_canceled'] / all_orders['is_canceled'] * 100).round(2)


# In[ ]:




