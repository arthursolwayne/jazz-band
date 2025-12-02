
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature (D minor)
pm.key_signature_changes = [pretty_midi.KeySignature(midi=-2, time=0)]  # D minor

# Set up instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# Define time per beat (0.375 seconds at 160 BPM)
beat = 0.375
bar_length = 4 * beat  # 1.5 seconds per bar

# Helper function to add notes to a track
def add_notes(instrument, notes, time, duration=beat):
    for note in notes:
        n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
        instrument.notes.append(n)

# --- DRUMS (Little Ray) ---
# Kick on 1 and 3 of each bar
add_notes(drums, [36], 0)  # Kick on beat 1
add_notes(drums, [36], beat * 3)  # Kick on beat 3

# Snare on 2 and 4
add_notes(drums, [38], beat * 1)  # Snare on beat 2
add_notes(drums, [38], beat * 3)  # Snare on beat 4

# Hi-hats on every eighth note
for i in range(0, 4):
    add_notes(drums, [42], beat * i)  # Hi-hat

# Fill on beat 3 of bar 3
add_notes(drums, [36, 38, 42, 43], beat * 6)  # Kick, snare, hi-hat, cymbal

# --- BASS (Marcus) - Walking line in Dm (D, F, G, Bb) with chromatic approaches ---
# Bar 1: D -> F -> G -> Bb
# Bar 2: Bb -> C -> D -> F
# Bar 3: F -> G -> A -> Bb
# Bar 4: Bb -> C -> D -> F

notes = [
    [62, 65, 67, 69],  # D, F, G, Bb
    [69, 60, 62, 65],  # Bb, C, D, F
    [65, 67, 69, 69],  # F, G, A, Bb
    [69, 60, 62, 65],  # Bb, C, D, F
]

for i, bar_notes in enumerate(notes):
    for j, note in enumerate(bar_notes):
        add_notes(bass, [note], beat * (i * 4 + j), duration=beat / 2)

# --- PIANO (Diane) - Open voicings, resolving on beat 4 ---
# Bar 1: Dm7 (D, F, A, C)
# Bar 2: Bbm7 (Bb, D, F, A)
# Bar 3: F7 (F, A, C, E)
# Bar 4: Dm7 (D, F, A, C)

chords = [
    [62, 65, 67, 60],  # Dm7
    [69, 62, 65, 67],  # Bbm7
    [65, 67, 60, 64],  # F7
    [62, 65, 67, 60],  # Dm7
]

for i, chord in enumerate(chords):
    # Play on beat 2 and 4
    for j in [1, 3]:
        add_notes(piano, chord, beat * (i * 4 + j), duration=beat / 2)

# --- SAX (You) - Haunting motif: Dm7 → F → C → rest, then repeat on beat 3, with a half rest at the end ---
# Bar 1: D (62), F (65), C (60) + rest
# Bar 3: repeat the motif on beat 3

motif = [62, 65, 60]
sax_notes = [
    [62, 65, 60],  # Bar 1
    [],            # Bar 2 (rest)
    [62, 65, 60],  # Bar 3
    [],            # Bar 4 (half rest)
]

for i, notes in enumerate(sax_notes):
    for j, note in enumerate(notes):
        add_notes(sax, [note], beat * (i * 4 + j), duration=beat / 3)

# Add half rest at end of bar 4
add_notes(sax, [], beat * 12, duration=beat * 2)

# Save the MIDI file
pm.write('Wayne_Leans_Forward.mid')

print("MIDI file generated: 'Wayne_Leans_Forward.mid'")
