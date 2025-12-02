
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif (C - E - G - Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),
    # Bar 2 - 4th beat: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif starting a half step lower (Bb - D - F - Ab)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),
    # Bar 3 - 4th beat: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif again starting a half step lower (Ab - C - Eb - G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),
    # Bar 4 - 4th beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.5)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("jazz_intro.mid")
