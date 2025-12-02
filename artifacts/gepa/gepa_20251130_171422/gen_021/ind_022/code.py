
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with space, dynamics, and subtle rhythm
drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=0.0, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=0.25, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=0.5, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=0.75, end=1.0))

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=0.0, end=0.1))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=0.75, end=0.85))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=0.5, end=0.6))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=1.25, end=1.35))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Dm key: D, F, A, C
# Dm7 chord (D F A C) in first bar of the motif

# Saxophone: Short motif — simple, emotional
# D (D4), F (F4), A (A4), C (C5) — but fall in on the third note, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))  # A4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5))  # C5

# Repeat the motif with slight variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))

# Repeat again, slightly delayed and with a half-step variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75))  # D#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0))  # G4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25))  # A4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5))  # C5

# Marcus: Walking bass line in Dm, chromatic approaches, never the same note twice
# Dm7 walking line
bass_notes = [50, 51, 53, 52, 49, 50, 51, 52, 53, 54, 52, 50, 49, 51, 52, 50]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25]
for i, time in enumerate(bass_times):
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=bass_notes[i], start=time, end=time + 0.25))

# Diane: Piano comping on 2 and 4 with Dm7 chords (D F A C)
# Dm7 (D, F, A, C)
piano_notes = [
    62, 65, 69, 72,  # Dm7 on 2
    62, 65, 69, 72   # Dm7 on 4
]
piano_times = [2.0, 2.25, 2.5, 2.75, 4.0, 4.25, 4.5, 4.75]
for i, time in enumerate(piano_times):
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=piano_notes[i], start=time, end=time + 0.25))

# Little Ray: Drums continue with the same pattern, but more aggressive
# Bar 2-4 (1.5 - 6.0s): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for i in range(2):  # two full bars (bars 2 and 3)
    start = 1.5 + i * bar_length

    # hihat on every eighth
    for j in range(8):
        piano.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=start + j * 0.125, end=start + j * 0.125 + 0.125))
    
    # kick on 1 and 3
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=start, end=start + 0.1))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=start + 0.75, end=start + 0.85))

    # snare on 2 and 4
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=start + 0.5, end=start + 0.6))
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=snare, start=start + 1.25, end=start + 1.35))

# Append the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('dante_intro.mid')
