
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

# Time per beat in seconds (BPM = 160 → 60 / 160 = 0.375s per beat)
beat = 0.375

# Function to add note
def add_note(instr, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instr.notes.append(note)

# -----------------------------
# Drums: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: [Kick, Hihat, Hihat, Snare]
# Bar 2: [Kick, Hihat, Hihat, Snare]
# Bar 3: [Kick, Hihat, Hihat, Snare]
# Bar 4: [Kick, Hihat, Hihat, Snare]
# Each bar is 1.5s long (4 beats)
for bar in range(4):
    bar_start = bar * 1.5
    # Kick on 1
    add_note(drums, 36, bar_start + 0.0, bar_start + 0.1)
    # Snare on 2
    add_note(drums, 38, bar_start + 0.75, bar_start + 0.8)
    # Hihat on every 8th
    for i in range(4):
        add_note(drums, 42, bar_start + i * 0.375, bar_start + i * 0.375 + 0.05)

# -----------------------------
# Bass: Marcus
# Walking line in Dm, roots and fifths, chromatic approaches

# Dm = D - F - A
# Root = D2 (MIDI 38)
# Fifth = A2 (MIDI 45)
# Chromatic approaches on the upbeats

# Bar 1 (Dm)
add_note(bass, 38, 0.0, 0.375)  # 1
add_note(bass, 45, 0.375, 0.75)  # 2
add_note(bass, 37, 0.75, 1.125)  # &1
add_note(bass, 38, 1.125, 1.5)  # 3

# Bar 2 (Fm)
add_note(bass, 41, 1.5, 1.875)  # 1
add_note(bass, 48, 1.875, 2.25)  # 2
add_note(bass, 47, 2.25, 2.625)  # &1
add_note(bass, 41, 2.625, 3.0)  # 3

# Bar 3 (A°)
add_note(bass, 45, 3.0, 3.375)  # 1
add_note(bass, 52, 3.375, 3.75)  # 2
add_note(bass, 51, 3.75, 4.125)  # &1
add_note(bass, 45, 4.125, 4.5)  # 3

# Bar 4 (Dm)
add_note(bass, 38, 4.5, 4.875)  # 1
add_note(bass, 45, 4.875, 5.25)  # 2
add_note(bass, 37, 5.25, 5.625)  # &1
add_note(bass, 38, 5.625, 6.0)  # 3

# -----------------------------
# Piano: Diane
# Open voicings, one chord per bar, resolve on the last

def add_chord(chord, bar_start, duration, vel=100):
    for pitch in chord:
        add_note(piano, pitch, bar_start, bar_start + duration, vel)

# Bar 1: Dm7 - D - F - A - C
add_chord([62, 65, 67, 70], 0.0, 0.75)  # On 2 and 4

# Bar 2: Fm7 - F - A♭ - C - E♭
add_chord([65, 67, 69, 71], 1.5, 0.75)

# Bar 3: A°7 - A - C - E - G
add_chord([67, 70, 72, 75], 3.0, 0.75)

# Bar 4: Dm7 (resolve) - D - F - A - C
add_chord([62, 65, 67, 70], 4.5, 0.75)

# -----------------------------
# Sax: You
# Motif: D (MIDI 62) descending to C (60), then back up to D

# Bar 1: D (62) on beat 1
add_note(sax, 62, 0.0, 0.375)

# Bar 2: C (60) on beat 1, then D (62) on beat 3
add_note(sax, 60, 1.5, 1.875)
add_note(sax, 62, 3.0, 3.375)

# Bar 3: C (60) on beat 1, then D (62) on beat 3
add_note(sax, 60, 3.0, 3.375)
add_note(sax, 62, 4.5, 4.875)

# Bar 4: D (62) on beat 1, resolving
add_note(sax, 62, 4.5, 5.25)

# -----------------------------
# Add instruments to the MIDI
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
# midi.write disabled
