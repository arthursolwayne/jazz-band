
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),    # F2
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),   # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),   # D2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),    # D2
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),    # F2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),   # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),   # D2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),    # D2
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),    # F2
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),   # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),   # D2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),    # D2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.5 + 0.375), # F4
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.5 + 0.375), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375), # Db5
    # Bar 3 (Bbm7)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.25 + 0.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.25 + 0.375), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.375), # F5
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.25 + 0.375), # Gb5
    # Bar 4 (Fm7)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.0 + 0.375), # F4
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.0 + 0.375), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.375), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.375), # Db5
]
piano_notes.extend([
    # Bar 2 (Comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # Db5
    # Bar 3 (Comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # F5
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375), # Gb5
    # Bar 4 (Comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125), # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # C5
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # Db5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, finish it
# Fm scale: F, Gb, Ab, A, Bb, B, Db, D
# Motif: F (Ab) -> Gb (Bb) -> D (Db) -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.6875),  # F (start)
    pretty_midi.Note(velocity=100, pitch=59, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625), # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.4375), # Db
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=2.8125), # F (finish)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),   # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),   # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
