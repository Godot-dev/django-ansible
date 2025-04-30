<script setup>
// eslint-disable-next-line no-undef
defineProps({
  fields: Array,
  formTitle: String,
  submitText: String,
  redirectionPath: String,
  redirectionText: String,
  accText: String,
  submit: Function,
});
let formData = {};
</script>

<template>
  <div class="container">
    <div class="heading">{{ formTitle }}</div>
    <form @submit.prevent="submit(formData)">
      <div v-for="field in fields" :key="field.name" class="input-field">
        <input :required="field.required"
               :type="field.type"
               :id="field.name"
               v-model="formData[field.name]"
               :placeholder="field.placeholder"
        />
        <label :for="field.name">{{ field.name.charAt(0).toUpperCase() + field.name.slice(1) }}</label>
      </div>
      <div class="btn-container">
        <button type="submit">
          {{ submitText }}
          <div class="arrow-wrapper">
            <div class="arrow"></div>
          </div>
        </button>
        <div class="acc-text">
          {{ accText }}
          <router-link :to="redirectionPath">{{ redirectionText }}</router-link>
        </div>
      </div>
    </form>
  </div>
</template>

<style scoped>

*{
  --primary-color: #645bff;
  --secondary-color: #fff;
  --hover-color: #111;
  --arrow-width: 10px;
  --arrow-stroke: 2px;
}
.container {

  justify-content: center; /* horizontal */
  align-items: center;     /* vertical */
  display: flex;
  flex: 1;
  flex-direction: column;

  background-color: var(--secondary-color);
}

.container .heading {
  font-size: 1.3rem;
  margin-bottom: 20px;
  font-weight: bolder;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  gap: 30px;
  border: solid 1px #8d8d8d;
  border-radius: 20px;
  padding: 3em;
  margin: 1em;
}

form .btn-container {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 20px;
}

.input-field {
  position: relative;
}

.input-field label {
  position: absolute;
  color: #8d8d8d;
  pointer-events: none;
  background-color: transparent;
  left: 15px;
  transform: translateY(0.6rem);
  transition: all 0.3s ease;
}

.input-field input {
  padding: 10px 15px;
  font-size: 1rem;
  border-radius: 8px;
  border: solid 1px #8d8d8d;
  letter-spacing: 1px;
  width: 95%;
}

.input-field input:focus,
.input-field input:valid {
  outline: none;
  border: solid 1px var(--primary-color);
}

.input-field input:focus ~ label,
.input-field input:valid ~ label {
  transform: translateY(-51%) translateX(-10px) scale(0.8);
  background-color: #fff;
  padding: 0px 5px;
  color: var(--primary-color);
  font-weight: bold;
  letter-spacing: 1px;
  border: none;
  border-radius: 100px;
}

button {
  box-sizing: border-box;
  border: 0;
  border-radius: 20px;
  color: var(--secondary-color);
  padding: 1em 1.8em;
  background: var(--primary-color);
  display: flex;
  transition: 0.2s background;
  align-items: center;
  gap: 0.6em;
  font-weight: bold;
}

button .arrow-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

button .arrow {
  margin-top: 1px;
  width: var(--arrow-width);
  background: var(--primary-color);
  height: var(--arrow-stroke);
  position: relative;
  transition: 0.2s;
}

button .arrow::before {
  content: "";
  box-sizing: border-box;
  position: absolute;
  border: solid var(--secondary-color);
  border-width: 0 var(--arrow-stroke) var(--arrow-stroke) 0;
  display: inline-block;
  top: -3px;
  right: 3px;
  transition: 0.2s;
  padding: 3px;
  transform: rotate(-45deg);
}

button:hover {
  background-color: var(--hover-color);
  cursor: pointer;
}

button:hover .arrow {
  background: var(--secondary-color);
}

button:hover .arrow:before {
  right: 0;
}

</style>