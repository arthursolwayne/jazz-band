
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_2])

# Snare on 2 and 4
drum_snare_1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_1, drum_snare_2])

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm7: F, Ab, Bb, Db
# Walking line in F Dorian: F, Gb, G, Ab, A, Bb, B, C, etc.

# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # Ab
]
bass.notes.extend(bass_notes)

# Bar 3
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Bar 4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),   # Gb
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db
# Cm7: C, Eb, F, Gb
# Gm7: G, Bb, C, D
# Dm7: D, F, G, A

# Bar 2: Fm7 (beat 2)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.25),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Cm7 (beat 2)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # Gb
]
piano.notes.extend(piano_notes)

# Bar 4: Gm7 (beat 2)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs

# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Gb
]
sax.notes.extend(sax_notes)

# Bar 4: Come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for i in range(2, 4):
    start = i * 1.5 + 0.0
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=end)
    drums.notes.append(note)
    start = i * 1.5 + 1.125
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=end)
    drums.notes.append(note)

# Snare on 2 and 4
for i in range(2, 4):
    start = i * 1.5 + 0.75
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=38, start=start, end=end)
    drums.notes.append(note)
    start = i * 1.5 + 1.875
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=38, start=start, end=end)
    drums.notes.append(note)

# Hi-hat on every eighth
for i in range(2, 4):
    for j in range(4):
        start = i * 1.5 + j * 0.375
        end = start + 0.375
        note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
