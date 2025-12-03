
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    (36, 0.0),   # Kick on beat 1
    (42, 0.375), # Hihat on 1&
    (38, 0.75),  # Snare on 2
    (42, 1.125), # Hihat on 2&
    (36, 1.5),   # Kick on 3
    (42, 1.875), # Hihat on 3&
    (38, 2.25),  # Snare on 4
    (42, 2.625)  # Hihat on 4&
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, Eb), with chromatic approaches
bass_notes = [
    (38, 1.5),  # F2 (root)
    (40, 1.75), # F#2 (chromatic up)
    (43, 2.0),  # Ab2 (fifth)
    (44, 2.25), # A2 (chromatic up)
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5),  # F (F4)
    (60, 1.5),  # C (C5)
    (62, 1.5),  # D (D5)
    (64, 1.5),  # Eb (Eb5)
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: Start the motif — a questioning phrase, one short motif, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, Db
sax_notes = [
    (53, 1.5),  # F4
    (57, 1.75), # Ab4
    (58, 2.0),  # A4
    (60, 2.25), # C5 (end of bar, unresolved)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Fm walking (F, Ab, D, Eb)
bass_notes = [
    (38, 3.0),  # F2
    (40, 3.25), # F#2 (chromatic up)
    (43, 3.5),  # Ab2
    (44, 3.75), # A2 (chromatic up)
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Bar 3: Dm7 (D, F, A, C)
piano_notes = [
    (50, 3.0),  # D4
    (55, 3.0),  # F4
    (57, 3.0),  # A4
    (60, 3.0),  # C5
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: Continue the motif, a half-answer
sax_notes = [
    (60, 3.0),  # C5 (continuation of motif)
    (62, 3.25), # D5 (new note, unresolved)
    (64, 3.5),  # Eb5 (chromatic)
    (62, 3.75), # D5 (half-answer)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Fm walking (F, Ab, D, Eb)
bass_notes = [
    (38, 4.5),  # F2
    (40, 4.75), # F#2 (chromatic up)
    (43, 5.0),  # Ab2
    (44, 5.25), # A2 (chromatic up)
]
for note, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Bar 4: Gm7 (G, Bb, D, F)
piano_notes = [
    (55, 4.5),  # G4
    (57, 4.5),  # Bb4
    (60, 4.5),  # D5
    (62, 4.5),  # F5
]
for note, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: End the motif — a whisper that lingers
sax_notes = [
    (62, 4.5),  # D5
    (64, 4.75), # Eb5
    (62, 5.0),  # D5
    (60, 5.25), # C5 (resolve)
]
for note, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
# midi.write disabled
