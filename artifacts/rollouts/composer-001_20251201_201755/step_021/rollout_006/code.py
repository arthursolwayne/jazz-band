
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F2 - Bb2 - Ab2 - Eb2 - D2 - G2 - F2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0), # Eb2
]
bass.notes.extend(bass_notes)

# Piano: open voicings
# Bar 2: Fm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Sax: motif (F, Ab, Bb, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25), # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2 - Bb2 - Ab2 - Eb2 - D2 - G2 - F2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5), # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5), # Ab
]
piano.notes.extend(piano_notes)

# Sax: motif (Bb, G, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75), # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2 - Bb2 - Ab2 - Eb2 - D2 - G2 - F2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0), # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax: motif (F, D, Eb, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=61, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25), # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
