export const useTest = () => {
    console.log('test.ts => useTest composables')
    return useState('foo', () => 'bar')
}