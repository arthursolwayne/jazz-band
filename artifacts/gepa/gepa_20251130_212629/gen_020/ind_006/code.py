
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),     # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.75),      # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.125),   # Hihat on 2 & 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),      # Hihat on 3 & 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: Walking line in D minor with chromatic approaches
# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),     # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),    # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),    # D#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),     # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),     # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),     # F#
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),     # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),     # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25),      # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.625),   # Hihat on 2 & 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0),      # Hihat on 3 & 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: Walking line in D minor with chromatic approaches
# Bar 3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),     # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),    # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),    # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.5),     # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 3: Bm7b5 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),     # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),     # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),     # F#
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),     # A
]
piano.notes.extend(piano_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.75),      # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),   # Hihat on 2 & 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.5),      # Hihat on 3 & 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: Walking line in D minor with chromatic approaches
# Bar 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),     # D#
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),    # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),    # D
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),     # C
]
bass.notes.extend(bass_notes)

# Sax: Melody - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),     # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),      # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),      # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),      # B (rest on 2.5-2.75)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),      # A
]
sax.notes.extend(sax_notes)

# Bar 3: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),      # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),      # B (rest on 3.75-4.0)
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),      # A
]
sax.notes.extend(sax_notes)

# Bar 4: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),      # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),      # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),      # A (rest on 5.0-5.25)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),      # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),      # A (rest on 5.75-6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
