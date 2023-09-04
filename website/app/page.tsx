import Head from 'next/head'

async function getData() {
  // { cache: 'force-cache' } -- for static content 
  // -- for getting every time
  // const res = await fetch('http://127.0.0.1:8000/api/test', { cache: 'no-store' })

  // with 10 seconds cache
  const res = await fetch('http://127.0.0.1:8000/api/test', {next: { revalidate: 10 },})
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.
 
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data')
  }
 
  return res.json()
}

async function getDinoClasses() {
  const res = await fetch('http://127.0.0.1:8000/api/get_class', { cache: 'force-cache' })

  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}
 
export default async function Page() {
  const data = await getData()
  const dino_class = await getDinoClasses()
  return (
    <div style={{ padding: 30 }}>
      <Head>
        <title>Testing API Server</title>
      </Head>
      <div>        
          <div
            key={data.key}>
            <h2>{data.info}</h2 >            
            <h2>{data.key}</h2>            
            {dino_class.map(dino => 
              <div key={dino.title}>                
                <a href={dino.link}>{dino.title}</a>
                <div dangerouslySetInnerHTML={ {__html: dino.header} }></div>
                <div dangerouslySetInnerHTML={ {__html: dino.fullInfo} }></div>
              </div>
            )}      
          </div>
      </div>
    </div>
  )
}