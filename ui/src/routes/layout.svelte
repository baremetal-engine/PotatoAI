<script>
  import Sidebar from './components/Sidebar.svelte';
  import ChatBubble from './components/ChatBubble.svelte';
  import { onMount } from 'svelte';

  let messages = [
    { sender: 'user', text: 'Hey PotatoAI!', timestamp: '2025-07-04 12:01' },
    { sender: 'ai', text: 'Hello! How can I help today?', timestamp: '2025-07-04 12:02' }
  ];
</script>

<div class="flex h-screen bg-gray-100 text-gray-900">
  <Sidebar />

  <main class="flex-1 flex flex-col p-4 overflow-y-auto">
    <div class="flex-1 space-y-2">
      {#each messages as msg (msg.timestamp)}
        <ChatBubble {msg} />
      {/each}
    </div>
  </main>
</div>

<style>
  main::-webkit-scrollbar {
    width: 0.5rem;
  }
  main::-webkit-scrollbar-thumb {
    background-color: #bbb;
    border-radius: 0.25rem;
  }
</style>
