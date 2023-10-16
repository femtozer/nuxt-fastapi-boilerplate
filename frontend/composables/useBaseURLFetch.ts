export const useBaseURLFetch: typeof useFetch = (request, opts?) => {
  const config = useRuntimeConfig()
  return useFetch(request, { baseURL: config.baseURL ?? config.public.baseURL, key: request.toString(), ...opts })
}
