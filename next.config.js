/** @type {import('next').NextConfig} */
const nextConfig = {
    rewrites: async () => {
        return [
            {
                source: '/api/:path*',
                destination:
                    process.env.NODE_ENV === 'development'
                        ? 'http://127.0.0.1:5328/api/:path*'
                        : '/api/'
            }
        ];
    },
    pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'mdx']
};

// module.exports = nextConfig;

const withNextra = require('nextra')({
    theme: 'nextra-theme-docs',
    themeConfig: './theme.config.jsx'
});

module.exports = withNextra(nextConfig);
