
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.1875, end=time + 0.3125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2-G2 walking line with chromatic approaches
bass_notes = [
    (2, 0.375),      # D2
    (3, 0.125),      # Eb2 (chromatic approach)
    (3, 0.375),      # G2
    (4, 0.125),      # Ab2 (chromatic approach)
]
for i, (pitch, duration) in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
chord = [2, 6, 9, 11]
for i, pitch in enumerate(chord):
    time = 1.5
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging.
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)  # E5
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)  # B5
sax.notes.append(note)
sax.notes.append(note2)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2-G2 walking line with chromatic approaches
bass_notes = [
    (2, 0.375),      # D2
    (3, 0.125),      # Eb2 (chromatic approach)
    (3, 0.375),      # G2
    (4, 0.125),      # Ab2 (chromatic approach)
]
for i, (pitch, duration) in enumerate(bass_notes):
    time = 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B D F# A)
chord = [1, 3, 6, 8]
for i, pitch in enumerate(chord):
    time = 3.0
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Continue motif
note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)  # E5
note2 = pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5)  # B5
sax.notes.append(note)
sax.notes.append(note2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2-G2 walking line with chromatic approaches
bass_notes = [
    (2, 0.375),      # D2
    (3, 0.125),      # Eb2 (chromatic approach)
    (3, 0.375),      # G2
    (4, 0.125),      # Ab2 (chromatic approach)
]
for i, (pitch, duration) in enumerate(bass_notes):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
chord = [7, 10, 2, 5]
for i, pitch in enumerate(chord):
    time = 4.5
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: Finish the motif
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)  # E5
note2 = pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0)  # B5
note3 = pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25)  # D6
note4 = pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5)  # B5
note5 = pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75)  # F5
note6 = pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)  # E5
sax.notes.append(note)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)

# Drums: Bar 4 (4.5 - 6.0s)
for i in range(4):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.1875, end=time + 0.3125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
