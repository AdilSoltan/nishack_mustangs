import React from 'react';
const Regin = () => {
  return (
    <div className="max-w-[1240px] m-auto p-4 h-screen">
      <h1 className="text-2xl font-bold text-center p-4">Регистрация</h1>
      <form className="max-w-[600px] m-auto">
        {% csrf_token %}
        <div className="grid grid-cols-2 gap-2">
          <input
            className="border shadow-lg p-3 first-letter:"
            type="text"
            name="first_name"
            placeholder="Ваше имя"
          />
          <input
            className="border shadow-lg p-3 first-letter:"
            type="text"
            name="last_name"
            placeholder="Ваша фамилия"
          />
        </div>
        <input
          className="w-full my-2 border shadow-lg p-3 first-letter:"
          type="email"
          name="email"
          placeholder="Ваша почта"
        />
        <input
          className="w-full my-2 border shadow-lg p-3 first-letter:"
          type="text"
          name="phone_number"
          placeholder="Ваш номер"
        />
        <input
          className="w-full my-2 border shadow-lg p-3 first-letter:"
          type="text"
          placeholder="Создайте пароль "
        />
        <input
          className="w-full my-2 border shadow-lg p-3 first-letter:"
          type="password"
          placeholder="Подтверждение пароля "
        />
        <div className="py-4">
          <p className="text-xl font-bold ">Ваша роль</p>
            <input type="radio" name="role" value="Ученик" /> {' '}
          <label for="html">Ученик</label> {' '}
          <input type="radio" name="role" value="Учитель" /> {' '}
          <label for="javascript">Учитель</label>
        </div>
        <button className="border shadow-lg p-3 w-full mt-2">
          Создать аккаунт
        </button>
      </form>
    </div>
  );
};

export default Regin;