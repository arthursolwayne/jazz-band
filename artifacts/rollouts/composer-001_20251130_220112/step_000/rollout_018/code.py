
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: 2nd beat (F7 - F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),
    # Bar 3: 2nd beat (Bb7 - Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),
    # Bar 4: 2nd beat (Eb7 - Eb, G, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.375), # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.75), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
