
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of the motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.75),  # A
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=note_start, end=note_end)

for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.75
    pretty_midi.Note(velocity=110, pitch=38, start=note_start, end=note_end)

for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.375
    pretty_midi.Note(velocity=80, pitch=42, start=note_start, end=note_end)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 0.375, end=note_start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 0.75, end=note_start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 1.125, end=note_start + 1.5)

# Bar 4: Drums continue
for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=note_start, end=note_end)

for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.75
    pretty_midi.Note(velocity=110, pitch=38, start=note_start, end=note_end)

for i in range(3):
    note_start = 1.5 + i * 1.5
    note_end = note_start + 0.375
    pretty_midi.Note(velocity=80, pitch=42, start=note_start, end=note_end)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 0.375, end=note_start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 0.75, end=note_start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=note_start + 1.125, end=note_start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
