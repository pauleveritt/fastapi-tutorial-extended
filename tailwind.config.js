module.exports = {
    content: [
        "./src/**/*.{html,js}",
        "./templates/**/*.{html,js}",
        "./index.html",
    ],
    plugins: [require("@tailwindcss/typography"), require("daisyui")],
};
