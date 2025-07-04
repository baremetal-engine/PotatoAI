<script>
  let folders = ['Project Alpha', 'Local Tasks', 'Global Ideas'];
  let activeFolder = folders[0];

  function selectFolder(folder) {
    activeFolder = folder;
  }
</script>

<aside class="w-64 bg-white border-r shadow-sm p-4 flex flex-col">
  <h2 class="text-xl font-bold mb-4">🗂 Projects</h2>
  <ul class="space-y-2 flex-1 overflow-y-auto">
    {#each folders as folder}
    <li>
    <button
        class={`w-full text-left cursor-pointer px-3 py-2 rounded hover:bg-gray-100 ${folder === activeFolder ? 'bg-gray-200 font-semibold' : ''}`}
        on:click={() => selectFolder(folder)}
    >
        {folder}
    </button>
    </li>
    {/each}
  </ul>
  <button class="mt-4 text-sm text-blue-500 hover:underline">
    ➕ New Folder
  </button>
</aside>
