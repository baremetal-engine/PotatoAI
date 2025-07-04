<script>
  export let msg;
</script>

<div class="flex items-start gap-2 {msg.sender === 'user' ? 'justify-end' : 'justify-start'}">
  {#if msg.sender !== 'user'}
    <div class="bg-gray-300 text-black p-3 rounded-xl max-w-lg shadow-sm">
      <p class="text-sm">{msg.text}</p>
      <span class="block text-xs text-right mt-1 text-gray-600">{msg.timestamp}</span>
    </div>
  {:else}
    <div class="bg-blue-600 text-white p-3 rounded-xl max-w-lg shadow-sm">
      <p class="text-sm">{msg.text}</p>
      <span class="block text-xs text-right mt-1 text-blue-200">{msg.timestamp}</span>
    </div>
  {/if}
</div>
