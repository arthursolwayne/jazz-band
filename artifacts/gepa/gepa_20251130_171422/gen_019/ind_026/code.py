
import pretty_midi

# Create the MIDI file with 160 BPM tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
bar_duration = 1.5
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * bar_duration / 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.375))
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=kick, start=time, end=time + 0.375))
    else:
        drums.notes.append(pretty_midi.Note(velocity=105, pitch=snare, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# 1. Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# Dm7: D, F, A, C
# Start on D, walk down chromatically
bass_notes = [62, 61, 60, 59, 62, 61, 60, 59, 62, 61, 60, 59, 62, 61, 60, 59]  # D, C#, C, B, D, etc.
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# 2. Piano (Diane): Comp on 2 and 4 with 7th chords
# Dm7 = D, F, A, C
# Comp on beats 2 and 4 of each bar
# Bar 2: Dm7 on beat 2, Bar 3: F7 on beat 2, Bar 4: A7 on beat 2
chords = [
    [62, 65, 67, 69],  # Dm7
    [65, 67, 71, 69],  # F7
    [67, 71, 76, 69],  # A7
]
for i, chord in enumerate(chords):
    for note in chord:
        start = 1.5 + (i + 1) * bar_duration + 0.75  # Beat 2 of each bar
        end = start + 0.375
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# 3. Sax (Dante): Motif - start it, leave it hanging, come back and finish it
# Dm7 - D F A C
# Motif: D -> F -> A (up a major third), then leave it hanging on A, come back with C
sax_notes = [
    62,  # D
    65,  # F
    67,  # A
    67,  # A (hold)
    67,  # A
    67,  # A
    69,  # C (resolve)
]
for i, note in enumerate(sax_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=end))

# 4. Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(6):
    start = 1.5 + i * bar_duration / 4
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=end))
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=kick, start=start, end=end))
    else:
        drums.notes.append(pretty_midi.Note(velocity=105, pitch=snare, start=start, end=end))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_cellar_intro.mid")
